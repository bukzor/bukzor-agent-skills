# bukzor-agent-skills

The skill fleet, one directory per skill, and two towers above them:

- `design-next.kb/` — v2 ecosystem design. Design-only.
- `docs/dev/` — ADRs and devlogs.

## What Belongs Here

One directory per skill, self-contained: its `SKILL.md`, its own `CLAUDE.md`
where maintenance rules differ from this file, its design tower where it has
one.

## What Does NOT Belong Here

Per-skill maintenance rules — with the skill they govern. Cross-skill
architecture — `design-next.kb/`. How a decision was reached — an ADR.

## When to Read / Update

**Read** before proposing a new skill, a new convention, or a change to one.
**Update** when a discussion establishes a lens that should outlive it.

## Design guidance

Rules only; rationale is in `llm-triggers/design.kb/`.

- A conditional directive is a trigger — a *(condition, target)* pair. Name
  the condition.
- A bare directive is well-formed only where its carrier was itself reached
  conditionally. A `must-read.kb/` entry qualifies; a `CLAUDE.md` does not.
  Fix unconditional carriers; leave conditional ones alone.
- Key a trigger on intent, not location. Below ~80% of arrivals needing the
  payload, do not fire unconditionally.
- Prefer letting the payload advertise its own trigger. Check whether the
  repair is deletion before designing a replacement.
- Every condition must be cheap to evaluate or explicitly judgment-only.
  Reject one that needs the payload to decide.
- Author for the planning-time floor; enforcement only strengthens the same
  meaning.
- State the firing condition only.
- Subtract before you add.
