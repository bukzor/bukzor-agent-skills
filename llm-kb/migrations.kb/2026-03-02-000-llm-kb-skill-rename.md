---
status: in-progress
scope: |
  Skill name and references: `llm.kb` → `llm-kb`. Triggered by the
  Agent Skills spec which requires kebab-case skill names (no `.` in
  the identifier).
originating-commits:
  - 71b6fca     # bukzor-agent-skills, 2026-03-02: Rename llm.kb skill to llm-kb for Agent Skills spec compliance
why: |
  The Agent Skills specification requires kebab-case skill identifiers
  with no `.` in the name. The original `llm.kb` skill name fit the
  naming style of its `.kb/` content but violated the spec. Renaming
  to `llm-kb` brought it into compliance.

  Inbound references — in other skills, agent config, the skill
  symlink under `~/.claude/skills/`, etc. — were updated as part of
  the same commit. New references all use the new name.
---

# Skill rename: llm.kb → llm-kb

## Why "in-progress" (re-downgraded 2026-05-26)

Initially marked `complete`; a drift check showed 20+ active
references to `Skill(llm.kb)` or `~/.claude/skills/llm.kb/` across
consumer projects that the original sweep did not catch. The skill
directory itself was renamed at the source (71b6fca), but consumer
references in OTHER repos were not swept.

**Active drift** (representative; live list from validate.sh):

- `prototyping.hearts-2025/CLAUDE.md` and `docs/CLAUDE.md` — frontmatter `requires:` still uses old name
- `traceman.research/CLAUDE.md`
- `bukzor.garden/packages/sttt-engine/.claude/settings.local.json` + design.kb CLAUDE.md files (8 references)
- `bukzor.garden/apps/super-tictactoe/docs/dev/mutation-testing.kb/CLAUDE.md`
- `git-partial.prototyping/.claude/settings.local.json` (3 references including `~/.claude/skills/llm.kb/bin/llm.kb-validate`)
- `private.bukzor-llc/.claude/settings.local.json` (hardcoded `complete-example` exploration path)
- `scratch.vim-work/CLAUDE.md`
- `prototype.chatfs/.claude/todo.kb/2026-01-02-002-apply-skill-conventions-post-evolution.md`
- `bukzor-agent-skills/llm-collab/.claude/todo.kb/2025-12-11-000-Update-skeleton-to-match-docs-dev--pattern-from-git-partial.md`
- `bukzor-agent-skills/llm-kb/.claude/todo.kb/2026-01-02-000-complete-d-to-kb-rename.md` (the skill's own todo!)

## Algorithm

`validate.sh` greps for `Skill\(llm\.kb\)` or `skills/llm\.kb/` paths
across inventory roots, excluding ADRs/devlogs/sessions (historical),
trash/, migrations.kb/, and Claude Code projects/file-history dirs.

`migrate.sh` is a careful sed-replace per file (s/Skill(llm.kb)/Skill(llm-kb)/g
and s|skills/llm.kb/|skills/llm-kb/|g), gated by user confirmation
because settings.local.json files have permission grants that should
be reviewed before sweeping.

Pre-confirmed pure-rename consumers (settings.local.json should be
reviewed):

- Top-level `CLAUDE.md` `requires:` references in user-owned project repos
- design.kb/ `CLAUDE.md` `requires:` references

## Notes

- The skill's directory pattern is still `*.kb/` — that's the
  knowledge-base convention, distinct from skill identifiers.
- The Agent Skills spec naming applies only to the skill identifier
  itself, not to its internal directory structure.
