---
name: list-open-questions
description: "Agent MUST load when asked what is open, what needs the user's input, or to walk through open questions, pending decisions, or open vetoes; when a reply of rulings (confirmations, rejections, amendments) needs filing; or when delegated work is about to calcify (merge, promotion, publication) carrying judgment calls no user has ruled on."
---

# /list-open-questions \[paths\]

An open is anything still awaiting the user's input, and it comes in
two species. An open *question* has no default: work is blocked on
it, or an agent declined to choose. An open *veto* has one:
delegated work runs on silence-is-consent -- the agent made a
judgment call, the user's veto is invited, and silence lets it
stand. Vetoes accumulate wherever work is delegated: agent-signed
claims, design choices inside a long refactor, a review's proposed
edits, assumptions a document states as if settled. This turn walks
the user through the opens and converts their reply into rulings on
the record. Every item presented says which species it is -- what
silence does is part of the question.

Paths scope the sweep; without them, sweep the current stretch of
work.

## Why, before how

The user's ruling is the one output no agent can produce -- every
other layer of the work can be regenerated, delegated, or checked
mechanically; this one exists only if the user makes it. Their
attention is also the budget the turn spends: a real reply costs an
hour. So everything below serves making that hour land on decisions
-- and expect the amendments, not the confirmations, to carry the
value. A walkthrough tuned for easy yeses has failed even when it
gets them.

## Settle by the record first

Open lists rot: work lands between when an open is queued and when
the user shows up. Before presenting anything, test every open
against current ground truth -- the record, not your memory of it.
An open dies here when the user already ruled on it somewhere (cite
the ruling), when intervening work dissolved it (the thing it
decided no longer exists, or a settled claim fixes its answer), or
when evidence you can fetch yourself settles it without user
judgment. Close each kill with its citation -- a silent drop is a
ruling you minted -- and open the walkthrough with the tally: swept
N, the record settled M, K remain. Expect most opens to die here;
that is the pass working. When in doubt whether the record shows a
ruling, it doesn't: present the open.

## Act grain

Group the survivors into acts -- the handful of real decisions,
never the item-by-item inventory. An act is a cluster of items that
stand or fall together because they implement one choice; the test:
the user could reject the act wholesale and the rejection would mean
something. Item-grain review manufactures fatigue wearing the
costume of consent -- thirty rulings from someone who cannot hold
thirty contexts are not judgments.

## The walkthrough

Order the acts so each one's priors were established by the acts
before it. For each act, concrete and in plain language:

1. **The priors** -- what the user must know to rule, established in
   place, assuming they retained nothing. The user has been
   skimming; that is why the opens are open.
2. **What the act decides.** Name the things it touches, not the
   abstractions it instantiates.
3. **What else could be chosen** -- alternatives that were live at
   decision time, not strawmen.
4. **The fallout** -- of rejecting a veto, of each live answer to a
   question: what unwinds, what re-opens, which later decisions lose
   their footing. An act with no stated fallout has not been offered
   up for a real decision.

## The rulings

Expect the reply to mix confirmations, rejections -- partial ones
included -- amendments, counter-questions, decisions the walkthrough
missed, and pointers to prior art. Three moves:

- **File what it settles.** Record each ruling in the substrate's
  own register -- a standing flipped, an edit made, an item closed
  -- and only on the user's word: nothing graduates to user-ruled by
  inference or by silence. A partial rejection filed as a
  confirmation destroys the finding.
- **Answer what it asks.** A counter-question is a ruling deferred;
  answer it and re-present that act.
- **Name what stays open.** The residue is the next sweep's open
  list; leaving it unnamed re-opens the silence window this turn
  closed.
