---
managed-by: Skill(llm-subtask)
status: open
related-effort: ./2026-08-21-000-ref-rollout-beyond-todo-ideas.md
suggested-reading:
  - ~/.claude/skills/llm-kb/migrations.kb/2026-08-21-003-schema-symlinks-to-ref-stubs.md
  - ~/.claude/skills/llm-kb/migrations.kb/2026-05-21-000-em-dash-to-ascii-double-hyphen.md
cost-benefit-sweh:
  timebox:
    "@value": 3.0
    rationale: |
      Two mechanical sweeps behind a classifier (fast) and one that needs
      a read per file (the 144 undeclared dialects). Past 3h the
      remainder is the 144, which can be split off as its own entry
      without loss.
    confidence: unsure
  benefit-2w:
    "@value": 0.5
    rationale: |
      Invisible to the validator, so nothing unblocks. The payoff is a
      language server that checks the right dialect, and canonical prose
      that stops fingerprinting as machine-written.
    confidence: confident
  cost-of-delay-2w:
    "@value": 0.25
    rationale: |
      Static and harmless. The one real risk is that each new stub copies
      a neighbour's stale first line, so the set grows slowly with the
      other lanes.
    confidence: confident
---

# Schema file hygiene: modeline, dialect, and em-dash

**Priority:** Low -- cosmetic to the validator, misleading to the editor.
**Complexity:** Small for two of three, given the surviving
classification.
**Context:** three textual defects that all live in the head or the
`description:` strings of `*.jsonschema.yaml`. They are one lane because
they are one write-set, not because they are one problem: an agent
holding those files must hold all three, or two sweeps collide.

## 1. Stale draft-07 modelines over 2020-12 schemas -- 229 files

Noted as a loose end by migration `2026-08-21-003`: "The house stub keeps
a `# yaml-language-server: ...draft-07...` first line... It is stale on
every one of them: the referenced canonicals are 2020-12."

The line is editor tooling only -- `llm.kb-validate` ignores it -- so the
cost is a language server silently checking the wrong dialect.

The classification survived the incident, in `trash/modeline-sweep/`:

- `class.json` -- **229 files genuinely 2020-12, 34 genuinely draft-07,
  0 unclassifiable.** Classified by the file's own `$schema:` key and by
  what its `$ref` targets declare, never by the modeline.
- `cand.list` -- the 263 draft-07-modeline files, after excluding the
  replication-run clone and the vendored litellm tree.
- `classify.py` -- the classifier.

The 34 genuine draft-07 files must keep their modeline. Only the 229
flip.

## 2. No dialect declared at all -- 144 files

144 of the 309 surveyed schema files declare no dialect. The house answer
exists -- `$schema: skill://llm-kb/jsonschema/dialect.jsonschema.yaml`,
already used by 12 files -- and adding it is nearly mechanical, but **not
uniformly**: a file using 2020-12 keywords must not be declared draft-07.
Each one needs a read.

This is the item to split off if the timebox binds.

## 3. Em-dash regression in the canonicals -- 11 files

Migration `2026-05-21-000-em-dash-to-ascii-double-hyphen` has regressed
into the canonical schemas: five in
`llm-subtask/jsonschema/todo.jsonschema.yaml` and six more across the
discourse quintet, `technical-policy`, and `claims`. Found 2026-08-21 and
deliberately not fixed then -- it is that migration's sweep to run.

Why it regressed is the generalizable part: canonical schemas are *data*
files, so a prose-oriented sweep skips them. Whoever re-runs
2026-05-21-000 should put `*.jsonschema.yaml` `description:` strings in
scope permanently.

Note two files in this very collection carried em-dashes until
2026-08-23; a `todo.kb/` entry is squarely in that migration's scope.

## Implementation Steps

- [ ] Re-run `classify.py` -- the corpus moved under it (reverts, erased
      history, new hand-written schemas), so the counts want refreshing
      before anything is written
- [ ] Flip the modeline on the confirmed 2020-12 set
- [ ] Declare the dialect on the 144, one read each
- [ ] Sweep em-dashes from `description:` strings; widen
      2026-05-21-000's scope to say `*.jsonschema.yaml` is included
- [ ] `llm.kb-validate` per tree -- must be a no-op for steps 2 and 4;
      step 3 may newly bind files, which is the point
- [ ] Fold the result into migration `2026-08-21-003`, which predicted
      the first sweep

## Delegation

This is delegable. The 2026-08-22 failure was not that an agent did it;
it was that the agent was given an objective ("fix the modelines")
instead of a boundary. Stated as prohibitions it is safe:

- **Sole writer of:** `*.jsonschema.yaml` fleet-wide. Nothing else, ever
  -- not the `.md` files beside them, not `.kb/` contents.
- **Not parallel-safe with lane -000**, which creates new
  `*.jsonschema.yaml`. Run -000 first and re-classify, or run this first
  and let -000 write correct first lines itself.
- **Never delete or rewrite a `$schema:` key.** Only the
  `# yaml-language-server:` comment line moves in step 2. The 2026-08-22
  agent blanket-flipped 215 modelines, 8 of them onto files whose own
  `$schema:` said draft-07 -- and deleted that key in the same write, so
  the evidence of the mistake went with it.
- **Never trust the modeline as evidence of dialect.** It is the thing
  under repair. `class.json` and the file's own `$schema:` are the
  authority.
- **Never change a file's body** -- keys, structure, `$ref` targets. Step
  4 touches prose inside `description:` strings and nothing else.
- **Verify with:** `git diff` line counts. Steps 2 and 3 must show
  exactly one changed or added line per file. Any file with a larger
  diff is a mistake, not a judgment call.

## Open Questions

- Should the house `$ref` stub template stop carrying a modeline at all?
  A stub's dialect is whatever its target declares, so the stub asserting
  one is a second source of truth that can only ever go stale -- which is
  precisely how this got here.

## Success Criteria

- [ ] No `*.jsonschema.yaml` declares a modeline dialect its own
      `$schema:` (or its `$ref` target's) contradicts
- [ ] No `*.jsonschema.yaml` is silent about its dialect
- [ ] No U+2014 in any canonical's prose
