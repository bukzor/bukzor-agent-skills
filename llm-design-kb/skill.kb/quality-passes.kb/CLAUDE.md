# quality-passes.kb -- design-record passes

> [!DRAFT] agent-authored 2026-11-25, vetoable

One quality pass per file (`PASS_AT_OCCASION`, in the fleet ledger's
`authorship.kb/`): a way a design record breaks the rung discipline, the walk
over the record that finds it, what a finding means, and the repair. A pass
names no occasion: `../must-read.kb/` does, and
`../procedures.kb/run-quality-passes.md` runs the passes in tiers.

## What Belongs Here

- A pass on authoring design claims that generalizes beyond any one
  project's record, kebab-case, named for the quality it passes over

## What Does NOT Belong Here

- A pass any claims.kb owes -- `Skill(llm-claims-kb)`'s; cite it, don't copy
- A decision heuristic, with no record to walk
- Project-specific mission/goals/requirements -- that project's own ledger
- How a pass was discovered -- an ADR or devlog

## When to Add

When a design-authoring lesson recurs across two or more projects, or is
general enough to state once for all future ones. Adding one means adding it
to the sweep's tiers and to each trigger whose occasion it is due at.
