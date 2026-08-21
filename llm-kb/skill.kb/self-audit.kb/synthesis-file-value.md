# Self-audit: synthesis-file value

## Goal

Every `$CATEGORY.md` alongside `$CATEGORY.kb/` adds value beyond
`ls -RF`, and carries no frontmatter.

## Procedure

For each `$CATEGORY.md` next to a `$CATEGORY.kb/`:

> Does this file tell readers something `ls -RF $CATEGORY.kb/`
> doesn't -- themes, authority, navigation, when to consult?

If yes, also:

> Is it free of frontmatter?

## Recovery

- Duplicates `ls`? Strip the file.
- Carries frontmatter? Ask what the keys are for. A date the collection's
  own git history already gives, or a constant nothing reads, is a
  subtraction. Anything else is a member of some collection and belongs
  in one -- see `references/frontmatter-outside-a-collection.md`.
