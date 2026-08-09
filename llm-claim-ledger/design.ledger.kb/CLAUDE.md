--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-claim-ledger)
---

# design.ledger.kb -- maintenance guide

The design of this notation, kept as a claim ledger in the notation
itself. One theory per collection, one claim per file, label and
standing in frontmatter. `../design.ledger.md` is the reader's entry
point and carries the poset.

## What belongs here

A commitment the design makes, or a goal or criterion it answers to —
anything whose standing could be contested and whose reversal would
change the notation.

## What does NOT belong here

Instructions for using a ledger -> `../SKILL.kb/`. Those are directives:
nothing about them is contestable in the way a claim is, and dressing
one in `label:`/`standing:` frontmatter produces a claim-shaped file
that says nothing about its own standing.

The tell is the standing field. If the honest value is `user` for
every file in a collection, the field is carrying no information and the
collection is a manual, not a theory.

## Filing a new claim

Placement is fixed by vocabulary, not by topic
(`Skill(llm-claim-ledger)` § Theories): a claim goes in the earliest theory whose
ontology — its own plus its priors' — admits every word the claim needs.
If no theory admits them, either the claim is using a word loosely, or
some theory's ontology is understated and should be widened on purpose.

Each collection's `CLAUDE.md` carries its theory header: `prior:`,
`ontology:`, `defeated by:`.
