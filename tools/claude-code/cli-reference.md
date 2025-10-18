# Claude Code CLI Reference

Complete reference for Claude Code command-line interface, including all commands, flags, options, and interactive features.

## Table of Contents

- [Basic Commands](#basic-commands)
- [Command Line Flags](#command-line-flags)
- [Slash Commands](#slash-commands)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Environment Variables](#environment-variables)
- [Configuration Files](#configuration-files)
- [Advanced Usage](#advanced-usage)

## Basic Commands

### Starting Claude Code

```bash
# Start interactive REPL
claude

# Start with initial prompt
claude "Help me understand this codebase"

# Query and exit (non-interactive)
claude -p "What does the main() function do?"
claude --print "Explain the authentication flow"

# Continue previous conversation
claude -c
claude --continue

# Resume specific conversation
claude --resume <conversation-id>
```

### Update and Version

```bash
# Check version
claude --version
claude -v

# Update to latest version
claude update

# Help
claude --help
claude -h
```

## Command Line Flags

### Core Options

| Flag | Long Form | Description | Example |
|------|-----------|-------------|---------|
| `-p` | `--print` | Print response without interactive mode | `claude -p "Fix the bug"` |
| `-c` | `--continue` | Continue most recent conversation | `claude -c` |
| `-v` | `--version` | Display version information | `claude -v` |
| `-h` | `--help` | Show help information | `claude -h` |

### Model Selection

| Flag | Description | Example |
|------|-------------|---------|
| `--model <name>` | Set model for session | `claude --model opus` |
| `--opus` | Use Opus model | `claude --opus` |
| `--sonnet` | Use Sonnet model | `claude --sonnet` |
| `--haiku` | Use Haiku model | `claude --haiku` |

### Directory Management

| Flag | Description | Example |
|------|-------------|---------|
| `--add-dir <path>` | Add additional working directory | `claude --add-dir ../lib` |
| `--dir <path>` | Set working directory | `claude --dir /project` |

### Permission Control

| Flag | Description | Example |
|------|-------------|---------|
| `--permission-mode <mode>` | Set permission mode (allow/ask/deny) | `claude --permission-mode ask` |
| `--no-tools` | Disable all tools | `claude --no-tools` |

### MCP Configuration

| Flag | Description | Example |
|------|-------------|---------|
| `--mcp-config <file>` | Load MCP configuration | `claude --mcp-config mcp.json` |
| `--mcp-config <f1> <f2>` | Load multiple MCP configs | `claude --mcp-config mcp1.json mcp2.json` |

Note: Claude Code handles multiple MCP servers well. Benchmarks show Claude models excel at managing 70+ MCP servers with 500+ tools.

### Output Control

| Flag | Description | Example |
|------|-------------|---------|
| `--format <type>` | Output format (text/json/stream) | `claude --format json` |
| `--max-turns <n>` | Limit number of agentic turns | `claude --max-turns 5` |
| `--verbose` | Enable detailed logging | `claude --verbose` |
| `--quiet` | Suppress non-essential output | `claude --quiet` |

### System Prompt Modification

| Flag | Description | Example |
|------|-------------|---------|
| `--append-system-prompt <text>` | Append to system prompt | `claude --append-system-prompt "Focus on security"` |
| `--output-style <style>` | Set output style | `claude --output-style explanatory` |

### Advanced Options

| Flag | Description | Example |
|------|-------------|---------|
| `--api-key <key>` | Override API key | `claude --api-key sk-...` |
| `--base-url <url>` | Override API base URL | `claude --base-url https://...` |
| `--resume <id>` | Resume specific conversation | `claude --resume abc123` |
| `--no-history` | Disable conversation history | `claude --no-history` |

## Slash Commands

Interactive commands available within Claude Code sessions:

### Session Management

```mermaid
flowchart LR
    A[Slash Commands] --> B["/help"]
    A --> C["/quit or /exit"]
    A --> D["/clear"]
    A --> E["/history"]
    A --> F["/resume"]
    A --> G["/cost"]
    B --> H[Show available commands]
    C --> I[Exit Claude Code]
    D --> J[Clear screen]
    E --> K[Show conversation history]
    F --> L[List resumable sessions]
    G --> M[Token usage & statistics]
```

| Command | Description |
|---------|-------------|
| `/help` | Display help for slash commands |
| `/quit` or `/exit` | Exit Claude Code |
| `/clear` | Clear the terminal screen |
| `/history` | Show conversation history |
| `/resume` | List resumable conversations |
| `/reset` | Reset current conversation |
| `/cost` | Show detailed token usage and session statistics (v1.0.84+) |
| `/context` | Debug context issues and check what's being included (v1.0.86+) |
| `/doctor` | Run diagnostic checks for Claude Code |

### Model Control

| Command | Description | Example |
|---------|-------------|---------|
| `/model` | Show/change current model | `/model opus` |
| `/model list` | List available models | `/model list` |
| `/model opus-plan` | Use Opus for planning, Sonnet otherwise | `/model opus-plan` |
| `/model sonnet [1m]` | Use Sonnet with 1M token context (API pricing only) | `/model sonnet [1m]` |

#### Model Options

- **Sonnet**: Default model (Claude 3.5 Sonnet)
- **Opus**: Most capable model (Claude 3 Opus)
- **Haiku**: Fast, efficient model (Claude 3 Haiku)
- **Opus-plan**: Uses Opus 4.1 for planning, Sonnet 4 for execution
- **Sonnet [1m]**: 1 million token context (requires API billing, not subscription)

### Permission Management

| Command | Description | Example |
|---------|-------------|---------|
| `/permissions` | Open permissions management interface | `/permissions` |
| `/permissions ask` | Set to ask mode | `/permissions ask` |
| `/permissions allow` | Set to allow mode | `/permissions allow` |
| `/permissions deny <tool>` | Deny specific tool | `/permissions deny bash` |

#### Permission Interface Options

When using `/permissions`, you can:
1. **Always allow** - Add commands that never need permission
2. **Always ask** - Add commands that always require confirmation
3. **Always deny** - Block specific commands entirely
4. **Additional directories** - Add directories Claude can read

#### Default Mode Accept Edits

Claude Code can remember your file edit preferences:
- When prompted to edit files, choose "Yes and always allow modifying files in this project"
- This adds `"defaultModeAcceptEdits": true` to `.claude/settings.local.json`
- Remove this line to re-enable edit confirmations

#### Permission Configuration in settings.local.json

```json
{
  "defaultModeAcceptEdits": true,
  "permissions": {
    "alwaysAllow": ["npm run install", "npm run lint"],
    "alwaysAsk": ["supabase"],
    "alwaysDeny": ["rm -rf"],
    "additionalReadDirs": ["/path/to/docs"]
  }
}

### MCP Integration

```mermaid
flowchart TD
    A[Claude Code] --> B[MCP Config]
    B --> C{MCP Servers}
    C --> D[GitHub Server]
    C --> E[Figma Server]
    C --> F[Custom Server]
    D --> G[GitHub Tools]
    E --> H[Design Tools]
    F --> I[Custom Tools]
```

| Command | Description | Example |
|---------|-------------|---------|
| `/mcp` | List MCP connections | `/mcp` |
| `/mcp connect <server>` | Connect to MCP server | `/mcp connect github` |
| `/mcp disconnect <server>` | Disconnect from server | `/mcp disconnect github` |
| `/mcp tools` | List available MCP tools | `/mcp tools` |

**MCP Workflow Example:**
```bash
# Check MCP status
/mcp

# Connect to GitHub MCP server
/mcp connect github

# List available tools
/mcp tools

# Use MCP tools naturally in conversation
claude "Search GitHub issues for authentication bugs"
```

### UI Customization & Output Styles

| Command | Description | Example |
|---------|-------------|---------|
| `/statusline` | Configure status line | `/statusline` |
| `/output-style` | Open output style menu | `/output-style` |
| `/output-style <name>` | Switch to specific style | `/output-style explanatory` |
| `/output-style:new` | Create custom style with Claude's help | `/output-style:new` |
| `/output-style:list` | List available styles | `/output-style:list` |
| `/theme` | Change color theme | `/theme` |

#### Output Style Details

**Built-in Styles:**
- `default` - Standard software engineering focus
- `explanatory` - Educational with detailed insights
- `learning` - Collaborative with TODO(human) markers

**Custom Styles:**
- Stored in `~/.claude/output-styles/` (user) or `.claude/output-styles/` (project)
- Written as markdown files with instructions
- Completely replace the system prompt

### Debugging & Feedback

| Command | Description |
|---------|-------------|
| `/bug` | Report a bug |
| `/feedback` | Send feedback |
| `/debug` | Toggle debug mode |
| `/logs` | Show session logs |

### File Management

| Command | Description | Example |
|---------|-------------|---------|
| `/add <path>` | Add file to context | `/add src/main.js` |
| `/remove <path>` | Remove file from context | `/remove src/test.js` |
| `/files` | List files in context | `/files` |

**@-Mentions in Commands** (v1.0.70+):
- Use @-mentions in slash command arguments for file references
- Supports files with spaces in paths (v1.0.83+)
- Works with `~/.claude/*` files for agents, output styles, and commands (v1.0.84+)
- Example: `/add @main.js` or `/custom-command @config.json`

### Task Management

| Command | Description |
|---------|-------------|
| `/todo` | Show current todo list |
| `/todo add <task>` | Add task to todo list |
| `/todo complete <id>` | Mark task as complete |

### Agent Management

```mermaid
mindmap
  root((Agent System))
    Built-in Agents
      general-purpose
      statusline-setup
      output-style-setup
      meta-agent
    User Agents
      ~/.claude/agents/
      Available everywhere
    Project Agents
      .claude/agents/
      Project-specific
      Highest priority
```

| Command | Description | Example |
|---------|-------------|---------|
| `/agents` | Open agent management interface | `/agents` |
| `/agents create` | Create new agent | `/agents create` |
| `/agents edit <name>` | Edit existing agent | `/agents edit code-reviewer` |
| `/agents delete <name>` | Delete custom agent | `/agents delete test-runner` |
| `/agents list` | List all available agents | `/agents list` |

#### Agent Details

**Agent Hierarchy:**
```mermaid
flowchart TD
    A[Agent Request] --> B{Priority Check}
    B -->|Highest| C[Project Agents<br/>.claude/agents/]
    B -->|Medium| D[User Agents<br/>~/.claude/agents/]
    B -->|Lowest| E[Built-in Agents]
    C --> F[Execute Agent]
    D --> F
    E --> F
```

**Agent Types:**
- **Built-in agents**: Pre-configured by Claude Code (general-purpose)
- **User agents**: Stored in `~/.claude/agents/` (available across projects)
- **Project agents**: Stored in `.claude/agents/` (highest priority)

**Agent Configuration:**
- **Name**: Unique identifier (lowercase with hyphens)
- **Description**: When to use the agent (include "PROACTIVELY" for auto-triggering)
- **Tools**: Specific tools or inherit all (optional)
- **Color**: Visual identifier in terminal (optional)

**Creating Agents via /agents:**
1. Choose location (project or user)
2. Generate with Claude (recommended) or manual
3. Select tools (read-only, edit, execution, MCP, or all)
4. Choose color for visual tracking
5. Edit system prompt if needed (press 'e' in interface)

**Agent Execution:**
- **Sequential**: Default for chained tasks, context passes between agents
- **Parallel**: For independent tasks, speeds up workflows
- **Clean slate**: Each agent starts fresh without memory of previous runs
- **Separate TODOs**: Each agent maintains its own TODO list

**Agent Workflow:**
```mermaid
sequenceDiagram
    participant User
    participant Main as Main Claude
    participant Agent as Subagent
    participant Tools
    
    User->>Main: Request task
    Main->>Agent: Delegate to specialist
    Agent->>Tools: Use specific tools
    Tools->>Agent: Return results
    Agent->>Main: Complete with results
    Main->>User: Deliver solution
```

**Invoking Agents:**
```bash
# Automatic delegation based on task
"Debug this error"  # May trigger debugger agent

# Explicit invocation
"Use the code-reviewer agent to check my changes"

# Chaining agents (sequential)
"Analyze performance, then optimize, then write release notes"

# Parallel execution
"Run security audit and documentation review simultaneously"
```

## Keyboard Shortcuts

### During Input

| Shortcut | Action |
|----------|--------|
| `Ctrl+C` | Cancel current operation |
| `Ctrl+D` | Exit Claude Code (on empty line) |
| `Ctrl+L` | Clear screen |
| `Ctrl+O` | Toggle verbose output (shows detailed tool usage) |
| `Ctrl+R` | Search command history |
| `Ctrl+V` (macOS/Linux) / `Alt+V` (Windows) | Paste image from clipboard |
| `Tab` | Autocomplete |
| `↑/↓` | Navigate command history |
| `@` | Trigger file path autocomplete |
| `?` | Show available keyboard shortcuts |

### Special Features

| Shortcut | Action |
|----------|--------|
| `Ctrl+B` | Run command in background |
| `Ctrl+Z` | Suspend current process |
| `Esc` | Cancel OAuth flow or dialog |

**Note**: Keyboard shortcuts may vary by platform and terminal. Press `?` to see shortcuts for your specific environment.

## Environment Variables

Configure Claude Code behavior through environment variables:

### API Configuration

```bash
# API Key
export ANTHROPIC_API_KEY="sk-ant-..."

# Custom API endpoint
export ANTHROPIC_BASE_URL="https://custom-api.example.com"

# API version
export ANTHROPIC_API_VERSION="2024-01-01"

# Default model aliases (v1.0.88+)
export ANTHROPIC_DEFAULT_SONNET_MODEL="claude-3-5-sonnet-20241022"
export ANTHROPIC_DEFAULT_OPUS_MODEL="claude-3-opus-20240229"
```

### Behavior Settings

```bash
# Default model
export CLAUDE_MODEL="opus"

# Default permission mode
export CLAUDE_PERMISSION_MODE="ask"

# Disable telemetry
export CLAUDE_TELEMETRY_DISABLED="1"

# Custom config directory
export CLAUDE_CONFIG_DIR="~/.config/claude-code"

# Use built-in ripgrep (v1.0.84+, enabled by default)
export USE_BUILTIN_RIPGREP="0"  # Set to 0 to use system ripgrep

# Prompt caching control (v1.0.88+)
export DISABLE_PROMPT_CACHING="1"         # Disable for all models (takes precedence)
export DISABLE_PROMPT_CACHING_HAIKU="1"   # Disable for Haiku models only
export DISABLE_PROMPT_CACHING_SONNET="1"  # Disable for Sonnet models only
export DISABLE_PROMPT_CACHING_OPUS="1"    # Disable for Opus models only
```

### Debug & Logging

```bash
# Enable debug logging
export CLAUDE_DEBUG="1"

# Set log level
export CLAUDE_LOG_LEVEL="debug"  # debug, info, warn, error

# Log file location
export CLAUDE_LOG_FILE="/tmp/claude.log"
```

## Configuration Files

### Settings Location

```bash
# User settings
~/.claude/settings.json

# Project settings
./.claude/settings.json

# MCP configuration
~/.claude/mcp.json
./.claude/mcp.json
```

### Settings File Format

```json
{
  "model": "opus",
  "permissionMode": "ask",
  "outputStyle": "default",
  "statusLine": {
    "enabled": true,
    "format": "[{model}] {cwd}"
  },
  "tools": {
    "bash": {
      "enabled": true,
      "timeout": 30000
    },
    "file": {
      "enabled": true,
      "maxSize": 1048576
    }
  },
  "mcp": {
    "autoConnect": ["github", "linear"]
  }
}
```

### Project Configuration (CLAUDE.md)

Create a `CLAUDE.md` file in your project root:

```markdown
# Project Configuration for Claude Code

## Commands
- Build: `npm run build`
- Test: `npm test`
- Lint: `npm run lint`

## Architecture
[Project structure description]

## Conventions
[Coding standards]
```

### Ignore File (.claudeignore)

Exclude files from Claude Code's context:

```gitignore
# Dependencies
node_modules/
vendor/

# Build outputs
dist/
build/
*.min.js

# Large files
*.log
*.sql
data/

# Sensitive files
.env
secrets/
```

## Advanced Configuration

### Increasing Thinking Tokens

Add to `.claude/settings.local.json` to increase Claude's thinking capacity:

```json
{
  "env": {
    "MAX_THINKING_TOKENS": "32000"
  }
}
```

This allows Claude to think through complex problems more thoroughly before responding.

### 1 Million Token Context Window

Available only with API pricing (not subscription):

```bash
# Log out of subscription
claude logout

# Reconnect with API billing
claude
# Choose "Anthropic console account (API usage billing)"

# Enable 1M context
/model sonnet [1m]
```

### Settings Hierarchy

Settings are loaded in order of precedence:
1. Command-line arguments (highest priority)
2. `.claude/settings.local.json` (project-specific)
3. `~/.claude/settings.json` (user-level)
4. Default settings (lowest priority)

### Debugging System Prompt

View the actual system prompt being used:

```bash
# Enable trace mode
export ANTHROPIC_TRACE=1
claude

# Check raw API calls in trace output
# Look for "system" field in the JSON
```

### SDK Enhancements

Claude Code's programmatic interface has been enhanced with several new capabilities:

#### UUID Support (v1.0.86)
All SDK messages now include UUID support for better message tracking and correlation.

#### User Message Replay (v1.0.86)
```bash
# Replay user messages back to stdout
claude --replay-user-messages
```

#### Request Cancellation (v1.0.82)
The SDK now supports canceling long-running operations:
```bash
# Operations can be cancelled mid-execution
# Useful for complex searches or large file operations
```

#### Additional Directories Configuration
Configure custom search paths beyond the default project structure:
```bash
# Add multiple directories for enhanced code discovery
claude --add-dir ../shared-lib --add-dir ../config-files
```

This is particularly useful for:
- Monorepo configurations with shared libraries
- Projects with external dependencies
- Custom tooling and configuration directories

#### Settings Validation
Enhanced validation prevents configuration errors:
- Invalid fields in `.claude/settings.json` are automatically detected
- Clear error messages help resolve configuration issues
- Improved stability when loading project settings

## Advanced Usage

### Piping and Redirection

```bash
# Pipe input to Claude
echo "Explain this error" | claude -p

# Process file content
cat error.log | claude -p "Identify the root cause"

# Redirect output
claude -p "Generate a README" > README.md

# Chain commands
git diff | claude -p "Explain these changes" | tee review.md
```

### Scripting with Claude

```bash
#!/bin/bash
# claude-review.sh

# Get git changes
CHANGES=$(git diff --staged)

# Review with Claude
REVIEW=$(echo "$CHANGES" | claude -p "Review these changes for issues")

# Display review
echo "$REVIEW"

# Ask for confirmation
read -p "Proceed with commit? (y/n) " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]; then
    git commit
fi
```

### Background Processes

```bash
# Start dev server in background (use Ctrl+B in interactive mode)
claude "Start the dev server in the background and continue working"

# Monitor logs
tail -f app.log | claude -p "Alert me if you see errors"
```

### Batch Processing

```bash
# Process multiple files
for file in src/*.js; do
  claude -p "Add JSDoc comments to $file"
done

# Parallel processing
find . -name "*.py" | xargs -P 4 -I {} claude -p "Check {} for security issues"
```

### Integration Examples

```bash
# Git hooks (.git/hooks/pre-commit)
#!/bin/bash
claude -p "Review staged changes for issues" || exit 1

# Continuous monitoring
while true; do
  claude -p "Check system health" < /proc/loadavg
  sleep 60
done

# Automated documentation
claude -p "Generate API docs from src/" > docs/api.md
```

### Working with Different File Types

```bash
# JSON processing
cat config.json | claude -p "Validate and format this JSON"

# SQL queries
claude -p "Optimize this query: SELECT * FROM users WHERE..."

# Docker
claude -p "Create a Dockerfile for this Node.js app"

# Kubernetes
claude -p "Generate k8s manifests for this service"
```

## Workflow Patterns

```mermaid
flowchart TD
    A[Start Claude] --> B{Mode?}
    B -->|Interactive| C[REPL Session]
    B -->|One-shot| D[Query & Exit]
    B -->|Continue| E[Resume Session]
    
    C --> F[Slash Commands]
    C --> G[Natural Language]
    C --> H[Background Tasks]
    
    D --> I[Process Output]
    I --> J[Exit]
    
    E --> K[Load Context]
    K --> C
    
    F --> L[Command Examples]
    G --> M[Code Tasks]
    H --> N[Long-running Processes]
```

## Performance Tips

### Context Management

```bash
# Limit context size
claude --max-context 50000

# Clear unnecessary context
/clear

# Use .claudeignore effectively
echo "node_modules/" >> .claudeignore
```

### Efficient Queries

```bash
# Be specific
claude -p "Fix the type error in src/auth/login.ts line 42"

# Batch related tasks
claude "1. Run tests 2. Fix failures 3. Create commit"

# Use appropriate models
claude --haiku -p "Format this JSON"  # Simple task
claude --opus -p "Refactor the architecture"  # Complex task
```

## Troubleshooting Commands

```bash
# Check installation
which claude
claude --version

# Test API connection
claude -p "Hello" --verbose

# Debug mode
CLAUDE_DEBUG=1 claude

# Check configuration
cat ~/.claude/settings.json

# Clear cache
rm -rf ~/.claude/cache

# Reset configuration
rm ~/.claude/settings.json
claude  # Will recreate with defaults
```

## See Also

- [Claude Code Guide](./claude-code-guide.md) - Comprehensive overview
- [Workflow Examples](./workflow-examples.md) - Practical scenarios
- [MCP Servers Guide](../mcp/mcp-servers-guide.md) - External integrations
- [Official Documentation](https://docs.anthropic.com/en/docs/claude-code)