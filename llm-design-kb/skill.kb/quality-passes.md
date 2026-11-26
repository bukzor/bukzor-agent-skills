# quality-passes -- the design-record quality checks

Each pass in `quality-passes.kb/` is one way a design record breaks the rung
discipline: the walk that catches it, what a finding means, how it is
repaired. They add to `Skill(llm-claims-kb)`'s passes, which a design record
also owes. Triggers in `./must-read.kb/` link to them at the occasion each is
due.

## When to consult

- **While writing a design claim, after an edit** -- the trigger that fired
  names the passes due.
- **Before committing** -- `./procedures.kb/run-quality-passes.md` runs them
  in tiers, after `Skill(llm-claims-kb)`'s sweep.
- **At consolidation** -- `Skill(llm-claims-kb)`'s smoothing walk, which in a
  design tower applies `quality-passes.kb/each-rung-says-only-what-its-question-asks.md`
  at every node.

## Naming convention

`Skill(llm-kb)`'s: `quality-passes.kb/X.md` reads as "quality pass X".
