# Promote pattern recognition over promotion procedure in SKILL.md

**Date:** 2026-07-09
**Status:** Accepted

## Context

SKILL.md's "Promotion Signals" section only documented one starting
shape: a flat `.md` file with listing signals (plural filename, parallel
sections, etc.) that should become a `.kb/` directory. A user session hit
a different starting shape — an already-split ad hoc directory
(`todo.kb/reunify-dotfiles/`, one file per task) that was missing the
`.kb` suffix, a date-prefix matching its siblings, and a top-level
pointer file. None of the documented signals matched, so the agent
didn't recognize it needed promotion; the user did the reorg by hand
after asking the agent multiple times. See the paired case-study:
`../case-studies.kb/2026-07-09-000-ad-hoc-directory-promotion-not-recognized.md`.

Separately, the section's procedural detail (4 signals + 3-step promote
algorithm) turned out to be a near-verbatim, less-complete duplicate of
content already living in `SKILL.kb/self-audit.kb/promotion-signals.md`
and `SKILL.kb/procedures.kb/promote-to-collection.md`.

## Decision

Replace "Promotion Signals" with "Recognizing the Shape": state the
pattern as an end-state (homogeneous items sharing a parent → one file
per item in a `.kb/`), recognized regardless of starting form — flat
file, ad hoc directory, or scattered files — and note that a promoted
collection inherits its parent scope's existing naming convention
(e.g. a date-prefixed sibling implies the promoted collection keeps
that prefix). Demote the mechanical procedure to a single pointer at
two existing files instead of restating it. Move the section earlier,
right after Anatomy, ahead of Naming/When-to-Use.

## Alternatives Considered

### Add an "ad hoc directory" bullet to the existing signals list
- **Pros:** Minimal, directly targets the gap that was found.
- **Cons:** Treats each starting-shape as its own enumerable case; the
  list grows every time a new starting-shape surfaces; leaves the
  procedural duplication in place; doesn't address why the agent failed
  to generalize in the first place.

### Leave SKILL.md alone, only fix `self-audit.kb/promotion-signals.md`'s wording
- **Pros:** No change to the always-loaded file.
- **Cons:** SKILL.md is what actually gets read first and most often;
  the redundant procedural detail there was crowding out the
  higher-value conceptual content, which was the user's actual
  objection ("agent internalize the pattern" over "procedure spelled
  out").

## Consequences

**Positive:**
- SKILL.md net -12 lines despite adding new content.
- Recognition principle covers any non-canonical starting shape without
  needing a new enumerated signal per shape.
- Procedural detail has one authoritative home; no duplication to drift.

**Negative:**
- Agents skimming for "the 4 bulleted triggers" now read a short
  principle paragraph instead of a checklist — marginally higher
  reading cost for the common flat-file case.

**Neutral:**
- `self-audit.kb/promotion-signals.md` and
  `procedures.kb/promote-to-collection.md` unchanged; still the
  authoritative flat-file-specific checklist and steps, now referenced
  rather than restated.

## Related

- Related to: `../case-studies.kb/2026-07-09-000-ad-hoc-directory-promotion-not-recognized.md`
