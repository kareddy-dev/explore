# Common Skill Patterns

Real-world patterns extracted from production skills. Use these as building blocks.

## Pattern 1: Progressive Disclosure with References

**When to use:** Skill has comprehensive documentation that would make SKILL.md too long.

**Structure:**
```
skill-name/
├── SKILL.md                    # Core (100-150 lines)
└── references/
    ├── detailed-guide.md       # In-depth documentation
    └── examples.md             # Extensive examples
```

**SKILL.md references:**
```markdown
For complete API reference, see [references/detailed-guide.md](references/detailed-guide.md).
```

**Example from ggrep skill:**
- SKILL.md: 140 lines with core instructions
- references/parameters.md: 314 lines with all parameters
- references/examples.md: 797 lines with 50+ examples

**Benefits:**
- Keeps SKILL.md scannable
- Claude loads details only when needed
- Saves context tokens

## Pattern 2: Tool Restriction with allowed-tools

**When to use:** Limit skill to specific safe operations or ensure focused behavior.

**Example - Read-only skill:**
```yaml
---
name: Code Reviewer
allowed-tools: Read, Grep, Glob
---
```

**Example - Specific command patterns:**
```yaml
---
name: Git Helper
allowed-tools: Bash(git:*), Read
---
```

**Example - Log analysis:**
```yaml
---
name: Grafana Loki LogCLI
allowed-tools: Bash(logcli:*)
---
```

**Benefits:**
- Prevents accidental modifications
- Improves security
- Makes skill purpose clearer

## Pattern 3: Checklist-Based Workflows

**When to use:** Multi-step processes where users should follow specific order.

**Implementation:**
```markdown
## Review Checklist

- [ ] Code organization and structure
- [ ] Error handling
- [ ] Performance considerations
- [ ] Security concerns
- [ ] Test coverage
```

**Example domains:**
- Code review processes
- Deployment workflows
- Security audits
- Configuration validation

**Benefits:**
- Ensures completeness
- Provides structure
- Easy to follow

## Pattern 4: Phase-Based Instructions

**When to use:** Complex workflows with distinct stages.

**Implementation:**
```markdown
## Instructions

### Phase 1: Research
<Instructions for research phase>

### Phase 2: Configuration
<Instructions for configuration phase>

### Phase 3: Implementation
<Instructions for implementation phase>

### Phase 4: Validation
<Instructions for validation phase>
```

**Example from ggrep skill:**
```markdown
## Subagent Workflow

1. **Research**: Search Markdown for tool documentation
2. **Configure**: Find JSON/YAML config examples
3. **Implement**: Search code for API usage patterns
4. **Validate**: Compare with production error handling
```

**Benefits:**
- Clear progression
- Prevents skipping steps
- Natural workflow

## Pattern 5: Example-Driven Documentation

**When to use:** Skills where showing is better than telling.

**Implementation:**
```markdown
## Examples

### Example 1: <Use Case> (Tested ✓)
**Input:**
```<language>
<input>
```

**Output:**
```<language>
<output>
```

**Explanation:** <why this works>
```

**Best practices:**
- Label tested examples with ✓
- Show both input and output
- Include real, working code
- Explain expected results

## Pattern 6: Common Patterns Quick Reference

**When to use:** Users need quick lookup without reading full instructions.

**Implementation:**
```markdown
## Common Patterns

- Setup: `command1`, `command2`, `command3`
- Config: `file1`, `file2`, `file3`
- Usage: `pattern1`, `pattern2`, `pattern3`
```

**Example from ggrep skill:**
```markdown
## Common Patterns

- Setup: `## Installation`, `## Setup`, `## Getting Started`
- Config: `config.json`, `settings.yaml`, `.env`
- CLI: `npm install`, `pip install`, `docker run`
```

**Benefits:**
- Quick reference
- Reduces need to read full docs
- Easy to scan

## Pattern 7: DO/DON'T Best Practices

**When to use:** Help users avoid common mistakes.

**Implementation:**
```markdown
## Best Practices

✅ DO: <Good practice>
✅ DO: <Good practice>

❌ DON'T: <Common mistake>
❌ DON'T: <Common mistake>
```

**Tips:**
- Use actual mistakes you've seen
- Explain why (briefly)
- Pair DON'Ts with DO alternatives

## Pattern 8: Scripts for Automation

**When to use:** Skill involves repetitive or complex commands.

**Structure:**
```
skill-name/
├── SKILL.md
└── scripts/
    ├── validate.sh       # Validation script
    └── generate.py       # Generation script
```

**SKILL.md references:**
```markdown
Run validation:
```bash
bash scripts/validate.sh input.txt
```
```

**Example - Helm chart validation:**
```
helm-chart-scaffolding/
├── SKILL.md
└── scripts/
    └── validate-chart.sh
```

**Benefits:**
- Consistent execution
- Less error-prone
- Reusable logic

## Pattern 9: Asset Templates

**When to use:** Skill generates files from templates.

**Structure:**
```
skill-name/
├── SKILL.md
└── assets/
    ├── template.json     # JSON template
    └── config.yaml       # YAML template
```

**Usage in SKILL.md:**
```markdown
Use template:
```bash
cp assets/template.json project/config.json
# Edit config.json with specific values
```
```

**Example structures:**
- Configuration templates
- Code scaffolding templates
- Documentation templates

## Pattern 10: Multi-File Reference Organization

**When to use:** Different aspects of skill need separate documentation.

**Structure:**
```
skill-name/
├── SKILL.md
└── references/
    ├── getting-started.md    # Basics
    ├── advanced.md           # Advanced topics
    ├── api-reference.md      # API details
    └── troubleshooting.md    # Common issues
```

**Example from api-design-principles:**
```
api-design-principles/
├── SKILL.md
└── references/
    ├── rest-best-practices.md
    └── graphql-schema-design.md
```

**Link from SKILL.md:**
```markdown
## Additional Resources

- **references/getting-started.md**: Quick start guide
- **references/advanced.md**: Advanced patterns
- **references/api-reference.md**: Complete API documentation
```

## Pattern 11: Inline Parameter Documentation

**When to use:** Skill has parameters that need explanation.

**Implementation:**
```markdown
### Parameters

**Required:**
- `param1` (type): Description

**Optional:**
- `param2` (type): Description
  - Default: value
  - Examples: value1, value2
```

**Example from ggrep skill:**
```markdown
### Optional Parameters

- **`language`** (array): Filter by programming language(s)
  - Examples: `["Markdown"]`, `["Python"]`
  - Common values: TypeScript, TSX, JavaScript, Python
```

## Pattern 12: Troubleshooting Section

**When to use:** Users commonly encounter specific issues.

**Implementation:**
```markdown
## Troubleshooting

### Issue 1: <Symptom>
**Cause:** <Why it happens>
**Solution:** <How to fix>

### Issue 2: <Symptom>
**Cause:** <Why it happens>
**Solution:** <How to fix>
```

**Example structure:**
- Symptom (what user sees)
- Cause (why it happens)
- Solution (specific steps)

## Pattern 13: Context-Aware Descriptions

**When to use:** Always - description determines skill activation.

**Pattern:**
```yaml
description: <What it does>. Use when <specific triggers>. <Keywords users mention>.
```

**Good examples:**
```yaml
# Specific with triggers
description: Query and explore logs in Grafana Loki via logcli. Use when user asks to pull logs, analyze log patterns, or debug using Loki logs.

# Domain keywords
description: Search millions of GitHub repos for real code patterns, API examples, configuration guides. Use when you need to find how developers implement features, configure tools, or document APIs.
```

**Bad examples:**
```yaml
# Too vague
description: Helps with logs

# No triggers
description: A tool for searching code
```

**Key elements:**
1. Core capability (what)
2. When-to-use triggers (when)
3. Domain keywords (that users would say)

## Pattern 14: Supporting File References

**When to use:** Link to external resources or related skills.

**Implementation:**
```markdown
## Additional Resources

- **references/file.md**: Description
- **scripts/script.sh**: Description
- **assets/template.txt**: Description

## Related Skills

- **skill-name**: Description and when to use it instead
```

## Pattern 15: Version/Update Tracking

**When to use:** Skill content changes over time and users need to know.

**Implementation:**
```markdown
## Version History

- v2.0.0 (2025-10-01): Breaking changes description
- v1.1.0 (2025-09-15): New features description
- v1.0.0 (2025-09-01): Initial release
```

Or simpler:
```markdown
**Last Updated:** 2025-10-18
**Changes:** Added support for X, removed deprecated Y
```

## Combining Patterns

Most production skills combine multiple patterns:

**Example - Comprehensive Skill:**
```
skill-name/
├── SKILL.md                           # Pattern 1, 4, 7, 11, 13
└── references/
    ├── detailed-guide.md              # Pattern 1
    ├── examples.md                    # Pattern 5
    └── troubleshooting.md             # Pattern 12
```

**SKILL.md includes:**
- Progressive disclosure (Pattern 1)
- Phase-based instructions (Pattern 4)
- DO/DON'T practices (Pattern 7)
- Parameter documentation (Pattern 11)
- Context-aware description (Pattern 13)

**Select patterns based on:**
- Skill complexity
- User needs
- Documentation depth
- Tool requirements
