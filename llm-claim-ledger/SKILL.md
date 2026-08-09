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
3. Governance is one line over labels: `claim accept: MULTIBYTE` re-signs it `MULTIBYTE!`

<!-- /Core -->

The core block alone runs in chat-only environments; typed claim kernels
and proof-transport systems are harder rungs of the same ladder, and the
invariant holds at every rung -- every claim sound, open, or retracted.

The rest of this file is what it takes to *read* a ledger. Everything
past reading is one file per rule in `SKILL.kb/`, each named for its own
trigger: `ls SKILL.kb/` is the index, and you read the ones whose names
match the work.

## Sigils

The sigil trails the label, so the label stays a greppable prefix:
`grep XY` finds `XY`, `XY?`, `XY!`, and every reference. Sigils go
wherever the label goes: `XY <- AB! CD?` shows the warrant-mix exactly
where weight is placed on it.

Four marks exhaust the space -- no judge needed, user, agent, no judge
yet. A signature records residual choice: if accepting every premise
settles the claim, nothing was left to decide, and the claim stays
bare -- its standing rides its premises. Unsure whether a judgment
crept in? Sign it `+`: a needless signature invites a needless veto,
but a false bare hides a judge.

`?` and `+` both want the user's eye, and want opposite things -- `?`
an answer, `+` a veto. One scan finds both: `grep -nE '[A-Z_][?+]'`.

## Statuses

A sigil sometimes needs one more word; suffix the line:

    * XY: claim text                  -- certified(CHECK)

`certified(CHECK)` names the re-runnable check that discharged the
claim. A certified claim goes **bare** -- the check made it a fact --
and keeps the note so anyone can re-run CHECK. `retracted` withdraws
with nothing in its place. The signatures need no verbose form: the
sigil is the record.

## Two shapes you'll meet

A struck-through label -- `~~AX~~: claim text` -- is a retraction left
visible in place; `grep AX` still finds it.

A ledger too large for one readable list is split into **theories**,
each opened by a defining claim whose `<-` names the theories it
stands on -- so reading one starts at its imports, which carry the
vocabulary its claims are written in. A claim's theory is fixed by the
words its text needs, not by the turn that produced it:
`SKILL.kb/theories.md`.

A closed ring -- `AB <- CD` and `CD <- AB` -- is mutual support, which
is no support at all. Nothing rejects it at entry; the ring stays `?`
until something outside it lands.

Render a ledger as a list, one claim per line, in ASCII (`<-`).

A ledger kept as files -- one claim per file, standing in frontmatter
-- is `Skill(llm-claim-ledger-kb)`. Why the notation is shaped this
way, and where to argue with it: `design.ledger.md`.
