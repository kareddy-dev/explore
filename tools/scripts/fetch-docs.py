#!/usr/bin/env python3
"""
Generic documentation fetcher for various documentation sources.
Fetches documentation from sitemaps and tracks changes via manifest files.

Features:
- Parallel fetching for improved performance
- Retry logic with exponential backoff
- Progress bar for visual feedback
- Hash-based change detection
"""

import argparse
import hashlib
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from threading import Lock
from typing import Dict, List, Optional, Tuple
import xml.etree.ElementTree as ET

try:
    import requests
except ImportError:
    print("Error: requests library not installed. Run: pip install requests")
    sys.exit(1)

# Try to import tqdm for progress bars, but make it optional
try:
    from tqdm import tqdm
    TQDM_AVAILABLE = True
except ImportError:
    TQDM_AVAILABLE = False
    # Fallback progress indicator
    class tqdm:
        def __init__(self, iterable=None, total=None, desc=None, disable=False, **kwargs):
            self.iterable = iterable
            self.total = total or (len(iterable) if iterable else 0)
            self.desc = desc
            self.disable = disable
            self.n = 0
            
        def __iter__(self):
            if not self.disable and self.desc:
                print(f"{self.desc}: Processing {self.total} items...")
            for item in self.iterable:
                yield item
                self.n += 1
                
        def update(self, n=1):
            self.n += n
            
        def set_description(self, desc):
            if not self.disable:
                print(desc)
                
        def close(self):
            pass
            
        def __enter__(self):
            return self
            
        def __exit__(self, *args):
            self.close()


class DocumentationFetcher:
    def __init__(self, config_file: str = "docs-config.json", max_workers: int = 5, max_retries: int = 3):
        """Initialize with configuration file."""
        self.config_file = Path(__file__).parent / config_file
        self.max_workers = max_workers
        self.max_retries = max_retries
        self.manifest_lock = Lock()
        self.config = self.load_config()
        
    def load_config(self) -> dict:
        """Load configuration from JSON file."""
        if not self.config_file.exists():
            print(f"Error: Configuration file {self.config_file} not found")
            sys.exit(1)
        
        with open(self.config_file, 'r') as f:
            config = json.load(f)
            # Apply config defaults
            for source in config.get('sources', []):
                source.setdefault('max_workers', self.max_workers)
                source.setdefault('max_retries', self.max_retries)
                source.setdefault('retry_delay', 1.0)
            return config
    
    def fetch_with_retry(self, url: str, timeout: int = 30) -> Optional[requests.Response]:
        """Fetch URL with retry logic and exponential backoff."""
        delay = 1.0
        last_error = None
        
        for attempt in range(self.max_retries):
            try:
                response = requests.get(url, timeout=timeout)
                response.raise_for_status()
                return response
            except requests.RequestException as e:
                last_error = e
                if attempt < self.max_retries - 1:
                    time.sleep(delay)
                    delay *= 2  # Exponential backoff
                    
        # All retries failed
        return None
    
    def fetch_sitemap(self, url: str) -> List[str]:
        """Fetch and parse sitemap XML to get all URLs."""
        response = self.fetch_with_retry(url)
        if not response:
            print(f"Error: Failed to fetch sitemap from {url} after {self.max_retries} attempts")
            return []
        
        # Parse XML
        try:
            root = ET.fromstring(response.content)
            # Handle namespace in sitemap
            namespace = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            urls = []
            
            # Try with namespace first
            loc_elements = root.findall('.//sm:loc', namespace)
            if not loc_elements:
                # Try without namespace
                loc_elements = root.findall('.//loc')
            
            for loc in loc_elements:
                if loc.text:
                    urls.append(loc.text)
            
            return urls
        except ET.ParseError as e:
            print(f"Error parsing sitemap XML: {e}")
            return []
    
    def filter_urls(self, urls: List[str], pattern: str) -> List[str]:
        """Filter URLs based on pattern."""
        return [url for url in urls if pattern in url]
    
    def get_document_hash(self, content: str) -> str:
        """Generate SHA256 hash of document content."""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    
    def load_manifest(self, manifest_file: str) -> dict:
        """Load manifest file if it exists."""
        manifest_path = Path(manifest_file)
        if manifest_path.exists():
            with open(manifest_path, 'r') as f:
                return json.load(f)
        return {
            "last_updated": None,
            "source": None,
            "documents": {}
        }
    
    def save_manifest(self, manifest_file: str, manifest: dict):
        """Save manifest file."""
        manifest_path = Path(manifest_file)
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
    
    def fetch_markdown(self, url: str, verbose: bool = False) -> Optional[str]:
        """Fetch markdown content from URL by appending .md."""
        markdown_url = url.rstrip('/') + '.md'
        
        response = self.fetch_with_retry(markdown_url)
        if response:
            return response.text
        else:
            if verbose:
                print(f"  Failed to fetch {markdown_url} after {self.max_retries} attempts")
            return None
    
    def process_document(self, url: str, doc_name: str, output_dir: Path, 
                        existing_hash: Optional[str], force: bool, 
                        dry_run: bool, verbose: bool) -> Tuple[str, str, Optional[str], Optional[str]]:
        """Process a single document. Returns (doc_name, status, content, hash)."""
        
        # Check if we need to fetch
        if not force and existing_hash:
            # Fetch to check if changed
            content = self.fetch_markdown(url, verbose)
            if content:
                new_hash = self.get_document_hash(content)
                if new_hash == existing_hash:
                    return doc_name, "unchanged", None, None
                else:
                    # Content changed, need to update
                    if not dry_run:
                        doc_path = output_dir / f"{doc_name}.md"
                        with open(doc_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        return doc_name, "updated", content, new_hash
                    else:
                        return doc_name, "would_update", None, None
            else:
                return doc_name, "failed", None, None
        
        # Need to fetch (new or forced)
        if dry_run:
            return doc_name, "would_update", None, None
        else:
            content = self.fetch_markdown(url, verbose)
            if content:
                # Save content
                doc_path = output_dir / f"{doc_name}.md"
                with open(doc_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                new_hash = self.get_document_hash(content)
                return doc_name, "updated", content, new_hash
            else:
                return doc_name, "failed", None, None
    
    def process_source(self, source: dict, force: bool = False, dry_run: bool = False, 
                      verbose: bool = False, disable_progress: bool = False) -> dict:
        """Process a single documentation source with parallel fetching."""
        name = source['name']
        sitemap_url = source['sitemap']
        url_pattern = source['url_pattern']
        output_dir = Path(source['output_dir'])
        manifest_file = source['manifest_file']
        fetch_markdown = source.get('fetch_markdown', True)
        max_workers = source.get('max_workers', self.max_workers)
        
        print(f"\nProcessing: {name}")
        print(f"  Sitemap: {sitemap_url}")
        print(f"  Pattern: {url_pattern}")
        print(f"  Max workers: {max_workers}")
        
        # Load existing manifest
        manifest = self.load_manifest(manifest_file)
        manifest['source'] = sitemap_url
        
        # Fetch and filter URLs
        all_urls = self.fetch_sitemap(sitemap_url)
        filtered_urls = self.filter_urls(all_urls, url_pattern)
        
        print(f"  Found {len(filtered_urls)} matching URLs")
        
        if not filtered_urls:
            return {"updated": 0, "unchanged": 0, "failed": 0}
        
        # Create output directory
        if not dry_run:
            output_dir.mkdir(parents=True, exist_ok=True)
        
        # Prepare documents to process
        docs_to_process = []
        for url in filtered_urls:
            # Extract document name from URL
            doc_part = url.split(url_pattern)[-1] if url_pattern in url else ''
            doc_name = doc_part.rstrip('/').split('/')[-1] if doc_part else ''
            if doc_name and fetch_markdown:
                existing_hash = manifest['documents'].get(doc_name, {}).get('hash')
                docs_to_process.append((url, doc_name, existing_hash))
        
        if not docs_to_process:
            return {"updated": 0, "unchanged": 0, "failed": 0}
        
        stats = {"updated": 0, "unchanged": 0, "failed": 0}
        
        # Process documents in parallel with progress bar
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all tasks
            futures = {
                executor.submit(
                    self.process_document, 
                    url, doc_name, output_dir, existing_hash, 
                    force, dry_run, verbose
                ): (url, doc_name)
                for url, doc_name, existing_hash in docs_to_process
            }
            
            # Use progress bar if available and not disabled
            if not disable_progress and not verbose:
                progress_bar = tqdm(
                    total=len(futures),
                    desc=f"  Fetching {name}",
                    disable=not TQDM_AVAILABLE
                )
            else:
                progress_bar = None
            
            # Process completed futures
            for future in as_completed(futures):
                url, doc_name_orig = futures[future]
                try:
                    doc_name, status, content, new_hash = future.result()
                    
                    # Update stats
                    if status == "unchanged":
                        stats["unchanged"] += 1
                        if verbose:
                            print(f"    Unchanged: {doc_name}")
                    elif status in ["updated", "would_update"]:
                        stats["updated"] += 1
                        if verbose or dry_run:
                            action = "Would fetch" if dry_run else "Updated"
                            print(f"    {action}: {doc_name}")
                        
                        # Update manifest (thread-safe)
                        if not dry_run and new_hash:
                            with self.manifest_lock:
                                manifest['documents'][doc_name] = {
                                    "url": url,
                                    "hash": new_hash,
                                    "last_fetched": datetime.utcnow().isoformat() + "Z"
                                }
                    elif status == "failed":
                        stats["failed"] += 1
                        if verbose:
                            print(f"    Failed: {doc_name}")
                    
                    # Update progress bar
                    if progress_bar:
                        progress_bar.update(1)
                        if not TQDM_AVAILABLE:
                            # Simple progress indicator for fallback
                            if stats["updated"] + stats["unchanged"] + stats["failed"] == len(futures):
                                print(f"  Completed: {stats['updated']} updated, {stats['unchanged']} unchanged, {stats['failed']} failed")
                        
                except Exception as e:
                    print(f"    Error processing {doc_name_orig}: {e}")
                    stats["failed"] += 1
                    if progress_bar:
                        progress_bar.update(1)
            
            if progress_bar:
                progress_bar.close()
        
        # Save manifest
        if not dry_run and stats["updated"] > 0:
            manifest['last_updated'] = datetime.utcnow().isoformat() + "Z"
            self.save_manifest(manifest_file, manifest)
            print(f"  Manifest updated: {manifest_file}")
        
        return stats
    
    def check_updates(self, source_name: Optional[str] = None) -> Dict[str, List[str]]:
        """Check which documents need updating without fetching."""
        sources = self.config['sources']
        if source_name:
            sources = [s for s in sources if s['name'] == source_name]
        
        updates = {}
        
        for source in sources:
            name = source['name']
            sitemap_url = source['sitemap']
            url_pattern = source['url_pattern']
            manifest_file = source['manifest_file']
            
            # Load manifest
            manifest = self.load_manifest(manifest_file)
            
            # Fetch current URLs
            all_urls = self.fetch_sitemap(sitemap_url)
            filtered_urls = self.filter_urls(all_urls, url_pattern)
            
            current_docs = set()
            for url in filtered_urls:
                # Extract document name from URL
                doc_part = url.split(url_pattern)[-1] if url_pattern in url else ''
                doc_name = doc_part.rstrip('/').split('/')[-1] if doc_part else ''
                if doc_name:
                    current_docs.add(doc_name)
            
            # Find changes
            existing_docs = set(manifest['documents'].keys())
            new_docs = current_docs - existing_docs
            removed_docs = existing_docs - current_docs
            
            # Check for content changes (with parallel fetching)
            changed_docs = []
            docs_to_check = []
            
            for doc_name in current_docs & existing_docs:
                url = next((u for u in filtered_urls if doc_name in u), None)
                if url and source.get('fetch_markdown', True):
                    old_hash = manifest['documents'][doc_name].get('hash')
                    docs_to_check.append((url, doc_name, old_hash))
            
            # Check in parallel
            if docs_to_check:
                with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                    futures = {
                        executor.submit(self.fetch_markdown, url, False): (doc_name, old_hash)
                        for url, doc_name, old_hash in docs_to_check
                    }
                    
                    for future in as_completed(futures):
                        doc_name, old_hash = futures[future]
                        content = future.result()
                        if content:
                            new_hash = self.get_document_hash(content)
                            if new_hash != old_hash:
                                changed_docs.append(doc_name)
            
            updates[name] = {
                "new": list(new_docs),
                "changed": changed_docs,
                "removed": list(removed_docs)
            }
        
        return updates
    
    def run(self, args):
        """Main execution based on command line arguments."""
        # Update max_workers and max_retries if provided
        if hasattr(args, 'max_workers') and args.max_workers:
            self.max_workers = args.max_workers
        if hasattr(args, 'max_retries') and args.max_retries:
            self.max_retries = args.max_retries
        
        if not TQDM_AVAILABLE and not args.no_progress:
            print("Note: Install tqdm for better progress bars: pip install tqdm")
        
        if args.check:
            # Check for updates
            updates = self.check_updates(args.source)
            
            for source_name, changes in updates.items():
                print(f"\n{source_name}:")
                if changes['new']:
                    print(f"  New documents: {', '.join(changes['new'])}")
                if changes['changed']:
                    print(f"  Changed documents: {', '.join(changes['changed'])}")
                if changes['removed']:
                    print(f"  Removed documents: {', '.join(changes['removed'])}")
                if not any([changes['new'], changes['changed'], changes['removed']]):
                    print("  No updates needed")
            return
        
        # Process sources
        sources = self.config['sources']
        
        if args.source:
            sources = [s for s in sources if s['name'] == args.source]
            if not sources:
                print(f"Error: Source '{args.source}' not found in configuration")
                sys.exit(1)
        elif not args.all:
            print("Error: Specify --source <name> or --all")
            sys.exit(1)
        
        total_stats = {"updated": 0, "unchanged": 0, "failed": 0}
        
        for source in sources:
            # Update source-specific settings
            if hasattr(args, 'max_workers') and args.max_workers:
                source['max_workers'] = args.max_workers
            if hasattr(args, 'max_retries') and args.max_retries:
                source['max_retries'] = args.max_retries
                
            stats = self.process_source(
                source, 
                force=args.force, 
                dry_run=args.dry_run,
                verbose=args.verbose,
                disable_progress=args.no_progress
            )
            
            for key in total_stats:
                total_stats[key] += stats[key]
        
        # Print summary
        print("\n" + "="*50)
        print("Summary:")
        print(f"  Updated: {total_stats['updated']}")
        print(f"  Unchanged: {total_stats['unchanged']}")
        print(f"  Failed: {total_stats['failed']}")
        
        if args.dry_run:
            print("\nDry run completed - no files were modified")


def main():
    parser = argparse.ArgumentParser(
        description="Fetch and manage documentation from various sources"
    )
    
    parser.add_argument(
        "--source", "-s",
        help="Specific source to fetch (e.g., 'claude-code')"
    )
    
    parser.add_argument(
        "--all", "-a",
        action="store_true",
        help="Fetch all configured sources"
    )
    
    parser.add_argument(
        "--check", "-c",
        action="store_true",
        help="Check for updates without fetching"
    )
    
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Force re-fetch all documents (ignore hashes)"
    )
    
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Show what would be fetched without actually fetching"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output"
    )
    
    # New options for enhanced features
    parser.add_argument(
        "--max-workers", "-w",
        type=int,
        default=5,
        help="Maximum number of parallel download threads (default: 5)"
    )
    
    parser.add_argument(
        "--max-retries", "-r",
        type=int,
        default=3,
        help="Maximum number of retry attempts (default: 3)"
    )
    
    parser.add_argument(
        "--no-progress",
        action="store_true",
        help="Disable progress bar"
    )
    
    args = parser.parse_args()
    
    # Run fetcher
    fetcher = DocumentationFetcher(
        max_workers=args.max_workers,
        max_retries=args.max_retries
    )
    fetcher.run(args)


if __name__ == "__main__":
    main()