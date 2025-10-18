# Knowledge Base System - Instructions for Claude Code

**Version:** 1.0.0
**Last Updated:** 2025-10-18
**System Type:** AI-First Knowledge Management

---

## 🎯 System Overview

This is a comprehensive knowledge management system ("digital brain") optimized for Claude Code integration. You (Claude) are designed to be the primary interface for saving, finding, and organizing information.

**Critical Files:**
- `MANIFEST.json` - Complete system map (READ THIS FIRST)
- `CONVENTIONS.md` - Rules and standards you must follow
- `INDEX.md` - Human-readable navigation
- Domain `INDEX.md` files - Domain-specific content maps

---

## 🔍 When User Asks to SEARCH

### Search Protocol:
1. **Check MANIFEST.json** - Find relevant domain(s)
2. **Read domain INDEX.md** - Get overview of available content
3. **Search specific documents** - Read relevant files
4. **Synthesize answer** - Combine information from multiple sources
5. **Cite sources** - Always reference file paths

### Search Examples:
```
User: "What are OpenBB's limitations?"
You:
1. Read MANIFEST.json → find domains.finance.openbb
2. Read domains/finance/openbb/capabilities.md
3. Extract limitations section
4. Answer: "OpenBB has these limitations... (See kb/domains/finance/openbb/capabilities.md)"
```

### Search Tips:
- **Start broad:** Check domain indexes first
- **Be thorough:** Search related domains (e.g., finance + dev for "OpenBB with pandas")
- **Cross-reference:** Look for related topics in MANIFEST.json
- **Always cite:** Format: `(See kb/domains/[domain]/[file].md)`

---

## 💾 When User Asks to SAVE

### Save Protocol:
1. **Analyze content type** - Determine what kind of information it is
2. **Select domain** - Use MANIFEST.json to find correct location
3. **Choose template** - Apply appropriate template from templates/
4. **Follow conventions** - Use naming rules from CONVENTIONS.md
5. **Save file** - Write to correct location
6. **Update indexes** - Update domain INDEX.md with new entry
7. **Update manifest** - Update MANIFEST.json if new subtopic
8. **Confirm** - Tell user exact save location

### Domain Selection Logic:
```
Financial analysis/stocks → domains/finance/
API/library documentation → domains/dev/apis/
Code snippets → domains/dev/snippets/
Python-specific → domains/dev/python/
Data analysis methods → domains/data/techniques/
Analysis tools → domains/data/tools/
Project work → projects/[project-name]/
```

### Template Selection Logic:
```
Stock analysis → templates/stock-analysis.md
API docs → templates/api-reference.md
Code snippet → templates/code-snippet.md
Learning note → templates/learning-note.md
Project → templates/project-spec.md
```

### Naming Conventions (CRITICAL):
```
✅ General files: lowercase-with-hyphens.md
✅ Stock symbols: UPPERCASE-SYMBOL.md (e.g., RELIANCE.md)
✅ Code snippets: [language]-[purpose].md (e.g., python-sharpe-ratio.md)
✅ Dates: YYYY-MM-DD-[description].md

❌ NO spaces in filenames
❌ NO CamelCase (except stock symbols)
❌ NO special characters except hyphens
```

### Save Example:
```
User: "Save this analysis of RELIANCE stock"
You:
1. Identify: Stock analysis
2. Domain: domains/finance/stocks/
3. Template: templates/stock-analysis.md
4. Filename: RELIANCE.md (uppercase symbol)
5. Write file to domains/finance/stocks/RELIANCE.md
6. Update domains/finance/INDEX.md:
   - Add RELIANCE.md to stocks section
   - Update document count
7. Update MANIFEST.json if needed
8. Confirm: "✅ Saved to kb/domains/finance/stocks/RELIANCE.md"
```

---

## 📝 When User Asks to UPDATE

### Update Protocol:
1. **Locate document** - Use MANIFEST.json or search
2. **Read current content** - Understand what exists
3. **Preserve structure** - Maintain template format
4. **Add new information** - Insert appropriately
5. **Update metadata** - Change "Last Updated" date
6. **Update indexes** - If major change, update domain INDEX.md

### Update Example:
```
User: "Update RELIANCE analysis with Q3 earnings"
You:
1. Read domains/finance/stocks/RELIANCE.md
2. Find appropriate section (Fundamentals or Notes)
3. Add Q3 earnings data
4. Update "Last Updated: YYYY-MM-DD"
5. If major change, update domains/finance/INDEX.md
6. Confirm update
```

---

## 🗂️ Content Organization Rules

### Domain Structure:
```
domains/
├── finance/
│   ├── INDEX.md           ← Update when adding content
│   ├── openbb/            ← OpenBB documentation
│   ├── stocks/            ← Individual stock analyses (SYMBOL.md)
│   ├── strategies/        ← Trading/investing strategies
│   └── tools/             ← Financial scripts
│
├── dev/
│   ├── INDEX.md
│   ├── python/            ← Python library references
│   ├── apis/              ← API documentation
│   └── snippets/          ← Code snippets ([language]-[purpose].md)
│
└── data/
    ├── INDEX.md
    ├── techniques/        ← Analysis methods
    └── tools/             ← Data analysis tools
```

### When to Create New Subtopic:
- **5+ related documents** in a domain
- **Clear category** that doesn't fit existing subtopics
- **User explicitly requests** organization change

When creating new subtopic:
1. Create directory
2. Move relevant files
3. Update domain INDEX.md
4. Update MANIFEST.json subtopics section
5. Update main INDEX.md if needed

---

## 🎨 Document Structure Standards

### Every Document MUST Have:
```markdown
# Title

**Domain:** [domain-name]
**Created:** YYYY-MM-DD
**Last Updated:** YYYY-MM-DD
**Tags:** tag1, tag2, tag3

Brief description.

---

## Main Content Here
```

### Required Elements:
- ✅ ONE H1 heading (title)
- ✅ Frontmatter with domain, dates, tags
- ✅ H2 (##) for main sections
- ✅ Relative links to other KB files
- ✅ Code blocks with language specified
- ✅ Consistent formatting

### Cross-Referencing:
```markdown
✅ Good: See [OpenBB Capabilities](../../finance/openbb/capabilities.md)
✅ Good: Related: [Python Guide](../dev/python/pandas.md)

❌ Bad: See /Users/kareddy/Desktop/explore/kb/... (absolute path)
❌ Bad: See OpenBB docs (no link)
```

---

## 🤖 Special Behaviors

### When User Says "Search KB":
- Read MANIFEST.json first
- Check relevant domain indexes
- Search multiple domains if topic spans areas
- Always provide file paths in citations

### When User Says "Save to KB":
- Ask clarifying questions if domain unclear
- Apply appropriate template
- Follow all naming conventions
- Update all necessary indexes
- Provide full save path in confirmation

### When User Says "What's in [domain]?":
- Read domain INDEX.md
- Summarize contents
- List key documents
- Suggest related queries

### When User Asks About KB Structure:
- Explain based on MANIFEST.json
- Show domain overview
- Explain how to navigate
- Reference README.md for details

---

## 📊 Index Maintenance

### Always Update domain INDEX.md When:
- ✅ Adding new document to domain
- ✅ Removing document from domain
- ✅ Significantly updating document content
- ✅ Creating new subtopic

### Update MANIFEST.json When:
- ✅ Creating new domain
- ✅ Creating new subtopic
- ✅ Adding key documents
- ✅ Changing domain structure
- ✅ Statistics change significantly

### Update main INDEX.md When:
- ✅ Creating new domain
- ✅ Domain descriptions change
- ✅ Statistics need updating (quarterly)

---

## 🎯 Common Workflows

### Workflow 1: New Stock Analysis
```
1. User: "Analyze RELIANCE and save"
2. Gather data (OpenBB or other source)
3. Apply templates/stock-analysis.md
4. Save to domains/finance/stocks/RELIANCE.md
5. Update domains/finance/INDEX.md
6. Confirm: "Saved to kb/domains/finance/stocks/RELIANCE.md"
```

### Workflow 2: Code Snippet
```
1. User: "Save this Python code"
2. Identify purpose (e.g., "calculate Sharpe ratio")
3. Apply templates/code-snippet.md
4. Save to domains/dev/snippets/python-sharpe-ratio.md
5. Update domains/dev/INDEX.md
6. Confirm save location
```

### Workflow 3: Learning Note
```
1. User: "I learned about [concept]"
2. Determine domain (finance/dev/data)
3. Apply templates/learning-note.md
4. Save to domains/[domain]/[concept].md
5. Update domain INDEX.md
6. Confirm save location
```

### Workflow 4: Cross-Domain Query
```
1. User: "How to use pandas with OpenBB?"
2. Read domains/finance/openbb/capabilities.md
3. Read domains/dev/python/pandas.md (if exists)
4. Synthesize answer from both
5. Cite both sources
6. Suggest creating new doc if useful
```

---

## 🚨 Critical Rules

### ALWAYS:
- ✅ Read MANIFEST.json before first save/search in session
- ✅ Follow naming conventions exactly
- ✅ Use templates when applicable
- ✅ Update domain INDEX.md after saves
- ✅ Cite sources with file paths
- ✅ Use relative paths for links
- ✅ Update "Last Updated" dates

### NEVER:
- ❌ Create files outside domains/ or projects/
- ❌ Skip frontmatter in documents
- ❌ Use absolute file paths in links
- ❌ Forget to update indexes
- ❌ Duplicate information across files
- ❌ Mix naming conventions
- ❌ Modify MANIFEST.json structure without user approval

---

## 🔍 Troubleshooting

### Can't Find Content:
1. Check MANIFEST.json for domain structure
2. Read relevant domain INDEX.md
3. Search specific directories
4. Check if content might be in different domain

### Unsure Where to Save:
1. Check MANIFEST.json save_patterns
2. Read CONVENTIONS.md
3. Look at similar existing content
4. Ask user for clarification if still unclear

### Template Doesn't Fit:
1. Use closest available template
2. Adapt sections as needed
3. Maintain consistent structure
4. Consider creating new template (with user approval)

---

## 💡 Optimization Tips

### For Speed:
- **Cache MANIFEST.json** in context for session
- **Read domain indexes** first for overview
- **Use grep** for keyword searches across files
- **Batch updates** when making multiple changes

### For Quality:
- **Always cite sources** - builds trust
- **Cross-reference** related topics
- **Update dates** consistently
- **Maintain templates** strictly
- **Keep indexes current**

### For User Experience:
- **Confirm saves** with exact paths
- **Suggest related content** when searching
- **Explain structure** when asked
- **Provide examples** when teaching

---

## 📚 Quick Reference

### File Paths:
```
Main index:       INDEX.md
System map:       MANIFEST.json
Rules:            CONVENTIONS.md
Templates:        templates/
Finance:          domains/finance/
Dev:              domains/dev/
Data:             domains/data/
Projects:         projects/
Meta docs:        meta/
```

### Common Commands (User):
```
"Search KB for [topic]"
"Save this to KB"
"What's in [domain]?"
"Update [document]"
"Create new [type] for [topic]"
```

### Your Response Format:
```
1. Acknowledge request
2. Perform action (search/save/update)
3. Provide result with citations
4. Confirm changes if saving
```

---

## 🎓 Learning Resources

For details on:
- **Usage patterns** → meta/how-to-use.md
- **Claude commands** → meta/claude-prompts.md
- **Maintenance** → meta/maintenance.md
- **System overview** → README.md

---

## ✅ Checklist for Every Save

Before confirming save, verify:
- [ ] Correct domain selected
- [ ] Template applied (if applicable)
- [ ] Naming convention followed
- [ ] Frontmatter complete
- [ ] Content structured properly
- [ ] Domain INDEX.md updated
- [ ] MANIFEST.json updated (if needed)
- [ ] User informed of exact save location

---

## 🎯 Success Metrics

You're doing well if:
- ✅ Users can find content in < 30 seconds
- ✅ All documents follow templates
- ✅ Indexes are always current
- ✅ No broken links
- ✅ Consistent naming across files
- ✅ Cross-references are accurate

---

**Remember:** This KB system is designed for YOU (Claude) to be the primary interface. The user should rarely need to manually manage files. Your job is to handle all file operations seamlessly while maintaining perfect organization.

**Core Principle:** Make it effortless for the user to store and retrieve knowledge by handling all the complexity behind the scenes.

---

**System Version:** 1.0.0
**Last Reviewed:** 2025-10-18
**Next Review:** Monthly or when structure changes
