# engine_tower

Mechanized witnesses for the engine-tower claim ledger
(`../../strata.claims.md`). One module per code-bearing theory --
`tower` lives as the test suite's poset check; `purpose`, `fleet`,
and `question` stay out of the code by design (regime requirements
and proper nouns have no computational content). A module imports
only from its declared priors, and `tests/test_tower.py` enforces it
-- the tower's own discipline applied to the tower's code.  That test
reads the poset out of the ledger's `why:` lines rather than keeping
a copy, so the ledger is the only place the poset lives.

Each test asserts one ledger claim on the smallest instance that
exhibits the phenomenon; the claim's `verify:` field names the test.
The exception is `tests/test_data_representation.py`, which runs the
act algebra over a real ledger (`llm-claims/design.claims.kb`) as
REIFY's degenerate case: fields desugared to acts, nothing striking,
stored standing reproduced by the computed one.

Run, from the repo root:

    uv --directory docs/dev/design-incubators/engine_tower run pytest
