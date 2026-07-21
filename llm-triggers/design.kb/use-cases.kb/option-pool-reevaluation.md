# Option-Pool Reevaluation

The option contract (`ideas.md` / `ideas.kb/`) is read back by a
periodic wholesale pass — commit / retire / keep — never by sweep
nags (design-next's task class). Nothing schedules that pass: v1's
wsjf ratings existed precisely to serve it, and it ran only when the
operator remembered.

Today: operator habit. The read-back that justifies every option
write has no recorded cadence and no reminder.

Satisficed when: a recurring wake condition can be recorded — per
instance, at an operator-chosen cadence — whose firing surfaces "the
option pool is due a reevaluation pass," and whose being overdue is
visible to an audit.
