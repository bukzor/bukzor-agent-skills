---
label: DISJOINT_SCOPE
standing: agent
why:
  - ../requirements.kb/unit-diff.md
  - ../goals.kb/focus.md
---

# Units own disjoint files

Each unit is scoped to a file list no other unit touches, and sized
for one sitting. A file several units would need belongs to exactly
one of them. Disjoint scopes are what let units in a wave run
concurrently, keep each unit's commits its own, and bound what each
agent has to read.
