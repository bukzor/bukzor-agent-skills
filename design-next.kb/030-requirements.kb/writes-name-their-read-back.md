---
why:
  - ../020-goals.kb/write-economy.md
---

# Writes Name Their Read-Back

Every durable artifact class declares, in its collection's
maintenance guide, the moment its entries are read back: a session
juncture, a trigger condition, or a recurring question the entries
answer. An artifact class that cannot name its reader is a defect —
the content belongs in conversation, in a commit message, or nowhere.

Checkable: each collection's maintenance guide has a "when to read"
clause naming a concrete juncture, and spot-checks find entries
actually consumed there. V1's devlog is the motivating
counter-example: a per-session write whose read-back moment was
never named and never came.
