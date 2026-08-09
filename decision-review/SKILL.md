---
name: decision-review
description: "Slash-command: /decision-review [scope] -- walk the owner through the judgment calls in a body of work: each decision in plain language, with alternatives and the fallout of rejecting. Agent MUST load on /decision-review, or before presenting a batch of accumulated judgment calls for the user's ruling."
---

# /decision-review [scope]

Take a body of work -- a formalization, a review's adjudications, a
refactor, this conversation -- and walk its owner through the
**decisions** in it: the judgment calls that are genuinely theirs. The
deliverable is a numbered walkthrough the owner can answer inline,
quote by quote, in one sitting.

Scope defaults to the judgment calls accumulated in the current
conversation.

## Factor first

Sort every pending item into three kinds; only the third gets a
section:

- **Facts** -- checkable, or entailed by granted premises. Run the
  check, cite the source, state them. Never ask.
- **Adequacy** -- "this summary/model/reading fits reality." Attach the
  witness (diff, verify command, quote) and invite veto; silence is
  consent.
- **Decisions** -- value choices, scope, one-way doors. These are the
  review.

Expect the factoring to collapse the list; the incident that taught it
went 27 -> 8. More than ~10 sections means facts and adequacy crept
back in. One or two decisions don't want this skill: ask inline.

## The walkthrough

One numbered section per decision. The heading is short, assertive,
quotable -- it is the skeleton of the reply you want back. Three parts,
always:

- **The decision:** what is being decided, in one or two plain
  sentences. Concrete over abstract; where it merely codifies existing
  practice, say so.
- **Alternatives:** the genuinely viable other choices, each with its
  honest appeal and its honest cost, inline. A straw man here voids the
  ruling you're asking for.
- **If you reject:** daily-life fallout, dated -- "breaks now" vs
  "recurs forever" vs "nothing today, because". Name the other
  decisions that lean on this one.

Argue against yourself in place: the caveat that favors an amendment,
the law that has no police yet, the weakness you'd otherwise save for
the defense -- inside the section, not after the ruling.

Below the sections, list the leftovers that are NOT decisions, each
with why: unforced, a work item, a fact already stated.

## The close

End open-ended, never a menu: "Rule in any form you like -- accept 1-8;
accept all but 6, argue 6; per-item amendments" -- and say concretely
what you will do with the ruling. Never AskUserQuestion: option boxes
cap the reply, and the freeform detailed ruling is the payload the
whole exercise was bought for.

## Adjudicating the reply

The reply will be amendments and re-groundings more than accept/reject.
Take its points in order:

1. Follow every pointer to prior art BEFORE answering the point that
   cites it; mark where it changed your answer.
2. Answer every question, including the rhetorical-looking ones.
3. The owner's rationales are often stronger than your warrants; file
   them into the work, credited.
4. Distinguish "rejects the decision" from "rejects your phrasing":
   re-present the latter, don't relitigate it.
5. Close with the amended plan, compactly; execute on go.

## Where rulings land

Whatever medium holds the work: claim-ledger signings
(`Skill(llm-claim-ledger)`: accepted claims re-sign `!`), file edits,
an ADR, a todo entry. The skill assumes none in particular.

Distilled from a 2026-08-09 ruling session over the strata ledger. The
factoring rule also stands at personal scope:
`~/.claude/must-read.kb/before/asking-the-user-to-approve-or-ratify.md`.
