--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-claim-ledger)
    - Skill(llm-claim-ledger-kb)
---

# strata.ledger.kb -- maintenance guide

The formal model of the skill ecosystem's engine tower, kept as a
claim ledger. `../strata.ledger.md` is the reader's entry point and
carries the theory poset. One theory per collection, one claim per
file, label and standing in frontmatter.

## What belongs here

A mathematical commitment about what the engines *are* -- a structure
identification, a law, or a theorem the design leans on -- anything
whose reversal would change what is safe to build.

## What does NOT belong here

Design decisions for particular tools or skills -> `design-next.kb/`.
Instructions for using ledgers or kbs -> the skills' `SKILL.kb/`.
Correspondence with named external systems belongs only in `fleet.kb/`
-- every other theory stays proper-noun-free so it survives those
systems changing.

## Filing a new claim

Placement is fixed by vocabulary: the earliest theory whose ontology
(its own plus its priors') admits every word the claim needs. Prefer
adding an auxiliary prior theory over widening an ontology with
machinery that is not really the theory's own. Each collection's
`CLAUDE.md` carries its theory header: `prior:`, `ontology:`,
`defeated by:`.
