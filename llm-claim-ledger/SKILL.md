---
name: llm-claim-ledger
description: "Conversational claim ledger -- the in-chat notation. Agent MUST load on `claim *` marker commands, or when a conversation's claims churn (reversals, contested points, retractions). For a ledger kept as files, load Skill(llm-claim-ledger-kb)."
---

<!-- Core: verbatim-shared with the user's claude.ai preferences.
     Merge improvements in either direction by copy-pasting this block. -->

## Claim Ledger

When claims churn, label them. A label names the locus; a trailing
sigil signs the judge -- `!` the user's call, `+` the agent's (veto
invited), `?` no one's yet -- and bare means no judge is needed: a
checkable fact, or it follows from its premises. `<-` names what a
claim rests on:

* PARSER: the crash is in the parser, reproduced on a minimal input
* MULTIBYTE+: it fires only on multibyte input (three samples, no counterexample)
* DECODER <- PARSER MULTIBYTE+: so the fix belongs in the decoder, not the parser

Policy:

1. Claim set: union over chat, last wins.
2. Every claim, both parties: sound, open, or retracted. Open claims are debt, priced by what rests on them.
3. Governance is one line over labels: `claim accept MULTIBYTE` re-signs it `MULTIBYTE!`

<!-- /Core -->

The core block alone runs in chat-only environments; typed claim kernels
and proof-transport systems are harder rungs of the same ladder, and the
invariant holds at every rung -- every claim sound, open, or retracted.

The rest of this file is what it takes to read a ledger and to name an
operation on one. What each operation *obliges* is a file apiece in
`SKILL.kb/must-read.kb/`.

> **IMPERATIVE:**
>
> Your FIRST action when this skill loads MUST be:
> `Bash("ls -RF SKILL.kb/must-read.kb/")`
>
> That listing is an index of triggers: each filename names the occasion to
> read it. Walk it while planning, before ANY action, and read every entry
> whose trigger matches the work at hand — `before/` entries must be read
> *before* the action they name, not alongside it.

## Sigils

The sigil trails the label, so the label stays a greppable prefix: `grep
XY` finds `XY`, `XY?`, `XY!`, and every reference. Sigils travel with the
label -- `XY <- AB! CD?` shows the warrant-mix exactly where weight rests
on it.

Four marks exhaust the space. A signature records *residual choice*: if
accepting every premise settles the claim, nothing was left to decide and
it stays bare, standing on its premises. Unsure whether a judgment crept
in? Sign `+` -- a needless signature invites a needless veto, but a false
bare hides a judge.

`?` and `+` both want the user's eye, for opposite things -- an answer, a
veto. One scan finds both: `grep -nE '[A-Z_][?+]'`.

## Arrows

`<-` names what a claim rests on. It is motivation, not entailment: it
says the writer had those claims in view, and nothing checks that the
conclusion follows. A closed ring -- `AB <- CD` and `CD <- AB` -- is
mutual support, which is no support at all; nothing rejects it at entry,
and the ring stays `?` until something outside it lands.

## Statuses and retraction

A sigil sometimes needs one more word; suffix the line:

    * XY: claim text                  -- certified(CHECK)

`certified(CHECK)` names the re-runnable check that discharged the claim.
A certified claim goes **bare** -- the check made it a fact -- and keeps
the note so anyone can re-run CHECK. Retraction withdraws with nothing in
its place and stays visible where it stood: `~~XY~~: claim text`, so `grep
XY` still finds it. The signatures need no verbose form; the sigil is the
record.

## Theories

`<-` tracks support -- what a claim rests on. Theories track **sense** --
what a claim cannot be read without. The two are independent: a claim can
rest on another without borrowing a word from it, and can borrow a word
without resting on it.

A **theory** is a stipulated word list -- its **ontology** -- together
with the claims confined to that list. It opens with a **defining claim**:
the label names the theory, the text states the ontology, its `<-` names
the **priors**, the theories whose words it also admits. The list comes
first and the grouping follows from it -- a claim belongs to the earliest
theory whose ontology admits every word its text needs. The theory's
standing is the defining claim's standing, and widening the ontology is a
revision to it.

- **Confinement** -- a claim uses only its own ontology plus its priors'.
  It greps: a word a theory does not admit is either a misplaced claim or
  an understated ontology.
- **Conservativity** -- a later theory never lowers a prior's standing.
  Where it seems to, the prior was wrong; fix it there.

You want a second theory when one word list stops serving every claim --
never because the list of claims got long. Twenty claims over two
vocabularies want this; a hundred over one do not.

Auxiliary theories, naming, and words that recur across theories:
`SKILL.kb/theories.md`.

## Commands

Marker commands (`Skill(llm-subtask)`); also act on your own initiative --
the core's "when claims churn" is the trigger, not a user request.

- `claim list` -- render the surviving ledger
- `claim add XY: TEXT` -- add a claim; the colon survives here alone,
  because what follows it *is* the claim line
- `claim accept XY` -- the user's ruling; re-sign `XY!`, with a clause of
  grounds -- also how a `+` graduates
- `claim contest XY` -- reopen; mark `XY?`
- `claim retract XY` -- retract and propagate
- `claim certify XY` -- name an executable check, run it; on success the
  claim goes bare, suffixed `-- certified(CHECK)`
- `claim flush` -- end-of-context extraction

Render a ledger as a list, one claim per line, in ASCII (`<-`). The last
three commands each carry a rule in the bank; `ls` it rather than guessing.

A ledger kept as files -- one claim per file, standing in frontmatter --
is `Skill(llm-claim-ledger-kb)`. Why the notation is shaped this way, and
where to argue with it: `design.ledger.md`.
