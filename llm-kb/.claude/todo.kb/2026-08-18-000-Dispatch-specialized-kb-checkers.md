---
managed-by: Skill(llm-subtask)
status: open
cost-benefit-sweh:
  timebox:
    "@value": 2
    rationale: |
      The mechanism is small -- a naming convention plus a subprocess
      fan-out. The cost is the contract: how a collection's kind is
      recognized, what a checker may assume, what its exit status
      means. Past 2h that contract is not converging and wants a
      ruling rather than more code.
    confidence: unsure
  benefit-2w:
    "@value": 0.5
    rationale: |
      Three claims-ledger checkers exist today, each run by hand. The
      cost of not dispatching them is not the typing -- it is that
      they get skipped at exactly the moment a ledger was edited.
    confidence: unsure
---

# Dispatch specialized-kb checkers

**Priority:** Medium
**Complexity:** Medium
**Context:** `bin/llm.kb-validate` checks every `.kb` the same way --
frontmatter against whatever schema the collection declares. Structural
checks that only make sense for one *kind* of collection live in that
kind's own skill, and nothing calls them.

## Problem Statement

`Skill(llm-claims-kb)` ships three checkers over `*.claims.kb/`:

- `bin/llm-claims-kb-graph` -- a `why:` pointing nowhere, a claim that
  never joined the graph, a citation cycle;
- `bin/llm-claims-kb-flatten` -- a `why:` resolving to no file, a
  defining claim stipulating no `ontology:`, two labels `grep` cannot
  tell apart;
- `bin/llm-claims-kb-mentions` -- prose naming a label the claim's
  theory never imported.

None of them runs unless an agent remembers it exists. `llm.kb-validate`
walks the same directories and is the command agents already run, but it
knows nothing about claim ledgers -- and should not. Teaching the generic
validator one collection kind's rules is the outcome this item exists to
avoid; the question is what to build instead.

## Open Questions

- **How is a checker found?** A registry file in `llm-kb`, a convention
  the checker's own skill satisfies (`bin/<skill>-check`), or a
  declaration in the collection's schema. The first two put the list in
  the wrong place when a skill lives outside this repo.
- **How is a collection's kind recognized?** `*.claims.kb/` announces
  itself by suffix; `Skill(llm-discourse-graph)`'s collections do not,
  and are told apart by shape. Suffix-matching is cheap and covers
  today's only case, which is either the right scope or a trap.
- **Per-collection or per-fleet?** `llm-claims-kb-mentions` reads every
  ledger in the tree whichever are checked, because whether a token is a
  label at all is a fleet fact. A dispatcher that hands each collection
  to a checker one at a time makes that N times more expensive, or wrong.
- **What does a finding mean?** `llm.kb-validate` exits nonzero on a
  schema violation. Ledger checkers report things that are sometimes
  intentional (an open theory has no `ontology:` yet). Either the
  contract distinguishes error from warning, or dispatch inherits the
  false-positive problem `2026-07-09-000` is already stuck on.
- **Does dispatch belong in `llm.kb-validate` at all?** The alternative
  is that `Skill(llm-claims-kb)` is simply required reading before
  touching a ledger, and its SKILL.md already says which command to run.
  That is the status quo, and it is failing quietly -- but a dispatcher
  nobody runs fails the same way.

## Success Criteria

- [ ] Running the ordinary kb validation over a tree containing a
      `*.claims.kb/` surfaces that ledger's own findings, with no
      per-collection wiring by hand.
- [ ] A new collection kind registers its checker without editing
      `llm-kb`'s code.
- [ ] A checker that needs the whole fleet gets it once, not per
      collection.
