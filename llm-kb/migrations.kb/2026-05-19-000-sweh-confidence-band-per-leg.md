---
status: in-progress
scope: |
  All cost-benefit-sweh legs (timebox/benefit-2w/cost-of-delay-2w, or
  post-001/post-002 their nested counterparts) across rated files.
  Each leg must carry a `confidence:` band from the 5-band vocabulary:
  hypothetical | tentative | unsure | confident | certain.
originating-commits:
  - 87f1c6c   # 2026-05-19: sweh: add optional cost-of-delay-2w and confidence fields
  - fc8c346   # 2026-05-19: sweh: 5-band probability confidence vocab; re-rate schema-reuse-with-ref
why: |
  Initial SWEH ratings carried only `@value` + `rationale` per leg.
  The 2026-05-19 schema evolution (fc8c346) introduced an optional
  `confidence:` band on each leg, drawn from a 5-band probability
  vocabulary. `wsjf-rank` uses confidence to compute exec_score
  (pessimistic) and swing (band uncertainty).

  Legs without confidence default to `unsure` in the consumer's math.
  That's a sensible default but visually indistinguishable from
  "deliberately rated as unsure" — the field's absence loses
  information. Filling in explicit confidence brings drift between
  intent and signal back into alignment.

  The new field is "optional" by schema but "recommended" by usage:
  every newly-written rating should carry it. Older ratings absorbing
  the default are technical debt that this migration tracks.
---

# Add confidence band to every cost-benefit-sweh leg

## Algorithm

`validate.sh` walks inventory-visible rated files, reads each leg of
`cost-benefit-sweh` (or its nested-2w counterpart per migration 001),
and reports legs that are objects with `@value` but no `confidence`.

Output format:

    <path>:<leg-key>

Where `<leg-key>` is one of `timebox` / `benefit-2w` /
`cost-of-delay-2w` (flat shape) or `2w.timebox` / `2w.benefit` /
`2w.cost-of-delay` (nested shape, post-001 and post-002).

No `migrate.sh` is provided. The confidence value requires per-leg
judgment — defaulting to `unsure` loses the migration's information.
The user reviews each flagged leg and assigns an honest band.

## Judgment guide (excerpt from the 5-band vocabulary)

- `hypothetical` (≤20% true value within 2× band): pure guess; revisit
  when data exists.
- `tentative` (~50%): plausible but not anchored.
- `unsure` (~60%): default; no strong belief either way.
- `confident` (~80%): backed by documented dollar flows, comparable
  rated items, or concrete blocking relationships.
- `certain` (~95%): re-runnable check confirms the number.

See `bukzor-agent-skills/llm-subtask/jsonschema/todo.jsonschema.yaml`
for the canonical vocabulary (propagation drift is no longer a concern:
all copies are now `$ref` stubs onto that file).

## Idempotency

Read-only validator; trivially idempotent. Per-file confidence
additions are themselves idempotent — once a band is set, it stays.

## Why "applying" not "applied"

Many older ratings (pre-2026-05-19 or otherwise) still lack
per-leg confidence. New ratings within the user's recent re-rate
sweeps carry it; the older long tail is what this migration tracks.
