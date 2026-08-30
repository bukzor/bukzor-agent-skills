---
label: RENAME
standing: agent
todo: true
why:
  - the-record-lives-under-docs-dev.md
  - old-towers-stay-legal.md
---

# The Older Ledgers Take Bare Subject Tokens

The six ledgers minted before the naming rule carry bare subject
tokens: `<scope>/claims.kb/design.kb/`, not
`<scope>/claims.kb/design.claims.kb/`, with each `.md` and
`.jsonschema.yaml` renamed to match.

- `docs/dev/claims.kb/` -- `design.claims.kb/` and `strata.claims.kb/`
- `deformalize/claims.kb/`, `formalize/claims.kb/`,
  `llm-claims/claims.kb/`, `llm-kb/claims.kb/` -- `design.claims.kb/`
  apiece

Both forms are legal meanwhile, on LEGACY's warrant and for the same
reason: a naming rule is not worth a flag day. Internal `why:` arrows
are file-relative and survive a directory rename untouched, so what a
sweep actually repairs is prose references, `skill://` paths, and the
two-hop `$ref` chains -- roughly 243 lines across 120 files. Devlogs
and ADRs keep the old name as provenance rather than being swept,
which is `Skill(llm-claims-kb)`'s rename rule, not an exception to it.

The route is
`../../../../../../.claude/todo.kb/2026-08-29-000-Rename-the-bare-claims-kb-children-to-bare-subject-tokens.md`,
which carries the per-ledger commit plan and the two code paths that
name these directories literally
(`llm_claims_kb/ledger.py`, `ownership.py`).

Deliberately not done in the pass that ruled it. A 120-file mechanical
rename in the same diff as the reform would have buried the reform, and
nothing depends on the new names: the old ones are legal, correct, and
only cosmetically redundant. The declined alternative was to rename
first and reform second, which trades the same burial in the other
direction and puts the wide, boring change ahead of the one with
rulings in it.
