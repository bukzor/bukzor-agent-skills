# Self-audit: filename discipline

## Goal

Each filename tells an `ls -RF` reader what's inside, in kebab-case,
without redundant prefixes the parent directory already supplies.

## Procedure

For each file you touched:

> Seeing only this name in `ls -RF`, would I know roughly the
> content?

For procedures:

> Does the name describe the **task** (`scope-refactor`) or the
> **technique** (`audit-method`)? Task-shaped wins.

For files inside a `$VERB.kb/` collection:

> Does the directory verb already supply what my prefix is
> repeating?

## Recovery

Rename. Cryptic -> descriptive. Technique -> task. Redundant prefix
-> strip. CamelCase or snake_case -> kebab-case.

Date prefixes (`$DATE-NNN-$SLUG.md`) and order prefixes
(`001-setup.md`) are fine.
