---
why:
  - ../020-goals.kb/single-source-improvement.md
trigger: Operator green-lights the v2 build.
---

# V1 Migration Bridge

The stack is incrementally reachable — no flag-day rewrite. Each v1
skill is gutted one at a time to defer to the engine: first the
engine absorbs the eight `bin/` scripts behind their existing names,
then SKILL.md prose shrinks to recognition content as procedures move
to commands, then hooks take over the action-shaped triggers, and
finally the plugin manifest replaces the symlink farm. Consumer
projects keep working at every step because the data formats (Layer
0) are v1-compatible from the start.

Estimated at 2–3 focused weeks of sessions to parity.
