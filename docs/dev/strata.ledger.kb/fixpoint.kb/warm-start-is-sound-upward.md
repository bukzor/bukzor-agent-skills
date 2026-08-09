---
label: WARM_START
standing: bare
why:
  - monotone-operators-have-least-fixpoints.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py::test_warm_start_from_old_fixpoint_matches_cold
---

# Warm-Start Is Sound Upward

If an operator grows pointwise (Phi' >= Phi), the old least fixpoint
x = lfp(Phi) satisfies x = Phi(x) <= Phi'(x), so x is a pre-fixed
point of Phi'. Upward iteration of Phi' from x converges to the least
fixpoint of Phi' above x -- which is lfp(Phi') itself, since
lfp(Phi') >= lfp(Phi).

Consequence: when the operator only grows, the new answer is
computable incrementally, continuing from the old answer.
