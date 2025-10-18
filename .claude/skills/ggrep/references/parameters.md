# ggrep Parameter Reference

Complete reference for all `mcp__ggrep__searchGitHub` parameters.

## Required Parameters

### query (string)
The literal code or text pattern to search for.

**Examples:**
```javascript
query: "useState("           // React hook
query: "## Installation"     // Markdown heading
query: "ANTHROPIC_API_KEY"  // Environment variable
query: "async function"      // JavaScript syntax
```

**Regex Patterns:**
```javascript
query: "class.*Component"                    // Basic regex
query: "(?s)useEffect\\(\\(\\) => {.*}"     // Multi-line (requires (?s) prefix)
query: "try.*catch.*Error"                   // Error handling pattern
```

## Optional Parameters

### language (array of strings)
Filter results by programming language.

**Common Languages:**
- Code: `["TypeScript"]`, `["TSX"]`, `["JavaScript"]`, `["Python"]`, `["Go"]`, `["Java"]`, `["Rust"]`
- Markup: `["Markdown"]`, `["HTML"]`, `["JSON"]`, `["YAML"]`
- Config: `["TOML"]`, `["INI"]`, `["Dockerfile"]`

**Multiple Languages:**
```javascript
language: ["TypeScript", "TSX"]           // React TypeScript
language: ["JavaScript", "TypeScript"]    // All JS-based code
language: ["Python", "Go", "Rust"]        // Systems languages
```

**Always required for documentation:**
```javascript
language: ["Markdown"]  // Essential for doc searches
```

### useRegexp (boolean)
Interpret query as a regular expression pattern.

**Default:** `false`

**When to use:**
- Matching patterns with variations
- Multi-line code patterns
- Complex matching logic

**Important:** Use `(?s)` prefix for multi-line matching:
```javascript
{
  query: "(?s)function.*return",
  useRegexp: true
}
```

**Escape special characters:**
```javascript
query: "useState\\(\\)"      // Escaped parentheses
query: "\\[key\\]"           // Escaped brackets
query: "interface\\{\\}"     // Escaped braces (Go)
```

### repo (string)
Filter to specific repository or organization.

**Repository:**
```javascript
repo: "vercel/next.js"       // Specific repo
repo: "facebook/react"       // Another repo
repo: "microsoft/TypeScript" // Microsoft repo
```

**Organization:**
```javascript
repo: "anthropics/"    // All Anthropic repos
repo: "vercel/"        // All Vercel repos
repo: "google/"        // All Google repos
```

**Partial matching:**
```javascript
repo: "claude"         // Matches repos with "claude" in name
```

### path (string)
Filter by file path pattern.

**Exact files:**
```javascript
path: "README.md"       // Only README files
path: "package.json"    // Only package.json
path: "Dockerfile"      // Only Dockerfiles
```

**Directories:**
```javascript
path: "docs/"           // Files in docs directory
path: "src/components/" // Specific subdirectory
path: "/api/"           // API directories at any level
```

**File types:**
```javascript
path: ".github/workflows/"  // GitHub Actions
path: "test/"               // Test directories
path: "examples/"           // Example code
```

### matchCase (boolean)
Enable case-sensitive search.

**Default:** `false` (case-insensitive)

**When to use:**
- Distinguishing between `User` and `user`
- Language-specific identifiers
- API endpoints with specific casing

```javascript
{
  query: "UserService",
  matchCase: true
}
```

### matchWholeWords (boolean)
Match complete words only (no substring matches).

**Default:** `false`

**When to use:**
- Avoiding false matches
- Finding exact identifier names
- Precise API searches

**Example:**
```javascript
{
  query: "use",
  matchWholeWords: true  // Matches "use", not "useState" or "user"
}
```

## Parameter Combinations

### Documentation Search Template
```javascript
{
  query: "<literal text from docs>",
  language: ["Markdown"],
  path: "README.md"  // or "docs/"
}
```

### Code Search Template
```javascript
{
  query: "<literal code pattern>",
  language: ["<PrimaryLanguage>", "<SecondaryLanguage>"],
  repo: "<optional-filter>"
}
```

### Regex Search Template
```javascript
{
  query: "(?s)<pattern>",  // (?s) for multi-line
  language: ["<Language>"],
  useRegexp: true
}
```

### Precise Search Template
```javascript
{
  query: "<exact-term>",
  language: ["<Language>"],
  matchCase: true,
  matchWholeWords: true
}
```

## Performance Tips

### Start Broad
Begin with simple searches, add filters based on results:
```javascript
// Step 1: Broad search
{ query: "useState", language: ["TypeScript"] }

// Step 2: Add TSX if needed
{ query: "useState", language: ["TypeScript", "TSX"] }

// Step 3: Filter to specific repos if too many results
{ query: "useState", language: ["TypeScript", "TSX"], repo: "facebook/" }
```

### Use Language Filter Always
Dramatically reduces noise:
```javascript
// Too broad - returns everything
{ query: "config" }

// Better - specific context
{ query: "config", language: ["Python"] }

// Best - most specific
{ query: "config.py", language: ["Python"], path: "src/" }
```

### Path vs Repo Filtering
**Use `path` for:**
- Documentation (README.md, docs/)
- Configuration files (package.json, Dockerfile)
- Specific directories (test/, examples/)

**Use `repo` for:**
- Official implementations
- Specific organizations
- Well-known projects

## Common Pitfalls

### ❌ Forgetting Language Filter
```javascript
// Bad - too many irrelevant results
{ query: "config" }

// Good - targeted results
{ query: "config", language: ["YAML"] }
```

### ❌ Using Keywords Instead of Code
```javascript
// Bad - no results
{ query: "react hooks tutorial" }

// Good - literal code
{ query: "useState(", language: ["TSX"] }
```

### ❌ Missing (?s) for Multi-line
```javascript
// Bad - won't match across lines
{ query: "function.*return", useRegexp: true }

// Good - matches multi-line
{ query: "(?s)function.*return", useRegexp: true }
```

### ❌ Not Escaping Regex Characters
```javascript
// Bad - regex interprets ( ) as grouping
{ query: "useState()", useRegexp: true }

// Good - escaped parentheses
{ query: "useState\\(\\)", useRegexp: true }
```

## Advanced Patterns

### Find API Implementations
```javascript
{
  query: "import { Anthropic }",
  language: ["TypeScript"],
  path: "src/"
}
```

### Find Configuration Examples
```javascript
{
  query: "```yaml",
  language: ["Markdown"],
  path: "docs/"
}
```

### Find Error Handling Patterns
```javascript
{
  query: "(?s)try {.*} catch.*Error",
  language: ["TypeScript"],
  useRegexp: true
}
```

### Find Test Patterns
```javascript
{
  query: "describe(",
  language: ["TypeScript", "JavaScript"],
  path: "test/"
}
```

### Find CLI Commands in Docs
```javascript
{
  query: "npm install",
  language: ["Markdown"],
  path: "README.md"
}
```
