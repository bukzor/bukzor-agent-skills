---
label: DESIGN
standing: open
ontology:
  - mission
  - goals
  - requirements
  - architecture
  - components
  - deliverables
non-claim-tokens:
  - DAG
stale-when: a rung nothing cites and nothing fills -- the chain was copied rather than chosen, and the stratification wants re-deriving from what this project actually argues about
---

# <project> -- the design, as a ledger

What this project is for and how it is built, kept as a claim ledger
(`Skill(llm-claims-kb)`): one claim per file, label and standing in
frontmatter, one theory per collection. Argue with a claim by editing
its file; the git diff is the strikethrough.

Six rungs, each a theory whose `why:` names the rung it serves. They
are a default, not a law: drop a rung this project does not argue
about, add one it does, and revise this claim to say so. Answering the
six questions below is what turns this skeleton into a design record.

| Rung | The question it answers |
|---|---|
| `mission` | What problem are we solving? Who benefits? |
| `goals` | How do we accomplish the mission? |
| `requirements` | How do we validate the goals are achieved? |
| `architecture` | How do we satisfy the requirements? |
| `components` | How do we implement the architecture? |
| `deliverables` | How do we build the components? |

Priors are a DAG, not a ladder: a claim's `why:` names whatever claims
it would be revisited over, one rung up or four. The column above is
the common shape, not a constraint.

## Scans

```bash
grep -rH '^standing:' docs/dev/claims.kb/     # who signed what
grep -rl '^todo: true' docs/dev/claims.kb/    # decided, not yet built
llm-claims-kb-flatten docs/dev/claims.kb/design.kb   # the whole ledger as one text
```
