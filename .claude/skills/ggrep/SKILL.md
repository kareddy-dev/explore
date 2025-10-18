---
name: GitHub Code & Documentation Search
description: Search millions of GitHub repos for real code patterns, API examples, configuration guides, and documentation. Use when you need to find how developers implement features, configure tools, or document APIs. Especially useful for unfamiliar libraries, setup instructions, best practices, and real-world usage examples.
allowed-tools: mcp__ggrep__searchGitHub
---

# GitHub Code & Documentation Search

Search millions of GitHub repositories for real-world code patterns and documentation examples.

## Instructions

### Search for Literal Patterns

**For code**: Use actual syntax like `useState(`, `async function`, `import React from`
**For documentation**: Use actual text like `## Installation`, `npm install`, `ANTHROPIC_API_KEY`

**Never** search for keywords like "react tutorial" or "best practices" - always use literal code or text.

### Always Specify Language

**Code searches**: `language: ["TypeScript", "TSX"]`, `["Python"]`, `["JavaScript"]`
**Documentation searches**: `language: ["Markdown"]` (required for docs)

### Use Filters for Precision

- `path: "README.md"` - Target specific files
- `repo: "anthropics/"` - Filter to organization/repo
- `useRegexp: true` - Enable regex patterns (use `(?s)` prefix for multi-line)

For complete parameter reference, see [references/parameters.md](references/parameters.md).

### Search Strategy

1. **Documentation first**: Find setup/config with `language: ["Markdown"]`
2. **Code second**: Find implementations with specific language
3. **Iterate**: Refine query based on initial results

## Examples

### Documentation Searches (Tested ✓)

**Installation instructions:**
```javascript
{
  query: "## Installation",
  language: ["Markdown"]
}
```

**Package commands:**
```javascript
{
  query: "npm install",
  language: ["Markdown"],
  path: "README.md"
}
```

**API configuration:**
```javascript
{
  query: "ANTHROPIC_API_KEY",
  language: ["Markdown"]
}
```

**CLI setup:**
```javascript
{
  query: "claude mcp",
  language: ["Markdown"]
}
```

**Config blocks:**
```javascript
{
  query: "```json",
  language: ["Markdown"]
}
```

### Code Searches

**React hooks:**
```javascript
{
  query: "useState(",
  language: ["TypeScript", "TSX"]
}
```

**Async patterns:**
```javascript
{
  query: "async function",
  language: ["JavaScript", "TypeScript"]
}
```

**Multi-line regex:**
```javascript
{
  query: "(?s)useEffect\\(\\(\\) => {.*removeEventListener",
  language: ["TSX"],
  useRegexp: true
}
```

For more examples organized by use case, see [references/examples.md](references/examples.md).

## Subagent Workflow

When researching before implementation:

1. **Research**: Search Markdown for tool documentation
2. **Configure**: Find JSON/YAML config examples
3. **Implement**: Search code for API usage patterns
4. **Validate**: Compare with production error handling

## Common Patterns

- Setup: `## Installation`, `## Setup`, `## Getting Started`
- Config: `config.json`, `settings.yaml`, `.env`
- CLI: `npm install`, `pip install`, `docker run`
- APIs: `import anthropic`, `POST /api/`, `completion(model=`
- Errors: `try.*catch`, `except.*Error` (with `useRegexp: true`)

## Best Practices

✅ Use literal code/text patterns
✅ Always add `language` filter
✅ Start simple, refine based on results
✅ Use `path` for targeted searches

❌ Avoid vague keywords
❌ Don't forget language filter
❌ Don't search for placeholders like `YOUR_KEY`

## Additional Resources

- **references/parameters.md**: Complete parameter reference with advanced usage
- **references/examples.md**: Extensive example library organized by use case
