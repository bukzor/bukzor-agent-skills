# Dependency Wake

A task blocked on another (`after: file:` desc naming the blocker)
should claim no attention while blocked and return exactly when the
blocker completes. This is where per-task blockage lives — v1's
`## Blocked` sections and blocked-by fields, made evaluable.

Today: blockage is prose; an unblocked task is noticed at the next
manual read of the list, if then.

Satisficed when: the sweep checks the referenced entry's disposition
and restores nag-eligibility on completion, mechanically — a `file:`
desc is a decidable cell, never a judgment one.
