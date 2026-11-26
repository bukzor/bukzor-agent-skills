# skill.kb -- maintenance guide

The manual: one rule per file, for everything past *reading* a ledger.
`SKILL.md` carries only what it takes to read one and points here for
the rest, so an agent that never operates a ledger never loads this
directory.

Single audience, and it is narrow — an agent with a ledger in front of
it and something to do to it. Write for that reader only. The reasoning
behind these rules lives in `../claims.kb/design.claims.kb/`, and mixing the two here
costs the operator tokens they cannot skip.

## What belongs here

`must-read.kb/` — an operation, a propagation obligation, or a writing
discipline: things an agent *does*, each filed under the juncture that
fires it. Format and naming are `Skill(llm-must-read-kb)`. If a reader
can decode a ledger line without it, it belongs there rather than in
`SKILL.md`.

Beside the bank, `reference.kb/` holds only vocabulary a *reader* needs
and `SKILL.md` links directly — `theories.md` is the sole instance, and
a second one wants justifying.

Directives, not claims. These files carry no frontmatter — no `label:`,
no `standing:`. A directive has no standing to contest; the decision it
implements does, and that decision is a claim in
`../claims.kb/design.claims.kb/notation.kb/`.

## Quality passes live in `Skill(llm-claims-kb)`

> [!DRAFT] agent-authored 2026-11-25, vetoable

No `quality-passes.kb/`, no sweep (`LAYOUT`, fleet `authorship.kb/`).
A pass that judges the notation (standing honesty, ruling fidelity,
corollaries, confinement) is `llm-claims-kb`'s, and a bank entry here
links it at the occasion due. A chat-only quality is a lens in the
entry for its one occasion. Add a collection only for a chat-only pass
that two occasions here need. A chat has no scans to tier, so
`before/presenting-claims-to-the-user.md` does the sweep's job. Flush
moves claims into files, where `llm-claims-kb`'s sweep fires.

## What does NOT belong here

- Notation a reader must decode in place — sigils, statuses, arrows,
  strikethrough -> `SKILL.md`. That is vocabulary, not lookup.
- Why a rule is the way it is -> `../claims.kb/design.claims.kb/`. A sentence of
  rationale is fine where it makes the rule memorable; an argument is
  not, and a rule that needs one is under-stated.

## Filenames name their own trigger

`SKILL.md` does not enumerate this directory; it says
`ls -RF skill.kb/must-read.kb/`. That only works if each filename, read
together with its juncture directory, says when to come read it —
`after/retracting-a-claim.md`, `before/changing-a-claim.md`. A name that
states the topic but not the occasion is a name that never fires, and a
thesis is not an occasion: put the thesis in the body's lead sentence
and spend the filename on the trigger.
