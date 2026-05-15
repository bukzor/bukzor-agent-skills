# Methodology kb (self-applied)

This skill (`llm-kb`) applies its own pattern to its own methodology. The
collections under `docs/dev/` are the result.

## Architecture

`procedures.kb/` is the **primary surface**. Filenames are task-shaped -- the
agent's mental description of what they're doing -- discoverable via
`ls -RF procedures.kb/`. When the user asks for a recurring kb task, find
the matching procedure first.

Procedures reach into **auxiliary collections** via cross-references:

- `failure-modes.kb/` -- what each procedure prevents. Many-to-many: a mode is
  prevented by multiple procedures; a procedure prevents multiple modes.
  Frontmatter fields `mitigated-by:` and `eliminated-by:` express the linkage.
- `case-studies.kb/` -- first-person narratives of instructive incidents. Raw,
  not authoritative on the items they name (see `concepts.kb/case-study.md`
  for the authority asymmetry).
- `concepts.kb/` -- structured definitions of *things* procedures operate on
  (a kb, a scope, a split, an audit). Distinct from a glossary: concepts have
  shape, authority, and relationships.

**Planned but not yet seeded:**

- `templates.kb/` -- output shapes procedures produce (audit table, debrief
  structure, ADR format). Procedures will cross-ref instead of inlining.
- `heuristics.kb/` -- soft decision rules invoked during procedure steps
  ("when in doubt, prefer smaller scope"). Distinct from principles
  (aphorisms) and procedures (multi-step methods).

**Flat support files** (promote to `.kb/` when growth pressure warrants):

- `glossary.md` (future) -- one-line word-to-meaning entries.
- `principles.md` (future) -- memorable methodological aphorisms.

## Authority asymmetry: raw vs distilled

**Case-studies are raw narrative**, captured before context expires. They name
failure modes, principles, and methodologies the writer perceives -- but those
names are *provisional*. The distilled collections (failure-modes.kb/,
procedures.kb/, future principles.kb/, etc.) are *authoritative* for their
respective content types. Case-studies cite distilled entries; case-studies do
not override them.

Capture (session → raw case-study) is the generic skill-level
procedure `../../SKILL.kb/procedures.kb/post-mortem.md`. Reconciliation
(raw → distilled) is `procedures.kb/reconcile-case-study.md`. The
split runs in disjoint contexts: the capturing agent stops at `raw`;
a fresh-context agent does the editorial pass.

## Filename discipline (cross-cutting)

For procedures specifically: **task-shaped, not technique-shaped.**

- Good: `scope-refactor.md`, `post-mortem.md`, `seed-empty-package-skeleton.md`.
- Bad: `audit-method.md`, `multi-scope-extraction.md`,
  `conditional-promotion.md`.

Agents pattern-match filenames against their mental description of the task,
not against technique labels. Discovery via `ls -RF procedures.kb/` works
*only if* names are task-shaped.

## Discovery model

The bet: an agent invoking this skill scans `ls -RF docs/dev/procedures.kb/`,
finds a task-shaped filename matching its situation, and loads that file. The
procedure's content directs the agent to the relevant auxiliary collections
via explicit cross-references. This works as long as:

1. Procedure filenames stay task-shaped (filename discipline above).
2. Each procedure declares what it prevents (frontmatter cross-refs to
   failure-modes.kb/).
3. Concepts are stubbed on first mention, so cross-references always resolve
   (per `../../SKILL.kb/must-read/when/introducing-a-novel-term.md`).

When any of these slips, the discovery model degrades to "agent reads
everything." That's a fallback, not the design.

## See also

- `../../SKILL.md` -- the `llm-kb` pattern itself.
- `../../SKILL.kb/procedures.kb/post-mortem.md` -- captures session
  into a raw case-study (skill-level, used by any consumer).
- `procedures.kb/reconcile-case-study.md` -- distills a raw case-study
  into authoritative entries (skill-internal).
- `case-studies.kb/2026-05-13-000-har-browse-rust-port-scope-refactor.md` --
  the seed case-study; the incident whose debrief produced this methodology kb.
