---
label: QUIVER
standing: agent
why:
  - ../record.kb/validation-is-a-typing-map.md
---

# Key-Valued Fields Present a Quiver

Mark which fields hold keys, and every typed instance presents a
directed graph on its keys -- edges read off the marked fields, no
separate edge store. Referential integrity is the condition that every
edge lands on an existing key, checkable at the same moment as typing.

The graph is derived structure: delete the marking convention and the
graph vanishes without touching a file.
