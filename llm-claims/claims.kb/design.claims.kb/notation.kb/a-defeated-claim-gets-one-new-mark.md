---
label: VOID
standing: agent
verdict: retracted
authority: "operator review, 2026-08-17: accepted only as an affordance to stop blocking on short-term, not on conviction; the mechanism below is rejected outright"
why:
  - the-sigil-signs-the-judge.md
  - settle-at-the-cheapest-judge.md
  - stipulation-is-a-legal-stop.md
---

# ~~A Defeated Claim Gets One New Mark~~ -- retracted, mechanism replaced

a-verdict-names-what-the-judge-ruled.md supersedes this: same conclusion (rejected and retracted
are one mark, chat needs none), reached from
`../purpose.kb/every-claim-sound-open-or-retracted.md` rather
than asserted, and landing on one open-vocabulary `verdict:` field
rather than a purpose-built boolean. The boolean itself is the
specific defect: a fresh field per phenomenon is the pattern
`../good-smells.kb/cheap-entry-expensive-promotion.md` and
`../purpose.kb/cheaper-to-use-than-to-ignore.md` both rule against --
it does not survive being asked "who pays for this on every claim
that never uses it," and a next phenomenon (contested? superseded?)
would have demanded a third boolean rather than a new word in an
already-open field.

`standing:` keeps naming the judge (the-sigil-signs-the-judge.md) --
unchanged. What is missing is a second axis: whether that judgment
came out for the claim or against it, which the notation has always
assumed without stating, because nothing before now needed to record
"no."

One boolean mark closes the gap: `defeated: true`, sibling to
`standing:`, present only when the answer is negative. Absent means
accepted, so every claim on file today is unchanged and needs no
migration. `standing:` under a defeat names whoever ruled the
defeat -- the-sigil-signs-the-judge.md already reads this way for a
retraction; this makes it a rule rather than an accident.

A rejected proposal and a withdrawn standing are the same mark. Which
one a reader is looking at -- whether an accepting ruling ever
preceded this one -- is a fact the body prose already carries, the
same way `authority:` elaborates a bare `standing:` today; the sigil
does not need to discriminate it, any more than it discriminates a
check from a fiat once both go bare (stipulation-is-a-legal-stop.md).

Chat form needs no new sigil either: `~~XY~~: text` already carries
this distinction in prose, the way it always has. A `-- rejected`
suffix would be a second way to say what the text already says --
declined, on the same test PROVISIONAL applies to a `superseded`
status.

Scans extend the existing pattern: `grep -rl 'defeated: true'` finds
every defeated claim, the same shape as
`grep -rl 'standing: open'`.
