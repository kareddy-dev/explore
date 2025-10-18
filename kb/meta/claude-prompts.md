# Useful Claude Prompts for KB

**Last Updated:** 2025-10-18

A collection of effective prompts for interacting with the knowledge base through Claude Code.

---

## 🔍 Searching & Finding

### Basic Search
```
"Search KB for [topic]"
"Find information about [subject]"
"What do I know about [topic]?"
```

### Specific Searches
```
"Find all stock analyses"
"Show me Python snippets"
"List everything in finance domain"
"What OpenBB limitations are documented?"
```

### Cross-Domain Search
```
"Find anything related to [topic] across all domains"
"How does [topic A] relate to [topic B]?"
"Show me everything about [company/technology]"
```

---

## 💾 Saving & Creating

### Save New Content
```
"Save this analysis to KB"
"Add this to knowledge base in [domain]"
"Document this in KB"
"Create a new entry for [topic]"
```

### Specific Document Types
```
"Create a stock analysis for [SYMBOL]"
"Save this as a code snippet"
"Document this API in KB"
"Create a learning note about [concept]"
"Start a new project called [name]"
```

### With Template
```
"Use stock-analysis template to analyze [SYMBOL]"
"Create new learning note using template"
"Set up project using project-spec template"
```

---

## ✏️ Updating

### Update Existing
```
"Update [document] with this new information"
"Add this finding to [topic]"
"Revise [document] with latest data"
```

### Update Indexes
```
"Update finance INDEX with new documents"
"Refresh MANIFEST.json"
"Update statistics in main INDEX"
```

---

## 📊 Analysis & Synthesis

### Compare
```
"Compare what I know about [A] vs [B]"
"Show differences between [topic1] and [topic2]"
```

### Synthesize
```
"Summarize everything in [domain]"
"Create overview of [topic] from KB"
"Compile all information about [subject]"
```

### Discover Gaps
```
"What's missing from [domain]?"
"What should I document about [topic]?"
"What related topics aren't covered?"
```

---

## 🗂️ Organization

### Review Structure
```
"Show me the KB structure"
"What's in [domain]?"
"List all templates"
"Show domains and their contents"
```

### Reorganize
```
"Should [document] be in a different domain?"
"Suggest better organization for [topic]"
"Find duplicate information in KB"
```

### Archive
```
"Archive [document]"
"Move completed project to archive"
"Clean up old content from [domain]"
```

---

## 🎯 Domain-Specific

### Finance
```
"Analyze [SYMBOL] and save to KB"
"Update RELIANCE analysis with latest data"
"What stocks have I analyzed?"
"Compare my analyses of [SYMBOL1] vs [SYMBOL2]"
"What do I know about OpenBB's limitations?"
```

### Development
```
"Save this Python snippet"
"Document FastAPI usage"
"Find pandas examples"
"What APIs have I documented?"
```

### Data Science
```
"Document this analysis technique"
"Save this statistical method"
"Find correlation analysis examples"
```

---

## 🚀 Project Management

### Start Project
```
"Create new project called [name]"
"Set up project workspace for [topic]"
"Initialize [project] with spec template"
```

### Track Progress
```
"Update [project] progress"
"What's the status of [project]?"
"Show all active projects"
```

### Complete Project
```
"Mark [project] as completed"
"Archive [project] work"
"Generate project summary for [name]"
```

---

## 📚 Learning & Reference

### Document Learning
```
"I learned [concept], save this"
"Document how [technology] works"
"Create reference for [library]"
```

### Quick Reference
```
"Quick reference for [topic]"
"Common commands for [tool]"
"How do I [task]?"
```

---

## 🔗 Cross-Referencing

### Find Related
```
"What's related to [topic]?"
"Find connections between [A] and [B]"
"Show me everything linked to [document]"
```

### Create Links
```
"Link [document A] to [document B]"
"Add cross-references for [topic]"
"Connect [concept] across domains"
```

---

## 📊 Reporting

### Generate Reports
```
"Generate summary of [domain]"
"Create report on [topic] from KB"
"List recently updated documents"
"Show KB statistics"
```

### Export
```
"Export all [domain] content"
"Compile [topic] information"
"Generate overview of [subject]"
```

---

## 🔧 Maintenance

### Check Health
```
"Check for broken links in KB"
"Find outdated documents"
"Verify MANIFEST.json accuracy"
"List documents needing review"
```

### Clean Up
```
"Remove duplicates in KB"
"Archive old content from [domain]"
"Clean up [domain]"
```

### Update System
```
"Update all indexes"
"Refresh domain statistics"
"Regenerate MANIFEST.json"
```

---

## 💡 Advanced Prompts

### Batch Operations
```
"Analyze these stocks and save: RELIANCE, TCS, INFY"
"Create learning notes for: [concept1], [concept2], [concept3]"
"Update all analyses in finance domain with latest data"
```

### Complex Queries
```
"Find all Python snippets related to financial analysis"
"Show me OpenBB capabilities for Indian stocks"
"Compare all my stock analyses by sector"
"Create a portfolio based on my stock analyses"
```

### Meta Operations
```
"Create new domain for [topic]"
"Add new template for [purpose]"
"Extend finance domain with new subtopic"
```

---

## 🎨 Custom Workflows

### Morning Research Routine
```
"Update stock watchlist analyses"
"Check for new information on tracked stocks"
"Generate daily finance summary from KB"
```

### Learning Session
```
"Document today's learning about [topic]"
"Add to [concept] notes"
"Create practice exercises for [skill]"
```

### Project Review
```
"Review [project] status"
"Update [project] decisions log"
"Check [project] against requirements"
```

---

## 🚫 What NOT to Ask

❌ **Don't:**
```
"Delete everything" (too dangerous)
"Change all files" (too broad)
"Override MANIFEST" (Claude should validate)
```

✅ **Instead:**
```
"Archive [specific content]"
"Update [specific document]"
"Regenerate MANIFEST based on current structure"
```

---

## 💬 Conversational Style

You can also use natural language:

```
"Hey, I just analyzed RELIANCE stock. Can you save this to the KB?"

"I'm looking for that pandas example we saved last week. Can you find it?"

"What do we know about OpenBB's Indian stock support?"

"Let's start a new project for building a portfolio tracker"
```

---

## 🎓 Tips for Best Results

1. **Be Specific:** "Save to finance/stocks" vs "save somewhere"
2. **Provide Context:** "Update RELIANCE analysis with Q3 earnings"
3. **Use Names:** Reference documents by name
4. **Ask for Confirmation:** Claude will confirm saves
5. **Request Citations:** "...and show me the sources"

---

## 📝 Template Prompts

Copy and customize these:

### For Stock Analysis
```
"Analyze [SYMBOL] stock:
- Get latest price and fundamentals from OpenBB
- Calculate key metrics
- Provide investment recommendation
- Save to KB with stock-analysis template"
```

### For Code Documentation
```
"Document this code:
[paste code]
- Explain what it does
- Add usage examples
- Save as code snippet in dev/python"
```

### For Learning Notes
```
"I learned about [concept]:
[your notes]
- Organize this
- Add examples
- Save as learning note in [domain]"
```

---

**Pro Tip:** Save your most-used prompts here for quick reference!

---

[← Back to META](how-to-use.md) | [← Back to INDEX](../INDEX.md)
