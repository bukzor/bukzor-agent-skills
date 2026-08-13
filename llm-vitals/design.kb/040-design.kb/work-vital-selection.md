---
why:
  - reduce-dropped-tasks
  - counter-tech-revenue-bias
status: proposal
blocked-on: discussion
---

# Work Vital Selection

The five recommended work vitals (revenue, customer, tech,
maintenance, exploration) emerged by **enumeration**, not by the
analytical process used for wellness vitals. Recording for revisit.

## Current set

- `revenue` — paid work; floor on hours/week
- `customer` — non-revenue customer obligations; floor on
  days-since-touched
- `tech` — technical work; no floor (fills itself)
- `maintenance` — keeping infrastructure alive; floor on hours/week
- `exploration` — rabbit holes (deep work with uncertain payoff);
  **ceiling** enforced by rabbit-hole budget

## What's missing from this design entry

Compared to `wellness-vital-selection.md`, this entry lacks:

- Explicit selection criteria for what counts as a work vital
- Taxonomies surveyed (do "core/context" categories help? what
  about lean's value/non-value-adding split?)
- Per-vital deliberation
- Alternatives considered and rejected

## What would deepen it

- Apply the wellness-selection criteria (independent predictor,
  rots independently, working-memory cap, covers non-task domains)
  to the work domain. Likely the criteria need adjustment — work
  is task-shaped where wellness is not.
- Survey relevant prior art: PARA (Tiago Forte), GTD project
  categories, OKR objectives, lean value streams.
- Reconsider whether `tech` is a vital at all if it has no floor
  (it might be a default residual category, not a vital).
- Reconsider whether `customer` and `revenue` should be separate
  or merged.

Trigger to deepen: when implementation requires per-work-vital
configuration (thresholds, kinds), or when the operator notices
work-vital tracking is failing in characteristic ways.
