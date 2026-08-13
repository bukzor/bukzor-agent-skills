--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-design-kb)
---

# Design Layer

How we satisfy the requirements: a thin core (spec, engine) plus
detachable classes, and the boundary decisions around them. Start
with `core-and-classes.md`; everything else elaborates one kind or
one cross-cutting policy.

## What Belongs Here

- Architectural primitives of the v2 system and their relationships
- Boundary decisions (hook vs skill vs rule vs data; automated vs
  manual)
- One abstraction per file; forward-facing prose (what the system
  *is*), alternatives as footnotes

## What Does NOT Belong Here

- Implementation detail (CLI flags, hook JSON, schema text) —
  component-layer, deferred until build
- Decision journeys — ADRs
- V1 critique beyond what motivates a design choice

## Frontmatter

`why:` lists file-relative paths of motivating requirements
(`../030-requirements.kb/<requirement>.md`, or a same-layer entry
where the motivation lives at this level).
Open-item markers per `../CLAUDE.md`; `blocked-on: discussion`
additionally marks a `status: proposal` entry that needs a
discussion before it can be ratified.

## When to Add / Read

- **Add** when a design discussion settles (or usefully frames) a new
  abstraction or boundary.
- **Read** before reshaping any v1 skill or building any v2 piece.
