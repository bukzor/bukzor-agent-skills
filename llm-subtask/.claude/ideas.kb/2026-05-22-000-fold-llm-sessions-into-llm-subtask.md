---
managed-by: Skill(llm-subtask)
---

# Fold Skill(llm-sessions) into Skill(llm-subtask)

`sessions.kb/` entries participate in the same inventory pipeline as
`todo.md` / `todo.kb/` / `todo.d/`: same `- [ ]` open-work convention,
surfaced together by `claude-open-tasks-list`, ranked together by
`wsjf-rank`.

Since 2026-05-22 the governance moved: as of 2026-11-21,
Skill(llm-sessions) owns the entry conventions (entry shape, start /
mid / end of session), and `~/.claude/sessions.kb/CLAUDE.md` is a thin
repo-specific pointer. So the original "thin pointer" half of this idea
is done. What remains is two skills over one domain.

## For

> [!DRAFT] agent-authored 2026-11-21, vetoable.

- PARSIMONY (bukzor-agent-skills authorship ledger: one skill beats two
  that overlap) and DOMAINS (skills are domains, occasions are triggers):
  sessions.kb is one more container of tracked work; "session" is an
  occasion, not a domain.
- The overlap is already load-bearing: llm-sessions restates the `- [ ]`
  rule and defers to llm-subtask for it; its schema `$ref`s
  `cost-benefit-sweh` across to llm-subtask; /session-end's Disposition
  ladder already routes ">1 hour or elsewhere" to `sessions.kb/`, i.e.
  sessions.kb is the ladder's top rung.
- Load cost stays neutral if the sessions content becomes a procedure
  file under llm-subtask that only loads for sessions work.

## Against

- sessions.kb is cross-project; llm-subtask models work inside one
  project (`$PWD/.claude/`). The four-tier system has no slot for
  "outside-current-project" without a fifth tier or a scope axis.
- Reference churn: `skill://llm-sessions` in /session-start,
  /session-end, the schema `$ref`, and ~16 per-entry addenda
  `CLAUDE.md` files.

## When

Promote to `todo.kb/` when the four-tier system gets its next revision.
Awaiting the owner's ruling on promotion (raised 2026-11-21).
