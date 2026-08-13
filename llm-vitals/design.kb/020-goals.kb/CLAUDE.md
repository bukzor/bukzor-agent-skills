--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-design-kb)
---

# Goals Layer

How we accomplish the mission. Each goal is a strategic stance; together
they cover the mission's success criteria.

## What Belongs Here

- Strategic stances that, taken together, accomplish the mission
- One goal per file; the file name is the goal slug

## What Does NOT Belong Here

- Tactical mechanisms (those are design or component-layer concerns)
- Validation criteria (those are requirements)

## Frontmatter

Each entry's `why:` references the mission slug `mission` (the single
.md at this layer's parent has no slug; we use `mission` as the
canonical reference).

## When to Add / Read

- **Add** a goal when a new strategic stance is needed to accomplish
  the mission, separable from existing goals.
- **Read** when extending requirements (to know what they must serve)
  or when reviewing whether the design still hangs together.
