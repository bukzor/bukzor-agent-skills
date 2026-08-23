---
managed-by: Skill(llm-subtask)
status: open
related-effort: ./2026-08-21-000-ref-rollout-beyond-todo-ideas.md
cost-benefit-sweh:
  timebox:
    "@value": 0.5
    rationale: |
      Three known sites, one known fix, already applied once at the
      instance level. Past 30 minutes means the template's generation
      path is not what this brief says it is -- stop and report.
    confidence: confident
  benefit-2w:
    "@value": 1.0
    rationale: |
      Every repo minted from this template gets a pre-commit hook that
      works inside a direnv shell and nowhere else, including under
      pre-commit itself. The debugging cost lands on whoever hits it,
      cold.
    confidence: confident
  cost-of-delay-2w:
    "@value": 0.5
    rationale: |
      Accrues per new project initialized from the template -- roughly
      one event per two weeks, and each one carries the defect forward
      permanently.
    confidence: unsure
---

# The `pnpm-run` hook, in the template that mints it

**Priority:** Low effort, and it stops a defect from replicating.
**Context:** residual of the 2026-08-21 `$ref` rollout. The instance was
fixed; the template that generates it was not -- exactly the shape of the
six stale schema snapshots the rollout spent its afternoon undoing.

## The defect

`pnpm-run` is not on `PATH`. It exists at `<repo>/bin/pnpm-run` and is
put on `PATH` by `.envrc` via direnv, so a hook declaring
`entry: pnpm-run` works in an interactive direnv shell and fails
everywhere else -- including under pre-commit, which is the only place
it is supposed to run. The fix, applied 2026-08-21 to
`template.python-project` itself, is `entry: bin/pnpm-run` plus a
`REPO=` backport inside the script.

## The three sites still carrying it

- [ ] `copier-template/.pre-commit-config.yaml.jinja` -- still emits
      `entry: pnpm-run`. This is the one that matters: it is the
      generator, so every new project inherits the broken form.
- [ ] `copier-template/config.d/pre-commit/javascript.yaml` -- reported
      fixed by the 2026-08-21 terminology pass, never independently
      confirmed
- [ ] `config.d/pre-commit/javascript.yaml` (repo root) -- same, same

The second and third are *verification*, not repair. Confirm before
editing; a report of a fix is not a fix.

## Delegation

- **Sole writer of:** `~/repo/github.com/bukzor/template.python-project`
  and nothing else.
- **Parallel-safe with:** every other lane. No overlap in either
  direction.
- **Never edit** a generated project to work around the template. The
  point of this lane is that the generator is the bug.
- **Verify with:** generate a throwaway project from the template into
  `trash/` and run its pre-commit hooks from a non-direnv shell (`env -i`
  or equivalent). The hook must resolve. A passing run inside a direnv
  shell proves nothing -- that is precisely how this shipped.

## Success Criteria

- [ ] A freshly generated project's `prettier` hook runs outside direnv
- [ ] No `entry: pnpm-run` (unqualified) remains anywhere in the repo
