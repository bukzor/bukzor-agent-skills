---
label: TAINT
standing: bare
why:
  - reachability-is-a-least-fixpoint.md
  - ../fixpoint.kb/downward-revision-overshoots.md
---

# Taint Inherits the Overshoot

Adding edges grows reachability monotonically, so taint marks can be
propagated incrementally. Removing an edge or a support cannot be
warm-started: naive downward revision leaves self-supporting cycles
standing. A correct remover either recomputes the affected cone from
scratch or maintains support counts precise enough to tell grounded
support from a loop.

This is a theorem about the shape of the computation, not an
implementation preference -- any system that deletes references owes
one of the two answers.
