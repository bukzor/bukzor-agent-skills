---
name: decision-review
description: "Agent MUST load before presenting a batch of accumulated judgment calls, approvals, or pending decisions for the user's ruling; when asked to walk through the decisions, open vetoes, or open questions in a body of work; or when a reply of rulings (confirmations, rejections, amendments) needs adjudicating and filing."
---

# /decision-review [scope]

An **open** is anything still awaiting the user's input, in two
species. An open *question* has no default: work is blocked on it, or
an agent declined to choose. An open *veto* has one: the agent made a
judgment call under silence-is-consent, and silence lets it stand.
Vetoes accumulate wherever work is delegated -- signed claims, design
choices inside a refactor, assumptions a document states as settled.
This turn walks the owner through the opens and converts their reply
into rulings on the record; every item presented says which species it
is, because what silence does is part of the question.

Scope defaults to the current stretch of work.

The ruling is the one output no agent can produce; the owner's
attention is the budget the turn spends. Everything below serves
making that attention land on real decisions -- and expect the
amendments, not the confirmations, to carry the value. A walkthrough
tuned for easy yeses has failed even when it gets them.

## Settle by the record first

Open lists rot: work lands between queueing and ruling. Test every
open against the record before presenting it. An open dies when the
user already ruled (cite the ruling), when intervening work dissolved
it, or when evidence you can fetch settles it without judgment. Close
each kill with its citation -- a silent drop is a ruling you minted.
In doubt whether the record shows a ruling? It doesn't; the open
survives.

## Factor the survivors

Three kinds; only the third gets a section:

- **Facts** -- checkable, or entailed by granted premises. Ground them
  yourself, minting whatever the grounding needs (citation, sub-claim,
  runnable check); a fact needs a warrant, not a fiat.
- **Adequacy** -- "this reading fits reality." Attach the witness
  (diff, verify command, quote) and let it rest; a signature adds
  nothing a witness didn't.
- **Decisions** -- value choices, scope, one-way doors: nothing
  external can ground them. Usually the minor residue of the open they
  came from. A decision restating a ruling made elsewhere is really a
  scope question -- "does that ruling bind here too?" -- so present it
  as one.

Expect the factoring to collapse the list; the incident that taught it
went 27 -> 8. One or two decisions don't want this skill: ask inline.

## Group and order

Cluster the residue into the handful of real decisions, never the
item-by-item inventory: a cluster earns a section when the owner could
reject it wholesale and the rejection would mean something. Item-grain
review manufactures fatigue wearing the costume of consent. Order the
sections so each one's priors were established by those before it, and
open with the tally: swept N, the record settled M, grounding
dissolved most of the rest, K decisions remain.

## The walkthrough

One numbered section per decision. The heading is short, assertive,
quotable -- it is the skeleton of the reply you want back. Four parts,
plain and concrete:

- **The priors:** what the owner must know to rule, established in
  place, assuming they retained nothing. They have been skimming; that
  is why the opens are open.
- **The decision:** what is being decided, in one or two plain
  sentences -- the things it touches, not the abstractions it
  instantiates. Where it merely codifies existing practice, say so.
- **Alternatives:** the choices that were live at decision time, each
  with its honest appeal and its honest cost, inline. A straw man here
  voids the ruling you're asking for.
- **If you reject:** daily-life fallout, dated -- "breaks now" vs
  "recurs forever" vs "nothing today, because" -- and for a question,
  the fallout of each live answer. Name the other decisions that lean
  on this one.

Argue against yourself in place: the caveat that favors an amendment,
the law that has no police yet, the weakness you'd otherwise save for
the defense -- inside the section, not after the ruling.

Below the sections, list the leftovers that are NOT decisions, each
with why: unforced, a work item, a fact already stated.

## The close

End open-ended, never a menu: "Rule in any form you like -- accept
1-8; accept all but 6, argue 6; per-item amendments" -- and say
concretely what you will do with the ruling. Never AskUserQuestion:
option boxes cap the reply, and the freeform detailed ruling is the
payload the whole exercise was bought for.

## Adjudicating the reply

The reply will mix confirmations, rejections -- partial ones included
-- amendments, counter-questions, decisions the walkthrough missed,
and pointers to prior art. Take its points in order:

1. Follow every pointer to prior art BEFORE answering the point that
   cites it; mark where it changed your answer.
2. Answer every question, including the rhetorical-looking ones; a
   counter-question is a ruling deferred, so re-present its decision
   once answered.
3. The owner's rationales are often stronger than your warrants; file
   them into the work, credited.
4. Distinguish "rejects the decision" from "rejects your phrasing":
   re-present the latter, don't relitigate it.
5. File what the reply settles, in the substrate's own register -- and
   only on the owner's word: nothing graduates to user-ruled by
   inference or by silence, and a partial rejection filed as a
   confirmation destroys the finding.
6. Name what stays open -- the next sweep's list -- then close with
   the amended plan, compactly; execute on go.

## Where rulings land

Whatever register the work already keeps: claim-ledger signings
(`Skill(llm-claim-ledger)`: accepted claims re-sign `!`), file edits,
an ADR, a todo entry. The skill assumes none in particular.

Distilled from a 2026-08-09 ruling session over the strata ledger,
then merged with `Skill(list-open-questions)`'s independent
distillation of the same turn. The factoring rule also stands at
personal scope:
`~/.claude/must-read.kb/before/asking-the-user-to-approve-or-ratify.md`.
