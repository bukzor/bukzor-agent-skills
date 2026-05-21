---
cost-benefit-sweh:
  timebox:
    "@value": 0.5
    rationale: |
      Single doc addition: integration section in subtask SKILL.md
      with example pattern + checkbox vs non-checkbox explanation.
      Self-classified Complexity: Low.
    confidence: tentative
  benefit-2w:
    "@value": 0.3
    rationale: |
      Future agents stop misreading the relationship. Modest doc-
      clarity win.
    confidence: tentative
  cost-of-delay-2w:
    "@value": 0.1
    rationale: |
      Misunderstanding leaks across sessions where llm-subtask is
      loaded. Small per-session cost, flowing.
    confidence: tentative
---

# Clarify the relationship between todo.md and todo.kb in subtask skill

**Priority:** Medium
**Complexity:** Low
**Context:** llm-collab-docs demonstrates the pattern in `.claude/todo.md`

## Problem Statement

The subtask skill documentation doesn't clearly explain how todo.md and todo.kb/ work together. They're complementary but docs treat them separately.

## Current Situation

Subtask skill has:
- Tier 2 (tactical): `.claude/todo.md` with markdown checkboxes
- Tier 3 (strategic): `.claude/todo.kb/YYYY-MM-DD-NNN-title.md` planning files

But it doesn't show how they integrate in practice.

## Proposed Solution

Add section showing how strategic todos are referenced from todo.md using relative paths.

**Example pattern from llm-collab-docs `.claude/todo.md`:**
```markdown
- [ ] todo.kb/2025-11-26-000-destructure-must-read-beforedcreating-documentationmd-into-referencesd-llmd-structure.md
  - [ ] Finalize references.kb/ categorization structure
  - [ ] Split content into small focused files
```

Key points:
- todo.md contains tactical tasks (inline text) AND strategic references (paths to todo.kb/*.md)
- Checkbox sub-bullets are subtasks that contribute to parent
- Non-checkbox sub-bullets provide clarifying context

## Implementation Steps

1. [ ] Add "Integration: todo.md + todo.kb/" section to subtask/SKILL.md
2. [ ] Show example snippet from llm-collab-docs
3. [ ] Explain checkbox vs non-checkbox sub-bullets

## Success Criteria

- [ ] Relationship between todo.md and todo.kb/ is documented
- [ ] Example demonstrates the pattern
- [ ] Stays terse (subtask skill style)

## Notes

llm-collab-docs `.claude/todo.md` serves as reference implementation.
