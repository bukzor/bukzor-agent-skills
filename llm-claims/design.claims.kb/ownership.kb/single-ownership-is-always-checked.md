---
label: CHECK_OWNERSHIP
standing: user
why:
  - the-data-holds-a-relation-the-law-needs-a-function.md
  - sibling-doubles-leave-the-law-undefined.md
authority: user ruling, 2026-08-20 -- "either mechanistically, in python, or agentically, in documented procedures"
---

# Single ownership is always checked

Because the fleet's data can hold what the law cannot read (ARITY),
single ownership is checked wherever ledgers are worked on -- by one
of exactly two means:

- **mechanistically**, in python: the ownership scan
  (`llm-claims-kb/bin/llm-claims-kb-ownership`), which fails on
  sibling doubles and queues the rest;
- **agentically**, in documented procedures: the confinement audit
  in `llm-claims-kb/SKILL.kb/self-audit.kb/confinement.md`, run by
  an agent reading the ledger.

A rule with neither is the staleness condition the theory names for
itself: a law no scan and no procedure enforces.
