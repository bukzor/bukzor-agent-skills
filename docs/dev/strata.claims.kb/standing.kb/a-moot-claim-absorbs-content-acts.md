---
label: ABSORB
standing: bare
why:
  - a-defeated-presupposition-collapses-sense.md
  - force-is-computed-never-asserted.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py tests/test_derived_theorems.py -k "absorbs or never_also"
---

# A Moot Claim Absorbs Content Acts

Acts on a moot claim are dropped before any interval is read, so
adding one moves no claim's color -- a content act on a claim with
no content has nothing to spend its force on. "Moot *and*
content-defeated" is therefore impossible by derivation: nothing
asserts the exclusion and no schema has to encode it.

The declined alternative is a precedence rule -- compute both, and
prefer moot wherever a claim comes out both ways. It prints the same
answer and is not the same commitment: precedence lives in whoever
does the printing, so the next reader of the same record (a query, a
port, another view) is free to resolve the pair the other way, and
the record no longer says which is right. Absorption puts the
exclusion in the record instead.

Standing is `bare` on that derivation, not on the check: `verify:`
quantifies over generated records, which is bounded evidence
(`../../strata.claims.md`, Verify) and not the proof.
