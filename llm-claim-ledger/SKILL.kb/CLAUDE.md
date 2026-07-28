# SKILL.kb -- maintenance guide

The manual: one rule per file, for everything past *reading* a ledger.
`SKILL.md` carries only what it takes to read one and points here for
the rest, so an agent that never operates a ledger never loads this
directory.

Single audience, and it is narrow — an agent with a ledger in front of
it and something to do to it. Write for that reader only. The reasoning
behind these rules lives in `../design.kb/`, and mixing the two here
costs the operator tokens they cannot skip.

## What belongs here

An operation, a propagation obligation, or a writing discipline: things
an agent *does*. If a reader can decode a ledger line without it, it
belongs here rather than in `SKILL.md`.

Directives, not claims. These files carry no frontmatter — no `label:`,
no `standing:`. A directive has no standing to contest; the decision it
implements does, and that decision is a claim in
`../design.kb/notation.kb/`.

## What does NOT belong here

- Notation a reader must decode in place — sigils, statuses, arrows,
  strikethrough -> `SKILL.md`. That is vocabulary, not lookup.
- Why a rule is the way it is -> `../design.kb/`. A sentence of
  rationale is fine where it makes the rule memorable; an argument is
  not, and a rule that needs one is under-stated.

## Filenames name their own trigger

`SKILL.md` does not enumerate this directory; it says `ls SKILL.kb/`.
That only works if each filename says when to come read it —
`retraction-propagates.md`, `changing-a-claim.md`. A name that states
the topic but not the occasion is a name that never fires.

The one exception is a term a *reader* needs, `theories.md`, which
`SKILL.md` links directly.
