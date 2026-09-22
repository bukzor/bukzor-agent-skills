---
label: BEGIN_AT_DECISION
standing: agent
why:
  - ../pullers.kb/a-begin-mid-flow-is-missed.md
---

# An Activity Begins at the Decision to Enter It

An activity occasion -- making code changes, debugging -- begins at the
moment the agent decides on it, not at its first action. Two grounds:

- A set whose members are `before/` triggers must be installed before
  any of them fires, and a `before/` member fires at the moment
  preceding its action; only a begin at the decision precedes that
  (`../firing.kb/a-set-begins-before-its-members-fire.md`).
- The decision moment is a deliberating state and the first action a
  flow state; the sibling audit found begins are noticed in the former
  and missed in the latter, so this is also where the notice is placed
  so that noticing works.

Declined: begin at first action, under which every `before/` member
of every set fires before its set exists.
