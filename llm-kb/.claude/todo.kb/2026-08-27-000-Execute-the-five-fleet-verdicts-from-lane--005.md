---
managed-by: Skill(llm-subtask)
status: open
related-effort: ./2026-08-21-000-ref-rollout-beyond-todo-ideas.md
cost-benefit-sweh:
  timebox:
    "@value": 3.0
    rationale: |
      Five edits, four of them small and one -- the decision-lifecycle
      canonical -- a publish plus a seven-consumer swap with zero data
      migration. Past 3h means a verdict is being relitigated instead of
      applied, which is the one thing lane -005 exists to prevent.
    confidence: confident
  benefit-2w:
    "@value": 1.0
    rationale: |
      Clears the last decisions gating the schema lanes, and kills the
      slug-vs-path fork in `superseded-by` before any instance data lands
      under either type.
    confidence: confident
  cost-of-delay-2w:
    "@value": 0.5
    rationale: |
      A verdict nobody applies decays back into a recommendation, and the
      next session re-argues it from scratch. The `superseded-by` fork also
      gets strictly more expensive with the first instance written.
    confidence: unsure
---

# Execute the Five Fleet Verdicts From Lane -005

**Priority:** high -- four of the five unblock other work
**Complexity:** low per item, except the canonical
**Context:** `2026-08-23-005-Fleet-rulings-that-gate-the-schema-lanes.kb/`

## Problem Statement

All five rulings were ruled by the owner on 2026-08-27 and recorded in the
`## Verdict` section of each recommendation file. Lane -005 is closed --
its charter was to produce recommendations and record verdicts, and the
edit a verdict authorizes happens in the lane that needed it, never there.
No lane currently owns any of these edits. This entry owns them.

Read the verdict before doing its work. Each carries the reasoning, the
evidence, and the declined alternative; none of that is restated here.

## Implementation Steps

- [ ] **Publish `decision-lifecycle`.** New
      `llm-design-kb/jsonschema/decision-lifecycle.jsonschema.yaml`, house
      two-entry-point shape, with the superseded-implies-`superseded-by`
      conditional folded inside `#base` so consumers stop hand-repeating
      the `allOf`. Swap the inline block in design-next 020/030/040/070,
      llm-triggers 040 and llm-vitals 040/070 for the one-line mixin;
      delete design-next's local `$defs` file; drop llm-vitals' slug
      `pattern` on `superseded-by`. Zero instance edits -- if a data file
      needs changing, stop, because the census was wrong.
- [ ] **Three local schemas, no canonical.**
      `~/claude/research.home-office/use-cases.jsonschema.yaml` admitting
      the observed union, every property optional and nothing required;
      `~/claude/github-manager/goals.jsonschema.yaml` and
      `maintenance-actions.jsonschema.yaml` transcribed from each
      collection's own CLAUDE.md contract. Nothing published under any
      skill's `jsonschema/`. `principles.kb` carries no frontmatter and
      `curriculum.kb` is not a collection; both get nothing.
- [ ] **`live:` on `deductions`**, under the derived-vs-declared rule,
      plus whatever checker that rule needs to be more than an assertion.
      `questions` gets nothing until the first hand-rolled death marker
      appears anywhere in the fleet.
- [ ] **Schedule the schema guard**: one `period 1` row in
      `~/.config/anacron/anacrontab`, a report at a fixed path, and a
      session-start step that reads it. Blocked on
      `2026-08-27-001` -- do not schedule a guard whose baseline is
      nine-tenths its own bug.
- [ ] **`$HOME/.vim` into `ROOTS`** in
      `migrations.kb/2026-05-15-000-schema-propagation-from-canonical/validate.sh`,
      with a comment saying why: it holds the only collections in the
      dotfiles tree outside `~/.claude`, and an unexplained root is what
      the next sweeper deletes.

## Open Questions

Two clauses inside those verdicts are agent-standing rather than the
owner's, and their veto window is open -- veto by editing the file:

- the anacron trial's stopping condition (ruling 4): pull the trial if a
  nonempty report survives two consecutive weeks of session starts
  unrepaired;
- declining to register the `$HOME` git-index enumeration in
  `bukzor_homedir_archeology` (ruling 5), with the revisit trigger being
  the first `.kb` that appears outside `repo/`, `claude/`, `.claude/`,
  `.vim/`.

## Success Criteria

- [ ] Each verdict is applied, or carries a written reason it was not
- [ ] `llm.kb-validate` clean in every tree touched
- [ ] Nothing written under any `*/jsonschema/` except the one new canonical
