# Mermaid Diagram Guide

A comprehensive guide for creating and validating Mermaid diagrams in documentation.

## Overview

Mermaid is a JavaScript-based diagramming tool that renders text definitions into diagrams. It's perfect for documentation as it keeps diagrams as code, making them version-controllable and easy to maintain.

## Installation

### Global Installation (Recommended)
```bash
# Install Mermaid CLI globally
npm install -g @mermaid-js/mermaid-cli

# Verify installation
mmdc --version
```

### Using with npx (No Installation)
```bash
# Run without installing
npx -p @mermaid-js/mermaid-cli mmdc --help
```

## Syntax Validation

### Validate Standalone Files
```bash
# Validate a .mmd file
mmdc -i diagram.mmd -o output.svg

# Quick validation from stdin
echo "graph TD; A-->B" | mmdc -i - -o -

# Validate without keeping output
mmdc -i diagram.mmd -o /dev/null
```

### Validate Markdown Files
```bash
# Extract and validate all Mermaid blocks in a markdown file
mmdc -i document.md -o /dev/null

# Generate diagrams from markdown
mmdc -i README.md -o README-diagrams.md
```

## Dark Mode Best Practices

Since documentation may be viewed in dark mode:

1. **Use neutral backgrounds**: Prefer `#f8f9fa` over pure white
2. **Ensure contrast**: Dark text on light backgrounds works in both modes
3. **Test both themes**: Validate readability in light and dark environments
4. **Avoid hard-coded colors**: Let the renderer handle theme adaptation

## Diagram Types

### Flowchart
```mermaid
flowchart TD
    Start([Start]) --> Input[/Input Data/]
    Input --> Process{Valid?}
    Process -->|Yes| Action[Process Data]
    Process -->|No| Error[/Show Error/]
    Action --> End([End])
    Error --> End
```

### Sequence Diagram
```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    participant D as Database
    
    C->>+S: Request Data
    S->>+D: Query
    D-->>-S: Results
    S-->>-C: Response
    
    Note over C,D: Synchronous Flow
```

### State Diagram
```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Loading: fetch()
    Loading --> Success: 200 OK
    Loading --> Error: Failed
    Success --> Idle: reset()
    Error --> Idle: retry()
    Error --> [*]: abort()
```

### Class Diagram
```mermaid
classDiagram
    class User {
        +String name
        +String email
        +login()
        +logout()
    }
    class Admin {
        +Array permissions
        +grantAccess()
        +revokeAccess()
    }
    User <|-- Admin
```

### Entity Relationship Diagram
```mermaid
erDiagram
    USER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    PRODUCT ||--o{ LINE-ITEM : includes
    
    USER {
        int id PK
        string name
        string email UK
    }
    ORDER {
        int id PK
        date created
        string status
    }
```

### Gantt Chart
```mermaid
gantt
    title Project Timeline
    dateFormat YYYY-MM-DD
    
    section Phase 1
    Research           :a1, 2024-01-01, 30d
    Design            :a2, after a1, 20d
    
    section Phase 2
    Development       :b1, after a2, 45d
    Testing          :b2, after b1, 15d
    
    section Deployment
    Staging          :c1, after b2, 7d
    Production       :after c1, 3d
```

### Git Graph
```mermaid
gitGraph
    commit
    branch develop
    checkout develop
    commit
    commit
    checkout main
    merge develop
    commit
    branch feature
    checkout feature
    commit
    commit
    checkout develop
    merge feature
    checkout main
    merge develop
```

### Mind Map
```mermaid
mindmap
  root((Mermaid))
    Diagrams
      Flowchart
      Sequence
      State
      Class
    Features
      Text-based
      Version Control
      Easy Updates
    Tools
      CLI
      Live Editor
      VS Code Extension
```

### Pie Chart
```mermaid
pie title Language Distribution
    "JavaScript" : 40
    "Python" : 30
    "TypeScript" : 20
    "Other" : 10
```

## CLI Options

### Common Flags
```bash
# Theme selection
mmdc -i input.mmd -o output.svg -t dark

# Custom background
mmdc -i input.mmd -o output.png -b transparent

# PDF output with scaling
mmdc -i input.mmd -o output.pdf --pdfFit

# Custom dimensions
mmdc -i input.mmd -o output.png -w 1200 -H 800

# Quiet mode (suppress logs)
mmdc -i input.mmd -o output.svg -q
```

### Output Formats
- **SVG** (default): Scalable, perfect for web
- **PNG**: Raster image with customizable resolution
- **PDF**: Document embedding, print-ready

## Integration Tips

### VS Code Extensions
- **Mermaid Preview**: Live preview while editing
- **Markdown Preview Mermaid Support**: Render in markdown preview

### GitHub
- Mermaid diagrams render automatically in markdown files
- Use ```mermaid code blocks

### Documentation Sites
- **MkDocs**: Use `pymdown-extensions` with `superfences`
- **Docusaurus**: Built-in Mermaid support
- **GitBook**: Mermaid plugin available

## Common Issues

### Syntax Errors
```bash
# Debug syntax issues
mmdc -i broken.mmd -o test.svg 2>&1 | grep Error

# Common fixes:
# - Check for missing semicolons in flowcharts
# - Verify participant names in sequence diagrams
# - Ensure proper indentation in state diagrams
```

### Rendering Issues
- **Large diagrams**: Increase dimensions with `-w` and `-H`
- **Text cutoff**: Adjust node spacing in config
- **Dark mode**: Use theme-neutral colors

### Performance
- **Complex diagrams**: Split into multiple smaller diagrams
- **Batch processing**: Use shell scripts for multiple files
- **Caching**: Save rendered SVGs for static content

## Best Practices

1. **Keep it simple**: Prefer clarity over complexity
2. **Use descriptive labels**: Make diagrams self-documenting
3. **Version control**: Track diagram source in Git
4. **Consistent style**: Maintain uniform appearance across docs
5. **Accessibility**: Include diagram descriptions in surrounding text
6. **Responsive design**: Use SVG format for web display

## Resources

- [Official Mermaid Documentation](https://mermaid.js.org/)
- [Mermaid Live Editor](https://mermaid.live/)
- [Mermaid CLI GitHub](https://github.com/mermaid-js/mermaid-cli)
- [Diagram Syntax Reference](https://mermaid.js.org/syntax/flowchart.html)

## Quick Reference

```bash
# Validate syntax
mmdc -i diagram.mmd -o /dev/null

# Generate SVG
mmdc -i diagram.mmd -o diagram.svg

# Dark theme PNG
mmdc -i diagram.mmd -o diagram.png -t dark -b "#1e1e1e"

# Extract from markdown
mmdc -i README.md -o output.md

# Batch process
for f in *.mmd; do mmdc -i "$f" -o "${f%.mmd}.svg"; done
```