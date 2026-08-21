---
label: COMPUTED
standing: agent
why:
  - evidence-induces-a-monotone-operator.md
  - the-status-order-is-not-a-complete-lattice.md
  - ../fixpoint.kb/monotone-operators-have-least-fixpoints.md
  - ../view.kb/a-cache-is-lawful-iff-the-triangle-commutes.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py::test_retraction_gap_keeps_the_ring
---

# Standing Is Computed, Not Stored

An entry's standing is *defined* as its value in the least fixpoint
of the evidence operator -- grounded support only, nothing standing on
itself. Not in the bare status order, which has no join over distinct
certificates and so admits no least fixpoint at all
(the-status-order-is-not-a-complete-lattice.md): the values live in
its antichain completion, where an entry certified twice holds both
certificates and the definition is total. Any written standing is
therefore a cache of a view, owing
the commuting triangle like every other cache: stamped, regenerable,
never read stale as truth. The staleness check is a diff of the
evidence set since the stamp -- additions and retractions both; a
query for new evidence alone misses the dangerous direction.
