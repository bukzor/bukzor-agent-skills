---
managed-by: Skill(llm-subtask)
status: open
required-reading:
  - ~/.claude/skills/llm-kb/references/schema-reuse.md
  - ~/.claude/skills/llm-kb/migrations.kb/2026-07-07-000-schema-copies-to-ref-stubs.md
suggested-reading:
  - ~/.claude/skills/llm-kb/.claude/todo.kb/2026-02-09-000-schema-reuse-with-ref.md
related-effort: ~/.claude/skills/llm-kb/.claude/todo.kb/2026-02-09-000-schema-reuse-with-ref.md
cost-benefit-sweh:
  timebox:
    "@value": 4.0
    rationale: |
      Two mechanical migrations (~1h each, scripts generalize from the
      2026-07-07 sibling) plus one genuine schema design (layer-entry,
      ~2h and wants frontier reasoning). Past 4h the remainder is
      per-file judgment on 12 drifted discourse copies, which belongs to
      whoever owns those projects, not to this effort.
    confidence: unsure
  benefit-2w:
    "@value": 2.0
    rationale: |
      ~35 full schema copies collapse to stubs. The immediate payoff is
      the three known-wrong files that copying hid: `in-progress` in
      ideation.physical-musings' todo enum (a status the canonical
      deliberately omits), the verdict-less claim schemas, and
      template.python-project minting a stale snapshot into every new
      repo.
    confidence: confident
  cost-of-delay-2w:
    "@value": 0.5
    rationale: |
      Drift is slow here -- these categories see few schema edits. The
      real cost accrues per new project initialized from a template or
      skeleton carrying a full copy, which is maybe one event per two
      weeks.
    confidence: unsure
---

# Finish the `$ref` rollout beyond todo/ideas

The 2026-02-09 effort (now `done`) built `$ref` resolution, wrote the
house rules in `references/schema-reuse.md`, and swept exactly two
categories: `todo` and `ideas`. This is its sequel, not a reopening.

A 2026-08-21 homedir survey (`uv run homedir-archeology jsonschemas`, 309
files) found seven clusters still on the pre-`$ref` copy pattern. They are
precisely the complement of the 2026-07-07 sweep's hardcoded scope --
which is the finding: this is an unfinished rollout, not a design problem.
Five of the seven had a published canonical already and need only
mechanical stubbing. Two needed a canonical designed; cluster 1's was
designed on 2026-08-21 (sub-kb `-001-` entry) and awaits ratification,
leaving cluster 6.

## Clusters and disposition

| # | cluster | copies | canonical | disposition |
|---|---------|--------|-----------|-------------|
| 1 | design-kb layer entry | 12 towers, 4 invented names | `llm-design-kb/jsonschema/layer-entry.jsonschema.yaml`, new | migration C |
| 2 | discourse quintet | 21 = 9 identical + 12 drifted | `llm-discourse-graph/jsonschema/` | migration A |
| 3 | incident-forensics, 6 schemas | 3 sites, byte-identical | in `skeleton/`, wrong place | migration B |
| 4 | claim | 2 stale ancestors | `llm-claims-kb/` | migration A |
| 5 | todo/ideas stragglers | 2 | `llm-subtask/jsonschema/` | migration A |
| 6 | `~/.claude` sessions | canonical outside any skill | `llm-sessions/jsonschema/`, new skill | done |
| 7 | technical-policy | 1 identical | exists | migration A |
| 8 | schema symlinks | 30, incl. 5 already dangling | various | migration D |

Migration A is `migrations.kb/2026-08-21-000-schema-copies-to-ref-stubs-all-categories.md`;
B is `.../2026-08-21-001-canonical-schemas-out-of-skeleton.md`; C is
`.../2026-08-21-002-layer-entry-why-slugs-to-paths.md`, which exists only
because cluster 1's canonical now does. Cluster 6 is deliberately *not* a
migration: per `migrations.kb/CLAUDE.md` no transformation exists until
the target is decided, so it stays todo work that unblocks a later one.

## Plan

- [x] Generalize the 2026-07-07 scripts to take a category table as data
      (migration A), run `validate.sh` homedir-wide, review the DIVERGED
      report. Done 2026-08-21. The scripts *subsume* the 2026-07-07 pair
      rather than replacing or copying it; that entry is `complete` and
      stays as executed. Scope lived in `categories.tsv` until
      2026-08-21, when the recurring guard replaced the declared table
      with one derived from the published canonicals -- the table had
      fallen nine categories behind the filesystem.
- [x] Apply migration A to clusters 2 (identical half), 4, 5, 7. Done
      2026-08-21: 18 files stubbed across 7 projects, 0 `STALE-REF` found
      anywhere. Prerequisite grew: six canonicals needed the
      two-entry-point conversion, not the one forecast -- the whole
      discourse quintet had `technical-policy`'s defect.
- [x] Apply migration B: `git mv` the incident-forensics schemas to skill
      root `jsonschema/`, stub the skeleton and both copy sites. Done
      2026-08-21. Verified on the two external trees, which hold the only
      bound instances; the in-repo run is vacuous.
- [x] Design the layer-entry canonical, or record the argument against one
      (cluster 1). Done 2026-08-21: verdict was canonicalize;
      `llm-design-kb/jsonschema/layer-entry.jsonschema.yaml` published,
      reasoning in the sub-kb's `-001-` entry. Ratified 2026-08-21 with one
      amendment: `minItems: 1` on `why` struck, `default: []` added.
- [x] Apply migration C: rewrite `why:` slug references as file-relative
      paths (har-browse ~184 refs, plus mitmproxy, llm-vitals, chatfs),
      then stub the 12 towers' layer schemas onto the canonical. Done
      2026-08-21: 268 of 271 across 175 files in 15 towers, idempotency
      demonstrated by md5 diff. Held at `in-progress` by 3 refs that are
      genuinely ambiguous, not by anything mechanical.
- [x] Decide `~/.claude` schema addressing (cluster 6). Done 2026-08-21:
      the canonical moved to a new `llm-sessions` skill and `~/.claude`
      keeps a stub. There was never an absolute-path `$ref`; the defect
      was a canonical outside any skill, unreachable by `skill://`.
- [x] Judge the drifted copies one at a time: stale, or local intent that
      should extend `#base`? There were **14, not 12**. Done 2026-08-21,
      all of them, with each ruling and its evidence under `## Residual`
      in migration A: 11 stale -> stubbed, 1 local intent -> `#base`
      extender, 2 genuinely rival -> left standalone with the reason
      written into the file so no later sweep re-opens it. Migration A is
      `complete`.

      The two rivals contest the same field, `status`: `ideation.epistemics`
      carries warrant by field presence and exists to *remove* the
      canonical's `status` requirement, and chatfs's `dev.kb/claims` is an
      observation ledger with a disjoint enum. That is where this schema
      family is actually disputed -- worth knowing before the next
      canonical change touches `status`.

      The `template.python-project` six were the largest cluster and the
      most valuable: stubbing them took `discourse.kb` from 15 errors to
      0. None of the 15 was content drift. Each file declared draft-07
      while using `type: date`, which only the house dialect supplies --
      a stale copy does not merely lag the canonical, it pins a dialect
      that cannot express its own data.
- [x] Apply migration D: schema *symlinks* to `$ref` stubs. Done
      2026-08-21, all 30 across 7 repos. This cluster was invisible to the
      census, which swept for copies; only `find -type l` finds it. Five
      had been dangling since `llm-discourse-graph/schemas/` was renamed.
- [x] Disambiguate the 3 `canonical-conversation-graph` `why:` refs in
      `prototype.chatfs`. Done 2026-08-21: all three resolve to
      `030-requirements.kb/`. Settled by distribution rather than by
      re-reading the ambiguous prose -- 13 of 13 sibling refs in that
      layer target 030 and none targets a 040 sibling. Migration C is
      `complete`.
- [x] Judge the 15 errors migration D exposed in
      `scratch.vim-work/docs/sources/2026-03-02-*.kb/`. Done 2026-08-21:
      15 -> 0. The stale-or-intentional framing this item was written
      with applied to none of them, because none was drift: all 15 said
      `No schema found`. `llm.kb-validate` resolves a schema strictly as
      a sibling of the `.kb/` it governs, with no inheritance from an
      ancestor scope, and the two elaborated questions are legitimate
      nested scopes that had no schema beside them. Fixed with 7 sibling
      stubs; zero frontmatter edited, so the 2026-03-02 capture validates
      exactly as authored.

      Generalized: the symlink-era graph got its schemas at the root,
      where the author was standing, and every scope elaborated later was
      silently unvalidated. That defect is now in the recurring guard's
      scope -- see the widening item below.
- [x] Fix `template.python-project`'s pre-commit `prettier` hook. Done
      2026-08-21, but not for the reason this item gives: `pnpm-run` does
      exist, at `<repo>/bin/pnpm-run`, put on PATH by `.envrc` via
      direnv. The hook worked inside a direnv shell and nowhere else --
      including under pre-commit. Fixed to `entry: bin/pnpm-run`, with a
      `REPO=` backport in the script itself.
- [x] Rename the coined term "symlink farm" where it leaked into the
      codebase: `llm-kb/lib/python/llmd/frontmatter_validate.py:68`,
      `llm-kb/references/schema-reuse.md:107`,
      `llm-kb/.claude/todo.kb/2026-02-09-000-schema-reuse-with-ref.md:63`,
      `design-next.kb/070-future-work.kb/v1-migration-bridge.md:14`. It
      is agent-coined, never user-sanctioned, and after migration D it
      also misdescribes what it labels: `~/.claude/skills/` is the skill
      *installation* mechanism, not a dedup device.
      Done 2026-08-21 (`e44a815`): four sites, plus two the census
      missed. The replacement is a plain description of skill
      installation, not another coinage.
- [x] Write the template-uses-`$ref` policy into
      `references/schema-reuse.md`. Ratified 2026-08-21 ("template should
      use `$ref` unless there's an excellent reason to the contrary") but
      never written down, which is how `template.python-project` came to
      mint six stale snapshots.
      Done 2026-08-21 (`deda3d9`), as a new section in
      `references/schema-reuse.md`.
- [x] Widen `migrations.kb/2026-05-15-000-schema-propagation-from-canonical`
      from todo/ideas to every category with a published canonical.
      Unblocked by the judgment pass and done 2026-08-21. Three things
      widened, and the third was not anticipated here:

      - **Categories, declared -> derived.** The plan was to copy A's
        nine-row `categories.tsv`. The filesystem had nineteen
        canonicals; the table was nine behind. The guard now globs
        `<skill>/jsonschema/`, so publishing a canonical enrolls it and
        there is no list to keep in sync. No exclusion list either:
        `dialect` and `layer-entry` are published but have no `.kb/`, so
        the guard is vacuous on them without being told.
      - **Roots.** `~/claude` and `~/.claude` had never been swept.
      - **Shape.** The old pattern matched only `.claude/<category>.kb/`.
        Collections nest, and only the outermost was ever checked -- the
        same defect found one level down in `scratch.vim-work`.

- [x] Work the widened guard's residual: **42 findings, 32 MISSING and
      10 NO-REF** (`2026-05-15-000/validate.sh`, no arguments). By
      category: todo 9, ideas 8, technical-policy 7, sessions 5,
      questions 3, timeline 2, findings 2, deductions 2, claims 2,
      sources 1, evidence 1. `migrate.sh` resolves MISSING mechanically;
      NO-REF wants the same stale/extender/rival ruling as the 14.

      The count understates the work. Every stub `migrate.sh` writes
      subjects a collection to validation for the *first* time, and
      `scratch.vim-work` is the precedent: one schema resolving newly
      checked 44 files. Expect frontmatter conformance work behind each.

      Done 2026-08-21: **42 -> 7**, in four file-disjoint lanes. 35
      resolved, 8 files ruled and marked. 67 files came under
      validation for the first time; 8 errors surfaced behind them,
      all fixed. The `scratch.vim-work` precedent held exactly --
      including two nested sub-scopes invisible to every previous
      sweep. Full record in the migration entry.

## Lanes

The residual is decomposed into six sibling entries, each one agent's
sole-writer territory. Run **-005 first** (its verdicts gate -002 and
-003) and **-003 alone** (it changes the validator every other lane
verifies through); the rest fan out.

- [ ] [-000 Close the 20 remaining schema gaps](2026-08-23-000-Close-the-20-remaining-schema-gaps-left-by-the-reverted-schema-blast.md)
      -- new `*.jsonschema.yaml` in 8 external repos; fan out by repo
- [ ] [-001 Schema file hygiene](2026-08-23-001-Schema-file-hygiene--modeline-dialect-and-em-dash.md)
      -- 229 stale modelines, 144 undeclared dialects, 11 em-dash
      regressions; one write-set, so one agent
- [ ] [-002 Conformance errors in three trees](2026-08-23-002-Conformance-errors-in-three-unbound-trees.md)
      -- chatfs 9, ai-coding-tools-facts.d ~40, ideation.epistemics 1
- [ ] [-003 Schema binding](2026-08-23-003-Schema-binding--roll-ups-scoping-rule-and-ruled-rivals.md)
      -- the roll-up false positive, ruled-rival recognition, the
      discourse scoping sentence
- [ ] [-004 The `pnpm-run` hook in its template](2026-08-23-004-pnpm-run-hook-in-template-python-project.md)
      -- the generator still mints the defect its instance was fixed for
- [ ] [-005 Fleet rulings that gate the lanes](2026-08-23-005-Fleet-rulings-that-gate-the-schema-lanes.md)
      -- five decisions handed up rather than defaulted
