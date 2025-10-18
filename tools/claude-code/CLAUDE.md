# Claude Code Documentation Context

Specialized guidance when working in the `tools/claude-code/` directory.

## Directory Purpose

This directory contains comprehensive Claude Code documentation with two distinct types:

### 1. Curated Guides (Root Level) - 🔵 MANUALLY MAINTAINED

**15 files** providing expert insights, practical examples, and real-world patterns:

- **README.md**: Navigation hub linking to all 44 official docs
- **CLAUDE-CODE-UPDATE-INFO.md**: Version tracking (v1.0.88+) and change summaries
- **claude-code-guide.md**: Comprehensive overview (installation, features, agents, MCP)
- **cli-reference.md**: Complete CLI reference (commands, flags, environment vars)
- **plugin-ecosystem-guide.md**: Plugin system guide (5 components including Skills)
- **workflow-examples.md**: Practical development workflows and patterns
- **hooks-cookbook.md**: Hook automation patterns and recipes
- **advanced-techniques.md**: Expert patterns from Ray Fernando and Eric Buess
- **context-management.md**: Context optimization strategies (50% rule)
- **performance-optimization.md**: Performance tuning for large codebases
- **subagent-templates.md**: Pre-built subagent configurations
- **subagent-workflows-guide.md**: Practical subagent development patterns
- **bash-apps-cli-agents.md**: CLI tool integration with Click framework
- **custom-commands.md**: Reusable slash command library
- **community-resources.md**: Frameworks, tools, IDE integrations catalog

### 2. Official Documentation (gen/) - 🟢 AUTO-FETCHED

**44 files** fetched from Anthropic's documentation:

- **⚠️ READ-ONLY**: Never edit these files directly
- **Auto-overwritten**: fetch-docs.py replaces them on updates
- **Source of truth**: Authoritative feature documentation from Anthropic

## Critical Rules

### DO ✅
- **Read CLAUDE-CODE-UPDATE-INFO.md first** for version context
- **Edit curated guides** (root level .md files) when needed
- **Update curated guides** when official docs change
- **Preserve expert insights** and practical examples in curated guides
- **Use Mermaid diagrams** for complex concepts
- **Include practical code examples** with language identifiers
- **Link updates** from README.md navigation table

### DON'T ❌
- **NEVER edit files in gen/ directory** - they're auto-overwritten
- **NEVER edit .docs-manifest.json** - managed by fetch-docs.py
- **DON'T create new files** without explicit request
- **DON'T document deprecated features** (check version first)

## Recent Changes (v1.0.88+)

**Latest Update: 2025-10-18**

Critical changes affecting documentation:
- **Skills system**: Added as 5th plugin component (model-invoked)
- **MultiEdit deprecated**: Removed from Claude Code entirely
- **New shortcuts**: Ctrl+O (verbose), Ctrl+V (paste image), @ (autocomplete), ? (help)
- **Homebrew install**: `brew install --cask claude-code`
- **Prompt caching**: Fine-grained environment variable control
- **Haiku 4.5**: New default for Bedrock/Vertex AI (manual upgrade required)

## Common Synchronization Patterns

When official docs change, update curated guides:

### Pattern 1: Feature Added (e.g., Skills)
```bash
# 1. Identify affected curated files
grep -r "plugin" *.md --exclude-dir=gen

# 2. Update each file:
# - Add Skills to architecture diagrams
# - Update component lists (4 → 5 components)
# - Add Skills examples and usage
# - Link to official Skills documentation
```

### Pattern 2: Feature Removed (e.g., MultiEdit)
```bash
# 1. Find all references
grep -r "MultiEdit" *.md --exclude-dir=gen

# 2. Remove from all locations:
# - Tool lists
# - Examples
# - Workflow patterns
# - Hook configurations
```

### Pattern 3: Feature Updated (e.g., New Shortcuts)
```bash
# 1. Update relevant guides:
# - cli-reference.md: Add to keyboard shortcuts table
# - claude-code-guide.md: Update interactive mode section
# - README.md: Update "What's New" section
```

## File Maintenance Matrix

| File Type | Edit? | Update Trigger | Validation |
|-----------|-------|----------------|------------|
| Curated guides (*.md) | ✅ Yes | Official doc changes, user feedback | Manual review |
| Official docs (gen/*.md) | ❌ No | Auto-fetched | Automatic |
| README.md | ✅ Yes | New docs added, navigation changes | Check links |
| CLAUDE-CODE-UPDATE-INFO.md | ✅ Yes | Every documentation update | Version check |
| .docs-manifest.json | ❌ No | Auto-managed by fetch-docs.py | Automatic |

## Quality Standards

All curated documentation must include:

1. **Clear structure**: Title, overview, examples, troubleshooting
2. **Mermaid diagrams**: For workflows, architectures, decision trees
3. **Code examples**: With proper language identifiers (```bash, ```json)
4. **Practical patterns**: Real-world usage scenarios
5. **Current information**: Verified against v1.0.88+
6. **No secrets**: Use placeholders like `YOUR_TOKEN`
7. **Internal links**: Relative paths to other docs

## Navigation Efficiency

Instead of searching, use PROJECT_INDEX.json at repository root:
```json
{
  "tools/claude-code/": {
    "curated_guides": { "count": 15, ... },
    "official_docs": { "location": "gen/", "count": 44 }
  }
}
```

## When to Update This Directory

### Trigger 1: Official Documentation Update
```bash
# After running fetch-docs.py
python ../../tools/scripts/fetch-docs.py --source claude-code

# Review changes
git diff gen/

# Update affected curated guides
# Update CLAUDE-CODE-UPDATE-INFO.md
```

### Trigger 2: Claude Code Version Release
```bash
# Check Anthropic's repository
# Update version references in:
# - CLAUDE-CODE-UPDATE-INFO.md
# - Root CLAUDE.md (version awareness section)
# - README.md (if major features added)
```

### Trigger 3: Community Feedback or Corrections
```bash
# Review the correction
# Update affected curated guide
# Verify accuracy against official docs
# Test examples if applicable
```

## Subagent Usage for Large Updates

When official docs have many changes, preserve context with subagents:

```bash
# Analyze all changes without polluting main context
claude "Spawn subagent to analyze all changes in gen/ directory
and return categorized summary: new features, deprecations, updates"

# Parallel updates
claude "Spawn 3 subagents to update curated guides:
1. plugin-ecosystem-guide.md - Skills integration
2. cli-reference.md - new keyboard shortcuts
3. claude-code-guide.md - Homebrew installation
Each returns brief completion report"
```

## Integration with Parent CLAUDE.md

This specialized context supplements the root CLAUDE.md. When working here:
- Root CLAUDE.md provides general documentation workflows
- This file provides Claude Code-specific patterns
- Both contexts are active (hierarchical loading)
- Use context efficiently with PROJECT_INDEX.json

---

*Remember: Curated guides are our value-add. Official docs are the source of truth. Keep them synchronized but distinct.*
