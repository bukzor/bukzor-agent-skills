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
- [ ] Decide whether the decision-lifecycle trio (`status` / `blocked-on` /
      `superseded-by`, three hand-synced copies found in cluster 1) earns
      its own canonical. Deliberately left out of layer-entry.
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
- [ ] Configure remotes, or record that there deliberately are none, for
      `~/claude/meta-reasoning` and `~/claude/crostini-health`. Both now
      hold committed-but-unpushable work from this effort.
- [ ] Sweep the stale `# yaml-language-server: $schema=...draft-07...`
      first line off every stub written under 2026-08-21-{000,003}
      (~48 files). Each references a 2020-12 canonical. Harmless to the
      validator, wrong for the editor. Do this *after* the judgment
      passes -- it touches the same files.
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
- [ ] Ten of those 42 were already in the old scope and old root -- six
      weeks of ordinary drift on a guard that only runs when someone
      opens a migration. Decide whether the recurring guards get a
      schedule (a hook, a cron, a `/session-end` step). A `kind:
      recurring` migration nobody runs is a `complete` one that lies.
- [ ] Teach the validators to distinguish a ruled rival from an
      unexamined one. All three rivals now open with a marker comment
      naming the canonical they depart from. This matters most for the
      **recurring** guard (`2026-05-15-000`), which reports the two
      `ideation.epistemics` rivals as NO-REF and will do so forever --
      a permanent two-line lie in a report meant to be read as drift.
      The one-shot `2026-08-21-000/validate.sh` wants it too, where it
      is what stands between `complete` and `verified`.
- [ ] `~/repo/github.com/bukzor/dotfiles` on branch `orphan-recovery`
      still holds the pre-stub `.claude/todo.jsonschema.yaml`,
      byte-identical to what `~/.claude/` had, plus 5 more MISSING. Not
      a second divergence -- the same file on an unmerged branch of a
      second clone, and the reunify effort carries it. Left alone rather
      than reaching into another workstream's branch, but a careless
      merge reinstates the stale copy over the stub.
- [ ] `template.python-project/copier-template/.pre-commit-config.yaml.jinja`
      still emits `entry: pnpm-run`. The template that mints the broken
      hook was not fixed when the hook was -- the same shape as the six
      stale schema snapshots, and the reason the template-uses-`$ref`
      policy item below is worth writing down.
- [ ] Add one sentence to `llm-discourse-graph/SKILL.md` §Scoping and
      hierarchy: a sub-scope that contains any of this skill's
      collection types needs its own `<category>.jsonschema.yaml` beside
      it. The section currently says a sub-scope "may contain any of
      this skill's collection types" and stops there, which is how
      `scratch.vim-work` went months with 15 unvalidated files.
- [ ] One surviving error in `ideation.epistemics` at
      `background.kb/prior-art`. Left after that repo's pass; not
      diagnosed.

## Deferred

144 of the 309 surveyed schema files declare no dialect at all. The house
answer exists (`$schema: skill://llm-kb/jsonschema/dialect.jsonschema.yaml`,
used by 12 files) and adding it is nearly mechanical, but not uniformly:
a file using 2020-12 keywords must not be declared draft-07, so each needs
a read. Candidate migration C; not written, out of scope here.

The em-dash migration (`migrations.kb/2026-05-21-000-em-dash-to-ascii-double-hyphen.md`)
has regressed into the canonical schemas themselves: five in
`llm-subtask/jsonschema/todo.jsonschema.yaml` and six more across the
discourse quintet, `technical-policy`, and `claims`. Found 2026-08-21
while converting those files and deliberately not fixed -- rewriting a
canonical's bytes invalidates nothing, but it is that migration's sweep
to run, not this one's. Worth noting *why* it regressed: canonical
schemas are data files, so a prose-oriented sweep can miss them. Whoever
re-runs it should include `*.jsonschema.yaml` descriptions in scope.

- [ ] Refresh the `dotfiles` clone at `~/repo/github.com/bukzor/dotfiles`
      (branch `orphan-recovery`). It is the *entire* remaining guard
      residual -- 7 findings -- and none of it is drift: that branch is an
      ancestor of the live checkout at `~`, and the clone has simply never
      fetched the commits that wrote the stubs. `git fetch` resolves all
      seven with no edit. Left alone because it is another workstream's
      checkout. Until it is refreshed the guard cannot reach `verified`.
- [x] Decide whether `llm-discourse-graph`'s `claims.status` needs a value
      for *moot / no longer applies*. Three entries in
      `summer-programming-project` use `superseded` and one uses
      `resolved`; nowhere else in the homedir. Retracting them would be
      false -- the bodies say the findings were not wrong. Legislation for
      the fleet, so it was handed up rather than defaulted.
      Ruled 2026-08-21 (user): not a status value at all. `status` holds
      epistemic standing, and "stopped mattering" is a second axis, so
      claims gained `live: bool` (default true) and `superseded-by:
      path[]` (`00dda9e`), with a `dependentSchemas` rule forbidding the
      two from disagreeing. Not "moot" -- it means *irrelevant* in
      American usage and *open to argument* in British and legal usage,
      opposite senses for a word going into a schema. `live`/`dead`
      inverts nowhere. All three entries migrated (`f4b693b`) and the
      second axis is documented in SKILL.md (`52c28ba`), which had
      described the metadata as one axis and so kept producing the bug.
- [ ] Rule on `prototype.chatfs`'s 9 remaining conformance errors:
      `status: exploring|active` and `kind: investigation` outside the
      closed enums, and `resolved:` holding a date where the canonical
      says string. Either the enums want widening (a canonical edit) or
      the data is wrong. Deliberately not papered over.
- [ ] Fix or document the roll-up quirk: an `X.md` beside `X.kb/` always
      reports `No schema found`, because `schema_for()` only looks
      *inside* `.kb/`. Confirmed in three independent trees including this
      repo's own `llm-kb/complete-example/decorations.md` and
      `llm-kb/.claude/todo.md`. Either the resolver walks to the sibling
      schema, or `references/frontmatter-outside-a-collection.md` is the
      answer and the validator should say so without calling it an error.
- [ ] Verify the two further `pnpm-run` sites the terminology pass
      reported fixing: `copier-template/config.d/pre-commit/javascript.yaml`
      and the root `config.d/pre-commit/javascript.yaml`. Same defect as
      `template.python-project` -- a hook entry that only resolves inside a
      direnv shell. Reported, not yet independently confirmed.
- [ ] Commit or discard two session entries left fixed-but-uncommitted in
      `2026-05-19--task-archeology/.claude/sessions.kb/` and
      `template.python-project/.claude/sessions.kb/` (`session.uuid`
      scalar -> list). Left alone as other agents' in-flight work.
- [ ] Decide whether the four collections with no published canonical want
      one: `research.home-office/use-cases.kb`,
      `summer-programming-project/.../curriculum.kb`, and
      `github-manager/{goals,maintenance-actions}.kb`. The guard is silent
      on them by construction, so they are invisible to every sweep.
- [ ] Fix the `ai-coding-tools-facts.d` tree (~40 errors). One schema
      declares `http://json-schema.org/draft-07/schema#` *with* the
      trailing `#`, which the validator rejects as an unknown dialect.
- [ ] Decide what to do about `~/claude/.claude/` and
      `~/claude/bug--parallel-path-contamination/`: neither is a repo nor
      tracked (`~/claude/.gitignore` is `*/`). Stubs were written there
      and cannot be committed anywhere.
- [ ] Decide whether `deductions` and `questions` want the same
      `live`/`superseded-by` axis that `claims` just gained. A claim's
      death often strands the deductions resting on it, and a question can
      stop mattering without being answered. Deliberately not done with
      claims: there is no observed instance yet, and legislating the
      shape of three collections from evidence about one is how the
      original conflation got in.
- [ ] Consider adding `~` to the guard's roots. Coverage of the dotfiles
      repo is currently an accident -- `~/repo/.../dotfiles` happens to
      sit inside a scanned root, which is the only reason
      `~/.vim/.claude/` was ever seen. Anything dotfiles tracks at top
      level outside `~/repo`, `~/claude`, `~/.claude` is invisible by
      construction. Weigh against what `~` drags in.
