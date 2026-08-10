---
label: COMPUTED
standing: agent
why:
  - evidence-induces-a-monotone-operator.md
  - ../fixpoint.kb/monotone-operators-have-least-fixpoints.md
  - ../view.kb/a-cache-is-lawful-iff-the-triangle-commutes.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py::test_retraction_gap_keeps_the_ring
---

# Standing Is Computed, Not Stored

An entry's standing is *defined* as its value in the least fixpoint
of the evidence operator -- grounded support only, nothing standing on
itself. Any written standing is therefore a cache of a view, owing
the commuting triangle like every other cache: stamped, regenerable,
never read stale as truth. The staleness check is a diff of the
evidence set since the stamp -- additions and retractions both; a
query for new evidence alone misses the dangerous direction.
