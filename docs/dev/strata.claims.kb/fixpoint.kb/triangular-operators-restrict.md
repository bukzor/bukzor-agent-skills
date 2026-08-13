---
label: RESTRICT
standing: bare
authority: "Bekic's lemma -- simultaneous fixpoints decompose (Bekic 1984)"
why:
  - monotone-operators-have-least-fixpoints.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_fixpoint.py::test_a_triangular_operator_restricts_to_its_first_coordinate
---

# Triangular Operators Restrict

On a product of complete lattices, call a monotone operator
*triangular* when the first coordinate of its output depends only on
the first coordinate of its input: pi1 . Phi = phi1 . pi1 for some
monotone phi1. Then the least fixpoint restricts exactly:
pi1(lfp Phi) = lfp(phi1). By induction on the iteration from bottom,
every stage satisfies pi1(Phi^a(bot)) = phi1^a(bot) -- successor
stages by triangularity, limit stages because joins are computed
coordinatewise -- so the first coordinate of the answer is the
answer computed on the first lattice alone, the second coordinate
never consulted.

Consequence: the first coordinate can be solved by itself, exactly
rather than approximately, and enlarging the product cannot move it.
An approximator is itself a monotone operator on an interval
lattice, so the lemma survives the approximation construction
unchanged.
