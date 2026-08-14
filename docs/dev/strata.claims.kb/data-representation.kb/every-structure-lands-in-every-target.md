---
label: COVERAGE
standing: agent
why:
  - a-target-is-a-realization-with-a-price.md
  - ../data-structures.kb/the-roster-is-read-off-the-carriers.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_data_representation.py::test_every_structure_lands_in_every_target
---

# Every Structure Lands in Every Target

The obligation is the product: each structure in the roster times
each target in the table, a representation in every cell. An empty
cell is filed debt -- named, priced, and scheduled -- never an
oversight discovered at write time. The check is mechanical once both
rosters are data rather than prose; the `verify:` above names the
owed test, acceptance debt until built.
