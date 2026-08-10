# engine_tower

Mechanized witnesses for the engine-tower claim ledger
(`../../strata.claims.md`). One module per code-bearing theory --
`tower` lives as the test suite's poset check; `purpose`, `fleet`,
and `question` stay out of the code by design (regime requirements
and proper nouns have no computational content). A module imports
only from its declared priors,
and `tests/test_tower.py` enforces it -- the tower's own discipline
applied to the tower's code.

Each test asserts one ledger claim on the smallest instance that
exhibits the phenomenon; the claim's `verify:` field names the test.

Run, from the repo root:

    uv --directory docs/dev/design-incubators/engine_tower run pytest
