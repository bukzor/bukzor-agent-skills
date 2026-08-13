---
label: DEFEAT
standing: user
why:
  - evidence-induces-a-monotone-operator.md
  - ../fixpoint.kb/nonmonotone-operators-approximate-on-intervals.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py -k "grounded or ruling"
---

# Defeat Is Evidence for an Approximator

Defeat evidence makes the operator non-monotone: more evidence can
lower a status. The canonical repair is not to forbid defeat but to
compute on the interval lattice, where the well-founded fixpoint
always exists and "contested" is a representable value between the
bounds. A *semantics* -- which fixpoint to read -- is then a
query-time choice, not a property of the store: the ledger keeps the
operator, and a ruling pins one coordinate of the answer rather than
rewriting the evidence.
