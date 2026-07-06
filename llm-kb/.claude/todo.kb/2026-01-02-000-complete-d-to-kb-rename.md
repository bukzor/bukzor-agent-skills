---
managed-by: Skill(llm-subtask)
required-reading:
  - ~/.claude/skills/llm.kb/docs/adr/2025-12-03-000-pivot-from-d-to-kb-naming-convention.md
  - ~/.claude/skills/llm.kb/SKILL.md
suggested-reading:
  - ~/.claude/skills/llm.kb/references/pattern-guide.md
related-effort: ~/repo/github.com/bukzor/prototype.chatfs/.claude/todo.kb/2026-01-02-000-harmonize-with-llm-skills.md
cost-benefit-sweh:
  timebox:
    "@value": 1.0
    rationale: |
      Mostly docs updates + mark ADR Accepted. Mechanical. Beyond 1h,
      scope crept beyond the original rename target.
  benefit-2w:
    "@value": 1.5
    rationale: |
      Clears stale ADR + unblocks part of llm-kb/.claude/todo.md.
      Closing a months-old rename frees mental bandwidth and removes
      contradictory examples in the complete-example/.
---

# Complete .d → .kb Rename in llm.kb

**Priority:** High
**Complexity:** Low
**Context:** Part of prototype.chatfs harmonization effort

## Problem Statement

The `.d → .kb` naming convention pivot (ADR 2025-12-03-000) is partially implemented:
- Done: `todo.kb/`, `ideas.kb/`, `references.kb/`
- Not done: `complete-example/` still uses `.d/` (guests.d/, food.d/, etc.)
- Not done: docs/references still reference `.d/`
- ADR status still "Proposed" (should be "Accepted")

## Current Situation

```
complete-example/
├── guests.d/      ← needs rename to guests.kb/
├── food.d/        ← needs rename to food.kb/
│   └── cake.d/    ← needs rename to cake.kb/
├── games.d/       ← needs rename to games.kb/
├── decorations.d/ ← needs rename to decorations.kb/
└── timeline.d/    ← needs rename to timeline.kb/
```

Docs referencing `.d/`:
- references/pattern-guide.md
- references/splitting-large-docs.md
- references/complete-example.md
- docs/documentation-conventions.md

## Implementation Steps

- [x] Rename complete-example directories: `*.d/ → *.kb/` (commit 799eb02, 2026-05-15)
- [x] Update complete-example/*.md files (references to .d/)
- [x] Update complete-example/*.jsonschema.yaml (descriptions)
- [x] Update complete-example/CLAUDE.md
- [x] Update references/complete-example.md
- [x] Rename docs/dev/devlog/2025-12-10-...-instruction-optimization.{d → kb}/ (additional scope)
- [x] Update references/pattern-guide.md (8 mentions; line 5 "Unix `.d/`" historical analogy stays)
- [x] Update references/splitting-large-docs.md (5 mentions; title + body)
- [x] Update docs/documentation-conventions.md (1 mention, line 10 in code block)
- [x] Mark ADR 2025-12-03-000 as Accepted (status still "Proposed")
- [x] Verify: `grep -r '\.d/' .` shows only acceptable uses (CLAUDE.d/ pattern is separate)
- [ ] Add auto-migrate step to scripts that read/write `.kb/` directories (like llm-collab-devlog does for docs/devlog → docs/dev/devlog) -- deferred: no concrete target script exists in llm-kb itself (only bin/llm.kb-validate, a symlinked validator with no stale-path migration to do); this needs a cross-skill scope decision, not a quick doc fix

## Success Criteria

- [x] No `.d/` directories in complete-example/ (verified `find . -type d -name "*.d"` empty)
- [x] All docs reference `.kb/` pattern (15 references remain in references/ + docs/documentation-conventions.md)
- [x] ADR status is "Accepted"
- [x] SKILL.md examples use `.kb/` (no `.d/` mentions in SKILL.md)
