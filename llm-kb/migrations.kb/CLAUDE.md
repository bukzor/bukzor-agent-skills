# migrations.kb/ — schema and convention migrations

## What belongs

A migration: a decision + a transformation + a scope + a status,
captured in a re-runnable shape. Examples:

- Schema field renames (`benefit-2w` → nested `2w.benefit`)
- Format conventions (`-` bullets → `- [ ]` for tracked tasks)
- Directory restructures (`.d` → `.kb`)
- Naming conventions (OR-class kbs gain `.oneOf.kb` suffix)
- New-field rollouts (introduce `cardinality:`)

Each entry is a single `$DATE-NNN-$SLUG.md` with frontmatter (status,
scope, supersedes, why) and prose rationale. When the migration carries
executable form (`migrate`, `validate`, optionally `rollback`), those
live in a sibling same-stem directory:

    migrations.kb/
      CLAUDE.md
      2026-05-26-000-some-migration.md      # the entry; rationale + status
      2026-05-26-000-some-migration/        # only when scripts exist
        migrate.sh                          # language case-by-case
        validate.sh

Convention-only migrations (pure-prose conventions with no transformer)
omit the sibling directory.

## What does NOT belong

- **Decisions without transformation** → `decision.kb/` (ADR-like)
- **One-off scripts** without durable rationale → `trash/` or `bin/`
- **Active tasks** waiting to be done → `todo.kb/` (until the work
  generalizes into a re-runnable migration)
- **Principles** (always do X) → `principle.kb/`

## Cardinality

`and` (implicit default; every .kb is `and` unless its name carries the
`.oneOf` suffix). Every migration is independently required. A
migration whose `scope:` matches zero files in some subtree applies
vacuously — that's no-op evaluation under and/all, not a third class.

## Idempotency (load-bearing)

Every executable in a migration must be **idempotent**. Re-running
must be safe. The whole point of the .kb is that migrations can be
applied as-needed, batched, or pivoted later — none of which is
possible without idempotency.

The contract:

- `validate.sh` is read-only; reports candidates or drift.
- `migrate.sh` either transforms in-place or no-ops if already done.
- `rollback.sh` (optional) is also idempotent.

Migrations that violate idempotency are anti-pattern; reject them at
review.

## Status vocabulary (fine gradation)

Linear lifecycle, choose the most-advanced stage that's true:

- `tentative` — idea floated; entry may not exist yet, certainly no scripts
- `planning` — entry written, decision recorded, scripts may exist but haven't run
- `started` — first execution; small subset applied to verify approach
- `in-progress` — substantially applying; multiple sweeps done; more to do
- `complete` — fully applied within declared scope; no known residual
- `verified` — `complete` AND a recent audit (e.g., `validate.sh` clean) confirms no drift
- `archival` — kept for history; the rule no longer applies (superseded, abandoned, or fully absorbed into something else)

## Kind (orthogonal to status)

- `one-shot` (default; field omitted) — finishes; reaches `complete` then maybe `verified`
- `recurring` — never one-shot-finishes; `validate.sh` runs forever to flag drift. May still be `complete`/`verified` in the sense "the rule and validator are in place."

Migrations that were pivoted-away-from become `archival`; the entry stays as the trace. Migrations that were rolled back become `archival` too, with prose explaining why.

## When to add

When a schema or convention change is about to touch >1 file across
the user's tree. Smaller changes can live in `todo.kb/` until the
generalization warrants migration shape.

## Sibling-dir naming

Same stem as the entry, no `.kb` suffix. The sibling is a plain script
bundle, not a kb-class collection — no `CLAUDE.md`, no nested entries.

This mirrors the `$NAME.md + $NAME.kb/` promotion pattern but uses a
non-`.kb` sibling because the directory holds executables, not
knowledge entries.
