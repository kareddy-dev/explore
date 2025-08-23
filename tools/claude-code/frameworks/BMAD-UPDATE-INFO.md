# BMAD-METHOD Update Information

## Last Documentation Update
- **Date**: 2025-08-23
- **Repository**: https://github.com/bmad-code-org/BMAD-METHOD
- **Commit ID**: `ab70bacef959a69c7a0c28e33ba43b1e96fb5e48`
- **Commit Message**: "fix: remove incorrect else branch causing flatten command regression (#452)"
- **Version**: 4.39.1 (no version change, bug fixes only)
- **NPM Package**: [bmad-method](https://www.npmjs.com/package/bmad-method)
- **Video Reference**: "The Official BMad-Method Masterclass (The Complete IDE Workflow)" - YouTube

## Source Location
- **Local Path**: `/Users/kareddy/Desktop/explore/tmp/BMAD-METHOD/`
- **Clone Command**: `git clone git@github.com:bmad-code-org/BMAD-METHOD`

## Documentation Created/Enhanced
1. `/tools/claude-code/frameworks/bmad-method.md` - Main BMAD documentation (ENHANCED 2025-08-17)
2. Updated `/tools/claude-code/README.md` - Added BMAD references
3. Updated `/tools/claude-code/workflow-examples.md` - Added BMAD workflow section
4. Updated `/tools/claude-code/claude-code-guide.md` - Added BMAD framework section

### Recent Changes (2025-08-23)
- Fixed flatten command regression issue
- Updated documentation to use BMAD-METHOD™ trademark
- Minor bug fixes and documentation improvements

### Major Enhancements Added (2025-08-17)
Based on Brian's masterclass video, added comprehensive documentation for:
- **20+ Brainstorming Techniques** with detailed descriptions
- **20+ Advanced Elicitation Methods** for pushing LLM quality
- **Agent Personas**: Mary (Analyst), James (Developer), Quinn (QA)
- **Course Correction Feature** for mid-project pivots
- **PO Checklist** validation command
- **Document Sharding** with md-tree details
- **Developer Configuration** (dev_load_always_files)
- **Unsafe Mode** option for faster development
- **Complete Workflow Example** from the video tutorial
- **Core Philosophy** of collaborative elevation
- **Workflow Best Practices** from Brian's experience
- **Model Selection Strategy** guidance
- **Project Organization** tips
- **Common Pitfalls** to avoid

## Key Files Referenced
- README.md (main documentation)
- docs/user-guide.md (workflow diagrams)
- docs/GUIDING-PRINCIPLES.md (framework principles)
- bmad-core/workflows/greenfield-fullstack.yaml (workflow example)
- bmad-core/templates/story-tmpl.yaml (story structure)
- bmad-core/tasks/create-next-story.md (story creation process)
- expansion-packs/bmad-creative-writing/README.md (expansion pack example)

## Next Update Instructions
To update the BMAD documentation in the future:

```bash
# 1. Pull latest changes
cd /Users/kareddy/Desktop/explore/tmp/BMAD-METHOD
git pull origin main

# 2. Check for changes since last update
git log --oneline f3cc410fb052eb0cb1162ffdb721c0c50e8b4867..HEAD

# 3. Review key files for updates
git diff f3cc410fb052eb0cb1162ffdb721c0c50e8b4867..HEAD README.md docs/user-guide.md

# 4. Update documentation accordingly
# Focus on:
# - New agents or workflows
# - Installation process changes
# - New expansion packs
# - Version-specific features
```

## Notes
- BMAD installs per-project, not globally
- Documentation emphasizes the two-phase approach (Planning → Development)
- Key innovation is document-based agent collaboration through story files
- Framework supports multiple IDEs (Claude Code, Cursor, Windsurf, etc.)