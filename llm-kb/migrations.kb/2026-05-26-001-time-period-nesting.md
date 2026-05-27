---
status: planning
scope: |
  All `cost-benefit-sweh` frontmatter blocks across the user's tree
  (todo*.md, todo.kb/*.md, todo.d/*.md, sessions.kb/*.md,
  CLAUDE.*Task*.md). Restructures from flat field-suffix shape to
  nested time-period shape.
why: |
  The `2w` qualifier in `benefit-2w` / `cost-of-delay-2w` is structural
  (it scopes the field to a time window), not part of the field name.
  Lifting it to a key makes multi-window views natural — the same
  artifact can carry `2w:` and `6mo:` siblings under
  `cost-benefit-sweh:` without proliferating suffixes — and resolves
  the WSJF denominator/numerator window mismatch where `timebox` was
  ambiguously total-scope vs in-window slice.

  Convention decided 2026-05-25 during the rate-unrated-after-inventory-
  coverage-fix session arc.
---

# Nest cost-benefit-sweh fields under their time window

## Before / after

```yaml
# Before
cost-benefit-sweh:
  timebox:        { "@value": 1, confidence: tentative, rationale: ... }
  benefit-2w:     { "@value": 2, confidence: tentative, rationale: ... }
  cost-of-delay-2w: { "@value": 3, confidence: tentative, rationale: ... }

# After
cost-benefit-sweh:
  2w:
    timebox:       { "@value": 1, confidence: tentative, rationale: ... }
    benefit:       { "@value": 2, confidence: tentative, rationale: ... }
    cost-of-delay: { "@value": 3, confidence: tentative, rationale: ... }
```

The per-leg sub-objects (`@value` / `confidence` / `rationale`) move
unchanged; only the keys at the cost-benefit-sweh level change.

## Algorithm

For each path in `claude-open-tasks-list`:

1. Read frontmatter via `md-frontmatter`.
2. If `@value.cost-benefit-sweh.2w` already exists → no-op (already
   migrated).
3. Else restructure: `cost-benefit-sweh` becomes `{2w: {timebox,
   benefit, cost-of-delay}}` where the right-hand-side values come
   from the flat `timebox` / `benefit-2w` / `cost-of-delay-2w`
   respectively. Drop legs whose source key is absent (`cost-of-delay`
   was optional in the flat shape).
4. Write back via `md-frontmatter-set`.

## Related code change (not in this migration)

`wsjf-rank` reads `benefit-2w` / `cost-of-delay-2w` / `timebox`. It
needs an update to read the nested path instead.

**Recommended rollout:** teach `wsjf-rank` to accept *both* shapes
first (read new shape if present, else fall back to flat). Land that
change. Then run `migrate.sh` to flip all data to new shape. Then
optionally remove the flat-shape fallback in `wsjf-rank` once all
files are migrated and `validate.sh` reports clean.

The migration script does not touch `wsjf-rank` — that's a separate
commit on its own merits.

## Idempotency

- `validate.sh` is read-only; reports files still in flat shape.
- `migrate.sh` checks for `.cost-benefit-sweh.2w` first and skips
  when present. Safe to re-run.

## Known scope

~65 rated files at time of writing (per `wsjf-rank` output count).
Numbers will shift as new entries arrive; the migration applies to
whatever shape it finds.

## Rollback

The reverse transformation (nested → flat) is mechanical; rollback
script not provided. Pre-commit reversal via `git checkout --`;
post-commit via `git revert`.
