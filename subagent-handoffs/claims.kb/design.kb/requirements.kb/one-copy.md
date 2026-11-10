---
label: ONE_COPY
standing: agent
why:
  - ../goals.kb/correctness.md
  - ../goals.kb/focus.md
---

# One copy of each fact

Every fact an agent reads exists in exactly one place, so no agent
works from a stale copy, and no agent reads the same fact twice.

Checked by finding any statement of design, an interface, or a finding
in two files of a plan, and asking which one a reader would trust.
