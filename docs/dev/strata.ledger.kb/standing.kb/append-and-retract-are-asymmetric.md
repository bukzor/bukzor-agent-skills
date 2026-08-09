---
label: ASYMMETRY
standing: agent
why:
  - standing-is-computed-not-stored.md
  - ../fixpoint.kb/warm-start-is-sound-upward.md
  - ../fixpoint.kb/downward-revision-overshoots.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py -k "warm_start or retraction"
---

# Append and Retract Are Asymmetric

New evidence grows the operator, so standing after an append is
computable by warm-start from the current fixpoint: appends are
cheap, and an append-only store is the architecture that keeps them
cheap. Retraction shrinks the operator, warm-start is unsound, and
the honest choices are recomputing the affected cone or maintaining
support counts. Mutual-warrant circles are the visible face of the
gap: exactly what naive downward revision wrongly preserves.

The asymmetry is fixpoint continuity, not a taste for immutability.
