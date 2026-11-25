---
managed-by: Skill(llm-subtask)
status: open
required-reading:
  - CLAUDE.md
  - ../../../llm-kb/migrations.kb/CLAUDE.md
  - ../../../llm-kb/migrations.kb/2026-11-25-001-skill-kb-quality-passes-and-reference-kb.md
  - ../../../docs/dev/claims.kb/design.claims.kb/authorship.kb/each-skill-keeps-passes-occasions-and-a-sweep.md
  - ../../../docs/dev/claims.kb/design.claims.kb/authorship.kb/the-pass-collection-is-quality-passes.md
  - ../../../docs/dev/claims.kb/design.claims.kb/authorship.kb/skill-kb-is-a-collection-of-kbs.md
  - ../../../docs/dev/claims.kb/design.claims.kb/authorship.kb/reference-docs-live-in-skill-kb-reference-kb.md
  - ~/.claude/must-read.kb/before/writing-bash-scripts.md
---

# `skill.kb/` layout: apply migration 2026-11-25-001

**Parent:** <https:../2026-11-25-000-Quality-passes-for-claim-ledgers.md> (wave
1, the mechanical move)

## Problem Statement

Apply the migration entry above to the whole repo: write its `migrate.sh` and
`validate.sh` in the sibling directory
`llm-kb/migrations.kb/2026-11-25-001-skill-kb-quality-passes-and-reference-kb/`,
run them, and advance the entry's `status:` to the most-advanced true stage
(`verified` is the target). Later waves write new passes, sweeps and triggers
at the new paths, so the paths themselves are the interface they consume.

Decisions already made:

- Moves, each a `git mv`:
  - `llm-kb/skill.kb/self-audit.kb/` → `quality-passes.kb/`, `self-audit.md` →
    `quality-passes.md`, `procedures.kb/run-self-audits.md` →
    `run-quality-passes.md`;
  - `llm-claims-kb/skill.kb/self-audit.kb/` → `quality-passes.kb/`;
  - `llm-design-kb/skill.kb/principles.kb/` → `quality-passes.kb/`, as a
    rename only. Recasting its entries as passes is wave 4's.
  - `references/` at the root of `llm-kb`, `llm-subtask`, `llm-must-read-kb`,
    and the loose `align/skill.kb/sort-goals-into-four-bins.md`,
    `llm-claims/skill.kb/theories.md`, `persist-clarity/skill.kb/persistence.md`
    → that skill's `skill.kb/reference.kb/`. Each new collection gets the
    `CLAUDE.md` that `llm-kb` asks of a new collection.
- Readers: rewrite every live reader of an old path -- `SKILL.md` bootstraps
  and mentions, `must-read.kb/` entries, `CLAUDE.md`s, relative links inside
  moved files, `skill://` URIs, code strings
  (`llm-kb/lib/python/llmd/frontmatter_validate.py`,
  `llm-claims-kb/lib/python/llm_claims_kb/ownership.py`), live ledgers
  including the fleet ledger, and open todo items. Leave frozen records alone
  (`CLAUDE.md` of this kb lists them).
- Vocabulary: where "self-audit" names the collection or an item in it, it
  becomes "quality pass" (`PASS_NAME`). Leave "audit" as an ordinary verb.
- `validate.sh` reads the entry's check literally, except that a schema
  sibling (`*.jsonschema.yaml`) in `skill.kb/` is not a loose file. Grep for
  old paths outside frozen records, not everywhere.
- Out-of-repo readers: grep the other repos under `~/repo/github.com/bukzor/`
  and `~/.claude/` (minus `skills/`, which symlinks here) for old paths.
  List them in the Final report; don't edit them.

**Scope (only these files):** the moved paths; each live reader of an old path
in this repo, except the parent plan, this kb, and files already dirty or
untracked; the migration entry and its sibling directory.

## Steps

## Decisions

## Open Questions

## Final report
