# Sequential Thinking Tool: Complete Usage Guide

## Overview

The `mcp__sequential-thinking__sequentialthinking` tool enables dynamic, step-by-step problem-solving where thoughts can evolve, branch, and revise as understanding deepens. Unlike linear thinking, it allows backtracking, course correction, and exploring multiple paths.

## MCP Server Configuration

Add this to your MCP configuration file:

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ]
    }
  }
}
```

## Core Concepts

### Thought Patterns

```mermaid
graph TD
    A[Linear Thinking] --> B[Thought 1]
    B --> C[Thought 2]
    C --> D[Thought 3]
    D --> E[Solution]
    
    F[Sequential Thinking] --> G[Thought 1]
    G --> H[Thought 2]
    H --> I{Need Revision?}
    I -->|Yes| J[Revise Thought 1]
    I -->|No| K[Thought 3]
    J --> K
    K --> L{Branch Needed?}
    L -->|Yes| M[Branch A]
    L -->|Yes| N[Branch B]
    L -->|No| O[Continue]
    M --> P[Synthesis]
    N --> P
    O --> P
    P --> Q[Solution]
```

## Usage Patterns

### 1. Linear Problem Solving

**Best for:** Well-defined problems with clear steps

```mermaid
sequenceDiagram
    participant U as User
    participant T as Tool
    
    U->>T: Thought 1: Identify problem
    T-->>U: Continue needed
    U->>T: Thought 2: Analyze root cause
    T-->>U: Continue needed
    U->>T: Thought 3: Apply solution
    T-->>U: Solution complete
```

**Example Parameters:**
```json
{
  "thought": "Step 1: Identify the performance bottleneck",
  "nextThoughtNeeded": true,
  "thoughtNumber": 1,
  "totalThoughts": 3
}
```

### 2. Revision Pattern

**Best for:** Problems where initial assumptions might be wrong

```mermaid
flowchart TD
    A[Initial Thought] --> B[Follow-up Thought]
    B --> C{Realize Error?}
    C -->|Yes| D[Mark as Revision]
    C -->|No| E[Continue Normally]
    D --> F[Revise Previous Thought]
    F --> G[New Direction]
    E --> H[Linear Continuation]
    G --> I[Final Solution]
    H --> I
```

**Example Usage:**
```json
{
  "thought": "Actually, I need to reconsider my earlier assumption about microservices",
  "isRevision": true,
  "revisesThought": 2,
  "thoughtNumber": 4,
  "totalThoughts": 5
}
```

### 3. Branching Exploration

**Best for:** Problems with multiple valid approaches

```mermaid
graph TD
    A[Problem Statement] --> B[Decision Point]
    B --> C[Branch A: Approach 1]
    B --> D[Branch B: Approach 2]
    B --> E[Branch C: Approach 3]
    C --> F[Explore Path A]
    D --> G[Explore Path B]
    E --> H[Explore Path C]
    F --> I[Compare & Synthesize]
    G --> I
    H --> I
    I --> J[Optimal Solution]
```

**Example Parameters:**
```json
{
  "thought": "Frontend-first approach: Start with React/Vue",
  "branchFromThought": 2,
  "branchId": "frontend-first",
  "thoughtNumber": 3,
  "totalThoughts": 6
}
```

## Parameter Reference

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thought` | string | Your current thinking step |
| `nextThoughtNeeded` | boolean | Whether another thought is needed |
| `thoughtNumber` | integer | Current step number |
| `totalThoughts` | integer | Estimated total steps (adjustable) |

### Optional Parameters

| Parameter | Type | Description | When to Use |
|-----------|------|-------------|-------------|
| `isRevision` | boolean | Marks thought as revision | When reconsidering previous thoughts |
| `revisesThought` | integer | Which thought to revise | With `isRevision: true` |
| `branchFromThought` | integer | Starting point for branch | When exploring alternatives |
| `branchId` | string | Branch identifier | To organize multiple branches |
| `needsMoreThoughts` | boolean | Need to extend beyond estimate | When realizing more steps needed |

## Decision Flow

```mermaid
flowchart TD
    Start([Start Problem]) --> Define[Define Initial Approach]
    Define --> Estimate[Estimate Total Thoughts]
    Estimate --> Think[Current Thought]
    Think --> Evaluate{Satisfied with Progress?}
    
    Evaluate -->|Yes| Continue[Continue Linear]
    Evaluate -->|Need Revision| Revise[Mark as Revision]
    Evaluate -->|Multiple Paths| Branch[Create Branch]
    
    Continue --> More{Need More Thoughts?}
    Revise --> More
    Branch --> More
    
    More -->|Yes| Think
    More -->|No| Complete([Solution Complete])
    
    style Start fill:#e1f5fe
    style Complete fill:#e8f5e8
    style Revise fill:#fff3e0
    style Branch fill:#f3e5f5
```

## Best Practices

### When to Use Each Pattern

```mermaid
mindmap
  root((Sequential Thinking))
    Linear
      Well-defined problems
      Clear step sequence
      Technical debugging
      Process optimization
    Revision
      Initial bias exists
      Assumptions might be wrong
      Learning new concepts
      Architecture decisions
    Branching
      Multiple valid solutions
      Trade-off analysis
      Strategy planning
      Creative problem solving
```

### Quality Indicators

✅ **Good Usage:**
- Express uncertainty when present
- Revise when realizing errors
- Adjust `totalThoughts` as understanding grows
- Use specific, actionable thoughts
- Only finish when truly satisfied

❌ **Poor Usage:**
- Forcing linear progression when revision needed
- Setting `nextThoughtNeeded: false` prematurely
- Avoiding revisions to save time
- Vague or non-actionable thoughts

## Advanced Techniques

### Hypothesis Testing Pattern

```mermaid
graph LR
    A[Generate Hypothesis] --> B[Test Against Evidence]
    B --> C{Hypothesis Valid?}
    C -->|Yes| D[Build Solution]
    C -->|No| E[Revise Hypothesis]
    E --> B
    D --> F[Verify Solution]
    F --> G{Solution Works?}
    G -->|Yes| H[Complete]
    G -->|No| I[New Hypothesis]
    I --> B
```

### Multi-Branch Synthesis

```mermaid
graph TD
    A[Core Problem] --> B[Branch Point]
    B --> C[Technical Branch]
    B --> D[Business Branch]
    B --> E[User Branch]
    C --> F[Technical Analysis]
    D --> G[Business Analysis]
    E --> H[User Analysis]
    F --> I[Synthesis Point]
    G --> I
    H --> I
    I --> J[Holistic Solution]
```

## Common Scenarios

### Debugging Complex Issues

1. **Symptom Identification** (Linear)
2. **Root Cause Analysis** (May require revision)
3. **Solution Brainstorming** (Branching)
4. **Implementation Planning** (Linear)

### Architecture Decisions

1. **Requirements Gathering** (Linear)
2. **Option Generation** (Branching)
3. **Trade-off Analysis** (Often requires revision)
4. **Decision Justification** (Synthesis)

### Learning New Technologies

1. **Initial Research** (Linear)
2. **Assumption Validation** (Revision-heavy)
3. **Hands-on Exploration** (Branching)
4. **Knowledge Consolidation** (Synthesis)

## Tool Response Format

The tool returns:
```json
{
  "thoughtNumber": 3,
  "totalThoughts": 5,
  "nextThoughtNeeded": true,
  "branches": ["frontend-first", "backend-first"],
  "thoughtHistoryLength": 12
}
```

Use this feedback to understand:
- Current position in thinking process
- Active branches being explored
- Total context accumulated

## Tips for Mastery

1. **Start Simple:** Begin with linear problems to understand the flow
2. **Embrace Uncertainty:** Don't pretend to know when you don't
3. **Revise Boldly:** It's better to correct course than continue wrong
4. **Branch Wisely:** Only branch when genuinely exploring alternatives
5. **Synthesize Thoughtfully:** Bring branches together meaningfully
6. **Finish Deliberately:** Only complete when truly satisfied with solution

The sequential thinking tool transforms complex problem-solving from a rigid process into an adaptive, intelligent exploration that mirrors how experts actually think through difficult challenges.