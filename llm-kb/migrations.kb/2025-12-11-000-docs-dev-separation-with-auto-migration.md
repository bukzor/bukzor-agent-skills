---
status: in-progress
scope: |
  Skill projects following the llm-collab pattern: `docs/` becomes the
  user-facing documentation home (examples, guides, API docs);
  `docs/dev/` becomes the developer documentation home (adr/, devlog/,
  design.kb/, milestones.kb/). The `llm-collab-adr` and
  `llm-collab-devlog` scripts auto-migrate prior `docs/adr/` and
  `docs/devlog/` to their `docs/dev/` homes on first use.
originating-commits:
  - 7f7f261     # bukzor-agent-skills, 2025-12-11: Add docs/ vs docs/dev/ separation with auto-migration
why: |
  Mingling user-facing and developer-facing documentation under a
  single `docs/` directory makes it hard to point external readers at
  "the docs" without exposing implementation chatter (devlogs, ADRs,
  living design notes). The split reserves `docs/` for content with a
  publishing audience; `docs/dev/` for internal/development context.

  The auto-migration in `llm-collab-adr` / `llm-collab-devlog` is the
  forcing function: any project running these scripts post-2025-12-11
  silently lands the new layout. No manual sweep was needed.
---

# Separate docs/ (user-facing) from docs/dev/ (developer-facing)

## What landed

- ADR added in llm-collab documenting the `docs/dev/` pattern.
- `llm-collab-adr` and `llm-collab-devlog` scripts auto-migrate:
  - `docs/adr/` → `docs/dev/adr/` on first use
  - `docs/devlog/` → `docs/dev/devlog/` on first use
  - Try `git mv` first, fall back to `mv` for untracked files.

## Self-maintaining — but only for adopters

The migration is partially self-maintaining:

- New projects from the llm-collab skeleton start with the right
  layout.
- Existing projects auto-migrate the FIRST TIME `llm-collab-adr` or
  `llm-collab-devlog` runs in them.

But projects that don't run those scripts (or pre-date the
auto-migration and haven't run them since) keep the old layout
indefinitely. This includes any project that author docs/adr/ or
docs/devlog/ by hand.

## Drift verified 2026-05-26 — 10+ projects still on old layout

`find ~/repo ~/.claude ~/claude -type d \( -name adr -o -name devlog
\)` excluding `/docs/dev/` and trash returns 10+ matches:

- `ideation.graph-fs/docs/{adr,devlog}/`
- `bukzor-agent-skills/llm-subtask/docs/adr/`
- `bukzor-agent-skills/llm-kb/docs/adr/`
- `~/.claude/skills/mutation-testing/{adr,devlog}/` (top-level, not under docs/dev/)
- `~/claude/bukzor.samsung-debloat/docs/devlog/`
- `~/claude/fixing-claude-introspection/docs/devlog/`
- `~/claude/github-manager/docs/{adr,devlog}/`

The new `~/claude/` content (3 of those projects) was invisible to the
inventory until migration 009 extended the roots, so this drift was
hidden until today.

Note: `~/.claude/skills/mutation-testing/{adr,devlog}/` at top level
may be a different convention (skill-internal docs at skill root), not
the docs/{adr,devlog} drift. Review case-by-case.

## Algorithm

`validate.sh` (not yet written) would do:

```sh
find ~/repo/github.com/bukzor ~/.claude ~/claude -type d \
  \( -name adr -o -name devlog \) 2>/dev/null \
  | grep -vE '/docs/dev/|/trash/'
```

`migrate.sh` would `git mv docs/adr → docs/dev/adr` and
`docs/devlog → docs/dev/devlog` per project, then prompt for inbound
link updates. The auto-migration logic from `llm-collab-adr/devlog`
scripts handles the move; copying that logic into a one-shot is
straightforward.

## Why "in-progress" (re-downgraded 2026-05-26)

Initially marked `complete`; drift check found 10+ projects still on
the old layout. The auto-migration is only triggered by specific
scripts running; consumers that author docs/{adr,devlog}/ by hand
never auto-migrate.
