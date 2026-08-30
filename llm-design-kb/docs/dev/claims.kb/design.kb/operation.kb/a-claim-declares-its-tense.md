---
label: TENSE
standing: user
why:
  - ../operation.md
  - ../stratification.md
---

# A Claim Declares Its Tense

A design record leads implementation as often as it trails it, so a
reader cannot assume its prose describes shipped behavior. Every claim
therefore declares its tense, and the rung decides how:

- **Mission, goals, and requirements are aspirational by nature** and
  take no mark. Nobody reads "the parser accepts every valid input" in
  a requirements collection as a report on today's parser.
- **From architecture down**, undecorated prose is descriptive -- a
  mismatch with the code is a bug in the claim -- and a claim about
  something not yet built carries `todo:`.

This is the incumbent's rule preserved exactly ("Layers 010-030 are
aspirational by nature and need no marker; the convention applies
where prose could be mistaken for a claim about current behavior"),
with the marker changed from a callout block to the ledger's own
token.
