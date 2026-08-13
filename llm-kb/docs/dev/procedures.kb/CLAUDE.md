# Procedures

Step-by-step methods for recurring kb tasks. See `../concepts.kb/procedure.md`
for the concept.

## What belongs here

- One file per task.
- Sections: when-to-use, inputs, outputs, ordered steps (with hard gates),
  what-prevents, related.
- Each procedure declares what failure modes it prevents
  (cross-ref to `../failure-modes.kb/`).

## Filename discipline

**Task-shaped, not technique-shaped.** Filename names the task as an agent
would describe it to itself.

- Good: `scope-refactor.md`, `post-mortem.md`, `seed-empty-package-skeleton.md`.
- Bad: `audit-method.md`, `multi-scope-extraction.md`, `conditional-promotion.md`.

The agent searching its own situation pattern-matches against the task name;
technique names are invisible.

## What does NOT belong here

- One-line aphorisms → `../principles.kb/`
- Definitions of things → `../concepts.kb/`
- Incident narratives → `../case-studies.kb/`

## Discovery

`ls -RF procedures.kb/` should be sufficient for an agent to find the right
procedure by filename alone.
