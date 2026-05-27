---
status: complete
scope: |
  Add `~/claude/` (no dot) to the ROOTS scanned by
  `~/bin/claude-open-tasks-list`. Existing ROOTS were `~/repo` and
  `~/.claude`; the user has real task surface under `~/claude/`
  (research.home-office, fixing-claude-introspection, github-manager,
  mitmproxy, and others) that was invisible to the inventory.
why: |
  Discovered 2026-05-26 during back-annotation of prior migrations:
  `~/claude/` task files (`.claude/todo.md`, `.claude/todo.d/*.md`,
  `.claude/todo.kb/*.md`) were filesystem-resident but inventory-
  invisible, so they didn't participate in WSJF ranking, weren't
  flagged by drift-detector migrations whose validators dispatch
  through `claude-open-tasks-list`, and silently dropped from
  prioritization.

  Fixing the inventory root is the upstream fix; all consumer
  validators inherit the correction automatically.
---

# Extend inventory roots to include ~/claude/

## Change

`/home/bukzor/bin/claude-open-tasks-list`:

```python
# Before
ROOTS = (Path.home() / "repo", Path.home() / ".claude")

# After
ROOTS = (Path.home() / "repo", Path.home() / ".claude", Path.home() / "claude")
```

## Surfaced after change

Previously-invisible task files now appear in `claude-open-tasks-list`:

- `~/claude/research.home-office/.claude/todo.md`
- `~/claude/fixing-claude-introspection/.claude/todo.d/*.md`
- `~/claude/github-manager/.claude/todo.md`
- `~/claude/mitmproxy/.claude/todo.kb/*.md`
- ...and others under sibling subprojects.

These are now visible to `wsjf-rank`, will surface as `unrated` until
rated, and feed into all migration validators that use the inventory
as their file source.

## Algorithm

One-line code change in the inventory script. Not migrate-able as
data; it's a tool change.

## Idempotency

Trivially idempotent: the change either is or is not in place. Future
sessions inherit the inventory's broader scope automatically.

## Why "complete" not "verified"

Change landed in `~/bin/claude-open-tasks-list`; spot-checked output
shows `~/claude/` content surfaces. Verification would be a sweep:
diff the inventory before/after against the actual filesystem
contents under `~/claude/` to confirm all task files surface.

## Cascading implications

The migrations whose validators dispatch through
`claude-open-tasks-list` (001 time-period-nesting, 002 effort/wallclock,
003 bullet-bracketed, 007 confidence-band) now see `~/claude/`
content as part of their scope. Re-running their validators will
report drift in `~/claude/` files that weren't visible before.
