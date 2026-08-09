# engine_tower

Mechanized witnesses for the engine-tower claim ledger
(`../../strata.ledger.md`). One module per theory; a module imports
only from its declared priors, and `tests/test_tower.py` enforces it
-- the tower's own discipline applied to the tower's code.

Each test asserts one ledger claim on the smallest instance that
exhibits the phenomenon; the claim's `verify:` field names the test.

Run, from the repo root:

    uv --directory docs/dev/design-incubators/engine_tower run pytest
