---
label: MIGRATE
standing: user
why:
  - what-becomes-of-llm-discourse-graph.md
  - where-the-migration-guide-and-its-trigger-live.md
  - the-stored-likelihood-is-neither-cache-nor-testimony.md
---

# The migration plan

`llm-discourse-graph` is reformed in place, and no existing instance
is required to move. Four commitments, ruled 2026-08-16:

- **Old instances stay legal.** The five-collection format keeps
  working; nothing is rewritten on a schedule.
- **The guide travels with the skill** -- under
  `llm-discourse-graph/skill.kb/`, with a `must-read.kb/when/`
  trigger pointing at it, so an agent that meets an old-format
  directory is routed to the guide by the skill it was already going
  to load.
- **The name and location do not move**
  (`what-the-successor-is-called.md`): a trigger inside a skill that
  no longer exists routes nobody.
- **Stored `likelihood` values are carried over verbatim**, until
  `what-need-does-a-stored-likelihood-serve.md` closes -- "We just
  keep the field until it's closed."

Modernization is therefore per-instance and opportunistic: an agent
already working inside an old instance does it if and as appropriate,
and no one goes looking for work.
