--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-design-kb)
---

# Goals Layer

How we accomplish the mission. Each goal is a strategic stance,
mostly a v1 lesson-learned promoted to a commitment.

## What Belongs Here

- Strategic stances that, taken together, accomplish the mission
- One goal per file; the file name is the goal slug

## What Does NOT Belong Here

- Mechanisms (design-layer concerns)
- Validation criteria (requirements)

## Frontmatter

Each entry's `why:` references the mission by file-relative path
(`../010-mission.md`).

## When to Add / Read

- **Add** when a new strategic stance is needed, separable from
  existing goals.
- **Read** when extending requirements, or when reviewing whether the
  design still hangs together.
