# quality-passes -- the ledger-specific quality checks

Each file in `quality-passes.kb/` is one way a claims.kb rots: the walk or
scan that catches it, what a finding means, how it is repaired. They add to
`Skill(llm-kb)`'s passes, which a claims.kb also owes. Triggers in
`./must-read.kb/` link to them at the occasion each is due.

## When to consult

- **While writing a claim file, after an edit** -- the trigger that fired
  names the passes due.
- **Before committing a batch of claims** --
  `./procedures.kb/run-quality-passes.md` runs them in tiers, after
  `Skill(llm-kb)`'s sweep.
- **At consolidation** -- `quality-passes.kb/smoothing.md`, the walk over
  every node of the ledger. No per-commit tier runs it.

## Naming convention

`Skill(llm-kb)`'s: `quality-passes.kb/X.md` reads as "quality pass X", the
filename naming the quality passed over.
