---
why:
  - ../010-mission.md
---

# Token Economy

Context is the scarcest resource in every session. Every token loaded
must pay for itself: knowledge loads only when a trigger condition
matches, indexes are cheap to scan (filenames, `ls`), and bodies stay
unloaded until needed.

V1 validated this goal thoroughly — it is the reason the filesystem
patterns work at all. V2 keeps it as the first filter on every design
choice: the question is never "is this useful?" but "does it repay
its load cost at the moment it loads?"
