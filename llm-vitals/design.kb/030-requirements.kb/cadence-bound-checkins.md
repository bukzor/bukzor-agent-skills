---
why:
  - reduce-dropped-tasks
  - wellness-as-upstream
  - grow-incrementally
---

# Cadence-Bound Check-Ins

Each vital must have a declared maximum interval between check-ins.
Breach of the interval is itself a tier-1 alert, independent of any
metric content.

This is the **observability floor**: without check-ins, no metrics can
be evaluated. Observability comes before SLOs (see `tier-1-before-tier-2`).

For journal-kind vitals, a check-in is a dated journal entry. For
task-kind vitals, a check-in is a mention of the vital in the
day-log. Both share the same cadence semantics — only the reporting
mechanism differs.
