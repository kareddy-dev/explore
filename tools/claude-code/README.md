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
      CLI Tool Agents
      Advanced Techniques
    Cookbooks
      Hooks Recipes
      Custom Commands
      Subagent Templates
      Subagent Workflows
    Frameworks
      BMAD-METHOD
      Development Methodologies
```

## ✨ What's New (October 2025)

### New Documentation
- 🔌 **Plugin System** - Extend Claude Code with custom commands, agents, and MCP servers
- 💻 **IDE Integrations** - Native JetBrains and VS Code extensions with quick launch
- 🤖 **Headless Mode** - Run Claude Code programmatically without terminal UI
- 💾 **Session Checkpointing** - Save and restore conversation sessions
- 🔄 **Migration Guide** - Smooth upgrades between versions
- ⚙️ **Advanced Config** - Model and network configuration options
- 🚀 **GitLab CI/CD** - GitLab integration (complementing GitHub Actions)

### Updated Documentation
41 documents updated with latest features and improvements (44 total official docs)

### New Community Guides
- 🌍 **Plugin Ecosystem Guide** - Complete guide to creating and using Claude Code plugins
- 🛠️ **Community Resources** - Comprehensive catalog of frameworks, tools, and IDE integrations
  - SuperClaude Framework (14 agents, 21 commands)
  - Spec Workflow for structured development
  - IDE integrations (Neovim, VS Code, Theia)
  - Web UIs, notification systems, and automation tools

## 🎯 Quick Navigation

### By Task

| What You Want to Do | Where to Look |
|---------------------|---------------|
| **Get Started** | [Quickstart](gen/quickstart.md) → [Setup](gen/setup.md) |
| **Learn Commands** | [CLI Reference](cli-reference.md) → [Slash Commands](gen/slash-commands.md) |
| **Build Features** | [Workflow Examples](workflow-examples.md) → [Common Workflows](gen/common-workflows.md) |
| **Use Subagents** | [Subagent Workflows Guide](subagent-workflows-guide.md) → [Subagent Templates](subagent-templates.md) |
| **Connect Tools** | [MCP Integration](gen/mcp.md) → [MCP Servers Guide](../mcp/mcp-servers-guide.md) |
| **Extend with Plugins** | [Plugin System](gen/plugins.md) → [Plugin Ecosystem Guide](plugin-ecosystem-guide.md) → [Community Resources](community-resources.md) |
| **IDE Integration** | [JetBrains](gen/jetbrains.md) → [VS Code](gen/vs-code.md) → [Dev Containers](gen/devcontainer.md) |
| **Community Tools** | [Community Resources](community-resources.md) → [SuperClaude Framework](community-resources.md#superclaude-framework) → [Spec Workflow](community-resources.md#claude-code-spec-workflow) |
| **Use AI Frameworks** | [BMAD-METHOD](frameworks/bmad-method.md) → [Structured Development Workflow](frameworks/bmad-method.md#workflow-phases) |
| **Build CLI Agents** | [Bash Apps Guide](bash-apps-cli-agents.md) → [CLI Tool Integration Patterns](bash-apps-cli-agents.md#templates) |
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
1. [Anthropic Best Practices](anthropic-best-practices.md) - Internal usage patterns from Anthropic's Applied AI team
2. [Plugin System](gen/plugins.md) - Extend Claude Code with custom plugins
3. [Hooks Cookbook](hooks-cookbook.md) - Automation patterns
4. [Custom Commands](custom-commands.md) - Build your command library
5. [BMAD-METHOD Framework](frameworks/bmad-method.md) - Structured AI agent workflows
6. [Headless Mode](gen/headless.md) - Run Claude Code without terminal UI
7. [Performance Optimization](performance-optimization.md) - Handle large codebases

## 📂 Complete File Index

### Core Documentation

#### Curated Guides (Experience-Based)
- [`claude-code-guide.md`](claude-code-guide.md) - Comprehensive overview with architecture, MCP, best practices
- [`anthropic-best-practices.md`](anthropic-best-practices.md) - Internal usage patterns and tips from Anthropic's Applied AI team
- [`cli-reference.md`](cli-reference.md) - Complete CLI commands, flags, and configurations
- [`workflow-examples.md`](workflow-examples.md) - Practical examples for real development scenarios

#### Cookbooks & Templates (New)
- [`subagent-workflows-guide.md`](subagent-workflows-guide.md) - Complete guide to practical subagent development workflows
- [`bash-apps-cli-agents.md`](bash-apps-cli-agents.md) - Build intelligent CLI tool agents with Click framework
- [`hooks-cookbook.md`](hooks-cookbook.md) - Advanced hook patterns and recipes
- [`custom-commands.md`](custom-commands.md) - Library of useful custom slash commands
- [`subagent-templates.md`](subagent-templates.md) - Pre-built subagent configurations
- [`performance-optimization.md`](performance-optimization.md) - Best practices for large codebases

#### Ecosystem & Community
- [`plugin-ecosystem-guide.md`](plugin-ecosystem-guide.md) - Complete guide to Claude Code plugin system
- [`community-resources.md`](community-resources.md) - Catalog of frameworks, tools, and IDE integrations

#### Development Frameworks
- [`frameworks/bmad-method.md`](frameworks/bmad-method.md) - BMAD-METHOD integration for structured AI development workflows

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
- [`model-config.md`](gen/model-config.md) - Model configuration
- [`network-config.md`](gen/network-config.md) - Network configuration
- [`migration-guide.md`](gen/migration-guide.md) - Version migration guide

#### Advanced Features
- [`mcp.md`](gen/mcp.md) - Model Context Protocol
- [`plugins.md`](gen/plugins.md) - Plugin system
- [`plugins-reference.md`](gen/plugins-reference.md) - Plugin technical specs
- [`plugin-marketplaces.md`](gen/plugin-marketplaces.md) - Plugin marketplaces
- [`headless.md`](gen/headless.md) - Headless mode
- [`checkpointing.md`](gen/checkpointing.md) - Session checkpointing
- [`github-actions.md`](gen/github-actions.md) - GitHub Actions integration
- [`gitlab-ci-cd.md`](gen/gitlab-ci-cd.md) - GitLab CI/CD integration

#### IDE Integrations
- [`jetbrains.md`](gen/jetbrains.md) - JetBrains IDEs (IntelliJ, PyCharm, WebStorm)
- [`vs-code.md`](gen/vs-code.md) - Visual Studio Code integration
- [`devcontainer.md`](gen/devcontainer.md) - Dev container support

#### Enterprise & Cloud
- [`amazon-bedrock.md`](gen/amazon-bedrock.md) - AWS Bedrock setup
- [`google-vertex-ai.md`](gen/google-vertex-ai.md) - Google Vertex setup
- [`llm-gateway.md`](gen/llm-gateway.md) - LLM gateway setup

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
4. **Plugin System**: Extend Claude Code with custom commands, agents, and hooks
5. **Custom Commands**: Create reusable prompts as slash commands
6. **MCP Servers**: Connect to 70+ external tools and services
7. **IDE Integration**: Native JetBrains and VS Code extensions

### Common Patterns
- Start broad with codebase questions, then narrow down
- Use subagents for specialized tasks to preserve context
- Configure hooks for automatic formatting and validation
- Create project-specific CLAUDE.md for team conventions

## 🤝 Related Resources

### Official & Curated Guides
- [Plugin Ecosystem Guide](plugin-ecosystem-guide.md) - Claude Code plugin system
- [Community Resources](community-resources.md) - Frameworks, tools, and integrations
- [MCP Servers Guide](../mcp/mcp-servers-guide.md) - Connect external tools
- [Sequential Thinking Guide](../mcp/sequential-thinking-guide.md) - Advanced problem-solving
- [BMAD-METHOD Framework](frameworks/bmad-method.md) - Structured AI agent development workflows
- [Chrome Extensions](../chrome-extensions/) - Browser productivity tools

### Community Frameworks
- [SuperClaude Framework](community-resources.md#superclaude-framework) - 14 agents, 21 commands, 6 modes
- [Claude Code Spec Workflow](community-resources.md#claude-code-spec-workflow) - Spec-driven development
- [Subagents Collection](community-resources.md#claude-code-subagents-collection) - Specialized AI agents

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

*Last Updated: October 2025 | Documentation Version: 1.1 | 44 Official Docs*