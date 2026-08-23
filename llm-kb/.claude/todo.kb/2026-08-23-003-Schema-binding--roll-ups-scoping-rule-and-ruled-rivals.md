---
managed-by: Skill(llm-subtask)
status: open
related-effort: ./2026-08-21-000-ref-rollout-beyond-todo-ideas.md
required-reading:
  - ~/.claude/skills/llm-kb/references/frontmatter-outside-a-collection.md
cost-benefit-sweh:
  timebox:
    "@value": 2.5
    rationale: |
      Three changes to one subsystem, two of them a few lines plus tests
      and one a doc sentence. The cost is the decision in item 1, not the
      code. Past 2.5h means the decision is being relitigated.
    confidence: confident
  benefit-2w:
    "@value": 1.5
    rationale: |
      Removes two permanent lies from validator output -- the roll-up
      false-positive and the ruled-rival false-positive. Report noise is
      what makes a recurring guard stop being run.
    confidence: confident
  cost-of-delay-2w:
    "@value": 0.5
    rationale: |
      Compounds slowly: every new roll-up and every new ruled rival adds
      another permanent line to a report meant to be read as drift.
    confidence: unsure
---

# Schema binding: roll-ups, the scoping rule, and ruled rivals

**Priority:** Medium-high -- this is the subsystem every other lane's
verification runs through.
**Context:** residual of the 2026-08-21 `$ref` rollout. Three findings
about *which schema governs what*, and what the validator says when the
answer is "none".

## 1. `X.md` beside `X.kb/` always reports `No schema found`

`schema_for()` (`llm-kb/lib/python/llmd/frontmatter_validate.py:333`)
resolves strictly: it walks hive partitions up, then requires the
directory itself to end in `.kb`. A roll-up sits *beside* the collection,
not inside it, so the walk returns `None` and the file is reported.

Confirmed in three independent trees, including this repo's own
`llm-kb/complete-example/decorations.md` and `llm-kb/.claude/todo.md`.
Six `todo.md` roll-ups in this repo are the standing error count in
`llm.kb-validate .`.

Three candidate answers, and picking is the work:

1. The resolver walks to the sibling schema. Then a roll-up is validated
   as a member of the collection it rolls up, which is probably wrong --
   a roll-up is prose *about* a collection, not a member of one.
2. The validator stops calling it an error and says something truer,
   e.g. reports it as unbound rather than failing.
3. The roll-ups are simply wrong to carry frontmatter. `Skill(llm-kb)`
   already says a synthesis file carries none, and
   `references/frontmatter-outside-a-collection.md` says strip it.

Option 3 is the cheapest and the most consistent with the written rule,
so the burden is on 1 and 2 -- but the reader sweep it depends on has
since come back mixed (2026-08-23, from `~/claude/meta-reasoning`),
and the mixed part is decisive:

- `managed-by:` has no reader. Grep found writers and the member
  schema's `const` pin, nothing that consumes it. Strippable.
- `cost-benefit-sweh:` **is read** -- `claude-open-tasks-list` and
  `wsjf-rank` rank the backlog off it, and this repo's own
  `llm-subtask/.claude/todo.md` carries a full one today. Stripping a
  roll-up wholesale deletes live prioritization data.
- `status:` is skeleton-set to `template` and hand-edited to `active`
  in at least one consumer; no reader found, sweep not exhaustive.

So option 3 cannot be applied as stated. Either it narrows to "strip
the constants, keep the data" -- which needs 1 or 2 anyway for what
remains -- or `cost-benefit-sweh` moves out of roll-ups entirely and
`### Synthesis Files`' "carries no frontmatter" stands unamended.
That choice is the decision this item is really about.

Scale, for whoever rules it: 24 files under `~` carry the skeleton
frontmatter (`find ~ -name todo.md -path '*/.claude/*' | xargs grep -l
'managed-by: Skill(llm-subtask)'`), across separate repos, so the
sweep is one commit each.

## 2. The validators cannot tell a ruled rival from an unexamined one

Three schemas were judged during the rollout and deliberately left
standalone rather than stubbed: two in `ideation.epistemics` and one in
`prototype.chatfs` (`dev.kb/claims`). Each now opens with a marker
comment naming the canonical it departs from.

Nothing reads that marker. The **recurring** guard
(`llm-kb/migrations.kb/2026-05-15-000-schema-propagation-from-canonical/validate.sh`)
reports the two `ideation.epistemics` rivals as `NO-REF` and will do so
forever -- a permanent two-line lie in a report whose whole purpose is to
be read as drift. The one-shot
`2026-08-21-000/validate.sh` wants the same, where it is what stands
between `complete` and `verified` on the parent effort.

Design note: the marker is currently a comment, i.e. not machine-shaped.
Whether to keep it a comment with an agreed prefix, or promote it to a
real key, is part of this item.

## 3. `llm-discourse-graph/SKILL.md` under-documents scoping

§Scoping and hierarchy says a sub-scope "may contain any of this skill's
collection types" and stops there. It does not say each such sub-scope
needs its own `<category>.jsonschema.yaml` beside it -- there is no
inheritance from an ancestor scope. That omission is how
`scratch.vim-work` went months with 15 unvalidated files behind a schema
placed only at the graph root.

One sentence prevents the next instance.

## Implementation Steps

- [ ] Rule item 1 among the three options; implement; fix the six
      roll-ups accordingly
- [ ] Make both guards marker-aware; re-run each and confirm the rival
      lines are gone and nothing else changed
- [ ] Add the scoping sentence to `llm-discourse-graph/SKILL.md`

## Delegation

- **Sole writer of:** `llm-kb/lib/python/llmd/`, `llm-kb/tests/`,
  `llm-kb/migrations.kb/2026-05-15-000-*/`, `llm-kb/references/`,
  `llm-discourse-graph/SKILL.md`, and the six `*/.claude/todo.md`
  roll-ups in this repo.
- **Not parallel-safe with any other lane.** Every other lane verifies
  through `llm.kb-validate`; changing it underneath them invalidates
  their before/after counts. Run this lane alone, or first, or last.
- **Never widen** what the validator accepts in order to make an error
  go away. The three rivals are ruled *rivals* -- they must stay
  reported as something, just not as drift.
- **Verify with:** the repo's own test suite plus `llm.kb-validate .` at
  the repo root; the six-error baseline must move to 0 by intent, not by
  suppression.

## Success Criteria

- [ ] `llm.kb-validate .` at this repo root is clean
- [ ] Neither guard reports a ruled rival as drift
- [ ] A reader of `llm-discourse-graph/SKILL.md` learns that a sub-scope
      needs its own schema
