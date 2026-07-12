--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-design-kb)
---

# Requirements Layer

How we validate the goals are achieved. Each requirement is a
checkable property of the built system — phrased so that an audit
could pass or fail it.

## What Belongs Here

- Verifiable properties the v2 system must exhibit
- One requirement per file; the file name is the requirement slug

## What Does NOT Belong Here

- Mechanisms that satisfy the requirement (design layer)
- Strategic stances (goals)

## Frontmatter

Each entry's `why:` references goal slugs from `../020-goals.kb/`.

## When to Add / Read

- **Add** when a goal has a success property not yet checkable via an
  existing requirement.
- **Read** before accepting a design entry: every design must satisfy
  at least one requirement here.
