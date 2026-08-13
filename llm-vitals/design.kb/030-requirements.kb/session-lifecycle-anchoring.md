---
why:
  - reduce-dropped-tasks
  - counter-tech-revenue-bias
---

# Session Lifecycle Anchoring

The review cadence must piggyback on an existing ritual the operator
already performs reliably — specifically, Claude Code's session-start
and session-end skills. No new ritual is to be introduced.

This addresses the cadence-installation problem directly: any system
that depends on remembering to do something weekly will decay.
Habit-anchoring (Fogg) is the well-attested mechanism: tie the new
behavior to an existing trigger.

Implies: the picker output displays at session-start; the day-log
entry prompts at session-end. Both fire automatically by virtue of
the skill hooks, not by operator memory.
