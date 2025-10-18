# Skill Discovery Guide

How to make skills discoverable so Claude uses them automatically.

## The Discovery Challenge

Skills are **model-invoked** - Claude autonomously decides when to use them based on:
1. The skill's description
2. The user's query
3. Context and conversation history

**Goal:** Write descriptions that match how users naturally ask for things.

## Critical: The Description Field

The description is the ONLY thing that determines when your skill activates.

### Anatomy of a Good Description

**Template:**
```yaml
description: <Core capability>. Use when <trigger scenarios>. <Domain keywords>.
```

**Example - Excellent description:**
```yaml
description: Query and explore logs in Grafana Loki via logcli. Use when user asks to pull logs, analyze log patterns, or debug using Loki logs.
```

**Why this works:**
- **Core capability**: "Query and explore logs in Grafana Loki"
- **Triggers**: "pull logs, analyze log patterns, debug"
- **Keywords**: "Loki", "logcli", "logs"

### Bad vs Good Descriptions

#### ❌ Too Vague
```yaml
# Won't activate reliably
description: Helps with data

# User asks: "Can you analyze this CSV?"
# Claude won't activate - no match
```

#### ✅ Specific
```yaml
# Will activate reliably
description: Analyze CSV files, generate statistics, create visualizations. Use when working with CSV data, spreadsheets, or tabular data analysis.

# User asks: "Can you analyze this CSV?"
# Claude activates - matches "CSV" and "analyze"
```

#### ❌ No Triggers
```yaml
# Unclear when to use
description: GitHub code search tool
```

#### ✅ Clear Triggers
```yaml
# Clear when to use
description: Search millions of GitHub repos for real code patterns, API examples, configuration guides. Use when you need to find how developers implement features, configure tools, or document APIs.
```

## Discovery Techniques

### 1. Include User Language

Think about how users naturally phrase requests:

**Users say:** "How do I set this up?"
**Include in description:** "setup instructions", "getting started", "installation"

**Users say:** "Show me examples"
**Include in description:** "examples", "sample code", "usage patterns"

**Users say:** "This isn't working"
**Include in description:** "troubleshooting", "debugging", "fixing errors"

### 2. Domain Keyword Saturation

Include all relevant terms users might mention:

**Example - API Integration Skill:**
```yaml
description: Integrate with Anthropic Claude API for completions, streaming, tool use. Use when building AI applications, working with Claude API, implementing chat features, or handling API authentication and errors.
```

**Keywords included:**
- Technical: "API", "completions", "streaming", "tool use"
- Actions: "integrate", "building", "working with", "implementing"
- Domains: "AI applications", "chat features"
- Operations: "authentication", "errors"

### 3. Include Anti-Triggers

Sometimes specify what the skill is NOT for:

**Example:**
```yaml
description: Format and lint Python code using black and ruff. Use for Python code formatting and style checking. NOT for running tests or executing code.
```

**Benefits:**
- Prevents incorrect activation
- Clarifies scope
- Reduces conflicts with other skills

### 4. Layer Multiple Trigger Patterns

Include various ways users might ask:

**Pattern 1 - Direct tool mention:**
```yaml
description: Work with Docker containers...
# User: "Can you help with Docker?"
```

**Pattern 2 - Action-based:**
```yaml
description: ...build, run, and manage containers...
# User: "How do I build a container?"
```

**Pattern 3 - Problem-based:**
```yaml
description: ...when containerizing applications or debugging container issues
# User: "My container won't start"
```

**Combined:**
```yaml
description: Work with Docker containers to build, run, and manage containerized applications. Use when working with Docker, containerizing applications, managing images, or debugging container issues.
```

## Testing Skill Discovery

### Step 1: Test with Natural Language

Ask questions how users would naturally ask:

**For a Git skill:**
- "How do I undo my last commit?"
- "Can you help me rebase?"
- "What's the command to see my changes?"

### Step 2: Check Activation

Verify the skill activates:
```bash
# In Claude Code, ask trigger questions
# Watch for skill activation (verbose mode shows this)
```

### Step 3: Refine Description

If skill doesn't activate, add keywords from your test questions:

**User asked:** "How do I undo my last commit?"
**Add to description:** "undo commits", "git reset", "revert changes"

### Step 4: Test Edge Cases

Try questions that SHOULD NOT activate the skill:

**For a Python testing skill:**
- Should activate: "How do I write tests for this function?"
- Should NOT activate: "How do I format this Python code?" (different skill)

## Common Discovery Issues

### Issue 1: Skill Never Activates

**Symptoms:**
- Relevant questions don't trigger skill
- Claude uses general knowledge instead

**Diagnosis:**
```yaml
# Check your description
description: Python testing
# Too short, no triggers
```

**Fix:**
```yaml
description: Write and organize Python tests using pytest. Use when creating unit tests, integration tests, or test fixtures. Includes patterns for mocking, parametrization, and async tests.
```

### Issue 2: Skill Activates Too Often

**Symptoms:**
- Skill triggers for unrelated questions
- Conflicts with other skills

**Diagnosis:**
```yaml
# Too broad
description: Helps with code
```

**Fix:**
```yaml
# More specific
description: Review Python code for style, patterns, and best practices. Use specifically for Python code review, NOT for other languages or writing new code.
```

### Issue 3: Conflicts Between Skills

**Symptoms:**
- Multiple skills match same queries
- Claude picks wrong skill

**Solution: Make descriptions mutually exclusive**

**Skill 1 - Data Analysis:**
```yaml
description: Analyze CSV files, generate statistics, create visualizations. Use for exploratory data analysis and statistical summaries.
```

**Skill 2 - Data Cleaning:**
```yaml
description: Clean and transform CSV data, handle missing values, normalize formats. Use for data preprocessing before analysis.
```

**Key differences:**
- Skill 1: "analysis", "statistics", "visualizations"
- Skill 2: "clean", "transform", "preprocessing"

## Discovery Optimization Checklist

When writing or updating a skill description:

- [ ] Includes core capability (what it does)
- [ ] Lists 3-5 specific trigger scenarios
- [ ] Contains domain keywords users would say
- [ ] Includes action verbs (analyze, generate, configure)
- [ ] Mentions specific tools/technologies by name
- [ ] Clear when to use AND when NOT to use
- [ ] Under 200 words (concise but comprehensive)
- [ ] Tested with natural language questions
- [ ] Doesn't conflict with other skill descriptions

## Description Formulas

### Formula 1: Tool-Focused
```
<Tool action> <object> using <tool name>. Use when <scenarios>. <Additional keywords>.
```

**Example:**
```yaml
description: Format JSON files using jq. Use when validating JSON syntax, pretty-printing JSON, or extracting JSON fields.
```

### Formula 2: Capability-Focused
```
<Capability description>. Use when <trigger scenarios>. Especially useful for <specific cases>.
```

**Example:**
```yaml
description: Generate REST API boilerplate with routing, middleware, and error handling. Use when creating new APIs or adding endpoints. Especially useful for Express.js and FastAPI projects.
```

### Formula 3: Domain-Focused
```
<Domain expertise> for <specific area>. Use when <problem scenarios>. <Technologies>.
```

**Example:**
```yaml
description: Security best practices for web applications including authentication, authorization, and input validation. Use when implementing security features or reviewing code for vulnerabilities. Covers OAuth, JWT, SQL injection, XSS prevention.
```

### Formula 4: Workflow-Focused
```
<Workflow description> to <outcome>. Use when <process triggers>. <Phases>.
```

**Example:**
```yaml
description: Code review workflow to identify bugs, improve performance, and ensure best practices. Use when reviewing pull requests or performing code audits. Includes style checking, security review, and test coverage analysis.
```

## Advanced: Semantic Matching

Claude uses semantic understanding, not just keyword matching:

**User asks:** "My container won't start"
**Skill description includes:** "debugging container issues"
**Match:** Even though exact words differ, semantic meaning matches

**Implication:** Use natural language in descriptions, not keyword stuffing.

**Good - Natural:**
```yaml
description: Troubleshoot Docker container startup failures, networking issues, and volume mounting problems.
```

**Bad - Keyword stuffed:**
```yaml
description: Docker container error debug fix problem issue startup failure network volume mount troubleshoot.
```

## Testing with Verbose Mode

Enable verbose output to see skill activation:

```bash
# See which skills Claude considers
claude --verbose

# Or set in conversation
# Ctrl+O to toggle verbose mode
```

**Look for:**
- Skill activation messages
- Why skills were selected
- Alternative skills considered

## Iteration Process

1. **Create initial description** with obvious keywords
2. **Test with natural questions** users would ask
3. **Check activation** in verbose mode
4. **Add missing keywords** from failed tests
5. **Remove too-broad keywords** causing false activations
6. **Test edge cases** to verify specificity
7. **Monitor real usage** and refine over time

## Examples of Well-Discovered Skills

### Example 1: GitHub Code Search
```yaml
description: Search millions of GitHub repos for real code patterns, API examples, configuration guides, and documentation. Use when you need to find how developers implement features, configure tools, or document APIs. Especially useful for unfamiliar libraries, setup instructions, best practices, and real-world usage examples.
```

**Why it works:**
- Clear capability: "Search GitHub repos"
- Multiple triggers: "code patterns", "API examples", "configuration"
- Natural phrases: "how developers implement", "real-world usage"
- Specific scenarios: "unfamiliar libraries", "setup instructions"

### Example 2: Loki Log Analysis
```yaml
description: Query and explore logs in Grafana Loki via logcli. Use when user asks to pull logs, analyze log patterns, or debug using Loki logs.
```

**Why it works:**
- Tool-specific: "Grafana Loki", "logcli"
- Action triggers: "pull logs", "analyze", "debug"
- Clear domain: log analysis

### Example 3: Python Testing
```yaml
description: Write and organize Python tests using pytest. Use when creating unit tests, integration tests, or test fixtures. Includes patterns for mocking, parametrization, and async tests.
```

**Why it works:**
- Language-specific: "Python", "pytest"
- Test types: "unit", "integration", "fixtures"
- Techniques: "mocking", "parametrization", "async"

## Summary

**Most important factors for discovery:**

1. **Specific description** (not vague)
2. **User language** (how they'd ask)
3. **Clear triggers** (when to use)
4. **Domain keywords** (technical terms)
5. **Testing** (verify activation)

**Remember:** The description is the bridge between user intent and skill activation. Invest time making it precise and comprehensive.
