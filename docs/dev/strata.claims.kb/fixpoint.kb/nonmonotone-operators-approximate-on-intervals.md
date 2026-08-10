---
label: APPROX
standing: bare
authority: "approximation fixpoint theory (Denecker, Marek, Truszczynski); Strass 2013 for the argumentation instance"
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py -k grounded
---

# Nonmonotone Operators Approximate on Intervals

A non-monotone operator on a complete lattice induces a monotone
*approximator* on the interval lattice (pairs (lower, upper) under the
precision order). The approximator always has a least-precise fixpoint
(Kripke-Kleene) and a canonical well-founded fixpoint; its exact
fixpoints (stable fixpoints) refine these.

Consequence: losing monotonicity does not lose canonical semantics --
it moves them to the interval lattice, where "undecided" becomes a
representable value between the bounds.
