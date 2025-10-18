# Claude Code Documentation Update Information

## Last Documentation Update
- **Date**: 2025-10-18
- **Documentation Last Fetched**: 2025-10-18 (17 documents updated)

### Changes Summary (2025-10-18)

#### Major Features & Changes

**1. Skills Added to Plugin System**
- Plugins can now provide Agent Skills as a fifth component type (alongside commands, agents, hooks, and MCP servers)
- Skills are model-invoked—Claude autonomously decides when to use them based on task context
- Location: `skills/` directory in plugin root with `SKILL.md` files
- Updated files: `plugins.md`, `plugins-reference.md`, `slash-commands.md`

**2. Skills vs Slash Commands Documentation**
- New comprehensive section explaining when to use Skills vs Slash Commands (`slash-commands.md:389-480`)
- Key differences table covering complexity, structure, discovery, files, scope, and sharing
- Usage guidelines and example comparisons
- Skills: Complex workflows with multiple files, automatic discovery
- Slash Commands: Simple prompts, explicit invocation

**3. MultiEdit Tool Removed**
- The `MultiEdit` tool has been deprecated and removed from the codebase
- All documentation updated to remove references (hooks, analytics, monitoring)
- Affected files: `hooks.md`, `hooks-guide.md`, `analytics.md`, `monitoring-usage.md`, `settings.md`

#### Interactive Mode Enhancements

**4. New Keyboard Shortcuts**
- `Ctrl+O`: Toggle verbose output (shows detailed tool usage and execution)
- `Ctrl+V` (macOS/Linux) or `Alt+V` (Windows): Paste image from clipboard
- `@` prefix: Trigger file path autocomplete
- `?` key: Display all available keyboard shortcuts for your environment
- Note: Shortcuts may vary by platform and terminal
- Updated file: `interactive-mode.md`

#### Installation & Configuration

**5. Homebrew Installation Added**
- New installation method: `brew install --cask claude-code`
- Available for macOS and Linux
- Auto-updates outside brew directory (can be disabled with `DISABLE_AUTOUPDATER`)
- Updated files: `quickstart.md`, `setup.md`

**6. Prompt Caching Configuration**
- New environment variables for fine-grained prompt caching control
- `DISABLE_PROMPT_CACHING`: Disable for all models (takes precedence)
- `DISABLE_PROMPT_CACHING_HAIKU`: Disable for Haiku models only
- `DISABLE_PROMPT_CACHING_SONNET`: Disable for Sonnet models only
- `DISABLE_PROMPT_CACHING_OPUS`: Disable for Opus models only
- Useful for debugging specific models or cloud provider variations
- Updated files: `model-config.md`, `settings.md`

#### Cloud Provider Updates

**7. Default Haiku Model Updated**
- Bedrock and Vertex AI now default to Haiku 4.5
- **Bedrock**: `us.anthropic.claude-haiku-4-5-20251001-v1:0` (was Haiku 3.5)
- **Vertex AI**: `claude-haiku-4-5@20251001` (was Haiku 3.5)
- **Important**: No automatic upgrade—manual update required via `ANTHROPIC_DEFAULT_HAIKU_MODEL`
- Updated files: `amazon-bedrock.md`, `google-vertex-ai.md`

#### MCP & Integrations

**8. MCP Server Configuration Simplifications**
- `claude mcp serve` command simplified (no longer requires `--transport stdio`)
- Updated Claude Desktop integration configuration
- Removed deprecated SSE endpoints for some third-party servers (Intercom, Linear, PayPal, Sentry)
- Linear switched from SSE to HTTP transport
- Updated file: `mcp.md`

#### Policy & Data Usage

**9. Bug Report Retention Policy Changed**
- Transcripts shared via `/bug` command now retained for 5 years (was 30 days)
- Updated file: `data-usage.md`

**10. Permission System Enhancement**
- `disableBypassPermissionsMode` setting now also disables `--dangerously-skip-permissions` CLI flag
- Enhanced security for enterprise managed policies
- Updated file: `settings.md`

#### Documentation Improvements

**11. Platform-Specific Keyboard Shortcut Note**
- Added note that keyboard shortcuts may vary by platform and terminal
- Press `?` to see shortcuts for your specific environment
- Updated files: `interactive-mode.md`, `quickstart.md`

#### Complete List of Updated Files
1. `amazon-bedrock.md` - Default Haiku model updated to 4.5
2. `analytics.md` - Removed MultiEdit references
3. `data-usage.md` - Bug report retention changed to 5 years
4. `google-vertex-ai.md` - Default Haiku model updated to 4.5
5. `hooks.md` - Removed MultiEdit references
6. `hooks-guide.md` - Removed MultiEdit from examples
7. `interactive-mode.md` - New keyboard shortcuts, @ mentions
8. `mcp.md` - Simplified serve command, updated server configs
9. `model-config.md` - Added prompt caching configuration
10. `monitoring-usage.md` - Removed MultiEdit references
11. `plugins.md` - Added Skills to plugin components
12. `plugins-reference.md` - Skills specification and documentation
13. `quickstart.md` - Added Homebrew installation, ? shortcut
14. `settings.md` - Removed MultiEdit, added prompt caching vars
15. `setup.md` - Added Homebrew installation method
16. `slash-commands.md` - Major Skills vs slash commands section
17. `skills.md` - Skills documentation (content update)

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
- **Total Documents**: 44 official docs
- **Manifest File**: `.docs-manifest.json` (tracks hashes and fetch times)
- **Recent Additions** (2025-10-11):
  - `plugins.md` - Plugin system for extending Claude Code
  - `plugins-reference.md` - Technical specifications for plugins
  - `plugin-marketplaces.md` - Marketplace management
  - `jetbrains.md` - JetBrains IDE integration
  - `vs-code.md` - VS Code integration
  - `headless.md` - Headless mode documentation
  - `checkpointing.md` - Session checkpointing feature
  - `migration-guide.md` - Migration guide for updates
  - `model-config.md` - Model configuration options
  - `network-config.md` - Network configuration
  - `gitlab-ci-cd.md` - GitLab CI/CD integration
- **Removed Documents**: `corporate-proxy.md`, `ide-integrations.md`, `sdk.md` (consolidated into other docs)

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

## Documentation Update History

### 2025-10-18 Update
- **Updated**: 17 documents
- **Major Changes**: Skills added to plugins, Skills vs slash commands guide, MultiEdit tool removed, new keyboard shortcuts (Ctrl+O, Ctrl+V, @-mentions, ?), Homebrew installation, prompt caching config, Haiku 4.5 defaults, MCP simplifications, bug report retention policy
- **Stats**: +232 lines, -43 lines across 16 files

### 2025-10-11 Update
- **Updated**: 41 documents (30 modified, 11 new)
- **New Docs**: plugins.md, plugins-reference.md, plugin-marketplaces.md, jetbrains.md, vs-code.md, headless.md, checkpointing.md, migration-guide.md, model-config.md, network-config.md, gitlab-ci-cd.md
- **Removed**: corporate-proxy.md, ide-integrations.md, sdk.md (consolidated)
- **Total**: 44 official documents (was 33)

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