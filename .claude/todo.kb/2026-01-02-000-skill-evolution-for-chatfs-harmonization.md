---
managed-by: Skill(llm-subtask)
cost-benefit-sweh:
  timebox:
    '@value': 0.1
    confidence: confident
    rationale: |
      Coordination file. Inline work is two grep-checks + one upstream notification once both children land. Same shape as a pointer file with effectively no substance of its own.
  benefit-2w:
    '@value': 0
    confidence: confident
    rationale: |
      Direct benefit is zero -- children (llm-collab/2025-12-11-000 and llm-kb/2026-01-02-000) carry all substantive payoff. This file is pure coordination; benefit cannot be realized in 2w independently of the children landing.
  cost-of-delay-2w:
    '@value': 0
    confidence: confident
    rationale: |
      No decay; children carry their own urgency. Notification value is bounded by children landing, which is independent of this file.
---
<anthropic-skill-ownership llm-subtask />

---
requested-by: ~/repo/github.com/bukzor/prototype.chatfs/.claude/todo.kb/2026-01-02-000-harmonize-with-llm-skills.md
---

# Skill Evolution for chatfs Harmonization

**Priority:** High
**Complexity:** Low
**Context:** Unblocks prototype.chatfs harmonization with llm-* skill conventions

## Problem Statement

prototype.chatfs wants to adopt llm-* skill conventions, but the skills themselves have incomplete evolution:
- llm.kb: `.d → .kb` rename partial (complete-example still uses `.d/`)
- llm-collab: skeleton needs `milestones.kb/` and `design.kb/` patterns

## Subtasks

**Recommended order:** llm-collab first (makes llm.kb rename patterns clearer)

1. [ ] [llm-collab: Update skeleton](../../llm-collab/.claude/todo.kb/2025-12-11-000-Update-skeleton-to-match-docs-dev--pattern-from-git-partial.md)
2. [ ] [llm.kb: Complete .d → .kb rename](../../llm-kb/.claude/todo.kb/2026-01-02-000-complete-d-to-kb-rename.md)

## Verification

```bash
# llm.kb: No .d/ directories in complete-example
ls -d llm-kb/complete-example/*.d/ 2>/dev/null && echo "INCOMPLETE" || echo "DONE"

# llm.kb: ADR status updated to Accepted
grep -A1 "^## Status" llm-kb/docs/adr/2025-12-03-000-*.md
```

## On Completion

Notify upstream: prototype.chatfs can proceed with Phase 2 of harmonization.
