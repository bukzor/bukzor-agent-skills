--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-design-kb)
---

# Design Knowledge — next-generation architecture

Layered design for the v2 rebuild of this repo's skill ecosystem: one
coherent system for durable knowledge, attention management, and
convention enforcement across many parallel human+LLM sessions, built
on 2026-native Claude Code primitives (hooks, rules, paths-gated
skills, plugins) instead of prose emphasis.

**Design-only.** Nothing here is implemented; the v1 skills
(`llm-kb`, `llm-collab`, etc.) remain the shipped system. Where this
tower contradicts a v1 ADR, the tower is the forward position;
entries not yet operator-ratified carry `status: proposal`.

## Layered Structure

Per `Skill(llm-design-kb)`. Entries carry `why:` frontmatter linking
to their motivation by file-relative path
(e.g. `../010-mission.md`).

- `010-mission.md` — what problem, who benefits
- `020-goals.kb/` — how we accomplish the mission
- `030-requirements.kb/` — how we validate goals are achieved
- `040-design.kb/` — how we satisfy requirements (the five-layer stack)
- `070-future-work.kb/` — deferred ideas with explicit triggers

## What Belongs Here

- The v2 layering: spec, engine, genres, delivery, instances
- Boundary decisions (what is a hook vs a skill vs a rule vs data)
- Lessons-learned from v1 recast as goals/requirements
- Deferred ideas with trigger conditions

## What Does NOT Belong Here

- V1 maintenance (per-skill todos, migrations) — those live with the
  skills they concern
- Decision journeys — write an ADR in `docs/dev/adr/`; this kb
  captures outcomes
- Implementation detail (CLI flags, hook JSON) — component-layer
  concerns, deferred until build

## When to Read / Update

- **Read** before any work that reshapes a v1 skill, to avoid
  investing against the grain of the target architecture.
- **Update** when a design discussion changes the target, or when a
  `proposal`-status entry gets decided.
