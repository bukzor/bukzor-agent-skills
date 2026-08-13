---
status: complete
kind: recurring
scope: |
  All inventory-visible task files: */.claude/todo.md,
  */.claude/todo.kb/*.md, */.claude/todo.d/*.md,
  */.claude/sessions.kb/*.md, CLAUDE.*Task*.md. Flags bare `-` bullets
  for human review.
why: |
  `~/bin/claude-open-tasks-list` keys off `- [ ]` exactly. A bare `-`
  bullet is invisible to backlog enumeration — does not appear in
  task-list.md, does not get rated by wsjf-rank, gets silently lost.

  This bit twice in 2026-05: once in
  `private.bukzor-llc/projects/test-results/.claude/todo.md` (whole
  file used `-`, was invisible until a coverage audit caught it), and
  once in `prototyping.hearts-2025/.claude/todo.md` (the pnpm-run PATH
  fix surfaced only via a session note, not as a tracked item).

  No transformer is appropriate — deciding whether a `-` is a task or
  prose requires human judgment. This migration is `recurring`:
  validate.sh runs forever as a drift-detector, surfacing candidates
  for human triage.

  Convention stressed in `Skill(llm-subtask)/SKILL.md` ("`- [ ]` is
  load-bearing") and `~/.claude/sessions.kb/CLAUDE.md` ("`- [ ]` is
  load-bearing") on 2026-05-22.
---

# Recurring: flag bare `-` bullets in inventoried task files

## What gets flagged

Lines matching `^ *- [^[]` in any inventoried task file — bare dash
followed by something that isn't an opening bracket. The most common
forms:

- `- pick an oss project, nothing too complicated` (whole prose-style
  bullet list; user meant tasks but wrote prose)
- `- some sub-item under a bracketed parent` (the parent was a task;
  user added children but forgot to bracket them)
- `- not a task at all` (legitimate prose-bullet that happens to live
  in an inventoried file; human resolves by either bracketing or
  rephrasing as prose)

The validator does **not** attempt to discriminate. It reports
candidates; the user judges each.

## How to resolve a flag

For each flagged line:

- **It's a task** → add `[ ]`: `- [ ]` (or `[x]` if already done).
- **It's not a task** → rephrase as prose: drop the bullet entirely,
  or restructure as a sentence with embedded items, or move out of
  the task file.

## Algorithm (validate-only)

For each path in `claude-open-tasks-list`:

1. grep for `^ *- [^[]` lines.
2. Emit `<path>:<line-no>:<content>` for each match.

Convention bullets `- [ ]`, `- [x]`, `- [~]`, `- [-]` are excluded by
the `[^[]` requirement after the dash-space.

## Why no migrate.sh

- A `-` could be a task (needs bracketing) or prose (needs
  rephrasing).
- The judgment depends on surrounding sentence structure, the file's
  section context, and the writer's intent — none of which is
  reliably mechanizable.
- Auto-bracketing all bare bullets would silently elevate prose into
  tracked work; the user would discover the noise weeks later when
  the WSJF queue inflates.

## Status: recurring

Unlike one-shot migrations, this one never reaches `applied`. The
validator is the enforcement: any session that surfaces a flagged
line resolves it, and the file enters compliance until the next bare
`-` slips through.

`Skill(llm-subtask)` and `sessions.kb/CLAUDE.md` carry the upstream
rule ("any task-shaped line uses `- [ ]`"); this validator catches
the drift.

## Idempotency

Read-only; deterministic; trivially idempotent.
