---
label: KNASTER
standing: bare
authority: "Knaster-Tarski fixpoint theorem"
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_fixpoint.py::test_iteration_from_bottom_computes_the_least_fixpoint
---

# Monotone Operators Have Least Fixpoints

On a complete lattice, a monotone operator has a least fixpoint: the
meet of its pre-fixed points, reached by iterating from bottom
(transfinitely in general; in finitely many steps on a finite
lattice). It likewise has a greatest fixpoint, dually.

This is the license behind every "X is *defined* as the least
fixpoint" claim downstream: the definition is total, canonical, and
computable by iteration.
