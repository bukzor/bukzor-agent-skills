--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-design-kb)
---

# Design Knowledge — llm-triggers

Layered design for the trigger subsystem: a runtime-neutral condition
vocabulary, kb-shaped trigger banks, and per-runtime interpreter
shims, all resting on a universal scan-time floor.

Grain note: this tower holds the subsystem's specifics. The
ecosystem-level properties it satisfies live in
`../../design-next.kb/` (`040-design.kb/class-trigger.md`,
`040-design.kb/delivery-boundary.md`, and the trigger requirements),
which cites down here rather than restating.

## Layered Structure

Per `Skill(llm-design-kb)`; entries carry `why:` as file-relative
paths, cross-tower where the motivation genuinely lives in
design-next.kb.

- `010-mission.md` — what problem, who benefits
- `040-design.kb/` — the subsystem design (other layers absent until
  needed; the governing goals and requirements are design-next.kb's)

## Open-Item Markers

Same grammars as design-next.kb: `status: proposal` (frontmatter)
awaits operator ratification; `> [!QUESTION]` (body) awaits evidence
or a decision at sub-entry grain.

## What Belongs Here

- The subsystem's condition vocabulary, bank format, interpreter
  contract, wake-condition grammar, and adapter bindings
- Boundary decisions the subsystem itself owns (which conditions are
  neutral vocabulary vs. adapter-only glue)

## What Does NOT Belong Here

- Ecosystem-level properties (why triggers exist, the action/judgment
  partition) — those live in `../../design-next.kb/`, cited not
  restated
- A built shim's implementation — component-layer, deferred until
  code exists
- Decision journeys — an ADR's job, not this tower's

## When to Read / Update

- **Read** before building any trigger machinery (shims, sweeps,
  schemas) or reshaping the v1 bank conventions.
- **Update** when a design discussion changes the subsystem, or when
  a `proposal`-status entry gets decided.
