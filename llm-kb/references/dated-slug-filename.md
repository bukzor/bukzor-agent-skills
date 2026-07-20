# Dated Slug Filenames

**Pattern:** `YYYY-MM-DD-NNN-slug.md`

The filename for one item in a collection whose items are dated
occurrences -- one file per occurrence, under a `$CATEGORY.kb/`
directory.

- `YYYY-MM-DD` -- the date the event happened, not the date the file was
  written. Backdate when filing a pickup late.
- `NNN` -- zero-padded, 3 digits. Resets to `000` at each new date; a
  second same-day item is `001`, not a continuation of the prior date's
  running count.
- `slug` -- kebab-case, descriptive, per `SKILL.md`'s general Naming
  rule.

## Ordering

Filename sort order is chronological order -- date first, then `NNN` for
same-day sequence. No index or registry file is needed; `ls` gives the
timeline.

## Not this file's concern

This defines the *name* only. What belongs inside a dated item, and how
much it may be edited after the date it's filed under, follows from
what the item represents -- no separate doctrine needed. State it
locally, in that collection's own `CLAUDE.md`, if it's ever
non-obvious.
