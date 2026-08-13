# Devlog: 2026-07-06 — Fix docs/dev migration drift in session-start and file-type docs

## Focus

`.claude/todo.kb/2025-12-11-000-Update-skeleton-to-match-docs-dev--pattern-from-git-partial.md`
proposed a 3-hour skeleton overhaul, but most of it had already landed
in an untracked earlier pass. Verifying against the actual skeleton on
disk (not the stale checklist) surfaced the real, narrower gap: three
places were never updated when `docs/adr`/`docs/devlog` moved to
`docs/dev/adr`/`docs/dev/devlog`.

## Decisions

### Fix the stale readers, don't re-do the already-done move

`llm-collab-init`, `llm-collab-adr`, and `llm-collab-devlog` all
already create/migrate to `docs/dev/{adr,devlog}`. But
`bin/llm-collab-session-start` still read from the pre-migration
`docs/adr`/`docs/devlog` paths — so on every project `llm-collab-init`
produces today, it silently showed zero devlog/ADR context, and its
"Quick commands" output named nonexistent scripts (`new-adr.sh` etc.)
instead of the real `llm-collab-adr`/`llm-collab-devlog`/`llm-subtask-todo`.
`references.kb/file-types.kb/ADRs.md` and `devlog.md` had the same
stale-path drift. Fixed all in place rather than re-verifying/redoing
the move itself, which was already correct.

**Alternatives considered:** Re-running the full todo's "Implementation
Steps" checklist top to bottom. Rejected — most steps described work
already done; doing so would have re-created already-correct
structure and obscured what was actually broken.

### Remove `skeleton/docs/dev/devlog/README.md`

Stale leftover with a static "Recent Entries: None yet" that
contradicted the CLAUDE.md-is-canonical, ls-is-source-of-truth
convention already in effect for every sibling dir (`adr/`, `design/`,
`technical-policy.kb/` all have only a `CLAUDE.md`, no `README.md`).
`TESTING.md`'s skeleton integrity check never expected it either.
Deleted rather than updated.

### `docs/milestones/` → `docs/dev/milestones.kb/` in ROADMAP.md

Initially mis-filed this as an open pattern question. It isn't — the
ADR (`docs/dev/adr/2025-12-11-001-...`) and `llm-kb`'s migration entry
both already name `docs/dev/milestones.kb/` as the destination,
parallel to `design.kb/`. Only `references.kb/file-types.kb/ROADMAP.md`
still pointed at the old `docs/milestones/`. Fixed the reference; the
skeleton directory/template for `milestones.kb/` itself still doesn't
exist and is separate, real implementation work, left open.

### Fixed `llm-collab-adr`/`llm-collab-devlog` sed delimiter bug

Discovered live: `llm-collab-devlog "Fix docs/dev migration drift..."`
failed with `sed: unknown option to 's'` and left a 0-byte devlog file,
because the title contains `/` — the same character `sed -e
"s/TITLE/$TITLE/g"` uses as its delimiter. Same bug existed in
`llm-collab-adr`'s title substitution. Fixed both by reading the
template into a bash variable and using `${var//pattern/replacement}`
parameter expansion instead of `sed` — per this repo's own
`~/.claude/reference.kb/bash-conventions.md` ("Simple substitution:
parameter expansion, not sed"), and it sidesteps the delimiter problem
entirely since bash substitution doesn't treat `/` in the replacement
as special. Verified both scripts against titles containing `/`.

## Conventions Established

- When a todo file's checklist looks daunting, verify against the
  actual filesystem state before executing it — drift between planned
  and actual work is common in this repo's multi-session workflow, and
  the real remaining gap is often much smaller than the checklist
  implies.
- Prefer bash parameter expansion (`${var//a/b}`) over `sed` for
  substituting user-supplied text (like a devlog/ADR title) into a
  template — user text can contain the delimiter.

## Open Questions

- Should `skeleton/docs/dev/milestones.kb/` actually get built (template
  + `llm-collab-init` wiring), or is that deferred until a real
  consumer (e.g. prototype.chatfs) needs it?

## References

- `llm-collab/.claude/todo.kb/2025-12-11-000-Update-skeleton-to-match-docs-dev--pattern-from-git-partial.md`
- `llm-collab/docs/dev/adr/2025-12-11-001-separate-user-facing-and-developer-facing-documentation.md`
- `llm-kb/migrations.kb/2025-12-11-000-docs-dev-separation-with-auto-migration.md`
- `~/.claude/reference.kb/bash-conventions.md`
