# Devlog: 2026-08-13 -- `stale-when:` replaces `defeated-by:`

## Focus

A theory's defining claim carried `defeated-by:` -- "the finding that
would retire the theory whole". The strata replication session, which
runs the largest ledger anyone has written in this notation, proposed
narrowing it to the observable condition alone and renaming it
`stale-when:`. Taken, and landed across the skill, both in-repo
ledgers, and the tools.

## The decision

`last-updated:` already treats a defining claim's roll-up as a stamped
cache -- *a cache is lawful iff it says what revision it derives from*.
`stale-when:` is that stamp's missing half: the cheapest observation
witnessing the theory no longer projects from the world it was stamped
against. The condition fires, the stamp is void, re-derive before
citing.

The old semantics asked a header to predict an outcome, and outcomes
are decided at re-check time. Surveying strata's twelve lines, most
"defeaters" would resolve as *repairs* -- the tower's upward reach means
re-stratify, genre's conservativity failure means redraw a boundary,
and fixpoint's says so outright ("fixed by restating, not by
argument"). Defeat is the re-derivation that comes back empty: an act
when it happens, not a prediction written months earlier.

Every existing value survived the rename verbatim, which is the
evidence that the field was already being written as a condition and
described as a verdict.

**Alternatives considered:** keeping the epistemic word and fixing the
description instead. Rejected -- the name is what a writer reads before
filling the field in, and `defeated-by` asks for a verdict in its
grammar.

**Ontology:** NOTATION stipulated `defeater` as a word; it now
stipulates `staleness condition`. A stipulated word changing is a
revision to a defining claim, and NOTATION's standing is `agent` --
signed on the user's behalf, veto invited, per the ledger's own
governance.

## Blast radius

- `llm-claims-kb/`: the schema field and its description, `SKILL.md`'s
  mapping row, `Claim.stale_when` through `llm_claims_kb.py`, and
  flatten rendering `-- stale when ...`.
- `llm-claims/design.claims.*`: five defining claims, the theory table
  in `design.claims.md`, and the prose in `THEORY_NODE+`.
- `docs/dev/design.claims.*`: two defining claims.
- Reading past the old key would have dropped the line silently, so
  `read_claim` now asserts `defeated-by` is absent. A ledger that has
  not migrated fails loudly rather than rendering a theory with no
  staleness condition.

## Two schema copies became one

`llm-claims/design.claims.kb/jsonschema/claim.jsonschema.yaml` and
`docs/dev/design.claims.kb/jsonschema/claim.jsonschema.yaml` were both
byte-identical copies of the skill's canonical schema, so this rename
would have been written three times. They are now a `skill://` stub and
a symlink respectively -- cross-skill gets the stub, same-repo gets the
symlink, matching what `strata.claims.kb/` already did. Per
`llm-kb/references/schema-reuse.md`.

## Verification

- `llm.kb-validate llm-claims docs/dev/design.claims.kb`: 46 files, 0
  errors.
- `llm-claims-kb-flatten llm-claims/design.claims.kb`: 30 claims in 5
  theories, each defining claim suffixed `-- stale when ...`.

## Left open

`docs/dev/strata.claims.kb/` is red until the replication session
migrates its thirteen lines -- its schema is a symlink to the
canonical, so the rename reached it the moment it landed. That session
proposed the change and asked for exactly this trigger; it was told the
moment it landed. Its prose in `strata.replication.run.kb/070`, `080`
and `strata.replication.md` still argues in the old vocabulary, which
is correct: those are records of turns that happened.

The ADR that introduced the field
(`adr/2026-08-11-000-A-theory-is-a-claim--containment-is-indentation.md`)
gained an amendment note rather than an edit -- it records a decision as
it was made.
