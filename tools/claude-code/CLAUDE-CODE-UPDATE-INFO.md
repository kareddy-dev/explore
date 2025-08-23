# Claude Code Documentation Update Information

## Last Documentation Update
- **Date**: 2025-08-23
- **Documentation Last Fetched**: 2025-08-23T17:32:00Z (7 documents updated)

## Repository Information
- **Repository**: https://github.com/anthropics/claude-code
- **Commit ID**: `eb0e4345dd1e37b4cc087f4e6b60cc8f0dc0beaf`
- **Commit Message**: "chore: Update CHANGELOG.md"
- **Commit Date**: 2025-08-23
- **Latest Version**: 1.0.88 (from CHANGELOG.md)
- **NPM Package**: [@anthropic-ai/claude-code](https://www.npmjs.com/package/@anthropic-ai/claude-code)

## Source Locations
- **Local Repository**: `/Users/kareddy/Desktop/explore/tmp/claude-code/`
- **Clone Command**: `git clone git@github.com:anthropics/claude-code`
- **Official Documentation**: https://docs.anthropic.com/en/docs/claude-code/

## Documentation Structure

### Curated Guides (Manually Created)
- `claude-code-guide.md` - Comprehensive overview with diagrams
- `cli-reference.md` - Complete CLI reference with examples
- `workflow-examples.md` - Practical development scenarios
- `hooks-cookbook.md` - Advanced hook patterns
- `custom-commands.md` - Custom slash command library
- `subagent-templates.md` - Pre-built subagent configurations
- `performance-optimization.md` - Best practices for large codebases

### Official Documentation (Auto-Fetched)
- **Source**: https://docs.anthropic.com/sitemap.xml
- **Location**: `gen/` directory
- **Total Documents**: 33 official docs
- **Manifest File**: `.docs-manifest.json` (tracks hashes and fetch times)

### Framework Documentation (New)
- `frameworks/bmad-method.md` - BMAD-METHOD integration guide
- `frameworks/BMAD-UPDATE-INFO.md` - BMAD update tracking

## Update Process

### Checking for Repository Updates
```bash
# 1. Pull latest changes
cd /Users/kareddy/Desktop/explore/tmp/claude-code
git pull origin main

# 2. Check changes since last update
git log --oneline da6d2f715e5081bf304e23aff6f282a73f0f9dc7..HEAD

# 3. Review CHANGELOG for new features
git diff da6d2f715e5081bf304e23aff6f282a73f0f9dc7..HEAD CHANGELOG.md

# 4. Check for new examples or features
git diff da6d2f715e5081bf304e23aff6f282a73f0f9dc7..HEAD README.md examples/
```

### Fetching Latest Official Documentation
```bash
# Check for documentation updates
python /Users/kareddy/Desktop/explore/tools/scripts/fetch-docs.py --check

# Fetch latest Claude Code docs
python /Users/kareddy/Desktop/explore/tools/scripts/fetch-docs.py --source claude-code

# Force re-fetch all documents
python /Users/kareddy/Desktop/explore/tools/scripts/fetch-docs.py --source claude-code --force

# View what changed
git diff tools/claude-code/gen/
```

### Documentation Categories to Monitor

#### From Repository
- **CHANGELOG.md** - Version updates and new features
- **examples/** - New example hooks, configurations
- **scripts/** - Utility scripts for Claude Code

#### From Official Docs
- **New Features** - Sub-agents, output styles, MCP servers
- **CLI Updates** - New commands, flags, options
- **Integrations** - IDE updates, new platform support
- **Enterprise** - Bedrock, Vertex AI, proxy configurations

## Key Files Referenced

### Repository Files
- `CHANGELOG.md` - Version history and feature updates
- `README.md` - Overview and getting started
- `LICENSE.md` - MIT License
- `SECURITY.md` - Security guidelines
- `examples/hooks/` - Example hook implementations

### Documentation Files
- `.docs-manifest.json` - Tracks all fetched documents
- `tools/scripts/fetch-docs.py` - Documentation fetcher script
- `tools/scripts/docs-config.json` - Sources configuration

## Version History
- **1.0.88** - Fixed "OAuth authentication is currently not supported" issue, status line input now includes `exceeds_200k_tokens`, fixed incorrect usage tracking in /cost, introduced `ANTHROPIC_DEFAULT_SONNET_MODEL` and `ANTHROPIC_DEFAULT_OPUS_MODEL` environment variables, Bedrock updated default Sonnet model to Sonnet 4
- **1.0.86** - Added `/context` command for debugging context issues, SDK: Added UUID support for all messages, SDK: Added `--replay-user-messages` to replay user messages back to stdout
- **1.0.85** - Status line input now includes session cost info, Hooks: Introduced SessionEnd hook
- **1.0.84** - Built-in ripgrep by default (major performance improvement), 13 new MCP servers (Box, Canva, Daloopa, Fireflies, HubSpot, Hugging Face, Jam, Monday, Netlify, Stytch, Vercel, plus Figma updates), enhanced `/cost` command with detailed session statistics, search troubleshooting guide, tool ID mismatch fixes, real-time steering improvements, @-mention enhancements (~/.claude/ files)
- **1.0.83** - @-mention files with spaces support, new shimmering spinner
- **1.0.82** - SDK request cancellation, settings validation, MCP improvements
- **1.0.81** - Output styles release (Explanatory, Learning)
- **1.0.80** - UI improvements, custom subagent colors
- **1.0.77** - Bash tool improvements, SDK session support
- **1.0.73** - Multiple MCP config files support

## Notes
- Documentation is fetched from Anthropic's official site
- Repository contains examples and implementation details
- Official docs provide comprehensive feature documentation
- Curated guides add practical examples and patterns
- Framework documentation (BMAD) provides integration patterns

## Next Update Checklist
- [ ] Check repository for new commits
- [ ] Review CHANGELOG for version updates
- [ ] Run documentation fetcher for official docs
- [ ] Update curated guides based on new features
- [ ] Test new examples from repository
- [ ] Update version references in documentation
- [ ] Add new workflow examples if applicable
- [ ] Update framework integrations (BMAD, etc.)

## Contact
- **Issues**: https://github.com/anthropics/claude-code/issues
- **Documentation**: https://docs.anthropic.com/en/docs/claude-code/
- **NPM**: https://www.npmjs.com/package/@anthropic-ai/claude-code