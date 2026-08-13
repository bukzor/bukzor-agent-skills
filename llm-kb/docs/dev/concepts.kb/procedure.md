# Concept: procedure

A step-by-step method for a recurring kb task.

## Shape

Sections:

- When to use -- trigger conditions.
- Inputs -- what state must exist or be accessible.
- Outputs -- what the procedure produces.
- Steps -- ordered work, with hard gates marked.
- Hard gates -- explicit "this must complete before that" rules.
- What it prevents -- cross-references to `../failure-modes.kb/` entries
  this procedure mitigates or eliminates.
- Related -- cross-references to sibling procedures, concepts, case-studies.

## Filename discipline

**Task-shaped, not technique-shaped.** The filename names the task an agent
would describe to itself, not the technique used.

- Good: `scope-refactor.md`, `post-mortem.md`, `seed-empty-package-skeleton.md`.
- Bad: `audit-method.md`, `multi-scope-extraction.md`.

Agents searching their own situation pattern-match against task descriptions,
not technique labels.

## Distinguished from

- A principle -- softer, one-line aphorism; no steps.
- A heuristic -- soft decision rule invoked during steps; not itself a
  method.
- A concept -- definition of a thing; not a method.

## See also

- `failure-mode.md` -- what procedures mitigate.
- `principle.md` -- softer cousin.
- `case-study.md` -- source of new procedures (distilled via
  `../procedures.kb/reconcile-case-study.md`).
