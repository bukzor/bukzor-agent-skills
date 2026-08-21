# Decision (2026-08-21): design-kb layer entries get a canonical -- layer-entry.jsonschema.yaml

## Verdict

Canonicalize. Published as
`llm-design-kb/jsonschema/layer-entry.jsonschema.yaml`, plain Draft
2020-12, two entry points per house convention: a strict root
(`$ref: "#/$defs/base"` + `unevaluatedProperties: false`) and an open
`#base` anchor for extenders. A third addressable anchor, `#why`, exposes
the motivation-edge definition alone for consumers that want the field
without the entry closure. The name `layer-entry` is kept: the skill's own
vocabulary is layers, and the entry is defined by its position in the
tower; mitmproxy's `why-linked-entry` names the mechanism instead of the
role, and the bare `why` files name one field of the thing rather than the
thing. All schema and instance facts below were re-derived from the live
files this session, not taken from the survey writeup -- three of its
counts turned out wrong, noted where they matter.

The cluster, re-derived: twelve design towers, not nine projects --
meta-reasoning carries two (formal-system-2.design.kb and
design-discussion.claim.kb/design.kb), and this repo carries three
(design-next.kb, llm-triggers/design.kb, llm-vitals/design.kb). The other
seven: mitmproxy/design, summer-programming-project curriculum design,
claude-empty/design.kb, ideation.physical-musings docs/dev/design,
prototype.chatfs docs/dev/design.kb, har-browse design.kb, and
template.python-project docs/dev/design. Excluded after inspection:
prototype.llm-stet's design.jsonschema.yaml (a claim-ledger theory header,
no why) and git-partial.prototyping's discovered-constraints (an auxiliary
collection, no why). Replication-run and worktree copies are duplicates,
not additional voters.

## 6. Whether to canonicalize at all (decided first; it gates the rest)

The extraction-floor argument says a definition a reader can restate from
memory costs more as a reference than as a copy. The field data refutes
its premise here: twelve authors restated "a why-linked entry" from memory
and produced four reference systems (file-relative paths, bare sibling
filenames, unpatterned slugs, `^[a-z0-9-]+$`-patterned slugs), two
minItems positions, three requiredness policies, two dialects, and four
invented names. The naive unit `why: {type: array, items: {type: string}}`
is indeed below the floor -- but that unit is not what the projects share.
What they share, and what they each got differently, is the semantic
contract: what a why edge points at, in what form, and when it may be
absent. Copies exist and demonstrably do not agree; that is the exact
condition schema-reuse.md names for extraction. Canonicalize.

## 1. Is `why:` required? No -- requiredness belongs to the layer binding

The five-versus-four split is an artifact of reading per-layer schemas as
per-project positions. The instance data dissolves it: in motivated layers
(020-060), essentially every entry across all twelve towers carries
`why:`. The entries lacking it fall into exactly four classes: tower roots
(010-mission, in every tower), auxiliary collections (use-cases,
background -- which SKILL.md already says are not layer entries), sub-kb
leaves whose parent motivates the whole collection (chatfs
capture-pattern.kb, har-browse disclosure-surfaces.kb, design-next's
synthesis file), and summer's 070-future-work, whose schema deliberately
opts out ("picked, not derived" -- and design-next/llm-vitals take the
opposite 070 position, requiring why plus trigger). So requiredness varies
by layer and by project, never by entry shape. The canonical base leaves
`why` optional; a motivated layer binds with the three-line extender
(`$ref ...#base`, `required: [why]`, `unevaluatedProperties: false`) --
the exact pattern meta-reasoning's formal-system-2 already runs against
the real validator. No project's data is invalidated by this answer, and
the "optional" projects (summer, physical-musings) lose nothing: their
motivated-layer instances all carry why anyway, so they can adopt the
stricter binding at zero data cost or keep the plain root.

## 2. `minItems: 1`? No -- overruled; `[]` is the field's default

The survey said mitmproxy alone asserts it; re-derivation says seven of
the twelve schema sets do (mitmproxy, har-browse, design-next, llm-vitals,
llm-triggers, claude-empty, chatfs) plus meta-fs2's why unit -- it is the
majority position, not an outlier. On the instance side the whole corpus
contains exactly one `why: []`: design-discussion's mission.md, annotated
"terminus -- rests on the user's marked fiat". Every other tower expresses
the same terminus by omitting the key (or by a mission schema with no why
at all). That was the argument for `minItems: 1`, and it was overruled by the
user on 2026-08-21. The objection is decisive: an empty list is the
*default value* of an array field, and a schema that rejects its own
default is incoherent. The distribution above shows authors defaulting,
not authors legislating -- omission is equally consistent with "terminus"
and with "motivation not written down yet", and a schema cannot tell
those apart. Under-documented is not invalid.

The canonical therefore carries `default: []` and no `minItems`, and
design-discussion's `why: []` is legal as written. A future change will
make this field a dedicated path type with enforced filesystem existence;
that check, not cardinality, is the one worth having.

## 3. What is a `why` entry? A file-relative path ending in `.md`

Instance counts, over the 15 towers that carry `why:` data (574 refs).
Seven use resolvable file-relative paths -- meta-fs2 (71 refs), summer
(69), design-next (68 + 1 bare sibling filename), physical-musings (37),
meta-dd (15 + 15 sibling filenames), llm-triggers (17, including
cross-tower `../../../design-next.kb/...` refs), claude-empty (10). Six
use bare slugs: har-browse (63), llm-vitals (61, schema-enforced
`^[a-z0-9-]+$`), chatfs (39), fuser-vfs (33), mitmproxy (21), chatfs-cli
(16, resolving cross-tower into `docs/dev/design.kb`). Two use
tower-root-relative paths that do not resolve from the entry that writes
them: sttt-engine (35) and template-py (3). Correcting the survey:
har-browse's instances are slugs (`data-possession`), whatever its schema
description implies -- only design-next actually uses paths of the pair
it named.

Paths win, and not merely on count. SKILL.md already prescribes "a list of
file-relative path references", so the slug towers are non-conforming to
the skill today; paths resolve mechanically (the 2026-06-03
validate-path-references task wants exactly this), follow the same
relative-reference rules as every `$ref` in the system, and survive entry
promotion into sub-kbs, where slug uniqueness quietly breaks. The
canonical enforces the choice with `pattern: '\.md$'` -- the cheapest
guard that accepts 100% of observed conforming refs (every path and
sibling-filename ref ends in .md) and rejects 100% of observed slugs
(none do). meta-reasoning's `aliases` is not a third reference system: it
holds grep-target claim labels (KINDGRADE-style), orthogonal to why, and
stays a project extension.

## 4. Tower or entry shape? Entry shape only

The layer sets genuinely differ by design, not by drift: llm-triggers
binds only 040; summer's 070 replaces why with difficulty/concepts;
design-next and llm-vitals add a required `trigger` at 070; auxiliary
collections sit outside the numbering entirely. A canonical that fixed
010-070 as a set would invalidate live, deliberate variation. The tower
stays where it is -- SKILL.md's layer table -- and SKILL.md needs no
change for this decision. The canonical's own description says so, so a
consumer arriving via the schema learns the boundary.

## 5. Extras? All extensions -- and one future second canonical

No extra field appears in more than five towers, and the most frequent,
`status`, is four mutually incompatible vocabularies wearing one name:
not-started/done (summer 060), idea/proposal/accepted/rejected/superseded
(design-next, llm-triggers, llm-vitals), active/deferred/superseded
(physical-musings), frontier-optimal/dominated (har-browse 070 sub-kb).
Canonicalizing any of them would manufacture agreement that does not
exist. So `tags`, `aliases`, `status`, `blocked-on`, `superseded-by`,
`trigger`, `background`, `source`, `last-updated`, `ratified`, `cluster`,
and har-browse's valued axes all stay project-local, added via `#base`.

One follow-up falls out of the data: the decision-lifecycle trio is an
identical enum hand-synced across three schemas in this repo family
(design-next's decision-lifecycle.jsonschema.yaml, llm-triggers 040
inline, llm-vitals inline) -- a real above-the-floor copy cluster of its
own. It deserves its own canonical file later; it does not belong inside
layer-entry, because its consumers and its churn are different.

## Verification

The published file was behavior-tested against the repo validator
(llmd.frontmatter_validate), eleven cases, and re-run after the `minItems`
strike: strict root accepts path and sibling refs, no-why, and empty
lists, rejects slugs and extra fields; a
skill://-resolving extender enforces required-why and local closure over
added fields; the `#why` fragment resolves standalone and rejects slugs.
All as intended.

## Per-project migration (a later run applies; nothing touched now)

Layer-binding schemas in every project become stubs or three-to-six-line
extenders of `skill://llm-design-kb/jsonschema/layer-entry.jsonschema.yaml`;
that is uniform and omitted from the table. "Breaks" lists what fails
under the canonical as data stands; "data edit" is the exact fix.

| Tower | Breaks under canonical | Data edit |
| --- | --- | --- |
| meta-reasoning/formal-system-2.design.kb | Nothing; already the canonical's shape minus the .md pattern | None. Local layer-entry file becomes an extender re-anchoring `base` (canonical base + `aliases`); local why unit becomes a stub to `#why` |
| meta-reasoning/design-discussion.claim.kb/design.kb | Nothing; `why: []` is legal after the minItems override | None for mission.md. `standing` becomes an extension field |
| mitmproxy/design | All 21 why refs are slugs | Rewrite each to a path: `final-say-over-injected-behavior` -> `../010-mission.kb/final-say-over-injected-behavior.md`; same-layer refs -> `<slug>.md` |
| summer-programming curriculum design | Nothing (all why refs are paths) | None. 020-060 may adopt the required-why extender at zero cost; 010 and 070 keep local schemas (070 binds `#base` and adds difficulty/concepts, or stays standalone) |
| design-next.kb (this repo) | Nothing (paths, minItems already) | None. why unit becomes a `#why` stub; layer schemas become 2020-12 extenders carrying the lifecycle trio |
| llm-triggers/design.kb (this repo) | Nothing (paths, incl. cross-tower) | None. 040 schema becomes an extender |
| llm-vitals/design.kb (this repo) | All 61 why refs are slugs; local `^[a-z0-9-]+$` pattern is the canonical's inverse | Rewrite each slug to a path (`mission` -> `../010-mission.md`, `multi-axis-surface` -> `../020-goals.kb/multi-axis-surface.md`, ...). Recommend same rewrite for slug-typed `superseded-by`, though as an extension field the canonical does not force it |
| claude-empty/design.kb | Nothing | None |
| ideation.physical-musings docs/dev/design | Nothing (all 37 why refs are paths) | None. Extensions: `ratified` (`type: date` -- its extender must declare the llmd dialect for that to mean anything; today it sits inert under draft-07), `status`, `cluster` |
| prototype.chatfs docs/dev/design.kb | All 39 why refs are slugs | Rewrite each slug to a path (`chatfs` -> `../010-mission.kb/chatfs.md`, ...). `background` slugs are extension-local; recommend the same rewrite for consistency |
| har-browse design.kb | All 63 why refs are slugs | Rewrite each slug to a path (`data-possession` -> `../010-mission.kb/data-possession.md`, ...). 070 sub-kb keeps its frontier fields as extensions |
| template.python-project docs/dev/design | All 3 why refs are tower-root-relative, so they do not resolve from the entry | Rewrite each to file-relative (`010-mission.md` -> `../010-mission.md`). Whether the template ships a stub or a copy is the still-open template question flagged in the survey; not settled here |
| bukzor.garden/packages/sttt-engine docs/dev/design | All 35 why refs are tower-root-relative | Same rewrite. No schemas in this tower |
| prototype.chatfs docs/dev/design-incubators/fuser-vfs/design.kb | All 33 why refs are slugs | Rewrite each slug to a path. No schemas in this tower |
| prototype.chatfs packages/chatfs-cli/design.kb | All 16 why refs are slugs, resolving cross-tower into `docs/dev/design.kb` | Rewrite each to a cross-tower path. Its 040 schema is a `$ref` stub onto the project tower's (a symlink until 2026-08-21-003) |

Net data cost of the canonical: the slug-to-path rewrite in the six slug
towers plus the relative-base fix in the two tower-root-relative ones --
271 refs across 176 files, fully mechanizable except where a slug names
two entries in its own tower. Nothing is deleted: `why: []` stays legal
after the `minItems` override. The other seven towers migrate with
schema-side edits only.
