# Knowledge Base Conventions

This document defines how to use and maintain the knowledge base system.

## 🎯 Core Principles

1. **AI-First Design** - Optimized for Claude Code interaction
2. **Single Source of Truth** - Each fact exists in one canonical location
3. **Cross-Referenced** - Related topics are linked
4. **Template-Driven** - Use templates for consistency
5. **Self-Documenting** - Indexes and manifests stay current

---

## 📁 Directory Structure Rules

### Domains
- **Location:** `domains/[domain-name]/`
- **Purpose:** Organize knowledge by subject area
- **Required:** INDEX.md in each domain
- **Subdirectories:** Group related topics

### Projects
- **Location:** `projects/[project-name]/`
- **Purpose:** Active work and project-specific knowledge
- **Required:** README.md, spec.md
- **Structure:** Code, research, decisions as subdirectories

### Templates
- **Location:** `templates/`
- **Purpose:** Reusable document structures
- **Naming:** `[purpose].md`
- **Content:** Include placeholder sections and instructions

### Meta
- **Location:** `meta/`
- **Purpose:** System documentation
- **Content:** How-to guides, maintenance docs, Claude prompts

### Archive
- **Location:** `_archive/YYYY-MM/`
- **Purpose:** Completed or outdated content
- **Organization:** By month of archival

---

## 📝 File Naming Conventions

### General Files
```
✅ Good: openbb-capabilities.md
✅ Good: python-pandas-reference.md
❌ Bad: OpenBB_Capabilities.md
❌ Bad: python pandas reference.md
```

**Rule:** lowercase-with-hyphens.md

### Stock Analysis
```
✅ Good: RELIANCE.md
✅ Good: TCS.md
❌ Bad: reliance.md
❌ Bad: tata-consultancy-services.md
```

**Rule:** UPPERCASE-SYMBOL.md (use official ticker)

### Code Snippets
```
✅ Good: python-openbb-analysis.md
✅ Good: bash-git-workflow.md
❌ Bad: snippet1.md
❌ Bad: code.md
```

**Rule:** [language]-[purpose].md

### Date-Stamped Files
```
✅ Good: 2025-10-18-market-analysis.md
✅ Good: weekly-report-2025-W42.md
❌ Bad: oct-18-analysis.md
❌ Bad: analysis-10-18-25.md
```

**Rule:** YYYY-MM-DD-[description].md or [description]-YYYY-Www.md

---

## 📋 Document Structure

### Required Front Matter
Every document should start with:

```markdown
# Document Title

**Domain:** [domain-name]
**Created:** YYYY-MM-DD
**Last Updated:** YYYY-MM-DD
**Tags:** tag1, tag2, tag3

Brief description of what this document contains.
```

### Heading Hierarchy
```markdown
# Title (H1) - Document title only
## Section (H2) - Main sections
### Subsection (H3) - Subsections
#### Detail (H4) - Fine details
```

**Rule:** Only ONE H1 per document

### Cross-References
```markdown
✅ Good: See [OpenBB Capabilities](domains/finance/openbb/capabilities.md)
✅ Good: Related: [Python Guide](../dev/python/basics.md)
❌ Bad: See /Users/kareddy/Desktop/explore/kb/domains/finance/...
❌ Bad: See OpenBB docs (no link)
```

**Rule:** Use relative paths from kb/ root

---

## 🔍 Where to Save Different Content

### Financial Analysis
```
Stock analysis     → domains/finance/stocks/[SYMBOL].md
Strategy research  → domains/finance/strategies/[name].md
Tool/script        → domains/finance/tools/[name].py or .md
General concept    → domains/finance/[concept].md
```

### Development Knowledge
```
API documentation  → domains/dev/apis/[api-name].md
Code snippet       → domains/dev/snippets/[language]-[purpose].md
Library reference  → domains/dev/[language]/[library].md
Tutorial           → domains/dev/[language]/[concept]-tutorial.md
```

### Data Science
```
Technique/method   → domains/data/techniques/[method].md
Tool documentation → domains/data/tools/[tool-name].md
Analysis example   → domains/data/examples/[example-name].md
```

### Project Work
```
Project files      → projects/[project-name]/[file].md
Research notes     → projects/[project-name]/research/[topic].md
Code               → projects/[project-name]/code/
Decisions          → projects/[project-name]/decisions.md
```

---

## 🤖 Claude Interaction Patterns

### Saving Information

**User Says:**
```
"Save this OpenBB analysis"
"Create a stock analysis for RELIANCE"
"Add this Python snippet"
```

**Claude Should:**
1. Read MANIFEST.json to find correct location
2. Check if template applies
3. Create document with proper structure
4. Update relevant INDEX.md
5. Confirm save location to user

### Finding Information

**User Says:**
```
"What are OpenBB's limitations?"
"Find my RELIANCE analysis"
"Show Python pandas examples"
```

**Claude Should:**
1. Check INDEX.md for quick reference
2. Consult MANIFEST.json for document paths
3. Read relevant documents
4. Synthesize answer
5. Cite source documents

### Updating Information

**User Says:**
```
"Update RELIANCE analysis with new data"
"Add this finding to OpenBB limitations"
```

**Claude Should:**
1. Locate existing document
2. Read current content
3. Add new information appropriately
4. Update "Last Updated" date
5. Update INDEX if major change

---

## 📊 Index Maintenance

### Domain INDEX.md
Update when:
- ✅ New document added to domain
- ✅ Document significantly updated
- ✅ Document archived or deleted
- ✅ New subtopic created

Should contain:
- Quick reference for domain
- List of all major documents
- Recently updated items
- Common questions with answers

### Master INDEX.md
Update when:
- ✅ New domain created
- ✅ Domain description changes
- ✅ Statistics change significantly
- ✅ New templates added

### MANIFEST.json
Update when:
- ✅ New domain added
- ✅ New subtopic created
- ✅ Document paths change
- ✅ Key documents change
- ✅ Statistics need updating

---

## 🎨 Formatting Standards

### Tables
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data     | Data     | Data     |
```

### Code Blocks
````markdown
```python
# Always specify language
def example():
    pass
```
````

### Lists
```markdown
✅ Checklist items
- Regular bullet
1. Numbered item
```

### Emphasis
```markdown
**Bold** for importance
*Italic* for emphasis
`code` for inline code
```

### Status Indicators
```markdown
✅ Working / Complete
⚠️ Limited / Warning
❌ Not Working / Broken
🚧 In Progress
📝 Note / Info
💡 Tip / Insight
```

---

## 🗄️ Archival Process

### When to Archive
- Document is outdated
- Project is completed
- Information no longer relevant
- Better version exists

### How to Archive
1. Create `_archive/YYYY-MM/` if needed
2. Move document(s) to archive
3. Update relevant INDEX.md files
4. Update MANIFEST.json
5. Add note in INDEX about archival

### Archive Structure
```
_archive/
├── 2025-10/
│   ├── old-document.md
│   └── completed-project/
└── 2025-11/
```

---

## 🔄 Regular Maintenance

### Weekly
- [ ] Review recently added documents
- [ ] Ensure proper formatting
- [ ] Check broken links
- [ ] Update statistics in INDEX.md

### Monthly
- [ ] Review all domain indexes
- [ ] Archive outdated content
- [ ] Update MANIFEST.json
- [ ] Review and improve templates

### Quarterly
- [ ] Full knowledge base audit
- [ ] Reorganize if needed
- [ ] Update conventions
- [ ] Improve Claude integration

---

## 💡 Best Practices

### For You
1. **Let Claude do the work** - Use natural language to save/find
2. **Use templates** - Ensures consistency
3. **Cross-reference** - Link related topics
4. **Update indexes** - Keep them current
5. **Archive regularly** - Keep KB clean

### For Claude
1. **Always check MANIFEST.json first** - Know the structure
2. **Use templates when appropriate** - Maintain consistency
3. **Update indexes** - Keep navigation current
4. **Cite sources** - Reference documents used
5. **Follow conventions** - Maintain system integrity

---

## 🚫 Anti-Patterns (Don't Do This)

❌ Duplicate information in multiple places
❌ Create files without checking conventions
❌ Forget to update indexes
❌ Use absolute file paths
❌ Skip templates when they apply
❌ Leave broken links
❌ Mix naming conventions
❌ Ignore document structure rules

---

## 🆘 Troubleshooting

### "Where should I save this?"
1. Check MANIFEST.json for similar content
2. Look at existing structure
3. Ask Claude: "Where in KB should I save [content]?"

### "Can't find what I'm looking for"
1. Check main INDEX.md
2. Check domain INDEX.md
3. Ask Claude: "Search KB for [topic]"
4. Use grep: `grep -r "search term" domains/`

### "Structure doesn't fit my content"
1. Check if new domain/subtopic needed
2. See `meta/how-to-use.md` for guidance
3. Consider if content belongs in KB

---

**Last Updated:** 2025-10-18
**Next Review:** Monthly
