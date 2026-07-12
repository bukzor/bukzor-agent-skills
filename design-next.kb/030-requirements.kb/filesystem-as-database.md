---
why:
  - token-economy
  - session-continuity
---

# Filesystem as Database

All durable knowledge is plain files whose names carry query
semantics. `ls`, `grep`, and `head` are the query language; no
runtime index, daemon, or database is required to answer "what
exists?", "what's open?", or "what changed?".

Checkable: any orientation question an agent needs at session start
is answerable with shell one-liners over the data directories, and a
directory listing never lies (no separate index files that can
drift).
