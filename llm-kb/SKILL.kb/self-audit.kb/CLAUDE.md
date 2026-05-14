# self-audit.kb -- maintenance guide

User-facing description lives in `../self-audit.md`. This file is for
maintainers adding or revising audits.

## File shape

Each audit file has these sections:

- Goal -- one sentence stating what the audit's pass-state is.
- Procedure -- one question, or two if a follow-up gates a branch.
  Concrete signals beat abstract checks.
- Recovery -- one or two direct actions per finding-type.

Target ~15-25 lines. Run `bloat.md` after writing.

## Filename convention

`self-audit.kb/X.md` reads as "self-audit X". X is the thing audited,
kebab-case. No `audit-` or `scan-` prefix; the verb is implied by the
directory.

## What belongs here

- Proactive quality checks: ask a question, then act on the answer.

## What does NOT belong here

- Multi-step methods invoked when work calls for them, rather than
  proactively -> `../procedures.kb/`.
