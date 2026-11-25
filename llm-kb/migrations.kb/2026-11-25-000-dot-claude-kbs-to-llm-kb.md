---
status: tentative
scope: |
  Every `.claude/*.kb` collection and its synthesis file, in `~` and in every
  repo of bukzor's: `todo.md`/`todo.kb/`, `ideas.kb/`, `must-read.md`/
  `must-read.kb/`, `sessions.kb/`, `reference.kb/`, and their schemas. They
  move to `llm.kb/*.kb` at the same root. Claude Code's own `.claude/` files
  (`settings*.json`, `commands/`, `agents/`, `skills/`, `projects/`) stay.
why: |
  `.claude/` is Claude Code's configuration directory, and the collections in
  it are a vendor-neutral convention of this fleet living in one vendor's
  namespace, where the next directory Claude Code adds can collide with them.
  `llm.kb/` is an honest collection of kbs, and it aligns each collection with
  its skill: `llm.kb/todo.kb` with `llm-todo` (`llm-subtask` renamed),
  `llm.kb/claims.kb` with `llm-claims-kb`.
---

# `.claude/*.kb` to `llm.kb/*.kb`

Tentative: bukzor may schedule it (59b55f01, 2026-11-25). This entry is what
scheduling needs.

## Open questions

- [ ] Symmetry with the vendor-neutral `CLAUDE.md`, which is `AGENTS.md`: keep
      `llm.kb/` (aligns with the `llm-*` skills), or `agents.kb/` (aligns with
      `AGENTS.md`)? And does `CLAUDE.md` itself move to `AGENTS.md`, with a
      `CLAUDE.md` that points there?
- [ ] Rename `llm-subtask` to `llm-todo` in the same migration, or apart?

## Before scheduling

- [ ] Inventory the roots: `migrations.kb/2026-05-26-009-extend-inventory-roots-to-include-claude-dir.md`
      already extended the inventory to `.claude/`; reuse it to list every
      repo with a `.claude/*.kb`.
- [ ] Route every reader (`ROUTING`). Tools that hardcode the old paths, as of
      2026-11-25: in this repo `claude-code-archeology/bin/dead-sessions`,
      `llm-collab/bin/llm-collab-session-start`, `llm-kb/bin/llm.kb-validate-links`,
      `llm-subtask/bin/llm-subtask-{idea,init,todo}`, and two migration
      `validate.sh`; in `~/bin` `claude-open-tasks`, `claude-open-tasks-list`,
      `claude-rename`, and `llm-must-read-ls`. Each reads both locations until
      the sweep is verified.
- [ ] Prose readers: every `CLAUDE.md`, `SKILL.md`, skill skeleton, and trigger
      naming a `.claude/*.kb` path; `~/.claude/CLAUDE.md`'s trigger bootstrap
      (`must-read://~`).
- [ ] Write `migrate.sh` (`git mv` per repo, then a path sweep) and
      `validate.sh` (no `.claude/*.kb` left; no reader names one).
