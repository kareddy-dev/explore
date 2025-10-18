# Skill Templates

Ready-to-use templates for common skill types. Copy and adapt for your needs.

## Template 1: Simple CLI Tool Wrapper

```markdown
---
name: <Tool Name>
description: <Tool description>. Use when <specific scenarios>.
allowed-tools: Bash(<tool>:*), Read
---

# <Tool Name>

<Brief overview of what the tool does>

## Instructions

### When to Use
- <Scenario 1>
- <Scenario 2>
- <Scenario 3>

### Common Commands

**Command 1:**
```bash
<tool> <command> <flags>
```

**Command 2:**
```bash
<tool> <command> <flags>
```

## Examples

**Example 1: <Use case>**
```bash
<actual command>
```
Result: <what happens>

**Example 2: <Use case>**
```bash
<actual command>
```
Result: <what happens>

## Best Practices

✅ <Best practice 1>
✅ <Best practice 2>

❌ <Common mistake 1>
❌ <Common mistake 2>
```

## Template 2: Workflow/Process Skill

```markdown
---
name: <Process Name>
description: <Process description>. Use when <workflow triggers>.
allowed-tools: Read, Edit, Bash(git:*), Bash(npm:*)
---

# <Process Name>

Guide for <workflow description>.

## Instructions

### Phase 1: <Phase Name>
1. <Step 1>
2. <Step 2>
3. <Step 3>

### Phase 2: <Phase Name>
1. <Step 1>
2. <Step 2>
3. <Step 3>

### Phase 3: <Phase Name>
1. <Step 1>
2. <Step 2>
3. <Step 3>

## Checklist

- [ ] <Checkpoint 1>
- [ ] <Checkpoint 2>
- [ ] <Checkpoint 3>
- [ ] <Checkpoint 4>

## Examples

**Scenario 1:**
<Walkthrough of process for specific scenario>

**Scenario 2:**
<Walkthrough of process for different scenario>

## Best Practices

✅ <Practice 1>
✅ <Practice 2>

❌ <Mistake 1>
❌ <Mistake 2>
```

## Template 3: Domain Expertise Skill

```markdown
---
name: <Domain> <Topic>
description: <Domain expertise description>. Use when <domain keywords>.
---

# <Domain> <Topic>

<Brief overview of domain expertise>

## Core Principles

### Principle 1: <Name>
<Explanation>

**Example:**
```<language>
<code example>
```

### Principle 2: <Name>
<Explanation>

**Example:**
```<language>
<code example>
```

### Principle 3: <Name>
<Explanation>

**Example:**
```<language>
<code example>
```

## Common Patterns

### Pattern 1: <Pattern Name>
**When to use:** <Scenario>
**How:**
```<language>
<implementation>
```

### Pattern 2: <Pattern Name>
**When to use:** <Scenario>
**How:**
```<language>
<implementation>
```

## Anti-Patterns

### ❌ Anti-Pattern 1: <Name>
**Why it's bad:** <Explanation>
**Instead, do this:**
```<language>
<better approach>
```

### ❌ Anti-Pattern 2: <Name>
**Why it's bad:** <Explanation>
**Instead, do this:**
```<language>
<better approach>
```

## Additional Resources
- references/<file>.md: <Description>
```

## Template 4: Code Generator Skill

```markdown
---
name: <Generator Name>
description: Generate <what it generates>. Use when creating <specific structures>.
allowed-tools: Write, Read, Glob
---

# <Generator Name>

Generate <description> following <standards/conventions>.

## Instructions

### Step 1: Gather Requirements
Ask user for:
- <Requirement 1>
- <Requirement 2>
- <Requirement 3>

### Step 2: Generate Structure
Create files:
- <File 1>: <Purpose>
- <File 2>: <Purpose>
- <File 3>: <Purpose>

### Step 3: Populate Content
Fill templates with:
- <Content type 1>
- <Content type 2>
- <Content type 3>

### Step 4: Validate
Check:
- [ ] <Validation 1>
- [ ] <Validation 2>
- [ ] <Validation 3>

## Templates

### Template: <File Type>
```<language>
<template content with placeholders>
```

### Template: <File Type>
```<language>
<template content with placeholders>
```

## Examples

**Example 1: Generate <item>**
Input:
- Name: <value>
- Type: <value>

Output: <description of generated files>

## Best Practices

✅ <Practice 1>
✅ <Practice 2>

❌ <Mistake 1>
❌ <Mistake 2>

## Additional Resources
- assets/<template-file>: <Description>
- scripts/<helper-script>: <Description>
```

## Template 5: API Integration Skill

```markdown
---
name: <API Name> Integration
description: Integrate with <API> for <capabilities>. Use when working with <API keywords>.
allowed-tools: Bash(curl:*), Read, Write
---

# <API Name> Integration

Guide for integrating with <API Name> API.

## Setup

### Authentication
<Authentication method>

**Environment variables:**
```bash
export <API_KEY>=your-key-here
export <API_URL>=https://api.example.com
```

### Installation
```bash
<install commands>
```

## Common Operations

### Operation 1: <Name>
**Endpoint:** `<METHOD> /path/to/endpoint`

**Request:**
```bash
curl -X <METHOD> <URL> \
  -H "Authorization: Bearer $<TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{ "<key>": "<value>" }'
```

**Response:**
```json
{
  "<field>": "<value>"
}
```

### Operation 2: <Name>
**Endpoint:** `<METHOD> /path/to/endpoint`

**Request:**
```bash
<curl command>
```

**Response:**
```json
<response structure>
```

## Error Handling

### Error 1: <Error Name>
**Cause:** <Why it happens>
**Solution:** <How to fix>

### Error 2: <Error Name>
**Cause:** <Why it happens>
**Solution:** <How to fix>

## Best Practices

✅ <Practice 1>
✅ <Practice 2>

❌ <Mistake 1>
❌ <Mistake 2>

## Additional Resources
- references/authentication.md: Detailed auth patterns
- references/error-codes.md: Complete error reference
```

## Template 6: Testing/Validation Skill

```markdown
---
name: <Testing Framework> Patterns
description: <Testing framework> best practices and patterns. Use when writing tests for <language/framework>.
allowed-tools: Read, Write, Bash(<test-command>:*)
---

# <Testing Framework> Patterns

Best practices for writing tests with <testing framework>.

## Test Structure

### Unit Tests
```<language>
<unit test template>
```

### Integration Tests
```<language>
<integration test template>
```

### End-to-End Tests
```<language>
<e2e test template>
```

## Common Patterns

### Pattern 1: <Test Type>
**When to use:** <Scenario>

**Template:**
```<language>
<test pattern>
```

### Pattern 2: <Test Type>
**When to use:** <Scenario>

**Template:**
```<language>
<test pattern>
```

## Mocking/Stubbing

### Mock <Dependency>
```<language>
<mocking example>
```

### Stub <External Service>
```<language>
<stubbing example>
```

## Best Practices

✅ <Practice 1>
✅ <Practice 2>

❌ <Mistake 1>
❌ <Mistake 2>

## Running Tests

```bash
# Run all tests
<command>

# Run specific test
<command>

# Run with coverage
<command>
```
```

## Template 7: Configuration Management Skill

```markdown
---
name: <Config Tool> Configuration
description: Manage <tool> configurations. Use when setting up <tool> or configuring <features>.
allowed-tools: Read, Write, Edit
---

# <Config Tool> Configuration

Guide for configuring <tool name>.

## Configuration Files

### Primary Config: <filename>
**Location:** `<path>`

**Structure:**
```<format>
<config structure>
```

### Secondary Config: <filename>
**Location:** `<path>`

**Structure:**
```<format>
<config structure>
```

## Common Configurations

### Configuration 1: <Use Case>
```<format>
<config example>
```

**Options:**
- `<option>`: <description>
- `<option>`: <description>

### Configuration 2: <Use Case>
```<format>
<config example>
```

**Options:**
- `<option>`: <description>
- `<option>`: <description>

## Environment-Specific Configs

### Development
```<format>
<dev config>
```

### Production
```<format>
<prod config>
```

## Best Practices

✅ <Practice 1>
✅ <Practice 2>

❌ <Mistake 1>
❌ <Mistake 2>
```

## Customization Guide

When adapting these templates:

1. **Replace all placeholders** in `<angle brackets>`
2. **Keep structure** but adapt content to your domain
3. **Add real examples** - tested, working code
4. **Include specifics** - actual commands, not generic descriptions
5. **Test the skill** - verify it activates correctly
6. **Refine description** - adjust triggers based on testing

## Selecting the Right Template

| Need | Template |
|------|----------|
| Wrap CLI tool | Template 1: CLI Tool Wrapper |
| Multi-step process | Template 2: Workflow/Process |
| Share expertise | Template 3: Domain Expertise |
| Generate code | Template 4: Code Generator |
| Integrate external API | Template 5: API Integration |
| Testing guidance | Template 6: Testing/Validation |
| Config management | Template 7: Configuration Management |

For skills combining multiple aspects, merge relevant templates or create custom structure following the patterns above.
