--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-design-kb)
---

# Future Work Layer

Ideas worth remembering, deferred with an explicit `trigger:` stating
when each becomes worth pursuing.

## What Belongs Here

- Deferred v2 features with a named trigger condition
- One idea per file

## What Does NOT Belong Here

- Anything the current design depends on (that's design-layer)
- Vague aspirations with no articulable trigger — sharpen or drop

## Frontmatter

`why:` may reference any earlier layer by file-relative path;
`trigger:` is required.

## When to Add / Read

- **Add** when a design discussion surfaces a good idea that would
  dilute the build if pursued now.
- **Read** on periodic review, or whenever a trigger condition may
  have fired.
