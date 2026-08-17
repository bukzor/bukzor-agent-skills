---
name: review-open-questions
description: "Agent MUST load before presenting a batch of accumulated judgment calls, approvals, or pending decisions for the user's ruling; when asked to walk through the open questions, vetoes, or decisions in a body of work; when delegated work is about to calcify (merge, promotion, publication) carrying judgment calls no user has ruled on; or when a reply of rulings (confirmations, rejections, amendments) needs adjudicating and filing."
---

# /review-open-questions [scope]

An **open** is anything still awaiting the owner's input. Its species
is what silence does: an open *veto* has a default -- the agent chose,
and silence lets the choice stand -- while an open *question* has
none, so silence stays blocked. Opens accumulate wherever work is
delegated: signed claims, design choices inside a refactor,
assumptions a document states as settled. This turn converts them into
rulings on the record. Scope defaults to the current stretch of work.

## One law: the cheapest competent court

Call anything that can settle an open a **court**, and order the
courts by cost: the record, a check, a witness, and dearest of all
the owner. Every open is settled in the cheapest court competent to
settle it, and a settlement from the wrong court is void both ways:
a fact ratified by the owner records a false judge; a stipulation
defaulted by an agent is a veto still waiting, not a ruling.

So before presenting anything, exhaust the cheap courts -- expect
them to settle most of the batch:

- **By the record.** Open lists rot, so test against the record, not
  your memory of it: the owner already ruled (cite it), intervening
  work dissolved it, or an existing ruling covers it -- then the real
  question is scope, "does that ruling bind here too?", and is
  presented as such. A silent drop is a ruling you minted. In doubt
  whether the record shows a ruling? It doesn't; the open survives.
- **By check.** Provable or fetchable without judgment: ground it
  yourself, minting what the grounding needs -- the citation, the
  sub-claim, the runnable check. A fact needs a warrant, not a fiat.
- **By witness.** "This reading fits reality" is empirical: attach
  the diff, verify command, or quote, and let it rest under standing
  veto; a signature adds nothing a witness didn't.

A kill is presented, not just performed: the owner audits the sweep
only through the kill list, and their context is empty there too.
One entry per kill, concrete twice over -- first the open in plain
words, as the owner would meet it (what was at stake, what they
would have been asked), never the codename the work coined for it;
then the settlement legible in place: the ruling's operative words
quoted, the check's one-line result shown, the change inlined as
before/after. The register citation rides along, but a hash or a
path is an address, not evidence -- the entry must convince by
itself. A kill the owner cannot verify from its own entry is void
like any wrong-court settlement: it returns to the batch.

What survives every cheaper court is the owner's jurisdiction:
stipulations -- value choices, scope, one-way doors -- usually the
minor residue of the opens they came from. However small the
residue, it still wants the walkthrough: long work accretes
vocabulary the owner never adopted, and the rebuild into plain
language is half the product.

## The owner's court

The ruling is the one output no agent can produce; the owner's
attention is the budget, and their context is empty -- they have been
skimming, which is why the opens are open. Spend accordingly:

- **Cluster grain.** Group survivors into the handful of real
  decisions, never the item inventory: a cluster earns a section when
  the owner could reject it wholesale and the rejection would mean
  something. Item-grain review manufactures fatigue wearing the
  costume of consent.
- **Order by priors**, each section leaning only on those before it.
- **Open with the tally:** swept N, the record settled M, grounding
  dissolved most of the rest, K decisions remain. The kill list
  itself goes below the decisions: it is audit trail, not payload,
  and must not stand between the owner and the rulings.

Then one numbered section per decision -- heading short, assertive,
quotable, the skeleton of the reply you want back:

1. **The priors:** what the owner must know to rule, rebuilt in
   place, in plain words, assuming nothing retained.
2. **The decision:** one or two plain sentences -- the things it
   touches, not the abstractions it instantiates; where it merely
   codifies existing practice, say so. Say what silence does.
3. **Alternatives:** the choices live at decision time, each with its
   honest appeal and honest cost. A straw man voids the ruling.
4. **If you reject:** daily-life fallout, dated -- "breaks now" vs
   "recurs forever" vs "nothing today, because"; for a question, the
   fallout of each live answer. Name the decisions that lean on this
   one.
5. **Your recommendation**, stated plainly, with its rationale -- a
   survey with no position makes the owner do your job.

Argue against yourself in place -- the caveat favoring an amendment,
the law with no police yet -- inside the section, not after the
ruling. Below the sections come the audit lists: the kills, then the
leftovers that are NOT decisions, each with why: unforced, a work
item, a fact already stated.

## The close is uncapped

The reply's value concentrates in what you failed to anticipate --
amendments, counter-questions, missing decisions, better warrants --
so the reply channel must admit the unanticipated. Never a menu,
never AskUserQuestion: option boxes cap the reply at your own
imagination, and a walkthrough tuned for easy yeses has failed even
when it gets them. End open-ended, saying concretely what you will do
with the ruling.

## The reply is a new sweep

Adjudicate it under the same law; its items sort into the same
courts:

- **Pointers to prior art** are fetchable evidence -- cheap court.
  Follow each BEFORE answering the point that cites it; mark where it
  changed your answer.
- **Questions** are new opens: answer every one, including the
  rhetorical-looking ones; a counter-question is a ruling deferred,
  so re-present its decision once answered.
- **Rationales** are warrants, often stronger than yours: file them
  into the work, credited.
- **Rulings** -- confirmations, rejections, partial ones included,
  amendments -- are the owner's court's output: file each in the
  substrate's own register, only on the owner's word. Nothing
  graduates by inference or silence; a partial rejection filed as a
  confirmation destroys the finding. Distinguish "rejects the
  decision" from "rejects your phrasing" -- the latter is a failed
  witness: re-present it, don't relitigate.

Name what stays open -- the next sweep's list -- then close with the
amended plan, compactly; execute on go.

## Registers

Rulings land in whatever register the work already keeps: claim-ledger
signings (`Skill(llm-claims)`: accepted claims re-sign `!`),
file edits, an ADR, a todo entry. The skill assumes none.

Where the register is files, it is also the *presentation* medium:
write the survivors into it, one file per decision, and let the chat
message carry the tally and the path and nothing else. Prose review
makes the owner quote your text back in order to rule on it -- toil
for them, and their multi-part reply arrives detached from what it
answered. On disk every ruling has an address, and they rule by
editing in place: the verdict, plus marginalia in their own words
wherever a rationale is worth keeping.

Then adjudicate those edits rather than merely accepting them. A
schematic edit the register's schema forbids is a ruling all the
same: implement what it means in the register's own terms, and say
plainly where you declined the literal form, and why.
