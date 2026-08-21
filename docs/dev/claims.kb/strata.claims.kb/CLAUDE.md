--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-claims)
    - Skill(llm-claims-kb)
---

# strata.claims.kb -- maintenance guide

The formal model of the skill ecosystem's engine tower, kept as a
claim ledger. `../strata.claims.md` is the reader's entry point and
carries the theory poset. One theory per collection, one claim per
file, label and standing in frontmatter.

## What belongs here

A mathematical commitment about what the engines *are* -- a structure
identification, a law, or a theorem the design leans on -- anything
whose reversal would change what is safe to build.

## What does NOT belong here

Design decisions for particular tools or skills -> `design-next.kb/`.
Instructions for using ledgers or kbs -> the skills' `skill.kb/`.
Correspondence with named external systems belongs only in `fleet.kb/`
-- every other theory stays proper-noun-free so it survives those
systems changing. (`question.kb/` excepted: its proper nouns are
past-tense provenance, which no future change reaches.)

## Filing a new claim

Placement is fixed by vocabulary: the earliest theory whose ontology
(its own plus its priors') admits every word the claim needs. Prefer
adding an auxiliary prior theory over widening an ontology with
machinery that is not really the theory's own. Representation
vocabulary -- file, directory, path, frontmatter, markdown, wire --
is admitted only at `data-representation.kb/`; a lower claim needing
those words is filed there or reworded. (These maintenance notes are
exempt: they are about the files, and are not claims.) A theory's own
defining claim -- `<theory>.md` beside its `<theory>.kb/` -- carries
the vocabulary it admits (`ontology:`), its priors (`why:`), and the
observable condition that voids its stamp (`stale-when:`); these
files are claims like any other, and the
collections' `CLAUDE.md` files are maintenance notes only.
