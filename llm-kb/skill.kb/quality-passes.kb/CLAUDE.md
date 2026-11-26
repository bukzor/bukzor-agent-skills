# quality-passes.kb -- maintenance guide

User-facing description lives in `../quality-passes.md`. This file is for
maintainers adding or revising passes.

## File shape

Required core: **Goal**, **Procedure**, **Recovery**.

- Goal -- one sentence stating what holds when the pass comes up clean.
- Procedure -- one concrete question (or a small branch). Concrete
  signals beat abstract checks.
- Recovery -- direct actions per finding-type.

Optional sections, when they earn their lines:

- **Frame** (preface) -- evaluation lens or audience stance the
  procedure presupposes.
- **When to run** / **When to skip** -- if the pass doesn't apply
  universally.
- **Non-examples / Examples** -- when the rule has high
  false-positive risk without exemplars.
- **Related** -- adjacent passes or procedures that the action might
  lead into.

Length: as short as preserves clarity for the intended Claude reader.
Run `bloat.md` after writing.

## Filename convention

`quality-passes.kb/X.md` reads as "quality pass X". X is the thing passed over,
kebab-case. No `pass-` or `scan-` prefix; the verb is implied by the
directory.

## What belongs here

- Proactive quality checks: ask a question, then act on the answer.

## What does NOT belong here

- Multi-step methods invoked when work calls for them, rather than
  proactively -> `../procedures.kb/`.
