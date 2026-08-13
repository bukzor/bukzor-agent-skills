---
why:
  - session-lifecycle-anchoring
  - grow-incrementally
---

# Demand-Driven Review

Review fires when the operator needs a fresh picker output, not on a
clock. The picker reads current state on every invocation and
recomputes debts on-demand.

Analogous to compiler invocation: compilers run when output is
requested, not on a schedule. The picker is a function from
(current state) → (today's surface), invoked at session-start.

This sidesteps the cadence-installation problem: there's no separate
ritual to remember. The review is a side effect of the operation
already happening (session-start). Habit-anchoring (see
`anchoring.md`) makes this concrete.

Implication: the picker must be fast (~sub-second) to be invoked
freely. State storage formats (JSONL day-log, kb-style journals)
support fast incremental reads.
