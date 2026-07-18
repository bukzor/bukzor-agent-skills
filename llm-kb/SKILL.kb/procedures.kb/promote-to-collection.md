# Promote to Collection

Flat `.md` → `.kb/`. Invoked from `../self-audit.kb/per-file-scope.md`
and `../self-audit.kb/promotion-signals.md`.

## Procedure

1. Choose the singular name. `tools.md` → `tool.kb/`.
2. `mkdir $singular.kb/`.
3. Each parallel section → `$singular.kb/$item-slug.md`. Preserve
   content verbatim; cleanup after.
4. Non-listing prose → `$singular.md` (parent synthesis file) or
   `$singular.kb/CLAUDE.md` (rules).
5. Write `$singular.kb/CLAUDE.md` if absent. Rules: what belongs,
   what doesn't, when to add.
6. Update inbound references.

## When to skip

Fixed 2-4 one-liners can stay flat. Signal is growth pressure.
