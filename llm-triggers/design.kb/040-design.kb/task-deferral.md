---
why:
  - ../../../design-next.kb/040-design.kb/class-task.md
status: proposal
---

# Task Deferral

A deferred task names its wake condition in frontmatter: a `trigger:`
field whose value is the trigger-desc grammar (`trigger-desc.md`). No
second grammar exists for deferral — the elaboration ladder is the
value grammar's own: a date compares mechanically; a prose condition
is judged by the sweep, with the same floor semantics as any `when/`
trigger.

Sweep contract by matrix cell:

- **`at:` / `after:` (deferral, dependency)** — the task stays listed
  (obligations are never invisible) but is not nagged until the
  condition holds: dates compare mechanically, `file:` descs check
  the referenced task's disposition, prose is judged.
- **`before:` + time (deadline)** — inverts the contract: the nag
  escalates as the instant approaches. Distinct sweep behavior, same
  value grammar.

Line-grain tasks cannot carry frontmatter, so deferring one is an
elaboration trigger: promote to file grain first — class-task.md's
ladder doing its job.

The future-work class's `trigger:` field
(`../../../design-next.kb/070-future-work.jsonschema.yaml`) is the
same primitive on the
option contract: where sweeps never nag anyway, the field marks
readiness rather than suspending anything.

> [!QUESTION] per-cell sweep semantics
> The deferral / dependency / deadline contracts above are proposed,
> not ratified cell-by-cell; settles when sweep tooling implements
> them.
