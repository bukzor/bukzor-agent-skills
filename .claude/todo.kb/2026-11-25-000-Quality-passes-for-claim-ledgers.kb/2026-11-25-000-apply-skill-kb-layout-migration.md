---
managed-by: Skill(llm-subtask)
status: done
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

- [x] Moves (`git mv`): the three `self-audit`/`run-self-audits` paths,
      `principles.kb`, three skills' `references/`, three loose reference files
- [x] `CLAUDE.md` in each of the six new `reference.kb/`
- [x] Readers: SKILL.md, must-read entries, CLAUDE.md files, in-file relative
      links, `skill://` and code strings, fleet ledger, open todos
- [x] Vocabulary: "self-audit" to "quality pass" where it names the collection
- [x] `migrate.sh`, `validate.sh`, `old_paths.py` written and run
- [x] Entry `status:` to `complete`; checks run; committed

## Decisions

- `complete`, not `verified`: `validate.sh` exits 1 on one finding that predates
  this unit and lies outside the brief's scope (Open Questions).
- `old_paths.py` is the one definition of "live reader", shared by
  `migrate.sh` (rewrite) and `validate.sh` (report), so a clean report is
  `rewrite`'s postcondition. Not live: devlogs, ADRs, case studies, other
  migrations, the replication run, this kb and the parent plan, the fleet
  ledger's note on the declined name `self-audit.kb`, todos with
  `status: done` (and the `.kb/` beside them), `- [x]` items with their
  continuation lines.
- Relative links: `skill.kb/` renames keep depth; files moved into
  `reference.kb/` gained one level (`creating-a-new-kb.md`, `persistence.md`).
- `llm-must-read-kb/SKILL.md`'s layout sketch put `self-audit.kb/` under
  `procedures.kb/` with `audit-` filename prefixes; redrawn as a sibling,
  prefixes dropped.
- `llm-kb/skill.kb/CLAUDE.md`: deleted "does not belong: references ->
  `references/`" (the collection now lives inside `skill.kb/`). `align`'s
  `skill.kb/CLAUDE.md` no longer calls the moved file a procedure.

## Open Questions

- `llm.kb-validate-links` flags
  `llm-collab/skill.kb/must-read.kb/before/writing-an-ADR-or-devlog-entry.md`
  (backticked `../../..`, a directory without trailing slash, read as a file).
  Out of scope; `../../../` clears the last `validate.sh` finding and lets the
  entry reach `verified`.
- Untouched, dirty before I started: `llm-kb/docs/dev/adr/2026-05-18-000-skill-uri-scheme.md`,
  `subagent-handoffs/*`; neither held an old path that needed a change.

## Final report

New homes: `llm-kb/skill.kb/quality-passes.kb/` (+ `quality-passes.md`,
`procedures.kb/run-quality-passes.md`), `llm-claims-kb/skill.kb/quality-passes.kb/`,
`llm-design-kb/skill.kb/quality-passes.kb/`, and `skill.kb/reference.kb/` in
`llm-kb`, `llm-subtask`, `llm-must-read-kb`, `align`, `llm-claims`,
`persist-clarity`. Scripts: `llm-kb/migrations.kb/2026-11-25-001-skill-kb-quality-passes-and-reference-kb/`.

Checks: `llm.kb-validate` 855 files 0 errors; `llm-triggers-lint llm-kb` clean;
link check shows no new errors (43 files with older broken links, none from
this move; one in a `skill.kb/` tree, above). Tests: `llm-claims-kb` 19 pass;
`llm-kb` 39 pass, 2 fail on `=` in the sandbox tmp path, unrelated.

Out-of-repo readers (not edited): `~/repo/github.com/bukzor/ideation.epistemics/`
`background.kb/prior-art.kb/bukzor.kb/llm-subtask-marker-commands.md:26` and
`acs-counterfactual.kb/incumbent-inventory.md` (cites `llm-kb/references/*`,
`run-self-audits.md`, `self-audit.kb/`); frozen devlogs in
`private.meta-reasoning-corpus` (`2026-08-29-002-*`) and `prototype.llm-postbox`
(`2026-08-31-000-*`). Nothing in `~/.claude/` outside `skills/` and history.
