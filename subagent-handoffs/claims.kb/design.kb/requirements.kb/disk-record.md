---
label: DISK_RECORD
standing: agent
why:
  - ../goals.kb/review.md
  - ../goals.kb/interruptibility.md
---

# Every handoff is on disk

Every handoff, in both directions, is the file the agent actually
worked from: what it was asked, and what it reported. Nothing a unit
depends on exists only in chat.

Checked by comparing each launch and each later message to the
handoff file it names: the message names a path and nothing else.
