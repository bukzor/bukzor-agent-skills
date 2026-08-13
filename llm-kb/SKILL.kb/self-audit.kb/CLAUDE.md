# self-audit.kb -- maintenance guide

User-facing description lives in `../self-audit.md`. This file is for
maintainers adding or revising audits.

## File shape

Required core: **Goal**, **Procedure**, **Recovery**.

- Goal -- one sentence stating the audit's pass-state.
- Procedure -- one concrete question (or a small branch). Concrete
  signals beat abstract checks.
- Recovery -- direct actions per finding-type.

Optional sections, when they earn their lines:

- **Frame** (preface) -- evaluation lens or audience stance the
  procedure presupposes.
- **When to run** / **When to skip** -- if the audit doesn't apply
  universally.
- **Non-examples / Examples** -- when the rule has high
  false-positive risk without exemplars.
- **Related** -- adjacent audits or procedures that the action might
  lead into.

Length: as short as preserves clarity for the intended Claude reader.
Run `bloat.md` after writing.

## Filename convention

`self-audit.kb/X.md` reads as "self-audit X". X is the thing audited,
kebab-case. No `audit-` or `scan-` prefix; the verb is implied by the
directory.

## What belongs here

- Proactive quality checks: ask a question, then act on the answer.

## What does NOT belong here

- Multi-step methods invoked when work calls for them, rather than
  proactively -> `../procedures.kb/`.
