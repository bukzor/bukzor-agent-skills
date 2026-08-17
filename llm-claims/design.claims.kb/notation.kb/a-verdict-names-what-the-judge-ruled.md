---
label: WITHDRAWN
standing: agent
why:
  - ../purpose.kb/every-claim-sound-open-or-retracted.md
  - the-sigil-signs-the-judge.md
  - ../good-smells.kb/cheap-entry-expensive-promotion.md
---

# A Verdict Names What the Judge Ruled

Reasoned from the one invariant this notation exists to hold
(`../purpose.kb/every-claim-sound-open-or-retracted.md`): a claim is
sound, open, or retracted, and never in a fourth state where it reads
as settled to a reader who does not know otherwise. The fourth state
is exactly what happens today when a claim is judged and the answer
is no -- there is nowhere to write that, so the claim sits `standing:
agent`/`user` looking accepted. The invariant asks for exactly one
thing: a way to say "retracted" that a reader who was not there can
see. It does not ask for a taxonomy of *why*.

`standing:` keeps naming the judge (the-sigil-signs-the-judge.md),
unchanged. `verdict:` is the one new field, present only on a
negative outcome, naming what they ruled: a word, not a boolean, open
vocabulary rather than an enum, because the next phenomenon that
needs a mark should cost a new word in an existing field, not a new
field. `../good-smells.kb/cheap-entry-expensive-promotion.md` and
`../purpose.kb/cheaper-to-use-than-to-ignore.md` both price a new
field on every claim that never uses it; a new word prices nothing on
claims that don't need it and everything on the one that does, which
is where the cost belongs.

Absent means accepted, so no claim on file needs migration.
`retracted` (a prior accepted standing withdrawn), `rejected` (a
proposal that never was accepted), and `dissolved` (the claim's own
question was never well-formed, so there was no content left to
judge -- a verdict on the framing, not on what was asserted) are
three words a reader can already tell apart from body prose, the same
way `authority:` elaborates a bare `standing:` without a second sigil
today; none earns its own field. Chat form needs no new mark either:
`~~XY~~: text` already carries whichever word applies, the way it
always has.

Scan: `grep -rl 'verdict:'`. Supersedes VOID and MOOT
(a-defeated-claim-gets-one-new-mark.md,
a-dissolved-question-is-not-a-verdict.md) -- both reached a version of
this conclusion by assertion, before checking it against the
invariant that actually decides it.
