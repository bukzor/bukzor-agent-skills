---
label: TAINT
standing: bare
authority: "DRed -- delete and rederive (Gupta, Mumick & Subrahmanian 1993)"
why:
  - reachability-is-a-least-fixpoint.md
  - ../fixpoint.kb/downward-revision-overshoots.md
---

# Taint Inherits the Overshoot

Adding edges grows reachability monotonically, so taint marks can be
propagated incrementally. Removing an edge or a support cannot be
warm-started: naive downward revision leaves self-supporting cycles
standing. A correct remover either recomputes the affected cone from
scratch or maintains bookkeeping that tells grounded support from a
loop -- derivation height, or another rank that a cycle cannot
forge. Support counts alone will not do it: in a cycle, the counts
are supplied by the cycle.

This is a theorem about the shape of the computation, not an
implementation preference -- any system that deletes references owes
one of the two answers.
