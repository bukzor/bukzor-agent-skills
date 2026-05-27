---
managed-by: Skill(llm-subtask)
---

# Fold sessions.kb governance into Skill(llm-subtask)

`~/.claude/sessions.kb/` and `*/.claude/sessions.kb/` participate in the
same inventory pipeline as `todo.md` / `todo.kb/` / `todo.d/`. They share
the same `- [ ]` open-work convention. They surface together in
`claude-open-tasks-list` and rank together in `wsjf-rank`.

But sessions.kb governance currently lives in `~/.claude/sessions.kb/CLAUDE.md`
as a freestanding collection, not attached to any skill. That works, but
it means the same load-bearing rules (e.g., "use `- [ ]` for open work")
have to be stated twice — once in `Skill(llm-subtask)/SKILL.md` and
once in `sessions.kb/CLAUDE.md` — with the risk of drift.

## What folding could look like

- `Skill(llm-subtask)` claims `sessions.kb/` as a tier-3+ container
  ("cross-context strategic" or "outside-current-project strategic").
- `~/.claude/sessions.kb/CLAUDE.md` becomes a thin pointer to the skill,
  keeping only the "what belongs here / how files are named" specifics.
- Inventory-signal rules, lifecycle phrasing, etc. live once in
  `SKILL.md` and propagate by reference.

## Arguments against

- sessions.kb is *cross-project* — its scope sits above any one CWD
  in a way `todo.kb/` does not. The skill currently models work
  inside a project; sessions are about work across projects.
- The current four-tier system (conversational / ephemeral / tactical /
  strategic) doesn't have a natural slot for "session-as-coarsest-unit"
  without expanding to five tiers.

## Trigger

This idea surfaced 2026-05-22 during the "rate-unrated after inventory
coverage fix" session, when the inventory script's coverage gap exposed
that `- [ ]` rules were under-stressed in *both* SKILL.md and
sessions.kb/CLAUDE.md. The double-stress required to fix that gap is
itself the smell that wants the merger.

Promote to `todo.kb/` when the four-tier system gets its next revision.
