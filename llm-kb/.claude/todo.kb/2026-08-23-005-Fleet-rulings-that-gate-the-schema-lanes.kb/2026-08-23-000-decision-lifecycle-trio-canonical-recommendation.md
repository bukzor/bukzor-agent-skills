# Recommendation (2026-08-23): Canonicalize -- `llm-design-kb/jsonschema/decision-lifecycle.jsonschema.yaml`, a `#base` mixin binding the whole trio plus its conditional

All facts re-derived from live files this session; the parent brief's
census was wrong in both directions and is corrected first.

## The cluster, re-derived

Not "three hand-synced copies." Four declaration sites carry the content,
across seven consumer schema files, and one site the brief missed:

| site | form | consumers |
| --- | --- | --- |
| `design-next.kb/jsonschema/decision-lifecycle.jsonschema.yaml` | already extracted locally: draft-07 `$defs` file (no modeline), fragment-consumed | 020, 030, 040, 070 layer schemas |
| `llm-triggers/design.kb/040-design.jsonschema.yaml` | inline | itself |
| `llm-vitals/design.kb/040-design.jsonschema.yaml` | inline | itself |
| `llm-vitals/design.kb/070-future-work.jsonschema.yaml` | inline -- **unlisted in the brief** | itself |

## Drifted, or identical?

The `status` enum (`idea/proposal/accepted/rejected/superseded`,
`default: accepted`), the `blocked-on` enum (`discussion/information`),
and the superseded-requires-superseded-by conditional are semantically
identical at all four sites. Two real divergences:

| axis | design-next + llm-triggers | llm-vitals (both files) |
| --- | --- | --- |
| `superseded-by` type | file-relative path, plain string | slug, `pattern: ^[a-z0-9-]+$` -- the canonical inverse, same fork the layer-entry ruling already settled for `why` |
| descriptions | shared wording (design-next adds a future-work parenthetical) | 070 rewrote all five state glosses bespoke |

So the copies exist and demonstrably do not agree -- the extraction
floor's own trigger (`schema-reuse.md`). The drift is the same
slug-vs-path fork that cost 271 ref rewrites when `why` drifted; here it
is caught before any instance data accumulated under either type.

## Coincidence or descent?

Descent, provably. `git log --follow` on design-next's file traces to
`e047381`/`29fa802` -- the trio originated in **llm-vitals**, was copied
into design-next (`757b46b`, later extracted to the `$defs` file and
path-typed in `88b03bb`), and into llm-triggers (`57332c7`). Identical
description prose confirms copy-paste lineage. Three authors did not
independently reach for three words; one text propagated and forked.

## What the instances say

Counts over the three live towers (replication-run and `trash/`
excluded); 84 entries sit under the seven bound layer schemas:

| key | uses | values | note |
| --- | --- | --- | --- |
| `status` | 16 | all `proposal` (design-next 8, llm-triggers 4, llm-vitals 4) | the other 68 entries omit it and rest on `default: accepted` -- the default mechanism carries most of the corpus |
| `blocked-on` | 4 | all `discussion` (llm-vitals only) | declared in 7 schemas, used in 1 tower |
| `superseded-by` | 0 | -- | the conditional has never fired |

Fleet-wide, `superseded-by` and enum-overlapping `status` values appear
elsewhere only in *other vocabularies*: the ADR genre
(`proposed/accepted/superseded`), remediations.kb (`done/shipped`),
claims' 2026-08-21 `superseded-by: path[]` axis. Word overlap, not
shared shape -- none may bind to this canonical.

## Name, binding, and rival protection

**Name:** `decision-lifecycle`, never `status`. It binds one thing: the
design-entry decision lifecycle -- the 5-state enum with
`default: accepted`, `blocked-on`'s 2-state enum, path-typed
`superseded-by` (`pattern: '\.md$'`, per the layer-entry path verdict),
and the superseded-implies-superseded-by rule, folded *inside* `#base` so
consumers can no longer forget the `allOf` wiring (today six files
hand-repeat it).

The §5 rivals cannot be dragged in, by construction on four independent
grounds: (1) the recurring guard matches canonical URIs and canonical
content -- the rivals share neither; (2) `ideation.epistemics` and
chatfs's `dev.kb/claims` carry ruled-rival `$comment` markers (lane
-003's mechanism); (3) extension is conjunction, and no rival vocabulary
(`not-started/done`, `active/deferred/superseded`,
`frontier-optimal/dominated`, chatfs's `exploring/active`) is a narrowing
of this closed enum -- a `#base` extender literally cannot express them;
(4) the file's description states the boundary, as layer-entry's does.

## Shape and migration

Publisher: `llm-design-kb/jsonschema/` -- the trio's only consumers are
design towers, and llm-design-kb is the skill that already owns their
shared vocabulary (`layer-entry` lives there). Not for addressability:
`design-next.kb` is symlinked into `~/.claude/skills/` like any skill,
and `_retrieve_schema` maps `skill://<name>/<path>` straight onto
`~/.claude/skills/<name>/<path>` with no `SKILL.md` requirement
(`frontmatter_validate.py:74`), so publishing from the tower would in
fact resolve. The ground is ownership: hosting fleet vocabulary inside
one project's design tower makes every other tower a dependent of that
project's content. House two-entry-point shape, 2020-12:
open `#base` (an object mixin: three optional properties + the
conditional, no closure) and a strict root
(`$ref: "#/$defs/base"` + `unevaluatedProperties: false`). A consumer is
one line inside its existing layer-entry extender:

    allOf:
      - $ref: "skill://llm-design-kb/jsonschema/decision-lifecycle.jsonschema.yaml#base"

| consumer | breaks under canonical | edit |
| --- | --- | --- |
| design-next 020/030/040/070 | nothing (16/16 statuses in-enum; paths already) | swap the 3-property + `allOf` block for the one-line mixin; delete or stub the local `$defs` file |
| llm-triggers 040 | nothing | same swap |
| llm-vitals 040, 070 | nothing *now* -- slug `superseded-by` has 0 instances; drops the slug pattern and 070's bespoke glosses (annotations only, no validation change) | same swap; aligns with its already-mandated slug-to-path `why` rewrite |

Net data cost: zero files edited. This is the cheapest canonical the
rollout will ever get -- extraction before instance data exists under
the fork.

## Declined alternative: leave the copies (steelmanned)

The strongest case against: **twenty instances do not earn a fleet
canonical.** `superseded-by` -- the only drifted field -- has zero uses;
`blocked-on` has four, one value, one tower; the conditional has never
fired. All three towers live in one repo, plausibly one author's
convention echoing, and legislating fleet vocabulary from one repo's
habit is the exact overreach ruling #3 declines for `live:`. Cheaper
fixes exist: llm-triggers and llm-vitals could `$ref` design-next's
existing `$defs` file file-relatively (same repo), or the copies could
simply stay -- churn is near zero, and the floor warns that a reference
to a restatable definition costs more than the copy.

Why it loses anyway: the trio is not restatable from memory (two enums,
a typed field, a conditional -- the same "semantic contract" test
layer-entry failed); drift already happened despite near-zero churn; and
pointing two skills' towers at a third project's internal `$defs` file
makes that project's private vocabulary load-bearing for them --
addressing is not the obstacle (`skill://design-next.kb/...` resolves),
ownership is. But if the verdict is "too few instances," the honest
residual is: stub llm-vitals' two inline copies onto design-next's
`$defs` file today (killing the slug fork before it collects data), and
set the canonical's trigger as "a fourth tower adopts the trio, or the
first `superseded` instance lands."

## Verdict

**Canonicalize** (user, 2026-08-27).

`llm-design-kb/jsonschema/decision-lifecycle.jsonschema.yaml`, house
two-entry-point shape, with the superseded-implies-`superseded-by`
conditional folded inside `#base` so no consumer hand-repeats the `allOf`.
Seven consumer schemas swap their inline block for the one-line mixin;
design-next's local `$defs` file goes; llm-vitals drops the slug `pattern`
on `superseded-by`. Zero instance edits.

The name is `decision-lifecycle`, never `status`, and the §5 rivals stay
out -- `STATUS_ENUM` in the design ledger now carries that argument in
its own right.
