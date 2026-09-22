---
label: TOP_PULLER
standing: agent
why:
  - each-set-has-its-own-puller.md
  - ../delivery.kb/reinstalling-the-top-set-restores-every-stub.md
---

# The Top Set May Be Pulled by a Hook

The top set's puller can be mechanical: a `SessionStart` hook on the
`compact` matcher re-lists after every compaction, and a `PreToolUse`
hook on the first tool call installs at the moment the host stanza
names. Neither meets the standing objection to a plain `SessionStart`
hook -- that a session with no tool calls has no need of the bank --
since compaction implies an active session and `PreToolUse` fires only
on a call. The ruling is the owner's and sits on the
trigger-installation session's table.
