---
status: planning
scope: |
  All .kb/ directories whose entries are mutually-exclusive alternatives
  (one will be picked, others rejected). Renames `<slug>.kb/` →
  `<slug>.oneOf.kb/`. Updates inbound textual references across the
  owning repo.
why: |
  cardinality: and is the implicit default on every .kb (every entry's
  state/requirement holds simultaneously). OR-class kbs are the rare
  exception. The frontmatter field that previously marked them
  (cardinality: or) is almost-never-written, which makes it easy to miss
  or ignore; structural marking in the directory name is impossible to
  miss because every reference to the .kb shows the OR-ness lexically.

  Suffix chosen: `.oneOf.kb/`. JSON Schema pedigree (matches existing
  *.jsonschema.yaml tooling vocabulary), XOR-precise (cardinality "or"
  means exactly-one, which bare OR is ambiguous about), minimal break
  from the lowercase-kebab-case tree (single capital O).

  Convention decided 2026-05-26 during the rate-unrated-after-inventory-
  coverage-fix session arc.
---

# Add `.oneOf` suffix to OR-class kbs

The convention defaults every .kb to `cardinality: and`. OR-class kbs
opt out by name. This migration finds them and renames them.

## Algorithm

`validate.sh` scans `~/repo` and `~/.claude` for .kb/ directories whose
shape signals alternative-set semantics (one chosen, others
considered/rejected). It outputs candidates ranked by signal strength,
for human review. Read-only.

Signals (in order of strength):

1. **Strong (+3):** The kb's own `CLAUDE.md` says "currently chosen" /
   "which one is chosen" / contains "chosen / rejected / selected"
   vocabulary.
2. **Strong (+3):** The parent same-stem `.md` has `**Answer.**`,
   `## Why this one`, or `## Resolution` — the shape of a synthesis
   file that picks among alternatives.
3. **Medium (+2):** Entries carry status frontmatter `chosen | rejected
   | selected | considered`.
4. **Weak (+1):** Small entry count (2–6) — alternative sets are
   typically small.

Threshold for surfacing: signal sum ≥ 3.

Excluded basenames (always AND by convention):
`decision.kb`, `principle.kb`, `reference.kb`, `observation.kb`,
`verified-claim.kb`, `todo.kb`, `sessions.kb`, `ideas.kb`,
`migrations.kb`, `todo.d`, and anything already `*.oneOf.kb`.

`migrate.sh <kb-path>...` takes a confirmed list, runs `git mv` for
each `<slug>.kb` → `<slug>.oneOf.kb`, then updates inbound references
within the owning git repo via grep + sed on the directory basename.

## Pre-confirmed targets

Verified by hand 2026-05-26 — no review needed before applying:

- `prototype.chatfs/docs/dev/design.kb/040-design.kb/capture-pattern.kb/`
  — 5 entries (raw-cdp, network-events, inject-ui-read-dom,
  inject-ui-read-state, assisted-manual); network-events chosen per
  parent `capture-pattern.md`'s `**Answer.**` line.
- `prototype.chatfs/docs/dev/design.kb/040-design.kb/user-interface.kb/`
  — five mechanisms; fuse-mount chosen per parent's same shape.

Additional candidates from `validate.sh` require human review before
inclusion.

## Idempotency

- `validate.sh` is read-only and deterministic; safe to re-run.
- `migrate.sh` skips paths already at `.oneOf.kb` (no-op); skips
  missing paths (treats as already-done if dst exists); safe to re-run
  any number of times against any superset of the target list.

## Inbound-link handling

After rename, references like `[capture mechanisms](capture-pattern.kb/)`
or path-based citations break. `migrate.sh` does `grep -rlF | sed -i`
on the directory basename within the owning repo to catch them.

Risk: false-positive replacements if the basename appears in unrelated
contexts. Mitigation: the basenames used (`capture-pattern.kb`,
`user-interface.kb`) are specific enough that collisions are unlikely;
review the diff after running.

For tree-wide references that cross repo boundaries: the user's tree
keeps most kb references within the owning repo. Cross-repo refs are
rare and surface in `git status` of the other repos when the rename
happens; handle as follow-ups.

## Rollback

Not provided as a script. Before commit: `git mv` reverse and undo the
sed edits via `git checkout --`. After commit: `git revert` the
migration commit.

## Notes on the convention itself

The choice of `.oneOf` over alternatives:

- `.OR.` — ALL-CAPS breaks kebab-case dialect too hard; also ambiguous
  between inclusive-or (any subset) and exclusive-or (exactly one).
- `.any.` — lowercase reads naturally but loses visual distinctiveness;
  `any` is also overloaded with quantifier semantics.
- `.candidates.` — English gloss, longer than `oneOf`, no formal
  pedigree.
- `.alternatives.` — synonymous with `.candidates.`, longer still.

`oneOf` wins on precision (XOR), pedigree (JSON Schema), and minimum
visual break from the surrounding tree.
