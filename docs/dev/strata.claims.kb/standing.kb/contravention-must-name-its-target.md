---
label: EXPLICIT
standing: user
authority: "user ruling, 2026-08-17, this conversation: 'you must list all (extant) acts you intend to contravene'"
why:
  - force-is-computed-never-asserted.md
  - an-act-is-a-bare-claim-of-the-record.md
  - ../purpose.kb/the-corpus-outgrows-any-reader.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py -k "strikes or clash or litigation or annulment"
---

# Contravention Must Name Its Target

An act leaves the effective set only when an admitted act targets
it. Recency resolves nothing: a corpus that outgrows any reader
outgrows its own authors, so a later act cannot be presumed issued
in view of the earlier ones, and last-wins would launder undetected
self-contradiction into amendment.

Amendment and inconsistency are therefore facts of the record, not
modes of the law:

- an act that cites the acts it strikes is an amendment;
- clashing acts with no citation between them both stand, and the
  conflict is computed -- the same contested interval whether the
  clashing assessors are two or one;
- litigation is one move: a resolving act naming what it strikes.

Every subtraction from the effective set is an addition to the
record, addressed to its target -- an append-only record as a
theorem rather than a policy.
