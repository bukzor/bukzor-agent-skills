# Recommendation (2026-08-23): none of the four wants a canonical; three want a plain local schema, and one is not a collection at all

Every fact below was re-derived from the live files this session. Three of
the brief's framings did not survive that: one of the four holds no
instance files, one names a category that is authored at three sites with
three different meanings, and github-manager has a *third* schema-less
collection (`principles.kb/`) the survey never listed. Locations, verified:
`~/claude/research.home-office/use-cases.kb`,
`~/claude/summer-programming-project/2026/.plan/curriculum.kb`,
`~/claude/github-manager/{goals,maintenance-actions}.kb`.

| Collection | Instance files | Frontmatter keys | Internally stable? | Sites authoring the category | `llm.kb-validate` today |
| --- | --- | --- | --- | --- | --- |
| research.home-office `use-cases` | 3 | `validated`+`current_solution` (1); `validated`+`surfaces`+`user_elbow_sitting` (1); none (1) | no | 3, three different nouns | 2 errors |
| summer `curriculum` | 0 | -- | n/a | 1, and it is a container | 2 errors, both roll-ups |
| github-manager `goals` | 5 | `principle`, `priority`, `metrics[{name,target,source}]` -- 5/5 | yes | 1 for this noun | 5 errors |
| github-manager `maintenance-actions` | 4 | `goal`, `frequency`, `duration` -- 4/4 | yes | 1, name unique fleet-wide | 4 errors |

The 20 published canonicals were enumerated directly (`find -L
~/.claude/skills -path '*/jsonschema/*.jsonschema.yaml'`); none covers
`goals`, `use-cases`, `curriculum`, `maintenance-actions`, or `principles`.
The invisibility finding is confirmed and is the guard's design, not a bug.

## research.home-office/use-cases.kb -- a permissive local `use-cases.jsonschema.yaml`, no canonical

On the merits this collection wants nothing, and that reading is
foreclosed by a standing ruling. Both belong in the record.

The merits: three files, and the two that carry frontmatter share
exactly one key. `desk-standing.md` carries none and validates clean.
Its sibling collections -- `requirements.kb` (12), `market-segments.kb`
(17), `solutions.kb` (7) -- carry no frontmatter at all, so `use-cases`
is the odd one out inside its own project rather than a member of a
fleet category. `findings.jsonschema.yaml` is already a `skill://` stub
to incident-forensics, so this project does receive fleet stubs where a
canonical exists; the absence here reflects that no fleet category
applies. Untouched since 2026-01-09.

The ruling: CANONICAL_PER_COLLECTION
(`claims.kb/design.claims.kb/every-collection-with-frontmatter-gets-a-schema.md`,
standing `user`) holds that a collection whose files carry frontmatter
and has no sibling schema gets one written -- "the ruling is to write
the schema, not to strip the frontmatter." That decides this case
against the merits argument; the paragraph above is an appeal to reopen
it, not a competing recommendation.

So: a local file admitting the observed union, every property optional,
no `required`, `additionalProperties: false` -- `validated` (date),
`current_solution` (string), `surfaces` (array of single-key objects),
`user_elbow_sitting` (string). All three files pass, the frontmatter-free
one included. Two errors to zero, twenty lines, no canonical, no fleet
claim. A schema that asserts little is the right output for a collection
whose vocabulary is genuinely unsettled; it is not an argument for
writing none.

## summer curriculum.kb -- not a collection; strike it from the list

It holds zero entries. Its members are `background.kb/`, `design/` (seven
layers, seven schemas), `discourse.kb/` (four schemas), and
`technical-policy.kb/` (a `$ref` stub) -- every one already bound. Its two
validator errors are `design.md` and `technical-policy.md`, roll-ups
sitting beside the collections they summarize, carrying only
`last-updated:`. That is precisely the false positive lane -003 owns;
ruling on it here would double-rule it. There is no such object as a
curriculum entry, so there is nothing for a `curriculum.jsonschema.yaml` to
describe. The survey's error was reading a container `.kb/` as a category.

## github-manager/goals.kb -- a local `goals.jsonschema.yaml`, no canonical

The contract already exists in prose: `goals.kb/CLAUDE.md` states
`principle:` (a `principles.kb/` path), `priority: high|medium|low`, and
`metrics[]` of name/target/source, and all five entries conform exactly.
This is transcription, not design. Single-site for this noun: the fleet's
other `goals.kb` are a design-tower layer (meta-reasoning's, already
`$ref`ing `layer-entry#base`) and a frontmatter-free prose collection
(type-theory's). A fleet grep for `^principle:`/`^metrics:` finds no other
author of this shape.

## github-manager/maintenance-actions.kb -- a local `maintenance-actions.jsonschema.yaml`, no canonical

Same story, cleaner: the name has no second author anywhere under `~/repo`,
`~/claude`, `~/.claude`, and all four entries conform to the CLAUDE.md
contract (`goal:` path, `frequency: daily|weekly|monthly|as-needed`,
`duration:`). Two local schemas take this tree from 9 errors to 0.

The honest cost side, stated plainly: nothing was caught in six months
because nothing moved. github-manager's last content change was
2025-11-05; the 2026-07-08 commit was the `.d`-to-`.kb` rename.
research.home-office froze 2026-01-09. Zero drift events across all four in
the window. The nine github-manager errors are not drift; they are a
prose contract that was never mechanized, and the value of mechanizing it
is paid on the project's next revival, not now. Note also that a *local*
schema stays invisible to the recurring guard, which keys on published
canonicals -- these two schemas buy per-tree `llm.kb-validate` cleanliness
and nothing fleet-wide. If the owner values that at less than the twenty
minutes, the honest form of "not now" is a deferral with a trigger --
not a ruling that these collections need no schema, which
CANONICAL_PER_COLLECTION has already decided the other way.

## The declined alternative: publish a `goals` canonical

Steelmanned: `goals` is the most-authored category name in the fleet --
every design tower carries `020-goals.kb`, plus github-manager and
type-theory. A canonical would give objectives one governed vocabulary
(what an objective points at, whether it must be measurable) exactly as
`layer-entry` did for design entries, and github-manager's
principle-plus-metrics shape is the most developed instance of it, so it is
the natural seed.

Declined because the sites do not share a noun. A design-tower goal is a
why-linked layer entry and already has its canonical; type-theory's are
untyped prose; github-manager's is an operationally measured objective
linked to a principle. Canonicalizing across them manufactures the
agreement rather than recording it -- the same error `status` was kept out
of `layer-entry` for. And no existing skill owns "operational objective":
publishing one would mean inventing a skill to host a single schema for a
five-file dormant collection, which is cluster 6's defect re-created
deliberately. The extraction floor is unmet in both directions: there are
no copies to reconcile, and the definition is short enough to read in
place.

## Verdict

**No canonical for any of the four. Local schemas for three. `curriculum`
struck from the list** (user, 2026-08-27).

- `research.home-office/use-cases.kb` -- a local schema admitting the
  observed union: every property optional, nothing required.
- `github-manager/goals.kb` and `github-manager/maintenance-actions.kb` --
  local schemas transcribed from each collection's own CLAUDE.md
  contract, which all nine entries already satisfy.
- `summer .plan/curriculum.kb` -- not a collection. Its two errors are
  roll-ups and belong to the roll-up scoping rule, not to this ruling.
- `github-manager/principles.kb`, surfaced during research and missing
  from the survey, needs nothing: none of its four entries carries
  frontmatter, so `CANONICAL_PER_COLLECTION` does not reach it.

Local means local -- no publication under any skill's `jsonschema/`, no
fleet category claimed, and the recurring guard stays blind to all three
by design.
