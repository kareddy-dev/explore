# MCP Servers Configuration Guide

## Overview
Model Context Protocol (MCP) servers extend AI capabilities by providing specialized tools and data sources. Here are documented MCP servers and their configurations.

### Recent Updates (Claude Code v1.0.82)
- **Improved Tool Name Consistency**: MCP tool names are now more consistent across integrations, reducing confusion and improving reliability when working with multiple MCP servers.

## Server Configurations

### 1. GGrep - Code Search

**Purpose**: Advanced code search capabilities across repositories

```json
{
  "mcpServers": {
    "ggrep": {
      "type": "http",
      "url": "https://mcp.grep.app"
    }
  }
}
```

**About grep.app**:
- Created by Vercel - a cloud platform for static and serverless deployment
- Searches across over 1 million GitHub repositories
- Web-based tool with modern, user-friendly interface
- Supports both light and dark modes
- Built using React and Next.js technologies

**Features**:
- Search code across multiple repositories simultaneously
- Advanced pattern matching and filtering
- Fast code discovery across massive repository collection
- Effortless navigation through search results
- Integration with grep.app search engine

**Use Cases**:
- Finding code examples and implementations
- Cross-repository code search and analysis
- API usage discovery and documentation
- Code pattern analysis and best practices research
- Learning from open source implementations

---

### 2. GitHub Copilot MCP

**Purpose**: GitHub integration with Copilot capabilities

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer YOUR_GITHUB_TOKEN"
      }
    }
  }
}
```

**Features**:
- GitHub repository access
- Issue and PR management
- Code suggestions and completions
- Repository insights

**Use Cases**:
- Repository management
- Code review assistance
- Issue tracking
- Pull request automation

**Setup Notes**:
- Requires GitHub Personal Access Token
- Token should have appropriate repository permissions
- Replace `YOUR_GITHUB_TOKEN` with actual token

---

### 3. Serena - IDE Assistant

**Purpose**: Advanced IDE assistance and project context understanding

```json
{
  "mcpServers": {
    "serena": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/oraios/serena",
        "serena-mcp-server",
        "--context",
        "ide-assistant",
        "--project",
        "/path/to/your/project"
      ],
      "env": {}
    }
  }
}
```

**About Serena**:
- Open-source coding agent toolkit by Oraios
- Transforms LLMs into advanced coding agents
- Decoupled from specific LLMs, frameworks, or interfaces
- Supports multiple programming languages via language servers
- Free and open-source alternative to proprietary coding assistants

**Key Capabilities**:
- **Semantic Code Analysis**: IDE-like symbolic code understanding
- **Multi-Language Support**: Works with various programming languages
- **LLM Integration**: Compatible with Claude, Codex, Gemini, and others
- **Flexible Integration**: Supports MCP server, tool calling, agent frameworks
- **Large Project Optimization**: Excels in complex, large codebases

**Features**:
- Semantic code retrieval and editing
- Precise code finding and referencing
- Symbol-level code understanding
- Project-aware code assistance
- Context-sensitive suggestions
- IDE integration capabilities

**Use Cases**:
- Enhancing coding agents in large, complex projects
- Intelligent code completion and navigation
- Context-aware refactoring and code editing
- Code analysis and architectural insights
- Boosting productivity in enterprise-scale development

**Performance Notes**:
- Most effective in large, complex projects
- May provide less value in very small projects
- Less useful when creating code from scratch
- Significant productivity boost reported by users

**Setup Notes**:
- Uses `uvx` (Python package runner)
- Installs from GitHub repository
- Requires project path configuration
- Context set to "ide-assistant"

---

## Claude Code Integration

### Using MCP Servers with Claude Code

Claude Code has built-in support for Model Context Protocol servers, allowing seamless integration with external tools and services. This extends Claude Code's capabilities beyond local file system and shell commands.

#### Configuration Methods

**1. Command Line Configuration**
```bash
# Load MCP configuration at startup
claude --mcp-config mcp.json

# Load multiple configurations
claude --mcp-config config1.json config2.json
```

**2. Project Configuration**
Place `mcp.json` in your project's `.claude/` directory:
```bash
.claude/
└── mcp.json
```

**3. User Configuration**
Global MCP settings in `~/.claude/mcp.json`

#### Interactive MCP Management

Within a Claude Code session:
```bash
# List connected MCP servers
/mcp

# Connect to a server
/mcp connect github

# Disconnect from a server
/mcp disconnect github

# List available MCP tools
/mcp tools
```

#### Example: Using GGrep with Claude Code

```json
{
  "mcpServers": {
    "ggrep": {
      "type": "http",
      "url": "https://mcp.grep.app"
    }
  }
}
```

Once configured:
```bash
claude --mcp-config mcp.json

# In the session
"Search for implementations of binary search algorithms across GitHub"
# Claude Code will use ggrep MCP server to search repositories
```

#### Example: GitHub Integration

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "YOUR_GITHUB_TOKEN"
      }
    }
  }
}
```

Usage in Claude Code:
```bash
claude --mcp-config github-mcp.json

# In the session
"Create an issue for the bug we just found"
"Check the status of PR #123"
"List open issues labeled as 'high-priority'"
```

#### Example: Serena for Large Projects

When working with complex codebases:
```bash
# Configure Serena for your project
claude --mcp-config serena.json

# Claude Code now has semantic understanding of your codebase
"Find all usages of the deprecated authenticate() method"
"Refactor the PaymentProcessor class to use the new API"
```

#### OAuth Authentication

Some MCP servers require OAuth authentication:
```bash
# Claude Code will prompt for authentication
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp

# Follow the OAuth flow in your browser
# Press Esc to cancel if needed
```

#### MCP Server Scopes

Claude Code supports different configuration scopes:

- **Local**: Project-specific servers (`.claude/mcp.json`)
- **User**: Personal servers across projects (`~/.claude/mcp.json`)
- **Project**: Team-shared configurations (checked into version control)

#### Auto-Connect Configuration

Configure servers to connect automatically:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "autoConnect": true
    }
  }
}
```

#### Troubleshooting MCP in Claude Code

```bash
# Enable verbose logging
claude --verbose --mcp-config mcp.json

# Check MCP connection status
/mcp

# View available tools from connected servers
/mcp tools

# Debug configuration issues
cat ~/.claude/mcp.json | claude -p "Check this MCP configuration for errors"
```

#### Best Practices for Claude Code + MCP

1. **Security**: Store tokens in environment variables
   ```bash
   export GITHUB_TOKEN="your-token"
   claude --mcp-config mcp.json
   ```

2. **Performance**: Connect only needed servers
   ```bash
   # Development session
   claude --mcp-config dev-servers.json
   
   # Documentation session
   claude --mcp-config doc-servers.json
   ```

3. **Organization**: Group related servers
   ```json
   {
     "mcpServers": {
       "development": { ... },
       "monitoring": { ... },
       "documentation": { ... }
     }
   }
   ```

See the [Claude Code Guide](../claude-code/claude-code-guide.md) for more details on MCP integration and advanced usage patterns.

---

## Security Considerations

### API Tokens
- Store tokens securely
- Use environment variables when possible
- Regularly rotate access tokens
- Follow principle of least privilege

### Network Access
- HTTP servers require internet connectivity
- Consider firewall and proxy configurations
- Validate server URLs and certificates

## Troubleshooting

### Common Issues
1. **Authentication failures**: Check token validity and permissions
2. **Network connectivity**: Verify URLs and network access
3. **Installation issues**: Ensure required tools (`uvx`, `npx`) are available
4. **Path configuration**: Verify project paths are correct and accessible

### Debug Steps
1. Check MCP server logs
2. Verify configuration syntax
3. Test network connectivity
4. Validate authentication credentials

## Best Practices

1. **Configuration Management**:
   - Use environment variables for sensitive data
   - Version control configuration files (without secrets)
   - Document server purposes and usage

2. **Performance**:
   - Monitor server response times
   - Configure appropriate timeouts
   - Consider caching strategies

3. **Maintenance**:
   - Keep servers updated
   - Monitor deprecation notices
   - Test configurations regularly

This configuration enables powerful code search, GitHub integration, and intelligent IDE assistance through MCP servers.