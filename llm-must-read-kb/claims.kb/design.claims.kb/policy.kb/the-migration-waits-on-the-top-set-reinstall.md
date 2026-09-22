---
label: MIGRATE_ORDER
standing: agent
why:
  - ../delivery.kb/what-reinstalls-the-top-set-after-compaction.md
---

# The Migration Waits on the Top-Set Reinstall

Moving today's bank to the set form is gated on the top set's
post-compaction re-install being settled -- a hook, an idempotent
per-context-window installer, or evidence that the hole is small.
Sets add no re-install burden of their own, but a bank whose top set
goes dark after compaction is not improved by nesting part of it.
