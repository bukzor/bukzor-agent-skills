---
label: COMPACTION
standing: open
why:
  - reinstalling-the-top-set-restores-every-stub.md
  - ../firing.kb/installing-is-idempotent-per-context-window.md
---

# What Reinstalls the Top Set After Compaction?

Nothing, today: the host stanza says "before your first tool call", a
resumed context has already made tool calls in its summary, and the
listing is not re-run. The trigger-installation session observed three
compaction boundaries with the listing never restored. Sets are out of
the question by the restore claim above; what is open is the top set's
re-install -- by an idempotent per-context-window installer, by a
`SessionStart` hook on the `compact` matcher, or by wording. An answer
settles whether the bank migration in `../instance.kb/` may proceed.
Owned by `~/.claude/sessions.kb/penguin.kb/trigger-installation.md`.
