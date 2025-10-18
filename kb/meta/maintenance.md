# Knowledge Base Maintenance Guide

**Last Updated:** 2025-10-18

---

## 🎯 Maintenance Philosophy

The KB is designed to be **self-maintaining** through Claude, but periodic reviews ensure quality and organization.

**Key Principles:**
- Claude handles routine updates
- You handle strategic decisions
- Regular reviews keep KB healthy
- Archive prevents clutter

---

## 📅 Maintenance Schedule

### Weekly (5 minutes)
```
Ask Claude:
"Check KB health and report issues"
"List recently added documents"
"Find any broken links"
```

**Manual Check:**
- [ ] New content makes sense
- [ ] No obvious duplicates
- [ ] Indexes look current

---

### Monthly (15 minutes)
```
Ask Claude:
"Generate KB monthly report"
"Find outdated documents"
"Check all domain indexes"
"Verify MANIFEST accuracy"
```

**Review:**
- [ ] Archive completed projects
- [ ] Update domain descriptions if needed
- [ ] Remove truly obsolete content
- [ ] Update templates if needed

---

### Quarterly (30 minutes)
```
Ask Claude:
"Perform full KB audit"
"Suggest organizational improvements"
"Find duplicate information"
"Check cross-references"
```

**Strategic Review:**
- [ ] Is structure still working?
- [ ] Need new domains/subtopics?
- [ ] Templates still relevant?
- [ ] Conventions still make sense?

---

## 🔍 Health Checks

### Check 1: Index Accuracy
```
Ask Claude:
"Verify all domain indexes match actual content"
"Check if MANIFEST.json is accurate"
"Find documents not listed in any index"
```

**Fix:** Update indexes and manifest

---

### Check 2: Broken Links
```
Ask Claude:
"Check for broken internal links"
"Find references to moved documents"
"Verify all cross-references work"
```

**Fix:** Update links or create redirects

---

### Check 3: Duplicates
```
Ask Claude:
"Find duplicate information in KB"
"Identify overlapping content"
"Suggest consolidation opportunities"
```

**Fix:** Consolidate or cross-reference

---

### Check 4: Outdated Content
```
Ask Claude:
"Find documents older than 6 months"
"Check if documented info is still current"
"List 'Last Updated' dates for all docs"
```

**Fix:** Update or archive

---

### Check 5: Orphaned Documents
```
Ask Claude:
"Find documents not linked from any index"
"Check for files in wrong locations"
"Identify documents without domain tag"
```

**Fix:** Move, link, or archive

---

## 🗂️ Archival Process

### When to Archive
- Project completed
- Information obsolete
- Better version exists
- No longer relevant

### How to Archive
```
Ask Claude:
"Archive [document/project] to [YYYY-MM]"
"Move completed project to archive"
"Archive all documents older than [date]"
```

**Manual Process:**
1. Create `_archive/YYYY-MM/` if needed
2. Move content (Claude can do this)
3. Update relevant indexes
4. Update MANIFEST.json
5. Add archive note in old location if needed

### What to Archive
✅ **Archive:**
- Completed projects
- Outdated analysis (keep for reference)
- Obsolete documentation
- Superseded versions

❌ **Don't Archive:**
- Current knowledge
- Templates (update instead)
- Core documentation
- Active projects

---

## 📊 Quality Assurance

### Document Quality Checklist
```
Ask Claude to check:
- [ ] Has required frontmatter
- [ ] Uses correct heading hierarchy
- [ ] Includes cross-references
- [ ] Has updated date
- [ ] Tagged appropriately
- [ ] Follows conventions
```

### Index Quality Checklist
- [ ] All documents listed
- [ ] Descriptions accurate
- [ ] Quick answers current
- [ ] Statistics match reality
- [ ] Links work

### MANIFEST Quality Checklist
- [ ] All domains listed
- [ ] Paths correct
- [ ] Key documents accurate
- [ ] Statistics current
- [ ] Instructions clear

---

## 🔧 Common Maintenance Tasks

### Task 1: Update Statistics
```
Ask Claude:
"Update KB statistics in INDEX.md"
"Count total documents per domain"
"Update MANIFEST.json statistics"
```

### Task 2: Reorganize Content
```
Ask Claude:
"Should [document] be in different domain?"
"Suggest better structure for [domain]"
"Reorganize [domain] for better navigation"
```

### Task 3: Clean Up Naming
```
Ask Claude:
"Check all files follow naming conventions"
"Rename files that don't follow standards"
"Standardize document titles"
```

### Task 4: Update Cross-References
```
Ask Claude:
"Add cross-references for related [topic]"
"Update links to moved documents"
"Create topic connection map"
```

---

## 🚨 Troubleshooting

### Problem: Can't Find Something
```
Solutions:
1. Ask Claude to search
2. Check domain indexes
3. Use grep: grep -r "term" kb/
4. Check MANIFEST.json for hints
```

### Problem: Duplicate Information
```
Solutions:
1. Consolidate into one document
2. Keep most complete version
3. Add cross-references
4. Archive duplicates
```

### Problem: Outdated Content
```
Solutions:
1. Update with current info
2. Add "Last Updated" note
3. Archive if obsolete
4. Link to newer version
```

### Problem: Broken Structure
```
Solutions:
1. Ask Claude to audit
2. Rebuild MANIFEST.json
3. Update all indexes
4. Fix file locations
```

---

## 📈 Growth Management

### When KB Gets Large

**Strategies:**
1. **Create more subtopics** - Break large domains into smaller pieces
2. **Use more specific paths** - Deeper directory hierarchies
3. **Archive aggressively** - Move old content regularly
4. **Improve search** - Better tagging and cross-references
5. **Create summaries** - High-level overview documents

### Adding New Domains

```
Ask Claude:
"Create new domain called [name]"
"Set up [domain] with standard structure"
"Add [domain] to MANIFEST and INDEX"
```

**Manual Checklist:**
- [ ] Create domains/[name]/ directory
- [ ] Create domain INDEX.md
- [ ] Add subtopics as needed
- [ ] Update MANIFEST.json
- [ ] Update main INDEX.md
- [ ] Consider new templates

---

## 🎨 Continuous Improvement

### Regularly Ask:
- "What's working well in KB structure?"
- "What's hard to find or confusing?"
- "What new templates would be useful?"
- "How can navigation be improved?"

### Track Metrics:
- Documents per domain
- Growth rate
- Most accessed content
- Common search queries
- Time to find information

### Evolve System:
- Adjust structure based on usage
- Create new templates as needed
- Improve conventions
- Enhance Claude instructions

---

## 🤖 Let Claude Help

### Routine Tasks Claude Can Do:
✅ Update indexes
✅ Check links
✅ Find duplicates
✅ Generate reports
✅ Move files
✅ Update MANIFEST
✅ Archive content
✅ Check conventions

### Strategic Tasks You Should Do:
👤 Decide what to archive
👤 Create new domains
👤 Set priorities
👤 Review quality
👤 Improve structure
👤 Update maintenance schedule

---

## 📝 Maintenance Log

### YYYY-MM-DD
- [ ] Task completed
- [ ] Issue found and fixed
- [ ] Improvement made

*(Add entries as maintenance is performed)*

---

## 🎯 Success Metrics

**Healthy KB Has:**
- ✅ All indexes current (< 1 week old)
- ✅ No broken links
- ✅ < 5% duplicate content
- ✅ 90%+ docs updated in last 6 months
- ✅ Easy to find information (< 30 seconds)
- ✅ Clear organization
- ✅ Consistent formatting

**If metrics decline:**
1. Run health checks
2. Address issues found
3. Consider structural changes
4. Update processes

---

## 🚀 Quick Maintenance Commands

```
# Weekly
"Check KB health"

# Monthly
"Generate KB report"
"Archive old content"

# Quarterly
"Full KB audit"
"Suggest improvements"

# As Needed
"Fix broken links"
"Update all indexes"
"Reorganize [domain]"
"Clean up duplicates"
```

---

**Next Scheduled Maintenance:** [Set date]
**Last Full Audit:** 2025-10-18

---

[← Back to META](how-to-use.md) | [← Back to INDEX](../INDEX.md)
