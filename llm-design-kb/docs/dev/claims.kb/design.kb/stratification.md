---
label: STRATA
standing: agent
why:
  - ../design.md
ontology:
  - rung
  - prior
  - confinement
stale-when: a project whose claims sort cleanly by graph depth alone -- then the rung names were carrying nothing the arrows did not already carry
---

# stratification -- what the rungs are

A **rung** is a theory: a defining claim beside its collection, whose
`ontology:` stipulates the rung's vocabulary and whose `why:` names
its **priors**. The default chain is mission, goals, requirements,
architecture, components, deliverables.

Rungs are semantic, not topological. "What problem are we solving"
and "how do we validate it" are different speech acts, which is why
they are named rather than derived: a claim's depth in the motivation
graph is topology, and being two hops from mission does not make
something a requirement.
