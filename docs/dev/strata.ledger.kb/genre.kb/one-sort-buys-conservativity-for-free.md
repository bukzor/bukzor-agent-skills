---
label: FREE_CONSERVE
standing: agent
why:
  - conservativity-is-the-semantic-half.md
  - confinement-is-the-syntactic-half.md
  - ../standing.kb/evidence-induces-a-monotone-operator.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_genre.py
---

# One Sort Buys Conservativity for Free

Keep one sort of node, and the evidence operator's rule format is
fixed once, below every genre. A genre extension can then only add
vocabulary and evidence, and each direction of conservativity is held
by one property: monotone growth keeps old standing from falling, and
confinement -- extension evidence concludes only on the genre's own
entries -- keeps it from rising. Monotonicity alone is not enough:
the unconfined counterexample in the verify suite breaks conservation
with a single appended row. Together they give conservativity by
construction, no proof per genre.

The tiers (higher-sorts-are-definitional.md): the base keeps one
primitive sort; defined sorts above it ride free, covered by the
same one-two punch; only a primitive new sort -- no down-translation,
rules reaching old entries -- degrades conservativity from a free
theorem into a per-genre proof obligation.

This is the mathematical content of the single-sorted-base ruling:
not parsimony for its own sake, but where the proof burden lands.
