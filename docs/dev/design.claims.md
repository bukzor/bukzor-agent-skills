---
label: FLEET_DESIGN
standing: agent
ontology:
  - fleet
  - repo
  - skill
  - claim
  - ledger
  - ruling
  - ADR
stale-when: a commitment that binds one skill only -- it belongs in that skill's own ledger, not here
last-updated: 2026-08-17
---

# The fleet's design, as a ledger

Design commitments of bukzor-agent-skills itself -- the rules its
skills are written under, kept as a claim ledger
(`Skill(llm-claims-kb)`): one claim per file, label and
standing in frontmatter, one theory per collection under
`design.claims.kb/`. Argue with a claim by editing its file; the git
diff is the strikethrough.

Division of labor with `adr/`: an ADR is the record of a ruling --
the context, the alternatives, the date; the ledger holds the
commitment's current standing and its warrant arrows. A claim whose
ruling has an ADR cites it as `authority:`.

## Theories

Each theory is the claim file beside its collection, so `ls` is the
index and nothing here needs to restate it.

Roots are roots: claims here connect where a warrant is real, and
stay disconnected where it is not.

## Scans

```bash
grep -rH '^standing:' docs/dev/design.claims.kb/     # who signed what
llm-claims-kb/bin/llm-claims-kb-graph docs/dev/design.claims.kb  # shape + lints
```
