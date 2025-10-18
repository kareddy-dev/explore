# How to Use the Knowledge Base

**Last Updated:** 2025-10-18

---

## 🎯 Quick Start Guide

### For Humans (You)

**Finding Information:**
1. Start with `INDEX.md` in the root
2. Navigate to domain-specific indexes
3. Or ask Claude: "Search KB for [topic]"

**Adding Information:**
1. Choose the right domain
2. Use a template if applicable
3. Or ask Claude: "Save this to KB"

### For Claude

**When I ask you to search:**
1. Check `MANIFEST.json` for structure
2. Read relevant domain indexes
3. Search specific documents
4. Synthesize and cite sources

**When I ask you to save:**
1. Determine domain from content
2. Use appropriate template
3. Follow naming conventions
4. Update indexes and manifest

---

## 📚 Common Workflows

### Workflow 1: Analyzing a Stock
```
You: "Analyze RELIANCE stock and save to KB"

Claude:
1. Uses OpenBB to gather data
2. Uses stock-analysis.md template
3. Saves to kb/domains/finance/stocks/RELIANCE.md
4. Updates finance/INDEX.md
5. Updates MANIFEST.json
```

### Workflow 2: Learning Something New
```
You: "I learned about FastAPI, save this"

Claude:
1. Asks clarifying questions if needed
2. Uses api-reference.md or learning-note.md template
3. Saves to kb/domains/dev/apis/fastapi.md
4. Updates dev/INDEX.md
```

### Workflow 3: Finding Related Information
```
You: "How do I use pandas with OpenBB?"

Claude:
1. Searches finance/openbb/ for OpenBB info
2. Searches dev/python/ for pandas info
3. Synthesizes both
4. Suggests creating new doc if useful
```

---

## 💡 Best Practices

### Do's ✅
- Let Claude handle file operations
- Use natural language
- Cross-reference related topics
- Keep indexes updated (Claude does this)
- Use templates for consistency

### Don'ts ❌
- Don't manually edit MANIFEST.json (ask Claude)
- Don't duplicate information
- Don't skip domain indexes
- Don't forget to update dates

---

## 🔍 Finding Information

### Method 1: Ask Claude (Recommended)
```
"Search KB for OpenBB limitations"
"Find all my stock analyses"
"What do I know about FastAPI?"
"Show me Python pandas examples"
```

### Method 2: Browse Indexes
```
1. INDEX.md → Overview
2. domains/[domain]/INDEX.md → Domain-specific
3. Follow links to documents
```

### Method 3: Search Files
```bash
cd kb
grep -r "search term" domains/
find . -name "*filename*"
```

---

## 💾 Saving Information

### Method 1: Ask Claude (Recommended)
```
"Save this analysis to finance domain"
"Create a learning note about [concept]"
"Add this code snippet to dev/python"
"Document this API in KB"
```

### Method 2: Manual (Advanced)
```
1. Choose domain: domains/[domain]/
2. Pick template: templates/[template].md
3. Copy template to destination
4. Fill in content
5. Update domain INDEX.md
6. Ask Claude to update MANIFEST.json
```

---

## 🎨 Document Types

| Want to save... | Use template... | Save to... |
|-----------------|-----------------|------------|
| Stock analysis | stock-analysis.md | domains/finance/stocks/ |
| API docs | api-reference.md | domains/dev/apis/ |
| Code snippet | code-snippet.md | domains/dev/snippets/ |
| Learning note | learning-note.md | domains/[domain]/ |
| Project | project-spec.md | projects/[name]/ |

---

## 🤖 Claude Commands

See [claude-prompts.md](claude-prompts.md) for complete list of useful commands.

**Most Used:**
```
"Search KB for [topic]"
"Save this to KB in [domain]"
"Update [document] with new info"
"What's in [domain]?"
"Create new [type] for [topic]"
```

---

## 📊 Understanding the Structure

```
kb/
├── INDEX.md              # Start here
├── MANIFEST.json         # Claude's map
├── CONVENTIONS.md        # The rules
│
├── domains/              # Knowledge by topic
│   ├── finance/
│   ├── dev/
│   └── data/
│
├── projects/             # Active work
├── templates/            # Document templates
├── meta/                 # This documentation
└── _archive/             # Old stuff
```

---

## 🔧 Maintenance

See [maintenance.md](maintenance.md) for detailed maintenance procedures.

**Quick Checklist:**
- [ ] Indexes are up-to-date
- [ ] No broken links
- [ ] Templates are current
- [ ] MANIFEST.json is accurate
- [ ] Archive old content

---

## ❓ FAQ

**Q: Where does X go?**
A: Ask Claude or check CONVENTIONS.md for the save_patterns section

**Q: How do I find Y?**
A: Ask Claude to search, or check domain indexes

**Q: Can I change the structure?**
A: Yes, but update MANIFEST.json and all indexes

**Q: What if I want a new domain?**
A: Ask Claude to create it, or follow the pattern in existing domains

---

## 🚀 Next Steps

1. Try searching: "Search KB for OpenBB"
2. Try saving: "Save my next analysis"
3. Explore domains: Check each INDEX.md
4. Read conventions: CONVENTIONS.md

---

[← Back to INDEX](../INDEX.md)
