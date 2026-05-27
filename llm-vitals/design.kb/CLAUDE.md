--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-design-kb)
---

# Design Knowledge — llm-vitals

Layered design documentation for the `llm-vitals` skill: a multi-axis
attention-allocation system across personal, wellness, and business
domains, modeled on SRE observability with two-tier accountability.

## Layered Structure

Per `Skill(llm-design-kb)`. Each layer justifies the one below and
realizes the one above; entries carry `why:` frontmatter linking to
their motivation.

- `010-mission.md` — what problem are we solving, who benefits
- `020-goals.kb/` — how we accomplish the mission
- `030-requirements.kb/` — how we validate goals are achieved
- `040-design.kb/` — how we satisfy requirements (architectural primitives)
- `050-components.kb/` — implementation pieces (deferred until coding)
- `060-deliverables.kb/` — phased build plan (deferred until coding)
- `070-future-work.kb/` — ideas deferred with explicit trigger conditions

`.kb/` vs `.md` follows growth pressure: a single entry that fits in
~60 chars stays `.md`; promote to `.kb/` when items need richer per-item
content.

## What Belongs Here

- Mission, goals, requirements, architectural design
- Vocabulary decisions and the reasoning behind them
- Boundary decisions (skill/data split, repo layout)
- Deferred ideas with explicit trigger conditions

## What Does NOT Belong Here

- Implementation details (config file format, CLI flags) — those live
  with components when written
- Per-user data (vital values, journals) — those live in the user's
  private data repos
- Decision journeys with alternatives weighed — write an ADR if needed;
  this kb captures outcomes

## When to Read

- Orienting on the system's concepts before implementing
- Before extending the design (new vital kinds, new SLO tiers)
- When deferred ideas in `070-future-work.kb/` become triggerable

## When to Update

- After an architectural change is decided
- When a deferred idea graduates from `070-future-work.kb/` into the design
- If documentation contradicts implementation, one is stale
