---
managed-by: Skill(llm-subtask)
status: not-started
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
      stays as executed. Scope lives in `categories.tsv`, so widening is
      one line.
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
- [ ] Judge the drifted copies one at a time: stale, or local intent that
      should extend `#base`? There are **14, not 12**, and they are not
      all discourse -- 10 discourse, 2 `todo`, 2 `technical-policy`.
      Enumerated with a reason each under `## Residual` in migration A.
      Six are `template.python-project`, the single largest cluster, and
      two of those six are semantically identical to canonical (drifted
      only in dialect and line-wrapping) -- the cheapest ruling to make
      first, and the one that stops minting stale copies into new repos.
- [x] Apply migration D: schema *symlinks* to `$ref` stubs. Done
      2026-08-21, all 30 across 7 repos. This cluster was invisible to the
      census, which swept for copies; only `find -type l` finds it. Five
      had been dangling since `llm-discourse-graph/schemas/` was renamed.
- [ ] Disambiguate the 3 `canonical-conversation-graph` `why:` refs in
      `prototype.chatfs` -- a real entry exists at both
      `docs/dev/design.kb/030-requirements.kb/` and `040-design.kb/`, and
      the prose does not settle which is meant. Migration C names all
      three bearer files. This is the only thing holding C at
      `in-progress`.
- [ ] Judge the 15 errors migration D exposed in
      `scratch.vim-work/docs/sources/2026-03-02-*.kb/`. All 44 files there
      were failing because the schema symlinks dangled; 29 conform. The
      15 are real drift getting its first honest reading, and want the
      same stale-or-intentional ruling as the 14.
- [ ] Fix `template.python-project`'s pre-commit `prettier` hook: it
      calls `pnpm-run`, which exists nowhere on this machine (only
      `pnpm`). Four files sit uncommitted behind it. Pre-existing, not
      migration damage -- but it blocks the largest DIVERGED cluster from
      being committed once judged.
- [ ] Configure remotes, or record that there deliberately are none, for
      `~/claude/meta-reasoning` and `~/claude/crostini-health`. Both now
      hold committed-but-unpushable work from this effort.
- [ ] Sweep the stale `# yaml-language-server: $schema=...draft-07...`
      first line off every stub written under 2026-08-21-{000,003}
      (~48 files). Each references a 2020-12 canonical. Harmless to the
      validator, wrong for the editor. Do this *after* the judgment
      passes -- it touches the same files.
- [ ] Rename the coined term "symlink farm" where it leaked into the
      codebase: `llm-kb/lib/python/llmd/frontmatter_validate.py:68`,
      `llm-kb/references/schema-reuse.md:107`,
      `llm-kb/.claude/todo.kb/2026-02-09-000-schema-reuse-with-ref.md:63`,
      `design-next.kb/070-future-work.kb/v1-migration-bridge.md:14`. It
      is agent-coined, never user-sanctioned, and after migration D it
      also misdescribes what it labels: `~/.claude/skills/` is the skill
      *installation* mechanism, not a dedup device.
- [ ] Write the template-uses-`$ref` policy into
      `references/schema-reuse.md`. Ratified 2026-08-21 ("template should
      use `$ref` unless there's an excellent reason to the contrary") but
      never written down, which is how `template.python-project` came to
      mint six stale snapshots.
- [ ] Widen `migrations.kb/2026-05-15-000-schema-propagation-from-canonical`
      from todo/ideas to every category with a published canonical, once A's
      validator can back the wider claim. Do not widen the `scope:` before
      then -- a recurring guard whose validator does not cover its stated
      scope is worse than a narrow one. Still blocked as of 2026-08-21:
      A's validator covers all nine categories but does not *pass*
      homedir-wide, because the 14 above are unjudged. Widen after the
      judgment pass, not after A.

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
