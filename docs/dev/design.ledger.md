---
last-updated: "2026-08-09"
---

# The fleet's design, as a ledger

Design commitments of bukzor-agent-skills itself -- the rules its
skills are written under, kept as a claim ledger
(`Skill(llm-claim-ledger-kb)`): one claim per file, label and
standing in frontmatter, one theory per collection under
`design.ledger.kb/`. Argue with a claim by editing its file; the git
diff is the strikethrough.

Division of labor with `adr/`: an ADR is the record of a ruling --
the context, the alternatives, the date; the ledger holds the
commitment's current standing and its warrant arrows. A claim whose
ruling has an ADR cites it as `authority:`.

## Theories

One so far, a root:

- **`authorship.kb/`** -- how any skill here is written: audiences,
  names, coupling, citation discipline. Priced against LOAD_COST: a
  skill is written once and paid for on every load. Defeated by a
  skill format with per-audience channels, or retrieval that consults
  neither names nor descriptions.

Roots are roots: claims here connect where a warrant is real, and
stay disconnected where it is not.

## Scans

```bash
grep -rH '^standing:' docs/dev/design.ledger.kb/*.kb/   # who signed what
llm-claim-ledger-kb/bin/llm.ledger-graph docs/dev/design.ledger.kb  # shape + lints
```
