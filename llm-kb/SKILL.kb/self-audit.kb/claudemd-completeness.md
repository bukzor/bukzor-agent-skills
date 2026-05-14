# Self-audit: CLAUDE.md completeness

## Goal

After reading the CLAUDE.md, a maintainer can make correct
add/skip decisions.

## Procedure

For each CLAUDE.md you touched, verify three rules are present:

1. **What belongs here** -- the type-of-thing.
2. **What does NOT belong** -- boundaries to adjacent collections.
3. **When to add / read files here** -- the trigger.

For a root CLAUDE.md, also verify frontmatter declares
`requires: Skill(llm-kb)` and the body identifies the project's
`.kb/` collections.

## Recovery

Write the missing rule. Describe the type-of-thing, not current
contents.

## Related

- `claudemd-enumeration.md` -- the opposite failure (listing
  current contents instead of stating rules).
