# Self-audit: summary-file value

## Goal

Every `$CATEGORY.md` alongside `$CATEGORY.kb/` adds value beyond
`ls -RF`, and declares `last-updated:` frontmatter.

## Procedure

For each `$CATEGORY.md` next to a `$CATEGORY.kb/`:

> Does this file tell readers something `ls -RF $CATEGORY.kb/`
> doesn't -- themes, authority, navigation, when to consult?

If yes, also:

> Does the frontmatter declare `last-updated: YYYY-MM-DD`?

## Recovery

- Duplicates `ls`? Strip the file.
- Adds value, missing or stale `last-updated`? Update it (and
  refresh the content if it has gone stale).
