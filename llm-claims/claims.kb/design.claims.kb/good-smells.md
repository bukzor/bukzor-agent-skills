---
label: GOOD_SMELLS
standing: agent
why:
  - purpose.md
ontology:
  - writer
  - consumer
  - token
  - medium
  - rendering
  - demo
  - migration
non-claim-tokens:
  - NC
  - OP
  - RR
stale-when: a change in who uses the notation -- a ledger written and read by tools, where entry cost and rendering hazards both vanish
last-updated: 2026-08-20
---

# Good Smells — criteria for conversational notation design

A design decision is answerable to a criterion stated before it and
independently of it: a property any claim notation should have, this
skill's own included. One criterion per file in `good-smells.kb/`,
each carrying its own `label` and `standing`; the decisions that answer
to them are `notation.md`'s.

Two poles organize the set: the notation should elicit every judgment
the writer can make now, while demanding none they can't make yet. The
remaining criteria are economies — of entry, reference, governance,
enforcement, and transport — that keep the ledger cheaper to use than to
ignore. One is not an economy but a test: the notation has
to be able to carry its own design.
