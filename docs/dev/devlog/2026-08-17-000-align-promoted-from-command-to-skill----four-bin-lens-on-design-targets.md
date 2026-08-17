# Devlog: 2026-08-17 — align promoted from command to skill -- four-bin lens on design targets

## Focus

Census of the 2026-08-16/17 verdict batch (see `docs/dev/align.claims.kb/`,
committed in b7b89c0), and standardizing what that census taught: /align
gains a conditional procedure for design-bearing targets.

## Decisions

### /align moves from ~/.claude/commands/ to a skill here

**Rationale:** The four-bin sort (below) is a conditional lens — it applies
only when the target embodies design decisions — and the fleet pattern for
conditional procedure is a `SKILL.kb/` procedure named by a
`SKILL.kb/must-read.kb/` trigger. Commands can't carry that structure; skills
do, and the harness routes `/align` to a skill named `align` just as well
(smoke-tested before deleting the command).
**Alternatives considered:** Inlining the four bins into the command body —
rejected: it would load on every /align including flat-prose targets, and
grows without the trigger discipline.

### Four-bin sort for design targets

An alignment pass over design work sorts each extracted goal into exactly
one of: rules (filter the design space), heuristics (sort it), short-term
plan, long-term plan. Rules first and fullest. A goal that straddles bins is
more than one goal — split it. Provenance: the unsorted first extraction of
the verdict-batch census conflated the bins and cost a full round trip.
Probationary: the next /align run over a design target discharges or defeats
the procedure (`align/SKILL.kb/sort-goals-into-four-bins.md`).

## Conventions Established

- `force:` grade names the kind (user ruling, recorded in
  `docs/dev/align.claims.kb/CLAUDE.md`): `must` is a rule, `should` is a
  heuristic; a file bundling both is two files.

## Open Questions

- Census lifecycle: `align.claims.kb/` contents are per-batch; the batch has
  committed, so they may be cleared or repopulated at the next review.

## References

- b7b89c0 — census + batch acceptance; 5fdfc5f — WITNESS todo
- `align/SKILL.md`, `align/SKILL.kb/`
- `~/.claude` repo: `commands/align.md` deleted the same session
