--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-claims)
    - Skill(llm-claims-kb)
---

# design.claims.kb -- maintenance guide

The design of `/deformalize`, kept as a claim ledger. `../design.claims.md`
is the reader's entry point and carries the poset.

## What belongs here

A commitment `/deformalize` makes, or a goal it answers to -- anything
whose standing could be contested and whose reversal would change the
procedure or the output shape.

## What does NOT belong here

Instructions for running `/deformalize` -> `../SKILL.md`. Those are
directives: nothing about them is contestable in the way a claim is.

Commitments about `/formalize`'s own procedure -> that skill's ledger.
What lives here is only the seam: what `/deformalize` receives, and
what it owes back.
