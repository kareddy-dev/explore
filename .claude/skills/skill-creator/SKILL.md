---
name: Skill Creator
description: Create new Claude Code skills following best practices. Use when you need to build custom skills for specific workflows, tools, or domain expertise. Generates properly structured SKILL.md files with optional supporting documentation.
allowed-tools: Write, Read, Glob, mcp__ggrep__searchGitHub
---

# Skill Creator

Create new Claude Code skills following official patterns and community best practices.

## Instructions

### 1. Clarify Skill Purpose

Ask the user:
- What capability should this skill provide?
- When should it activate? (trigger words)
- What tools does it need?
- Personal or team skill?

### 2. Research Similar Skills

Use ggrep to find examples:
```javascript
{
  query: "name:",
  path: "SKILL.md",
  language: ["Markdown"]
}
```

### 3. Choose Template

Select from [references/templates.md](references/templates.md):
- CLI Tool Wrapper
- Workflow/Process
- Domain Expertise
- Code Generator
- API Integration
- Testing/Validation
- Configuration Management

### 4. Create Structure

**Location:**
- Personal: `~/.claude/skills/<skill-name>/`
- Project: `.claude/skills/<skill-name>/`

**Files:**
- `SKILL.md` - Core (keep under 150 lines)
- `references/` - Optional detailed docs
- `scripts/` - Optional helper scripts
- `assets/` - Optional templates

### 5. Write SKILL.md

**Critical: Keep it concise!**

**Minimal structure:**
```markdown
---
name: Clear Name
description: What it does. Use when <triggers>. <Keywords>.
allowed-tools: Tool1, Tool2(pattern:*)
---

# Skill Name

Brief overview.

## Instructions
Step-by-step guidance (be specific)

## Examples
Tested examples with results

## Best Practices
✅ DO / ❌ DON'T

## Additional Resources
- references/file.md: Description
```

### 6. Write Effective Description

**Formula:**
```yaml
description: <Core capability>. Use when <trigger scenarios>. <Domain keywords>.
```

**Good:**
```yaml
description: Query logs in Grafana Loki via logcli. Use when user asks to pull logs, analyze patterns, or debug using Loki logs.
```

**Bad:**
```yaml
description: Helps with logs
```

See [references/discovery.md](references/discovery.md) for detailed guidance.

### 7. Test Activation

1. Restart Claude Code
2. Ask natural question matching triggers
3. Verify skill activates
4. Refine description if needed

## Examples

### Example 1: Simple Tool Skill
```markdown
---
name: JSON Formatter
description: Format and validate JSON using jq. Use when working with JSON files, formatting code, or validating syntax.
allowed-tools: Read, Edit, Bash(jq:*)
---

# JSON Formatter

## Instructions
1. Read target JSON file
2. Validate: `jq empty file.json`
3. Format: `jq '.' file.json > formatted.json`

## Examples
**Format:**
```bash
jq '.' input.json > formatted.json
```
```

### Example 2: Skill with References
```markdown
---
name: API Integration Guide
description: Integrate external APIs with auth, error handling, retries. Use when working with REST APIs, GraphQL, or webhooks.
---

# API Integration Guide

## Instructions
1. Setup authentication (see references/auth.md)
2. Implement endpoints
3. Add error handling (see references/errors.md)

## Additional Resources
- references/auth.md: Authentication patterns
- references/errors.md: Error handling
```

## Skill Structures

**Minimal:**
```
skill-name/
└── SKILL.md
```

**With docs:**
```
skill-name/
├── SKILL.md
└── references/
    ├── detailed.md
    └── examples.md
```

**Complete:**
```
skill-name/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

## Best Practices

✅ Keep SKILL.md under 150 lines
✅ Move details to references/
✅ Write specific descriptions with triggers
✅ Use allowed-tools to restrict scope
✅ Research real skills with ggrep first
✅ Test with natural language questions

❌ Create encyclopedic SKILL.md
❌ Write vague descriptions
❌ Skip testing activation
❌ Forget to link to references

## Troubleshooting

**Skill won't activate:**
- Add more trigger words to description
- Check YAML frontmatter is valid
- Test with different phrasings

**Skill activates wrong:**
- Make description more specific
- Check for keyword conflicts
- Add "NOT for X" clarifications

See [references/discovery.md](references/discovery.md) for complete troubleshooting.

## Additional Resources

- **references/templates.md**: 7 ready-to-use templates for common skill types
- **references/patterns.md**: 15 production patterns from real skills
- **references/discovery.md**: Complete guide to making skills discoverable

Search GitHub for real examples:
```javascript
{
  query: "name:",
  path: "SKILL.md",
  language: ["Markdown"]
}
```
