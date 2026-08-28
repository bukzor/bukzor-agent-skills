---
label: BINDINGS
standing: agent
authority: >-
  docs/dev/adr/2026-08-28-000-A-skill-states-a-stance--not-a-procedure.md
why:
    - stance-over-procedure.md
---

# Situational bindings are named, not removed

The setting-specific half of a skill — the field name, the command,
what counts as scarce here — is what makes its checks runnable, so
generality is not bought by deleting it. It is bought by collecting
it under one named heading that says outright it is local and is to
be rewritten rather than dropped on a port.

Minimisation reads as *as small as possible, but no smaller*. Content
that is inherently situational cannot be optimised away, and the best
available treatment is to make it easy to find and to replace.

The two failures this sits between are equally cheap to make: advice
so general no one can execute it, and a body so bound to one
repository that a reader elsewhere must guess which sentences still
apply. A single heading resolves both, because it tells the porting
agent exactly what its diff is.
