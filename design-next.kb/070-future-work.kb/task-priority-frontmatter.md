---
why:
  - ../040-design.kb/class-task.md
trigger: A second machine consumer of task priority appears (task-archeology's wsjf-rank is the first), or working-set reordering churn comes to dominate synthesis-file diffs.
---

# Task Priority Frontmatter

Frontmatter-driven prioritization for file-grain tasks: a minimal
canonical rating (e.g. 000-999 importance and urgency) or externally
defined metrics (task-archeology's wsjf sidecar is the working case
study). The working set's hand-maintained total order becomes
derived — or at least mechanically checkable — and tooling can
regenerate `- [ ]` listings from collection entries.

Operator-rated medium-to-high importance, long-term (2026-07-19).

Both task contracts are in scope, and the option pool came first:
v1's wsjf fields originated in the ideas.kb schema, added to
remember/refresh/reevaluate the priority of old ideas. That
read-back — a periodic commit / retire / keep pass over the option
pool — is the proven consumer; options carry no standing order, so
frontmatter ratings are their only priority signal above line grain.

Constraints already settled:

- Line-grain tasks have no frontmatter; the working-set order remains
  the only priority carrier at the lightest elaboration step. Any
  generator must preserve hand-written lines (tangent capture), never
  overwrite them.
- Per the T3 brief's case-study framing: wsjf's field vocabulary
  (`sweh`, `cod_2w`, …) is not canonized. The commitment is that
  extensions like it stay supportable from stable frontmatter, not
  that their fields enter the task schema.
- The engine is class-blind: a task-shaped regenerator is class-side
  convention or external tooling (task-archeology's existing shape),
  or a generic engine verb driven by class-supplied runtime data —
  never task logic in engine code.
