---
status: in-progress
scope: |
  All frontmatter blocks where ownership was previously declared via
  the `<anthropic-skill-ownership .../>` XML tag or the
  `anthropic-skill-ownership:` YAML key. Replace with
  `managed-by: Skill(<skill-name>)`.
originating-commits:
  - 9c4342f      # bukzor-agent-skills, 2026-05-18: Migrate ownership marker
  - c61191c      # bukzor-agent-skills, 2026-05-21: todo,ideas: migrate frontmatter
why: |
  Files managed by a skill declare ownership via YAML frontmatter:
  `managed-by: Skill(<skill-name>)`. The JSON Schema validates this
  with a const, turning agent write-time validation into the forcing
  function for the convention. Replaces both the legacy YAML key
  `anthropic-skill-ownership` and the legacy XML tag
  `<anthropic-skill-ownership ... />`.

  Originating commit 9c4342f (2026-05-18) swept the bukzor-agent-skills
  repo. Some files outside that scope, plus a handful inside, still
  carry the legacy XML-tag form.
---

# Migrate ownership marker: HTML tag / legacy YAML key → managed-by

## Drift verified 2026-05-26

`validate.sh` (anchored `^<anthropic-skill-ownership` to exclude
prose mentions) finds ~12 active task files still carrying the
legacy tag form across `~/repo/github.com/bukzor`, `~/.claude`, and
`~/claude/`. Run `validate.sh` for the live list. Representative
examples:

- `bukzor-agent-skills/.claude/todo.kb/2026-01-02-000-skill-evolution-for-chatfs-harmonization.md`
- `bukzor-agent-skills/llm-must-read-kb/.claude/todo.kb/2026-05-15-000-must-read-slash-command.md`
- `prototype.chatfs/.../todo.kb/*.md` (several)
- `prototyping.hearts-2025/packages/engine/.claude/todo.d/2025-12-17-002-immutability-refactor.md`
- `claude/research.home-office/.claude/todo.md`
- `claude/github-manager/.claude/todo.md`

**Excluded from migration (intentional):**

- `docs/dev/adr/*` — ADRs describe the historical convention; rewriting
  them would falsify the history they document.
- `.claude/projects/*.jsonl` and `.claude/file-history/*` — immutable
  session transcripts / Claude Code backups; out of scope.
- `trash/*` — backup folders.
- `migrations.kb/*` — this entry itself discusses the convention.
- `*.swp` — vim swap files.

## Algorithm

`validate.sh` greps for `<anthropic-skill-ownership` across inventory
roots, excluding `*/docs/dev/adr/*` (historical) and
`*/.claude/projects/*` (session logs).

`migrate.sh` is not provided — the transformation requires removing the
HTML tag block and adding a `managed-by:` line in YAML frontmatter,
which means restructuring around any existing frontmatter delimiters.
Easier done by hand with the small known list above than via a generic
regex.

Manual recipe per file:

1. Remove the `<anthropic-skill-ownership SKILL />` HTML tag line.
2. Ensure frontmatter `---` fences exist (add if absent).
3. Add `managed-by: Skill(SKILL)` inside the frontmatter, alongside
   any existing keys.

## Idempotency

`validate.sh` is read-only. The manual migration is naturally
idempotent — once the HTML tag is gone and the YAML key is present,
re-running the steps is a no-op.

## Why "applying" not "applied"

Two known active files still carry the legacy form. Until they're
migrated, the convention isn't uniform across the user-owned skill
tree, and the JSON Schema's `managed-by` const can't be a forcing
function for new writes (because the legacy syntax slips through).
