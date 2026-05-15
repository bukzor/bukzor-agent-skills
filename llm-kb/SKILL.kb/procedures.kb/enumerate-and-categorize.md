# Enumerate and Categorize

Plan items by type before committing to a directory shape. Skipping
causes under-scoped collections that need restructuring later.

Applies to:

- **New collection** -- before writing files.
- **Existing collection** -- re-derive categories from current content.
  Ignore where files currently sit; the value of the pass is fresh
  judgment against today's content, not endorsement of yesterday's
  layout.

## Procedure

1. List every item the collection should hold (or, for existing
   content, every item currently in scope -- including items
   half-described inside other files).
2. Categorize by **type**, not subject. Type drives directory shape.
3. Each type → one `$CATEGORY.kb/`. Sub-categories when items split
   into homogeneous subgroups.
4. Each item → one `$item-slug.md` inside its category.

For existing content, the result is a target layout. Compare against
the current layout; the diff is the restructure work.

## Flat-`.md` fallback

2-4 short items without shared structure can stay as flat prose. The
promotion signal is growth pressure (per-item frontmatter, lifecycle,
paragraph-length explanation).

## When invoked

- `references/creating-a-new-kb.md`
- `../self-audit.kb/enumeration-completeness.md` (re-run afresh
  against existing content)
