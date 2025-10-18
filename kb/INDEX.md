# Knowledge Base - Master Index

**Version:** 1.0
**Last Updated:** 2025-10-18
**Total Domains:** 3 (Finance, Dev, Data)

> 🤖 **For Claude:** See `MANIFEST.json` for complete system map and `CONVENTIONS.md` for interaction rules.

---

## 🎯 Quick Start

**I want to...**
- Find information → Ask Claude: "Search KB for [topic]"
- Save information → Ask Claude: "Save this to KB in [domain]"
- See what's available → Check domain indexes below
- Add new domain → See `CONVENTIONS.md`

---

## 📚 Knowledge Domains

### 💰 Finance
**Path:** `domains/finance/`
**Status:** Active | Last Updated: 2025-10-18

**Contents:**
- **OpenBB Platform** - API capabilities, limitations, test results
- **Stock Analysis** - Individual stock research and analysis
- **Strategies** - Trading/investing strategies
- **Tools** - Financial calculation scripts

**Quick Links:**
- [Finance Domain Index](domains/finance/INDEX.md)
- [OpenBB Capabilities](domains/finance/openbb/capabilities.md)
- [OpenBB Quick Reference](domains/finance/openbb/quick-reference.md)

**Common Questions:**
- "Can I get Indian stock prices?" → Yes, see [OpenBB NSE/BSE](domains/finance/openbb/capabilities.md#indian-markets)
- "How to calculate Sharpe ratio?" → See [Risk Metrics](domains/finance/tools/)
- "What's RELIANCE P/E ratio?" → Ask Claude to analyze using OpenBB

---

### 💻 Development
**Path:** `domains/dev/`
**Status:** Active | Last Updated: 2025-10-18

**Contents:**
- **Python** - Python libraries, patterns, references
- **APIs** - API documentation and integration guides
- **Snippets** - Reusable code examples

**Quick Links:**
- [Dev Domain Index](domains/dev/INDEX.md)
- [Python References](domains/dev/python/)
- [API Guides](domains/dev/apis/)

**Common Questions:**
- "How to use pandas?" → See [Pandas Reference](domains/dev/python/pandas.md)
- "FastAPI example?" → See [FastAPI Guide](domains/dev/apis/fastapi.md)
- "MCP server setup?" → See [MCP Guide](domains/dev/apis/mcp.md)

---

### 📊 Data Science
**Path:** `domains/data/`
**Status:** Active | Last Updated: 2025-10-18

**Contents:**
- **Techniques** - Analysis methods, statistical techniques
- **Tools** - Data analysis tools and libraries

**Quick Links:**
- [Data Domain Index](domains/data/INDEX.md)
- [Analysis Techniques](domains/data/techniques/)
- [Tools Reference](domains/data/tools/)

**Common Questions:**
- "How to calculate correlation?" → See [Statistical Techniques](domains/data/techniques/statistics.md)
- "Time series analysis?" → See [Time Series](domains/data/techniques/time-series.md)

---

## 🚀 Active Projects

**Path:** `projects/`

**Current Projects:**
- *No active projects yet*

**To create new project:**
```
Ask Claude: "Create new project called [name]"
Or manually: Copy templates/project-spec.md to projects/[name]/
```

---

## 📋 Templates

**Path:** `templates/`

Available templates for consistent documentation:

| Template | Use For | Path |
|----------|---------|------|
| `stock-analysis.md` | Stock research | For analyzing individual stocks |
| `api-reference.md` | API documentation | Documenting APIs and libraries |
| `code-snippet.md` | Code examples | Saving reusable code |
| `learning-note.md` | Concepts & tutorials | Educational content |
| `project-spec.md` | Project planning | New project specifications |

**Usage:**
```
Ask Claude: "Use [template-name] to create [new-doc]"
```

---

## 🔍 How to Find Information

### Method 1: Ask Claude (Recommended)
```
"Search KB for OpenBB limitations"
"Find all stock analysis for RELIANCE"
"Show me pandas examples"
```

### Method 2: Browse Indexes
1. Start with this INDEX.md
2. Navigate to domain INDEX.md
3. Follow links to specific content

### Method 3: Search Files
```bash
# From kb/ directory
grep -r "search term" domains/
find . -name "*filename*"
```

---

## 📝 How to Save Information

### Method 1: Ask Claude (Recommended)
```
"Save this OpenBB analysis to finance domain"
"Create a new learning note about FastAPI"
"Add this code snippet to dev/python"
```

### Method 2: Manual Creation
1. Choose appropriate domain
2. Use relevant template
3. Follow naming conventions (see CONVENTIONS.md)
4. Update domain INDEX.md
5. Update MANIFEST.json

---

## 📊 Knowledge Base Statistics

| Metric | Count |
|--------|-------|
| **Total Domains** | 3 |
| **Total Documents** | 10 |
| **Active Projects** | 0 |
| **Templates** | 5 |
| **Last Modified** | 2025-10-18 |

---

## 🎓 System Documentation

- **[CONVENTIONS.md](CONVENTIONS.md)** - How to use this system
- **[MANIFEST.json](MANIFEST.json)** - Machine-readable catalog
- **[meta/how-to-use.md](meta/how-to-use.md)** - Detailed usage guide
- **[meta/claude-prompts.md](meta/claude-prompts.md)** - Useful Claude commands
- **[meta/maintenance.md](meta/maintenance.md)** - System maintenance

---

## 🆕 Recently Added

*No recent additions yet*

---

## 📌 Frequently Accessed

*Top 10 most accessed documents will appear here*

---

## 🗺️ Domain Overview Map

```
kb/
├── Finance           [OpenBB, Stocks, Strategies, Tools]
├── Development       [Python, APIs, Code Snippets]
├── Data Science      [Techniques, Tools]
└── Projects          [Active work]
```

---

## 💡 Tips

**For Best Results:**
1. 🤖 Use Claude to interact with KB - it's designed for AI-first access
2. 📋 Use templates for consistency
3. 🔗 Cross-reference related topics
4. 📊 Keep domain indexes updated
5. 🗂️ Archive completed work to `_archive/`

**Claude Can:**
- Search across all domains
- Create new entries using templates
- Update indexes automatically
- Cross-reference related content
- Synthesize information from multiple sources

**You Should:**
- Start here for human browsing
- Check domain indexes for specific areas
- Follow links for deep dives
- Ask Claude for complex queries

---

## 🔗 External Resources

*Links to external knowledge bases, documentation, etc.*

- [OpenBB Official Docs](https://docs.openbb.co/)
- [Python Official Docs](https://docs.python.org/)
- *Add more as needed*

---

**Last Index Update:** 2025-10-18
**Next Review:** As needed
**Maintainer:** You + Claude
