---
label: WEIGHT
standing: bare
why:
  - reachability-is-a-least-fixpoint.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_reference.py -k "semiring or provenance"
---

# Weights Generalize Provenance

Value the quiver's edges in a semiring and reachability becomes a
weighted computation: booleans give bare reachability, counts give
support multiplicity, sets of paths give provenance. One computation,
several currencies -- choose the semiring by what question the reader
will ask, not by adding a new traversal per question.
