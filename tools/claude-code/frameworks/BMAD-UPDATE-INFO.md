# BMAD-METHOD Update Information

## Last Documentation Update
- **Date**: 2025-08-17
- **Repository**: https://github.com/bmad-code-org/BMAD-METHOD
- **Commit ID**: `f3cc410fb052eb0cb1162ffdb721c0c50e8b4867`
- **Commit Message**: "patch: move script to tools folder"
- **Version**: 4.39.1
- **NPM Package**: [bmad-method](https://www.npmjs.com/package/bmad-method)

## Source Location
- **Local Path**: `/Users/kareddy/Desktop/explore/tmp/BMAD-METHOD/`
- **Clone Command**: `git clone git@github.com:bmad-code-org/BMAD-METHOD`

## Documentation Created
1. `/tools/claude-code/frameworks/bmad-method.md` - Main BMAD documentation
2. Updated `/tools/claude-code/README.md` - Added BMAD references
3. Updated `/tools/claude-code/workflow-examples.md` - Added BMAD workflow section
4. Updated `/tools/claude-code/claude-code-guide.md` - Added BMAD framework section

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