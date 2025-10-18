# ggrep Examples Library

Comprehensive collection of tested search patterns organized by use case.

## Documentation Searches

### Finding Setup Instructions

**Installation sections:**
```javascript
{
  query: "## Installation",
  language: ["Markdown"]
}
```

**Prerequisites:**
```javascript
{
  query: "## Prerequisites",
  language: ["Markdown"]
}
```

**Getting started:**
```javascript
{
  query: "## Getting Started",
  language: ["Markdown"],
  repo: "anthropics/"
}
```

### Finding Configuration Examples

**JSON config blocks:**
```javascript
{
  query: "```json",
  language: ["Markdown"]
}
```

**YAML config blocks:**
```javascript
{
  query: "```yaml",
  language: ["Markdown"],
  path: "docs/"
}
```

**Environment variables:**
```javascript
{
  query: ".env",
  language: ["Markdown"],
  path: "README.md"
}
```

### Finding CLI Commands

**npm commands:**
```javascript
{
  query: "npm install",
  language: ["Markdown"],
  path: "README.md"
}
```

**Docker commands:**
```javascript
{
  query: "docker run",
  language: ["Markdown"]
}
```

**CLI tool usage:**
```javascript
{
  query: "claude mcp",
  language: ["Markdown"]
}
```

### Finding API Documentation

**API keys:**
```javascript
{
  query: "ANTHROPIC_API_KEY",
  language: ["Markdown"]
}
```

**API endpoints:**
```javascript
{
  query: "POST /api/",
  language: ["Markdown"]
}
```

**Authentication:**
```javascript
{
  query: "Bearer token",
  language: ["Markdown"],
  path: "docs/"
}
```

## Code Searches

### React & JavaScript

**React hooks:**
```javascript
{
  query: "useState(",
  language: ["TypeScript", "TSX"]
}
```

**useEffect with cleanup:**
```javascript
{
  query: "(?s)useEffect\\(\\(\\) => {.*removeEventListener",
  language: ["TSX"],
  useRegexp: true
}
```

**Async components:**
```javascript
{
  query: "async function",
  language: ["JavaScript", "TypeScript"]
}
```

**Error boundaries:**
```javascript
{
  query: "componentDidCatch",
  language: ["TSX", "JavaScript"]
}
```

**Context API:**
```javascript
{
  query: "createContext<",
  language: ["TypeScript"]
}
```

### Python

**Class inheritance:**
```javascript
{
  query: "class.*extends.*Component",
  language: ["Python"],
  useRegexp: true
}
```

**Async patterns:**
```javascript
{
  query: "async def",
  language: ["Python"]
}
```

**Exception handling:**
```javascript
{
  query: "try.*except.*APIError",
  language: ["Python"],
  useRegexp: true
}
```

**Type hints:**
```javascript
{
  query: "def.*-> ",
  language: ["Python"],
  useRegexp: true
}
```

**Anthropic API usage:**
```javascript
{
  query: "import anthropic",
  language: ["Python"]
}
```

### TypeScript

**Interface definitions:**
```javascript
{
  query: "interface Props {",
  language: ["TypeScript"]
}
```

**Generic types:**
```javascript
{
  query: "type.*<T>",
  language: ["TypeScript"],
  useRegexp: true
}
```

**Type guards:**
```javascript
{
  query: "is",
  language: ["TypeScript"],
  matchWholeWords: true
}
```

### Go

**Interface implementations:**
```javascript
{
  query: "interface\\{\\}",
  language: ["Go"],
  useRegexp: true
}
```

**Goroutines:**
```javascript
{
  query: "go func(",
  language: ["Go"]
}
```

**Error handling:**
```javascript
{
  query: "if err != nil",
  language: ["Go"]
}
```

## API Integration Patterns

### Anthropic Claude API

**Setup documentation:**
```javascript
{
  query: "ANTHROPIC_API_KEY",
  language: ["Markdown"]
}
```

**Python client:**
```javascript
{
  query: "from anthropic import Anthropic",
  language: ["Python"]
}
```

**Completion calls:**
```javascript
{
  query: "messages.create(",
  language: ["Python"]
}
```

**TypeScript client:**
```javascript
{
  query: "import Anthropic from",
  language: ["TypeScript"]
}
```

### MCP Servers

**MCP configuration:**
```javascript
{
  query: "claude mcp add",
  language: ["Markdown"]
}
```

**MCP server setup:**
```javascript
{
  query: "mcpServers",
  language: ["JSON"]
}
```

**Server implementation:**
```javascript
{
  query: "MCP server",
  language: ["Markdown"],
  repo: "anthropics/"
}
```

### REST APIs

**Express routes:**
```javascript
{
  query: "app.get(",
  language: ["JavaScript", "TypeScript"]
}
```

**FastAPI endpoints:**
```javascript
{
  query: "@app.post(",
  language: ["Python"]
}
```

**Axios requests:**
```javascript
{
  query: "axios.post(",
  language: ["TypeScript"]
}
```

## Configuration Searches

### Package Managers

**npm package.json:**
```javascript
{
  query: "\"scripts\":",
  language: ["JSON"],
  path: "package.json"
}
```

**Python requirements:**
```javascript
{
  query: "anthropic",
  path: "requirements.txt"
}
```

**Poetry pyproject:**
```javascript
{
  query: "[tool.poetry]",
  language: ["TOML"],
  path: "pyproject.toml"
}
```

### CI/CD

**GitHub Actions:**
```javascript
{
  query: "uses: actions/checkout",
  language: ["YAML"],
  path: ".github/workflows/"
}
```

**GitLab CI:**
```javascript
{
  query: "stages:",
  language: ["YAML"],
  path: ".gitlab-ci.yml"
}
```

**Docker builds:**
```javascript
{
  query: "FROM",
  path: "Dockerfile"
}
```

### Cloud Configuration

**AWS:**
```javascript
{
  query: "aws_",
  language: ["YAML", "JSON"]
}
```

**Terraform:**
```javascript
{
  query: "resource \"",
  language: ["HCL"]
}
```

**Kubernetes:**
```javascript
{
  query: "apiVersion:",
  language: ["YAML"],
  path: "k8s/"
}
```

## Testing Patterns

### Jest/Vitest

**Test suites:**
```javascript
{
  query: "describe(",
  language: ["TypeScript", "JavaScript"],
  path: "test/"
}
```

**Async tests:**
```javascript
{
  query: "it('.*async",
  language: ["TypeScript"],
  useRegexp: true
}
```

**Mocking:**
```javascript
{
  query: "jest.mock(",
  language: ["TypeScript"]
}
```

### Pytest

**Test functions:**
```javascript
{
  query: "def test_",
  language: ["Python"]
}
```

**Fixtures:**
```javascript
{
  query: "@pytest.fixture",
  language: ["Python"]
}
```

**Parametrization:**
```javascript
{
  query: "@pytest.mark.parametrize",
  language: ["Python"]
}
```

## Error Handling

### Try-Catch Patterns

**JavaScript:**
```javascript
{
  query: "(?s)try {.*} catch",
  language: ["JavaScript", "TypeScript"],
  useRegexp: true
}
```

**Python:**
```javascript
{
  query: "(?s)try:.*except",
  language: ["Python"],
  useRegexp: true
}
```

**Go:**
```javascript
{
  query: "(?s)if err != nil {.*return",
  language: ["Go"],
  useRegexp: true
}
```

### API Error Handling

**HTTP errors:**
```javascript
{
  query: "APIError",
  language: ["Python", "TypeScript"]
}
```

**Retry logic:**
```javascript
{
  query: "retry",
  language: ["Python"],
  path: "src/"
}
```

**Rate limiting:**
```javascript
{
  query: "RateLimitError",
  language: ["Python", "TypeScript"]
}
```

## Database Patterns

### SQL

**Queries:**
```javascript
{
  query: "SELECT.*FROM",
  language: ["SQL"],
  useRegexp: true
}
```

**Migrations:**
```javascript
{
  query: "CREATE TABLE",
  language: ["SQL"]
}
```

### ORMs

**Prisma:**
```javascript
{
  query: "prisma.user.create",
  language: ["TypeScript"]
}
```

**SQLAlchemy:**
```javascript
{
  query: "session.query(",
  language: ["Python"]
}
```

**Django:**
```javascript
{
  query: "models.Model",
  language: ["Python"]
}
```

## Security Patterns

### Authentication

**JWT:**
```javascript
{
  query: "jwt.sign(",
  language: ["JavaScript", "TypeScript"]
}
```

**OAuth:**
```javascript
{
  query: "OAuth2",
  language: ["Python", "TypeScript"]
}
```

**API keys:**
```javascript
{
  query: "Authorization: Bearer",
  language: ["Markdown", "TypeScript"]
}
```

### Input Validation

**Zod:**
```javascript
{
  query: "z.object({",
  language: ["TypeScript"]
}
```

**Pydantic:**
```javascript
{
  query: "BaseModel",
  language: ["Python"]
}
```

## Specialized Searches

### Finding Examples of Specific Libraries

**Template:**
```javascript
{
  query: "import <library>",
  language: ["<Language>"],
  repo: "<official-repo>/"
}
```

**Example - Next.js:**
```javascript
{
  query: "import { useRouter }",
  language: ["TypeScript"],
  repo: "vercel/next"
}
```

### Finding Configuration in Official Repos

**Template:**
```javascript
{
  query: "<config-key>",
  language: ["Markdown"],
  path: "README.md",
  repo: "<organization>/"
}
```

**Example - Claude Code MCP:**
```javascript
{
  query: "mcp.json",
  language: ["Markdown"],
  repo: "anthropics/"
}
```

### Finding Test Examples

**Template:**
```javascript
{
  query: "test_<functionality>",
  language: ["<Language>"],
  path: "test/"
}
```

**Example - API tests:**
```javascript
{
  query: "test_api_",
  language: ["Python"],
  path: "tests/"
}
```

## Multi-Step Research Workflows

### Integrating New API

**Step 1 - Find setup docs:**
```javascript
{
  query: "<API_NAME>_API_KEY",
  language: ["Markdown"]
}
```

**Step 2 - Find imports:**
```javascript
{
  query: "import <library>",
  language: ["Python"]
}
```

**Step 3 - Find usage:**
```javascript
{
  query: "<api_method>(",
  language: ["Python"],
  repo: "official-repo/"
}
```

**Step 4 - Find error handling:**
```javascript
{
  query: "except.*<Library>Error",
  language: ["Python"],
  useRegexp: true
}
```

### Understanding New Framework

**Step 1 - Find getting started:**
```javascript
{
  query: "## Quick Start",
  language: ["Markdown"],
  path: "README.md"
}
```

**Step 2 - Find basic example:**
```javascript
{
  query: "example",
  language: ["Markdown"],
  path: "examples/"
}
```

**Step 3 - Find advanced patterns:**
```javascript
{
  query: "<framework-specific-pattern>",
  language: ["<Language>"],
  path: "src/"
}
```

### Debugging Issues

**Step 1 - Find error message:**
```javascript
{
  query: "<error-message>",
  language: ["Markdown"]
}
```

**Step 2 - Find related code:**
```javascript
{
  query: "<error-causing-code>",
  language: ["<Language>"]
}
```

**Step 3 - Find solutions:**
```javascript
{
  query: "fix.*<error-keyword>",
  language: ["Markdown"],
  useRegexp: true
}
```
