# SKILL.kb -- maintenance guide

One rule per file, for everything past *reading* a ledger. `SKILL.md`
carries only what it takes to read one and points here for the rest, so
an agent that never operates a ledger never loads this directory.

## What belongs here

A rule an agent applies while running a ledger: an operation, a
propagation obligation, a structural discipline. If a reader can decode
a ledger line without it, it belongs here rather than in `SKILL.md`.

## What does NOT belong here

- Notation a reader must decode in place (sigils, statuses, arrows,
  strikethrough) -> `SKILL.md`. It is not lookup; it is vocabulary.
- Criteria for *judging* this notation against alternatives ->
  `design.kb/good-smells.kb/`. Those grade the design; these run it.

## Governed by the skill itself

Each entry is a claim in this skill's own ledger and carries its
`label` and `standing` in frontmatter (`SKILL.jsonschema.yaml`).
Standing is the sigil spelled out, so `grep -l 'standing: open'` is the
open-claims scan the skill prescribes, run on the skill. Labels are
unique across this collection *and* `design.kb/good-smells.kb/` — one
namespace, because a claim here may cite a criterion there.

Fiat entries (`standing: fiat`) are revocable on sight: they record
where an agent settled an underdetermined point without being asked.

## Filenames name their own trigger

`SKILL.md` does not enumerate this directory; it says `ls SKILL.kb/`.
That only works if each filename says when to come read it —
`retraction-propagates.md`, `changing-a-claim.md`. A name that states
the rule's topic but not its occasion is a name that never fires.

The one exception is a term a *reader* needs (`theories.md`), which
`SKILL.md` links directly.
