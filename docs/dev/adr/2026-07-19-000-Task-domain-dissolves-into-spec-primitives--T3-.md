# Task domain dissolves into spec primitives (T3)

**Date:** 2026-07-19
**Status:** Accepted

## Context

v1's task system spread one domain across four artifact kinds —
llm-subtask's `todo.md`/`todo.kb/`/`ideas.kb/`, the global
`sessions.kb/`, and personal `CLAUDE.<slug>.Task.md` taskfiles — and
encoded three independent axes (atom grain, horizon, scope) in a
single degree of freedom: which store you wrote to. Symptoms: agents
defaulting heavyweight, "invisible work" in bare bullets, a
disposition procedure per store, and a question (the T3 brief,
`.claude/todo.kb/2026-07-11-000-settle-task-grain-and-store-count-for-design-next.md`)
too large to settle as a side thread.

The session ran against the v2 design tower with the kb-spec
primitives already landed: linked node, synthesis file (relation
specialized per domain), dated record. That mattered — most of the
session's clarity was *withdrawn* from those primitives, not
invented.

## Decision

The forward-facing recording is
`design-next.kb/040-design.kb/class-task.md` plus two
`070-future-work.kb/` entries; this ADR keeps the derivation and the
rejected alternatives. The axes dissolved rather than resolved:

1. **Grain** is per-task elaboration, not a store choice: line →
   file → task kb, self-similar at every level
   (`todo.md` : `todo.kb/` :: `$slug.md` : `$slug.kb/`), growing a
   task tree on demand.
2. **Horizon** is the working set's total order, nothing else.
   Conditional deferral (a date, "after X ships") is trigger-shaped —
   punted to T4 as a task↔trigger boundary question.
3. **"Likelihood"** is not an axis but a binary contract: obligation
   (sweeps must nag; explicit disposition) vs option (sweeps must
   never nag; forgetting is valid). Each contract is a full synthesis
   pair — `todo.md`/`todo.kb/` and `ideas.md`/`ideas.kb/` — so
   contract-awareness in tooling is filename dispatch. v1's
   `## Later` retires; its one real job was holding the option pool.
4. **Scope** is filesystem position: per-project instances are
   canonical ("project" = ownership shape, not git boundary — one
   repository may hold several projects); `sessions.kb/` is the task
   class instanced at operator scope, machine-sharded because session
   state (worktrees, branches, uncommitted files) is machine-bound;
   taskfiles retire as a standalone concept.

"Supportable" (the rating-system question) resolved as
minimal-core-forever: the core commits to stable conventions
(frontmatter, naming, layout); ranking and query needs stay
externally built; `kb query` stays behind `structured-query.md`'s
three-occurrence trigger.

## Journey

The reusable maneuver, applied repeatedly, was
`evaluate-uses-independently` (llm-design-kb/principles.kb): each
apparent dilemma was several questions wearing one costume.

- **Store choice wore three costumes.** Capture weight, surfacing
  time, and ownership were all encoded in "which store," so every
  store decision fought all three axes at once. The founding reframe
  (seeded 2026-07-11): `todo.md` was never a store — it is the
  collection's synthesis.
- **`## Later` wore two.** Operator: Later existed for "good ideas
  that might be done never, and that's okay" — its contents were
  never deferred obligations (those sit low in the order; dated
  deferrals are triggers). The section break was a contract boundary
  in disguise — and the final step dissolved the boundary itself:
  the option pool got its own synthesis pair (`ideas.md`), restoring
  the spec's one-to-one `$name.md` : `$name.kb/` relation that a
  two-collection `todo.md` would have broken.
- **Operator corrections that shaped the outcome:**
  - wsjf's metrics *originated in the ideas.kb schema* (to
    refresh/reevaluate old ideas). So "ordering over options has no
    consumer" was wrong as stated: options have no *standing* order,
    but ratings-driven batch reevaluation (commit/retire/keep) is a
    proven read-back. task-archeology stays a case study — extensions
    must be supportable; their vocabulary is not canonized.
  - "repo" → "project": ownership shape, not git boundary.
  - Session entries already carry dated identity at the addenda
    level; extending it to the entries themselves (scheduled sweep)
    finishes the normalization. The old "do not number — sessions are
    not ordered" rule conflated chronological identity with priority
    ordering.
- **Pointer lines earned a rationale:** they hold an entry's position
  in the total order — which is why `todo.md` carries one per open
  entry, `ideas.md` carries none (`ls ideas.kb/` is the whole option
  index), and neither synthesis can decay into "merely a listing."

## Alternatives Considered

- **Horizon frontmatter or named buckets (`## Someday`, `## Blocked`)**
  — rejected: frontmatter cannot reach line grain; every bucket
  shadows the total order that makes the working set contentful;
  "blocked" is per-task state.
- **Scalar likelihood (000-999)** — rejected: sweeps need a binary
  (nag or don't), and the contract split is that binary; finer
  judgment happens at reevaluation time via ratings; a standing
  probability field is false precision with no reader.
- **File-grain atoms to solve working-set write contention** —
  rejected: the contended file is only the synthesis, and a total
  order is inherently unshardable; keep the synthesis thin instead.
- **sessions.kb as its own class; a global working set** — rejected:
  no distinct behavior remains once entries are ordinary task nodes;
  no consumer for a global ordering (`ls` + sweep tooling suffice).
- **Canonizing wsjf fields in the task schema** — rejected per the
  case-study framing; the deferred shape lives in
  `070-future-work.kb/task-priority-frontmatter.md`.
- **`## Later` as a permanent contract boundary** — adopted
  mid-session, superseded the same day by the `ideas.md` synthesis
  pair: structural separation beats positional.

## Consequences

**Positive:**

- `class-task.md` states the whole domain in spec primitives; four
  v1 stores reduce to instances of one shape.
- Contract-aware sweeps become filename dispatch (`todo` pairs nag,
  `ideas` pairs never do) — no section parsing.
- Deferred work has named triggers: `task-priority-frontmatter`,
  `task-synthesis-drift-check`.

**Negative:**

- Migration debt, all scheduled: sessions.kb dated-prefix +
  CLAUDE.md sweep and taskfile retirement (in the sessions repo's
  `reconcile-sessions-kb-schema-drift` session; last taskfile
  migrates on touch); v1 `## Later` sections migrate to `ideas.md`
  at v2 build.
- v1 docs teach the old shape until the rebuild (one clarifying
  sentence added to llm-subtask's SKILL.md).

**Neutral:**

- T4 inherits: the task↔trigger boundary; the skill-bundled command
  resolution question (residue of the retired
  `integrate-sessions-kb-into-llm-subtask` taskfile).

## Related

- Related to: `design-next.kb/040-design.kb/class-task.md` (the
  forward-facing recording);
  `.claude/todo.kb/2026-07-11-000-settle-task-grain-and-store-count-for-design-next.md`
  (the brief, now closed);
  `llm-design-kb/principles.kb/evaluate-uses-independently.md` (the
  maneuver, strengthened with this session's instances)
