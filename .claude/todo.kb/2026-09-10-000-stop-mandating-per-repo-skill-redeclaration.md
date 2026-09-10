---
managed-by: Skill(llm-subtask)
status: open
cost-benefit-sweh:
  timebox:
    "@value": 3
    rationale:
      the discrimination rule is the whole job; once stated, the sweep across
      ~20 skills and their consumer repos is mechanical. Stop if the rule turns
      out to need per-skill judgement rather than one criterion
    confidence: tentative
  benefit-2w:
    "@value": 1
    rationale:
      every redundant arrival-load is paid in every session in every consumer
      repo. `arrival-fired-directives.md` reports roughly half a session's tool
      calls falling before the first line of the answer -- that figure counts
      the whole bootstrap, so redundant skill loads are one contributor of
      several, never separately measured
    confidence: tentative
---

# Stop mandating per-repo skill re-declaration

**Priority:** Medium **Complexity:** Low mechanically, Medium in judgement (the
discrimination rule below is the real work) **Context:** raised 2026-09-10 —
"that's a leftover from a pre-triggers world. And there's other skills with the
same problem."

## Problem

A skill's `description:` **is** a trigger: it names the occasion to load the
skill, and it is trigger source #2 in the installation order. When a consumer
repo's `CLAUDE.md` also declares that skill — as `requires:`, `depends:`, or
even a correctly-formed `triggers:` entry — naming *the same* occasion, the
trigger has been authored twice. The copy can only drift from the original, and
it buys nothing: `read: skill://<name>` cannot resolve if the skill is absent
anyway.

This is a leftover from before `triggers:` existed, when a `CLAUDE.md` field was
the only way to route a skill.

## Evidence: llm-kb contradicts itself

`llm-kb/SKILL.md` already states the correct rule, under "Maintenance Guides":

> Root CLAUDE.md must have an overview of available `.kb/` collections and their
> purpose. **It needs no frontmatter declaring this skill; the `description:`
> carries the trigger.**

Two of its own audits mandate the opposite, and are the stale side:

- `llm-kb/skill.kb/self-audit.kb/claudemd-completeness.md:16` — "For a root
  CLAUDE.md, also verify the frontmatter declares this skill via `triggers:`,
  with a stated condition".
- `llm-kb/skill.kb/self-audit.kb/claudemd-enumeration.md:44` — the whole
  "Frontmatter check (root CLAUDE.md only)" section, which supplies
  `when: creating or maintaining a .kb/ collection` as the default condition.

That default string is a verbatim abbreviation of what llm-kb's `description:`
already names ("Agent MUST load when creating a .kb/ collection, when adding,
renaming, splitting, or removing files in one, …"). So the audit is not merely
permitting the duplication — it **generates** it, in every kb-using repo, and
re-generates it after removal: an agent running the self-audit sweep will
restore a declaration that was deliberately deleted.

Confirmed downstream: `basedpyright-as-pyright` removed exactly this
(commit `d28b932`, 2026-09-10) and is now non-conformant to those two audits.

## The discrimination rule (state this first — it is the deliverable)

Not every skill declaration in a consumer file is redundant. The sweep needs one
criterion, applied per instance:

- **Redundant → delete.** The declaration's occasion is already named by the
  skill's own `description:`. Nothing is lost; the description keeps routing it.
- **Genuinely conditional → migrate to `triggers:`.** The occasion is *narrower
  than*, or *different from*, what the description names — e.g. "before
  committing **in this repo**", or a local convention the skill cannot know
  about. Keep it, with a stated juncture.
- **Not a directive at all → leave it alone.** Two sub-cases: a `triggers:`
  entry whose `read:` is a file (`./commit.md`), and — the numerically larger
  one — a `depends:` that is *domain data under a schema* rather than a
  routing field. Touching the second corrupts a graph. See the collision item
  under Scope.

The failure to avoid is treating the whole sweep as the deprecated-field
migration (`requires:`/`depends:` → `triggers:`). That is a *separate axis*: a
`requires:` entry can be both deprecated-in-form and redundant-in-substance, and
the fix is deletion, not migration. Migrating it first makes a well-formed
duplicate — which lints clean and is still wrong.

## Scope to sweep

- [ ] **The two llm-kb audits above.** Reconcile them with `SKILL.md`. This is
      the generator; fix it before sweeping consumers, or the sweep undoes
      itself.
- [ ] **Every skill's `description:`** — confirm each genuinely names its
      occasion. A description that does *not* is the one case where a consumer
      declaration is load-bearing, and the fix belongs in the description.
- [ ] **Other skills carrying the same guidance.** Raised as known-plural; only
      llm-kb was confirmed outside `trash/` on 2026-09-10. Sweep rather than
      trust that count:
      `grep -rn --include='*.md' -iE 'declares? this skill|frontmatter declar' .`
- [ ] **`llm-must-read-kb`** — the predecessor subsystem; check whether its bank
      conventions still assume a per-repo declaration.
- [ ] **`depends:` is claimed by two live skills, and the linter arbitrates by
      accident.** `llm-triggers-lint` takes the field name unconditionally
      (`bin/llm-triggers-lint:51`, `DIRECTIVE_FIELDS = ('requires', 'depends',
      'triggers')`; `depends` is also in `RETIRED_FIELDS`) and consults no
      schema. `llm-discourse-graph` declares `depends:` in five of its own
      schemas — "Paths to nodes this claim depends on for context" — and
      `SKILL.md:131` tells authors to add it. Both are current, so every
      discourse graph in the fleet lints dirty permanently, and that noise
      trains the eye off a red count — a failure this backlog already records
      twice elsewhere. Decide who owns the name: rename one side, or teach the
      linter that a key declared by the collection's own schema is data. Until
      then a `bare-unconditional` count is not a to-do list.
- [ ] **Consumer repos.** `template.python-project`'s 21 `bare-unconditional`
      errors are two unrelated populations — a worked example of the
      discrimination rule, and the reason to state it before sweeping. **Six**
      are `CLAUDE.md` carriers declaring a skill (`Skill(llm-subtask)` ×2,
      `Skill(llm-kb)`, `Skill(llm-discourse-graph)`, `Skill(llm-design-kb)` ×2);
      those are this defect. The other **fifteen** are `discourse.kb/` claims
      and questions whose `depends: [claims.kb/….md]` is a graph edge under a
      `$ref`'d schema — false positives of the collision above, and not
      fixable from the consumer side. That repo's harvest todo has been
      corrected to say so.

## Success criteria

- [ ] The discrimination rule is written down where the sweep's agents will read
      it, not just applied once.
- [ ] No skill's guidance instructs a consumer to re-declare that skill for an
      occasion its `description:` already names.
- [ ] Running llm-kb's own self-audit against a conformant repo no longer
      re-introduces the declaration.
- [ ] `llm-triggers-lint` reaches 0 errors across the fleet — which needs the
      `depends:` collision settled first, since 15 of
      `template.python-project`'s 21 cannot be fixed from the consumer side.
      And clean lint is necessary, **not** sufficient: a well-formed duplicate
      passes it.

## Notes

The subsystem's own framing of the defect is
`llm-triggers/design.kb/use-cases.kb/arrival-fired-directives.md`: a directive
in a host `CLAUDE.md` is "a trigger carrying a directive with its condition
deleted", firing on arrival for every agent whatever they came to do. The
correction there is that the condition must travel with the directive — and when
the skill's `description:` already carries it, travelling means *staying in the
description*, not being restated per repo.
