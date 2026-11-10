---
label: DESIGN
standing: agent
ontology:
  - mission
  - goals
  - requirements
  - architecture
  - components
  - coordinator
  - unit
  - handoff file
non-claim-tokens:
  - DAG
stale-when: a rung nothing cites and nothing fills -- the chain was copied rather than chosen, and the stratification wants re-deriving from what this method actually argues about
---

# subagent-handoffs -- the design, as a ledger

Why the method in `../SKILL.md` is shaped the way it is: what it is for,
the goals it serves, and the options it declined. `SKILL.md` is the
usage manual and states every rule a coordinator always needs; this
ledger holds the rationale, read when changing the method or judging a
case the procedure does not cover. Kept as a claim ledger
(`Skill(llm-claims-kb)`): one claim per file, label and standing in
frontmatter, one theory per collection. Argue with a claim by editing
its file; the git diff is the strikethrough.

Words every rung uses:

- **coordinator**: the session that decomposes the plan, briefs units,
  and reviews what comes back; it implements nothing itself.
- **unit**: one sub-agent's piece of the plan, scoped to a disjoint file
  list and sized for one sitting.
- **handoff file**: the one file per unit carrying both directions --
  the coordinator's brief, then the agent's own record and report.

Five rungs, each a theory whose `why:` names the rung it serves. The
skeleton's sixth, `deliverables`, is dropped: the method has no build
step, and its components are files edited directly.

| Rung | The question it answers |
|---|---|
| `mission` | What problem are we solving? Who benefits? |
| `goals` | How do we accomplish the mission? |
| `requirements` | How do we validate the goals are achieved? |
| `architecture` | How do we satisfy the requirements? |
| `components` | How do we implement the architecture? |

Priors are a DAG, not a ladder: a claim's `why:` names whatever claims
it would be revisited over, one rung up or four.

## Scans

```bash
grep -rH '^standing:' claims.kb/     # who signed what
grep -rl 'verdict:' claims.kb/       # what was declined or superseded
llm-claims-kb-flatten claims.kb/design.kb   # the whole ledger as one text
```
