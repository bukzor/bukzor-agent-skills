# The sweep sheds the asking law

`review-open-questions` was rebuilt after its walkthrough failed twice
in one sitting before a third format worked. The interesting part of
the repair was not the new format — it was noticing that most of what
the skill said was not about sweeping at all.

## What moved out, and why it must not move back

The skill had been carrying the whole ask-side form: label discipline,
the file register's shape, the multiple-projections rule, the mandate
to state a position, and a section on keeping the reply uncapped. None
of that is sweep-specific. It governs *any* turn that puts questions to
the user — a one-off approval as much as a batch of accumulated opens.
Housing it in the skill meant invoking the skill was the only way to
get it, and the far more common case (a couple of questions mid-task)
got nothing.

It now lives in a trigger-bank entry at the juncture "before asking the
user", where every asking turn meets it. The skill keeps only what is
its own: the courts and the kill list, the tally, cluster grain, where
rulings get filed, and adjudicating the reply.

Two things a later editor should not undo:

- **The skill names the juncture, not a path.** It says the trigger
  bank's entry for that juncture governs the form. It does not link
  one, because the entry is operator-local and a fleet skill that
  cites `~/.claude/...` breaks for everyone else. The trigger system
  is the wiring; naming the occasion is the whole reference.
- **It does not enumerate what that entry contains.** An earlier draft
  listed "the labels, the file register, the projections, your stated
  position" — a restatement that goes stale the moment the entry
  changes, and re-imports the duplication the split just removed.

## Rules the skill no longer states, and the failures behind them

Kept here so a future editor doesn't reinvent them in a worse form:

- The mandated five-part decision skeleton is a **ruled failure**:
  "Too often it's just five similarly-opaque phrasings of the same
  thing." Keep the intent — several genuinely different
  concretizations — never the template.
- **No length caps.** "Length is not the problem." Opacity was.
- **Routing by expected reply size was rejected**: "how is agent to
  tell if the **reply** is word-size? It can't." The file register is
  unconditional. Exemptions were explicitly deferred to a cost/benefit
  case nobody has made.
- **Rulings arrive as principles, not picks.** The skill expects
  universal-shaped replies and applies them back to the batch itself.
  Generalizing is wanted; executing beyond the batch unilaterally is
  not — wait for the call to action.

## The razor found at the end

The pass ended with the owner catching drafting-time rationale written
into the artifacts:

> "You need to distinguish between what *you* needed to know to write
> the skill and what *the agent using the skill* needs to know."

Editorial feedback given while drafting addresses the writer. Provenance
citations, "this was the recorded failure", and the argument for a rule
are all writer-facing; the acting agent needs the stance, the criteria,
and the tools. That material is not deleted, it is relocated — which is
why this file exists.

## The razor's first two audits after it was named (2026-09-01)

**`use-cases.kb/goal-gated-conditions.md`** failed it, and the
collection's own CLAUDE.md said so in advance: entries hold "the need,
what serves it today, and what 'satisficed' means — stated as effects,
not mechanisms," and solutions "graduate into a `040-design.kb/`
entry." Three of its four paragraphs were neither. The provenance
paragraph is preserved here: the shape was deployed in dotfiles
`d4a11f4` and reverted at `a19d712` within hours, when the redesign
bank entry's chain to a worked side-by-side was narrowed to `when:
writing the side-by-side`; the owner's ruling was "I want the trigger
to *prompt* writing a side-by-side at appropriate junctures." The
stripped repair paragraph — state the condition over the situation
that makes the behavior owed, usually by leaving the entry bare so it
inherits its carrier's condition, a narrower juncture being legitimate
only for a genuine sub-situation — is design, and belongs in
`040-design.kb/trigger-desc.md` when that guidance is written.

**The register's own fourth question** failed the asking law twice,
and both failures were already covered by rules I had just finished
writing. "Does the staged remainder commit as-is?" is a *fact*:
"entailed by premises already granted" catches it, the granted premise
being the owner's standing law that a closed pass persists
immediately — which I quoted inside the question, so the answer was
determined by my own framing. It also violated "each question rules
alone: answerable in any order," and I documented the violation in the
question itself ("rule those first"). The owner's verdict: "not a
well-formed question, in two ways." No amendment followed. Two rules
already caught it and I shipped anyway; noticing an order-dependency
is a stop signal, not a caveat to ship with, and adding a third rule
to catch what two rules caught would have been the wrong repair.

## On record

A fleet-carried home for the asking law is punted on a tripwire: a
repo-level `must-read.kb/` here, or an imperative-named skill
(`ask-the-user` — skill names are verb phrases or system names), waits
until an external consumer or a second fleet-wide entry needs it. Until
then the law is operator-local and the skill points at the juncture.

Narrative address: session `c78bbbb7`, 2026-08-28/29. Companion ADR:
`adr/2026-08-29-001-No-aliasing--one-body-gets-one-filename.md`.
