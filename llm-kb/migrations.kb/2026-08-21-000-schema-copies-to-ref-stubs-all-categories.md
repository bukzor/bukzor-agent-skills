---
status: in-progress
kind: one-shot
scope: |
  Every full-copy `*.jsonschema.yaml` anywhere in the user's tree whose
  category already has a published canonical. Generalizes the 2026-07-07
  migration, which hardcoded exactly two categories (`todo`, `ideas`).
  The category table is data, not code:

      todo, ideas            -> skill://llm-subtask/jsonschema/
      claim                  -> skill://llm-claims-kb/jsonschema/
      technical-policy       -> skill://llm-design-kb/jsonschema/
      the discourse quintet  -> skill://llm-discourse-graph/jsonschema/

  Each in-scope file becomes the one-line stub:

      # yaml-language-server: $schema=https://json-schema.org/draft-07/schema
      $ref: "skill://<skill>/jsonschema/<category>.jsonschema.yaml"

  Excluded: categories with no canonical yet (design-kb layer entries,
  `~/.claude/sessions`) -- nothing to point at, see the related todo.
  Excluded: files that diverged on purpose; report, do not rewrite.
depends-on:
  - 2026-07-07-000-schema-copies-to-ref-stubs.md
related-todo: ~/.claude/skills/llm-kb/.claude/todo.kb/2026-08-21-000-ref-rollout-beyond-todo-ideas.md
why: |
  The 2026-07-07 sweep proved the transformation and left the scope
  boundary in the scripts. A 2026-08-21 homedir survey (309 schema files)
  found that the copy pattern survives exactly where that boundary fell:
  ~35 full copies across five categories that each already have a
  canonical. Same transformation, wider table -- so this is one entry
  parameterized by category, not one entry per category.

  Copying hid three outright errors, which is the sharper argument than
  DRY: ideation.physical-musings' todo copy admits `in-progress`, a
  status the canonical deliberately omits; two claim copies predate the
  verdict field; template.python-project mints a stale snapshot into
  every repo initialized from it.
---

# Schema copies to $ref stubs, all categories

## Transformation

Identical to `2026-07-07-000-schema-copies-to-ref-stubs`: classify each
in-scope file as `SNAPSHOT` (byte-identical to some historical canonical
blob), `STALE-REF` (stub pointing at a superseded path), or `DIVERGED`
(matches nothing -- human judgment). Rewrite the first two; report the
third. Idempotent: a conforming stub reclassifies as `SNAPSHOT` of the
current blob and its rewrite is a byte-identical no-op.

The one change is that scope comes from a category table rather than two
hardcoded globs. Generalize `../2026-07-07-000-schema-copies-to-ref-stubs/`
in place of copying it -- a second copy of that script is the same
pathology this migration exists to remove.

## Expected DIVERGED set

The drifted discourse copies will all report DIVERGED. That is correct
behavior, not a gap: each needs a read to decide stale-vs-intentional, and
an intentional one should become a `#base` extender rather than a stub.
Tracked in the related todo, not here.

Outcome: 14, not the 12 forecast, and not all discourse -- 10 discourse,
2 `todo`, 2 `technical-policy`. The forecast assumed `todo` and
`technical-policy` were settled; they were not. Listed below.

## Prerequisite: canonicals must be extendable

`llm-design-kb/jsonschema/technical-policy.jsonschema.yaml` is draft-07
with `additionalProperties: false` at the document root and no
`$defs.base` / `#base` anchor. Stubs onto it resolve fine, but a consumer
with one extra field then has no legal way to extend and stays DIVERGED
forever. Convert it to the two-entry-point form -- strict root
`$ref: "#/$defs/base"` + `unevaluatedProperties: false`, open `#base`
`$anchor` -- before or during this migration, and check every canonical
in the table for the same shape.

## On finishing

When the generalized `validate.sh` runs clean homedir-wide, widen
`2026-05-15-000-schema-propagation-from-canonical`'s scope from
`.claude/{todo,ideas}.kb/` to every category in this table -- its recurring
guard is what keeps this migration from needing a sequel.

## Applied so far

- 2026-08-21, prerequisite: six canonicals converted to the two-entry-point
  form, not the one this entry named. `technical-policy` had the defect and
  so did the entire discourse quintet -- same draft-07 closed root, same
  `additionalProperties: false`, same missing `#base`. `llm-claims-kb/claim`
  and `llm-subtask/{todo,ideas}` already conformed. All nine now report
  `CANON-OK`. The conversion is semantics-preserving: for each affected
  project, `llm.kb-validate` gave identical error counts with the six
  canonicals stashed and restored.
- 2026-08-21, homedir sweep: 18 files stubbed across 7 projects
  (bukzor-packaging, meta-reasoning, mitmproxy, summer-programming-project,
  ideation.epistemics, ideation.physical-musings,
  prototype.personal-reasoning-management). Zero `STALE-REF` anywhere --
  the 2026-07-07 repoint left none behind. Final census: 69 `OK`,
  2 `ALIAS`, 1 `EXTENDER`, 9 `CANON-OK`, 14 `DIVERGED`.
- Idempotency confirmed as required: `migrate.sh` run a second and third
  time produced no output, and the two `validate.sh` reports were
  byte-identical.
- Toolchain fix, **outside this migration's brief**, in another repo, and
  left uncommitted there where a reviewer of this effort will not think to
  look: `~/repo/github.com/bukzor/2026-05-19--task-archeology/lib/python/bukzor_homedir_archeology/cli.py`.
  `bukzor-homedir-archeology find -name X` was unusable -- argparse
  rejects `-name` as an unknown option before `REMAINDER` can collect it,
  and passing `--` leaked the `--` into the `find` expression. The
  subcommand now dispatches ahead of parsing. `validate.sh` depends on
  this; without it there is no homedir sweep.

Not copied from 2026-07-07: `validate.sh` and `migrate.sh` here *subsume*
that pair, whose scope -- `todo` and `ideas` under `~/repo` -- is two rows
of `categories.tsv`. Nothing was factored out of the completed entry,
which stays exactly as it was executed; its record must stay true.

Two classes the transformation model lacked, both found by reading
supposedly-DIVERGED files:

- `ALIAS` -- category is the basename, but the basename is not always the
  category. `questions.jsonschema.yaml` inside a `*.claims.kb/` names a
  claim-ledger collection, not the discourse-graph category; it already
  `$ref`s its own `claim` schema and this migration has no business there.
- `EXTENDER` -- a `$ref` at the canonical's `#base` plus local fields is
  the *prescribed* shape for a consumer with extra fields, so it must
  report conforming, not as a copy to overwrite.

`incident-forensics/` is excluded in `excluded-prefixes.txt` because
migration B owned it concurrently. The exclusion cost nothing: it hides
exactly one in-scope file, `incident-forensics/skeleton/todo.jsonschema.yaml`,
and a read-only check shows that file is already the conforming stub --
it would have reported `OK`. B's six schemas are `evidence`, `findings`,
`remediations`, `reports`, `root-cause`, `timeline`: no basename in this
migration's table. The two migrations never overlapped. The exclusion can
be dropped once B is committed.

## Residual: DIVERGED (14, untouched)

Reported, never rewritten -- each needs a human read.

Genuinely local intent:

- `dotfiles/.claude/todo.jsonschema.yaml` -- a 7-field subset; drops
  `status`, `managed-by`, `blocked-by`, `closeout`, the reading fields.
- `ideation.physical-musings/.claude/todo.jsonschema.yaml` -- adds
  `in-progress` and `deferred` to `status`, which the canonical omits
  on purpose. Already the sole residual of the 2026-07-07 sweep.
- `ideation.epistemics/{claims,deductions}.jsonschema.yaml` -- a rival
  epistemic vocabulary: `certified`/`stipulated` in place of `status`
  and `likelihood`.
- `prototype.chatfs/.../chatfs-cli-mockup/dev.kb/claims.jsonschema.yaml`
  -- an observation ledger, not a discourse claim: `evidence`,
  `first-recorded`, `last-checked`, `previously-claimed`, and a
  `status` enum of `observed`/`settled`/`refuted`.
- `ideation.physical-musings/docs/dev/claims.jsonschema.yaml` -- adds
  `ratified`.
- `ideation.physical-musings/docs/dev/{sources,technical-policy}.jsonschema.yaml`
  -- pre-`source` technical-policy; `kind` enum differs on sources.

Stale snapshots that drifted cosmetically, so they match no blob --
strongest stub candidates once someone confirms:

- `template.python-project/discourse.kb/{definitions,questions}.jsonschema.yaml`
  -- semantically identical to canonical; differ only in dialect and
  description line-wrapping.
- `template.python-project/discourse.kb/{claims,deductions,sources}.jsonschema.yaml`
  -- one field behind (`sources` shape, missing `sources`, `kind` enum).
- `template.python-project/docs/dev/technical-policy.jsonschema.yaml` --
  predates `source`.

This is the same template that minted a stale `todo` snapshot in 2026-07-07;
six more of its files are the single largest cluster here.

## Found along the way, not acted on

The em-dash migration (`2026-05-21-000`) has drifted back into the
canonical schemas themselves: `llm-subtask/jsonschema/todo.jsonschema.yaml`
has five, and six of the descriptions in the discourse quintet,
`technical-policy`, and `claims` carry one. Rewriting a canonical's bytes
is a wider blast radius than this migration's, so it is left for that
entry's own sweep.
