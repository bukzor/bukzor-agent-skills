---
status: planning
scope: |
  All `cost-benefit-sweh.2w.timebox` fields across rated files (i.e.,
  post-001). Renames `timebox` → `effort` 1:1. Does not auto-populate
  `wallclock`; that's a deliberate per-item judgment call.
depends-on:
  - 2026-05-26-001-time-period-nesting.md
why: |
  `timebox` was conflating two distinct physical quantities:
    1. effort — SWEh of labor required to complete the slice
    2. wallclock — calendar elapsed time the work takes to finish

  For most items the two collapse (1 SWEh of labor = ~1 day wallclock
  if pursued; close enough). For Ameriprise-class items they diverge
  drastically: ~1h labor to initiate ACATS, ~14 days wallclock for the
  transfer to clear. Cost-of-delay is denominated against wallclock
  but rating-driven prioritization is gated by effort. Collapsing
  both into one field hides the mismatch.

  Renaming `timebox` → `effort` makes the labor semantic explicit.
  `wallclock` is an *optional* sibling — present only when it differs
  meaningfully from effort. Absent means "same as effort."

  Convention decided 2026-05-25 during the rate-unrated-after-inventory-
  coverage-fix session arc.
---

# Rename timebox → effort; admit wallclock as optional sibling

## Before / after

```yaml
# Before (post-001)
cost-benefit-sweh:
  2w:
    timebox: { "@value": 1, ... }
    benefit: { "@value": 2, ... }
    cost-of-delay: { "@value": 3, ... }

# After
cost-benefit-sweh:
  2w:
    effort: { "@value": 1, ... }
    benefit: { "@value": 2, ... }
    cost-of-delay: { "@value": 3, ... }

# After, Ameriprise-class (manual addition; not done by migrate.sh):
cost-benefit-sweh:
  2w:
    effort:    { "@value": 1,    confidence: confident, rationale: ... }
    wallclock: { "@value": 0.05, confidence: confident, rationale: ... }
    benefit:   { "@value": 2,    ... }
    cost-of-delay: { "@value": 3, ... }
```

`wallclock` is denominated in 2w units like the other 2w-window
fields. `@value: 0.05` means 0.05 × 2 weeks = ~1 day; `@value: 1`
means ~2 weeks; `@value: 26` means ~1 year. Same scale as the rest.
(Or pick a unit; document on first use in the schema docs.)

## Algorithm

For each path in `claude-open-tasks-list`:

1. Read frontmatter via `md-frontmatter`.
2. Path of interest: `cost-benefit-sweh.2w.timebox`.
3. If `cost-benefit-sweh.2w.effort` already exists → no-op.
4. If `cost-benefit-sweh.2w.timebox` exists → rename to `effort` (move
   sub-object verbatim).
5. Do **not** auto-populate `wallclock`. That requires per-item
   judgment; flag candidates separately if desired.
6. Write back via `md-frontmatter-set`.

## Wallclock seed list (manual; out of script scope)

Known items where effort ≠ wallclock to a degree worth recording.
Each requires the user's judgment on the wallclock value:

- `private.evan-family/.claude/todo.kb/2026-04-17-001-exit-ameriprise-to-schwab.md`
  — effort: low (initiate ACATS); wallclock: ~14 days for transfer to
  clear; dollar-bleed accrues on wallclock.
- `private.evan-family/.claude/todo.kb/2026-04-17-000-financial-data-completeness-and-repeatability.md`
  — likely similar shape (tax window gates wallclock).

Others may surface; add as recognized.

## Related code change (not in this migration)

`wsjf-rank` reads `2w.timebox` (post-001). It needs to read `2w.effort`
after this migration. Same compat rollout pattern:

1. Teach `wsjf-rank` to read `effort` if present, fall back to
   `timebox`.
2. Land that change.
3. Run `migrate.sh`.
4. Remove the `timebox` fallback in `wsjf-rank` once `validate.sh`
   reports clean.

`wallclock` (when present) doesn't replace effort in the WSJF
denominator. The denominator stays effort; wallclock informs
cost-of-delay reasoning and the wallclock-sensitive aspects of
scope, but the unit of prioritization is labor.

## Idempotency

- `validate.sh` is read-only; reports any `2w.timebox` still present.
- `migrate.sh` checks `2w.effort` first and skips when present.

## Sequencing relative to 001

Hard depends-on. Run 001's `migrate.sh` first (nest the fields), then
002's (rename timebox → effort within the nest). Running 002 against
flat-shape files is a no-op because the path `2w.timebox` doesn't
exist yet.
