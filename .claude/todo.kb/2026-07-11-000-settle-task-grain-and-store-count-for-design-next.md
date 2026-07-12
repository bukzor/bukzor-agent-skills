---
managed-by: Skill(llm-subtask)
---

# Settle task grain and store count (design-next)

**Priority:** Medium
**Complexity:** High
**Context:** `design-next.kb/040-design.kb/genre-task.md`; tracked as
"T3" in the 2026-07-10/11 design sessions

## Problem Statement

The task domain's design was deferred mid-discussion: v1 collapsed
three independent axes into store choice, and neither v2.0
(`genre-task.md`) nor the v2.1 session resolved the right factoring.
Needs a dedicated session; too large to settle as a side thread.

## Current Situation

Three axes identified, currently entangled:

- **Atom grain**: checklist line (cheap write, machine-enumerable via
  `- [ ]`, shares a file — write contention) vs file (whole-file
  ownership, but v1 evidence says agents default heavyweight).
- **Horizon**: v1 encodes it in store choice (todo.md / todo.kb /
  sessions.kb → disposition procedure overhead); v2.1 proposed
  frontmatter metadata; v2.0 proposes tier discipline with
  engine-defaults-light.
- **Scope**: sessions.kb as global cross-repo store vs per-repo stores
  plus cross-scope enumeration (the latter depends on engine query,
  deferred behind `070-future-work.kb/structured-query.md`'s trigger).

Seed insight from 2026-07-11: todo.md is not a rival store — it is
the todo application's *specialized synthesis* of todo.kb/ (hot
working set; capture-a-tangent-in-one-line-without-taking-it). The
spec now allows applications to specialize the synthesis relation;
the task domain should be designed as its flagship user.

**Resolved 2026-07-11:** rating system is a real consumer, not
landfill. Operator confirmed `task-list.wsjf.toon`
(`~/repo/github.com/bukzor/2026-05-19--task-archeology/`) informed
the decision to focus the schema-reuse `$ref` work under `llm-kb`
(matches commit `042f698`, "refresh: backlog snapshot after
schema-reuse-with-ref closeout"). Not landfill — but operator flagged
the *framing*, not just the fact, as wrong: treat `wsjf-rank`/
task-archeology as a **case study**, not the primary use case that
dictates task-genre schema. The durable commitment is narrower and
more general — *extensions like it* must be possible and supportable,
not that its specific vocabulary (`sweh`, `timebox`, `benefit_2w`,
`cod_2w`, `execute_score`) becomes canonical.

That the extension already lives as a **separate repo** consuming
other repos' `todo.md`/`todo.kb/` via sidecar `cost-benefit-sweh`
frontmatter is itself the working existence proof of "supportable
without core absorption" — evidence for keeping the task genre's own
schema minimal, not for growing it toward wsjf's shape.

Open question this reframes rather than closes:
`070-future-work.kb/structured-query.md`'s trigger ("third occurrence
of ls/grep failing") — does "supportable" mean the core engine
eventually grows `kb query`, or does it mean the core stays minimal
(stable frontmatter, stable cross-repo file conventions, stable
naming) and ranking-shaped needs stay externally-built forever, as
task-archeology already demonstrates works? Don't resolve this
inline; it's part of the T3 session.

## Proposed Solution

Dedicated design session against design-next.kb: settle the three
axes, then record outcomes as design entries (and gut/replace
`genre-task.md` accordingly).

## Implementation Steps

- [ ] Operator answers the rating-system read-side question
- [ ] Settle atom grain (line vs file, and when each)
- [ ] Settle horizon representation (metadata vs tiers vs stores)
- [ ] Settle scope/store layout (global vs per-repo + enumeration)
- [ ] Record decisions in design-next.kb; update `genre-task.md`

## Open Questions

- Does `- [ ]` machine-enumerability survive if grain moves toward
  whole files? (existence-is-signal vs line contract)
- Is sessions.kb a task-domain instance or its own thing once todo.md
  is a synthesis?

## Success Criteria

- [ ] All three axes have decided design-next entries (why-linked)
- [ ] genre-task.md no longer contradicts the decisions

## Notes

Solutions floated in-session were proof-of-existence, not normative
(operator's explicit caveat) — re-derive at discussion time.
