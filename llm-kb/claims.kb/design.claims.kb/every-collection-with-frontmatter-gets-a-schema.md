---
label: CANONICAL_PER_COLLECTION
standing: user
authority: "user, 2026-08-22: 'Make a quick schema for these. maybe can use a mechanical agent for that.'"
---

# Every Collection With Frontmatter Gets a Schema

A collection whose files carry frontmatter and has no sibling
`X.jsonschema.yaml` is unvalidated, and reports `No schema found` on
every one of its files. The ruling is to write the schema, not to strip
the frontmatter.

Known instances include `~/.claude/reference.kb/`,
`~/.claude/user-preferences.kb/`, and collections in the private
repositories. The work is mechanical: read what keys the files actually
carry, write the schema that admits them, run the validator.

The rule generalizes past the current list. Any collection that grows
frontmatter grows a schema in the same commit; that is what makes
`No schema found` a real error rather than a routine one to skim past.
