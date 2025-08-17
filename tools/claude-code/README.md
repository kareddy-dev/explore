# Claude Code Documentation Hub

Welcome to the comprehensive documentation for Claude Code - Anthropic's agentic coding tool that lives in your terminal. This hub provides both official reference documentation and practical, experience-based guides.

## 🚀 Quick Start

```bash
# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Start coding
cd your-project
claude
```

## 📚 Documentation Structure

```mermaid
mindmap
  root((Claude Code Docs))
    Official Docs
      Setup & Installation
      CLI Reference
      Core Features
      Enterprise
      Integrations
    Curated Guides
      Practical Examples
      Workflow Patterns
      Advanced Techniques
    Cookbooks
      Hooks Recipes
      Custom Commands
      Subagent Templates
```

## 🎯 Quick Navigation

### By Task

| What You Want to Do | Where to Look |
|---------------------|---------------|
| **Get Started** | [Quickstart](gen/quickstart.md) → [Setup](gen/setup.md) |
| **Learn Commands** | [CLI Reference](cli-reference.md) → [Slash Commands](gen/slash-commands.md) |
| **Build Features** | [Workflow Examples](workflow-examples.md) → [Common Workflows](gen/common-workflows.md) |
| **Use Subagents** | [Subagents Guide](gen/sub-agents.md) → [Subagent Templates](subagent-templates.md) |
| **Connect Tools** | [MCP Integration](gen/mcp.md) → [MCP Servers Guide](../mcp/mcp-servers-guide.md) |
| **Customize Behavior** | [Output Styles](gen/output-styles.md) → [Hooks Guide](gen/hooks-guide.md) |
| **Debug Issues** | [Troubleshooting](gen/troubleshooting.md) → [Performance Guide](performance-optimization.md) |
| **Enterprise Setup** | [Security](gen/security.md) → [Amazon Bedrock](gen/amazon-bedrock.md) → [Google Vertex](gen/google-vertex-ai.md) |

### By Experience Level

#### 🌱 Beginners
1. [Overview](gen/overview.md) - Understand what Claude Code does
2. [Quickstart](gen/quickstart.md) - Get running in 5 minutes
3. [Interactive Mode](gen/interactive-mode.md) - Learn the REPL interface
4. [Common Workflows](gen/common-workflows.md) - Basic patterns

#### 🌿 Intermediate Users
1. [Claude Code Guide](claude-code-guide.md) - Comprehensive overview with diagrams
2. [Workflow Examples](workflow-examples.md) - Real-world scenarios
3. [Memory Management](gen/memory.md) - Configure CLAUDE.md files
4. [Subagents](gen/sub-agents.md) - Create specialized assistants

#### 🌳 Advanced Users
1. [Hooks Cookbook](hooks-cookbook.md) - Automation patterns
2. [Custom Commands](custom-commands.md) - Build your command library
3. [SDK Guide](gen/sdk.md) - Build custom agents
4. [Performance Optimization](performance-optimization.md) - Handle large codebases

## 📂 Complete File Index

### Core Documentation

#### Curated Guides (Experience-Based)
- [`claude-code-guide.md`](claude-code-guide.md) - Comprehensive overview with architecture, MCP, best practices
- [`cli-reference.md`](cli-reference.md) - Complete CLI commands, flags, and configurations
- [`workflow-examples.md`](workflow-examples.md) - Practical examples for real development scenarios

#### Cookbooks & Templates (New)
- [`hooks-cookbook.md`](hooks-cookbook.md) - Advanced hook patterns and recipes
- [`custom-commands.md`](custom-commands.md) - Library of useful custom slash commands
- [`subagent-templates.md`](subagent-templates.md) - Pre-built subagent configurations
- [`performance-optimization.md`](performance-optimization.md) - Best practices for large codebases

### Official Documentation (gen/)

#### Getting Started
- [`overview.md`](gen/overview.md) - Product overview
- [`quickstart.md`](gen/quickstart.md) - Quick start guide
- [`setup.md`](gen/setup.md) - Installation and setup
- [`common-workflows.md`](gen/common-workflows.md) - Common usage patterns

#### Core Features
- [`interactive-mode.md`](gen/interactive-mode.md) - REPL interface
- [`slash-commands.md`](gen/slash-commands.md) - All slash commands
- [`sub-agents.md`](gen/sub-agents.md) - Subagent system
- [`output-styles.md`](gen/output-styles.md) - Output customization
- [`memory.md`](gen/memory.md) - Memory management

#### Configuration
- [`settings.md`](gen/settings.md) - Settings configuration
- [`hooks.md`](gen/hooks.md) - Hooks reference
- [`hooks-guide.md`](gen/hooks-guide.md) - Hooks tutorial
- [`terminal-config.md`](gen/terminal-config.md) - Terminal setup
- [`statusline.md`](gen/statusline.md) - Status line configuration

#### Advanced Features
- [`mcp.md`](gen/mcp.md) - Model Context Protocol
- [`sdk.md`](gen/sdk.md) - SDK documentation
- [`github-actions.md`](gen/github-actions.md) - CI/CD integration
- [`ide-integrations.md`](gen/ide-integrations.md) - IDE integration

#### Enterprise & Cloud
- [`amazon-bedrock.md`](gen/amazon-bedrock.md) - AWS Bedrock setup
- [`google-vertex-ai.md`](gen/google-vertex-ai.md) - Google Vertex setup
- [`corporate-proxy.md`](gen/corporate-proxy.md) - Proxy configuration
- [`llm-gateway.md`](gen/llm-gateway.md) - LLM gateway setup
- [`devcontainer.md`](gen/devcontainer.md) - Dev container support

#### Security & Compliance
- [`security.md`](gen/security.md) - Security best practices
- [`iam.md`](gen/iam.md) - Permissions and access
- [`data-usage.md`](gen/data-usage.md) - Data usage policies
- [`legal-and-compliance.md`](gen/legal-and-compliance.md) - Compliance info

#### Operations
- [`monitoring-usage.md`](gen/monitoring-usage.md) - Usage monitoring
- [`costs.md`](gen/costs.md) - Pricing and costs
- [`analytics.md`](gen/analytics.md) - Analytics
- [`troubleshooting.md`](gen/troubleshooting.md) - Troubleshooting guide

#### Reference
- [`cli-reference.md`](gen/cli-reference.md) - Official CLI reference
- [`third-party-integrations.md`](gen/third-party-integrations.md) - Third-party tools

## 🔄 Documentation Updates

This documentation is maintained through two approaches:

1. **Official Documentation** (gen/): Automatically fetched from Anthropic's documentation
   ```bash
   # Check for updates
   python ../scripts/fetch-docs.py --check
   
   # Fetch latest
   python ../scripts/fetch-docs.py --source claude-code
   ```

2. **Curated Guides**: Manually maintained based on real-world usage and community feedback

## 🎨 Visual Learning

Many guides include Mermaid diagrams for visual understanding:

```mermaid
flowchart LR
    A[Your Request] --> B[Claude Code]
    B --> C{Analysis}
    C -->|Code| D[File Edits]
    C -->|Commands| E[Shell Execution]
    C -->|Tools| F[MCP Servers]
    D --> G[Results]
    E --> G
    F --> G
```

## 💡 Pro Tips

### Most Useful Features
1. **Background Processes** (Ctrl+B): Run long commands without blocking
2. **Task Management** (`/todo`): Claude tracks complex multi-step tasks
3. **Memory Files** (CLAUDE.md): Persistent project instructions
4. **Custom Commands**: Create reusable prompts as slash commands
5. **MCP Servers**: Connect to 70+ external tools and services

### Common Patterns
- Start broad with codebase questions, then narrow down
- Use subagents for specialized tasks to preserve context
- Configure hooks for automatic formatting and validation
- Create project-specific CLAUDE.md for team conventions

## 🤝 Related Resources

- [MCP Servers Guide](../mcp/mcp-servers-guide.md) - Connect external tools
- [Sequential Thinking Guide](../mcp/sequential-thinking-guide.md) - Advanced problem-solving
- [Chrome Extensions](../chrome-extensions/) - Browser productivity tools

## 📊 Documentation Coverage

| Category | Official Docs | Curated Guides | Cookbooks |
|----------|--------------|----------------|-----------|
| Setup & Installation | ✅ Complete | ✅ Enhanced | - |
| Core Features | ✅ Complete | ✅ Practical Examples | ✅ Patterns |
| Advanced Features | ✅ Reference | ⚡ In Progress | ✅ Templates |
| Enterprise | ✅ Complete | ⚡ Planned | - |
| Troubleshooting | ✅ Basic | ⚡ In Progress | - |

## 🚧 Coming Soon

- Enterprise Patterns Guide
- Troubleshooting Companion
- Output Style Gallery
- Team Collaboration Workflows

---

*Last Updated: January 2025 | Documentation Version: 1.0*