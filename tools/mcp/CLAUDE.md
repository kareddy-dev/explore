# MCP Documentation Context

Specialized guidance for Model Context Protocol (MCP) documentation in `tools/mcp/`.

## Directory Contents

This directory contains **2 comprehensive MCP guides**:

### 1. mcp-servers-guide.md
**Purpose**: Guide to popular MCP servers and integration patterns

**Covers**:
- **ggrep**: Code search across GitHub repositories
- **GitHub Copilot**: AI pair programming integration
- **Serena**: IDE assistant for Claude Code
- **Claude Code MCP Integration**: Using Claude Code as an MCP server

**Use cases**:
- Setting up external MCP servers
- Configuring authentication
- Integration patterns

### 2. sequential-thinking-guide.md
**Purpose**: Advanced problem-solving methodology using the sequential thinking tool

**Covers**:
- Step-by-step reasoning with the sequential-thinking MCP server
- Dynamic thought adjustment
- Branching and revision patterns
- Hypothesis generation and verification
- Problem-solving workflows

**Use cases**:
- Complex multi-step problem solving
- Structured reasoning about design decisions
- Iterative refinement of solutions

## MCP Configuration Reference

The repository includes a working MCP configuration at **root level**:

**File**: `/mcp.json`
```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

This serves as:
- A functional example for users
- A template for creating new MCP configurations
- Active configuration for this repository's sequential-thinking capability

## Content Standards for MCP Documentation

When documenting MCP servers:

### Required Sections
1. **Overview**: What the server does (2-3 sentences)
2. **Installation**: How to install and configure
3. **Authentication**: Security setup (if applicable)
4. **Configuration**: MCP config file examples
5. **Usage Examples**: Practical use cases
6. **Troubleshooting**: Common issues and solutions

### Security Considerations
- **Never include actual API keys or tokens**
- Use placeholders: `YOUR_GITHUB_TOKEN`, `YOUR_API_KEY`
- Document token scopes and permissions required
- Include security best practices
- Link to official authentication docs

### Configuration Examples
Always provide complete, working examples:
```json
{
  "mcpServers": {
    "server-name": {
      "command": "command-here",
      "args": ["arg1", "arg2"],
      "env": {
        "API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

## Integration with Claude Code Documentation

MCP documentation here complements the main Claude Code docs:

**Main Claude Code docs location**: `tools/claude-code/gen/mcp.md`
- Official MCP integration documentation
- Claude Code-specific MCP features
- Built-in MCP servers

**This directory focuses on**:
- Popular community MCP servers
- Advanced MCP patterns
- Specialized MCP tools (sequential-thinking, ggrep, etc.)

**Cross-reference appropriately**:
- Link to official MCP docs for basics
- Provide specialized guidance for specific servers
- Include integration examples with Claude Code

## Update Triggers

Update MCP documentation when:

1. **New MCP server becomes popular**
   - Research the server
   - Create integration guide
   - Add to mcp-servers-guide.md

2. **MCP protocol changes**
   - Review official MCP spec
   - Update configuration examples
   - Test existing examples

3. **Claude Code MCP integration updates**
   - Check official docs (tools/claude-code/gen/mcp.md)
   - Update integration patterns
   - Sync configuration examples

4. **Security best practices evolve**
   - Update authentication sections
   - Enhance security warnings
   - Add new token management patterns

## Common MCP Workflows

### Adding a New MCP Server Guide

```bash
# 1. Research the server
# - Official documentation
# - npm package details
# - Authentication requirements

# 2. Test the configuration
# - Create mcp.json
# - Test with Claude Code
# - Verify functionality

# 3. Document in mcp-servers-guide.md
# - Add server section
# - Include configuration
# - Provide use cases
# - Add troubleshooting

# 4. Update README if significant
# - Add to navigation if major server
```

### Updating Existing MCP Documentation

```bash
# 1. Check for changes
# - MCP server version updates
# - API changes
# - New features

# 2. Update affected sections
# - Configuration examples
# - Authentication flows
# - Usage patterns

# 3. Validate examples
# - Test configurations
# - Verify token scopes
# - Check error handling
```

## Quick Reference: Popular MCP Servers

Current documentation coverage:

| Server | Purpose | Auth Type | Doc Status |
|--------|---------|-----------|------------|
| sequential-thinking | Problem solving | None | ✅ Complete guide |
| ggrep | GitHub code search | GitHub PAT | ✅ In servers guide |
| GitHub Copilot | AI pair programming | OAuth | ✅ In servers guide |
| Serena | IDE assistant | None | ✅ In servers guide |
| Claude Code as server | Tool exposure | None | ✅ In servers guide |

## Quality Checklist

Before completing MCP documentation:

- [ ] All configuration examples are valid JSON
- [ ] Security placeholders used (no real tokens)
- [ ] Installation steps are tested
- [ ] Authentication flow is clear
- [ ] Troubleshooting covers common errors
- [ ] Links to official docs included
- [ ] Integration with Claude Code explained
- [ ] Use cases are practical and relevant

## MCP Resources

**Official**:
- [MCP Specification](https://modelcontextprotocol.io)
- [MCP Servers Repository](https://github.com/modelcontextprotocol/servers)

**Claude Code Integration**:
- Main docs: `../claude-code/gen/mcp.md`
- MCP config: `../../mcp.json` (root level)

**This Directory**:
- `mcp-servers-guide.md` - Popular servers and patterns
- `sequential-thinking-guide.md` - Advanced problem-solving

---

*MCP servers extend Claude Code's capabilities. Document them clearly, test thoroughly, and prioritize security.*
