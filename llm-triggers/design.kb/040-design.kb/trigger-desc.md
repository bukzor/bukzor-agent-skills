---
why:
  - ../010-mission.md
  - task-deferral.md
status: proposal
---

# Trigger-Desc: the Wake-Condition Value Grammar

One value grammar for every frontmatter field whose meaning is "when
this holds, act": task deferral (`task-deferral.md`), future-work
`trigger:` fields, and later wake-shaped uses. A wake condition is a
juncture key applied to a **trigger-desc**:

```yaml
trigger:
  - at: 2026-08-01                      # date
  - at: 2026-08-01T09:00:00-05:00       # instant
  - after: file:../task.md              # task-completion event
  - when: "the v2 build is green-lit"   # prose condition
```

Trigger-descs are self-disambiguating by syntax alone — date,
instant, `file:` path, prose — with room for disambiguation
attributes if a form ever needs them. Junctures reuse the bank's
vocabulary (`bank-format.md`) plus `at`, for time-points, which banks
don't need but wake conditions do.

The juncture × desc-type matrix expresses more than deferral. Cells
with an assigned meaning:

- `at:` + date/instant — scheduled wake
- `before:` + date/instant — deadline (a constraint, not a deferral)
- `after:` + `file:` — dependency wake (the referenced task's
  completion event; this is where per-task blockage lives)
- `after:`/`when:` + prose — conditional wake, judged at sweep time

Remaining cells are documented as unassigned, not schema-forbidden;
each gains a meaning (or a constraint) when a consumer needs it.

Prior art, independently converged:
`../../../llm-vitals/design.kb/070-future-work.kb/wake-conditions.md`
proposed a `wake:` field with an event / calendar / threshold / reflection taxonomy —
event and calendar are `after:` and `at:` here; threshold and
reflection are prose `when:` descs.

> [!QUESTION] is this the final schema shape?
> Adopted as a strawman with a stated expectation of redesign;
> settles when the first consumer (the task-deferral sweep) is built
> against it.
