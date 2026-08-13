--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-design-kb)
---

# Requirements Layer

How we validate that goals are achieved. Each requirement is an
observable property the system must exhibit.

## What Belongs Here

- Validation criteria the system must meet
- One requirement per file
- Each requirement linked to one or more goals via `why:`

## What Does NOT Belong Here

- Implementation mechanisms (those are design or component-layer)
- Wish-list features (those are `070-future-work.kb/`)

## Frontmatter

Each entry's `why:` references one or more goal slugs from
`020-goals.kb/`.

## When to Add / Read

- **Add** a requirement when a new observable property of the system
  is needed to validate one or more goals.
- **Read** when designing or evaluating a mechanism (to confirm it
  satisfies a requirement) and when reviewing whether goals are
  reachable from the current design.
