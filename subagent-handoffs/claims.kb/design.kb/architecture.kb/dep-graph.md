---
label: DEP_GRAPH
standing: agent
why:
  - ../requirements.kb/amend.md
  - homes.md
---

# Required reading is the dependency graph

A brief's `required-reading:` names the homes its unit reads, so the
handoff collection's frontmatter is the graph from each fact to the
units that depend on it. After an amendment, a grep for the amended
home over the open handoff files lists exactly the units to tell
"reread".

It holds only while briefs cite homes: a brief that pastes a fact
instead of naming its file drops out of the graph.
