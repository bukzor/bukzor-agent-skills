---
name: llm-claim-ledger
description: "Conversational claim ledger. Agent MUST load on `claim *` marker commands, or when a conversation's claims churn (reversals, contested points, retractions)."
---

<!-- Core: verbatim-shared with the user's claude.ai preferences.
     Merge improvements in either direction by copy-pasting this block. -->

## Claim Ledger

When claims churn, label them. A label names the locus, a trailing sigil
carries standing (bare asserted, ? open, + agent fiat, ! warranted), and
`<-` names what the claim rests on:

* PARSER!: the crash is in the parser, reproduced on a minimal input
* MULTIBYTE?: it fires only on multibyte input (three samples, no counterexample)
* DECODER <- PARSER! MULTIBYTE?: so the fix belongs in the decoder, not the parser

Policy:

1. Claim set: union over chat, last wins.
2. Every claim, both parties: sound, open, or retracted. Open claims are debt, priced by what rests on them.
3. Governance is one line over labels: `claim accept: MULTIBYTE` marks it `MULTIBYTE!`

<!-- /Core -->

The core block alone runs in chat-only environments; typed claim kernels
and proof-transport systems are harder rungs of the same ladder, and the
invariant holds at every rung — every claim sound, open, or retracted.

The rest of this file is what it takes to *read* a ledger. Everything
past reading is one file per rule in `SKILL.kb/`, each named for its own
trigger: `ls SKILL.kb/` is the index, and you read the ones whose names
match the work.

## Sigils

Compact standing, trailing the label — the label stays a greppable
prefix, so `grep XY` finds `XY`, `XY?`, `XY!`, and every reference:

| Sigil | Standing |
|---|---|
| bare | asserted — believed sound, unadjudicated |
| `?` | open — proposed, contested, or not yet stood behind |
| `+` | agent fiat — the agent settled an underdetermined point on the user's own subject; full warrant, revocable on sight |
| `!` | warranted — adjudicated by fiat, or certified by check |

Sigils go wherever the label goes: `XY <- AB! CD?` shows the premises'
warrant-mix exactly where weight is placed on them. `?` is the honest
out — finish the line now, upgrade in place when the judgment lands.

`?` and `+` are the two that want the user's eye, and they want
opposite things: `?` an answer, `+` a veto. One scan finds both —
`grep -nE '[A-Z_][?+]'` — which is the point of spending a glyph on
agent fiat rather than folding it into `!`.

## Statuses

Suffix a claim line with `-- STATUS` when standing needs more detail
than a sigil carries:

```
* XY: claim text                  -- certified(CHECK)
* XY <- AB CD: claim text         -- asserted      (premises: AB, CD)
```

| Status | Meaning |
|---|---|
| `asserted` | believed sound — the default when unmarked |
| `stipulated` | warranted by fiat (agreement or decree), not evidence; conclusions built on it inherit it as a premise |
| `certified(CHECK)` | discharged; CHECK names the re-runnable verification |
| `retracted` | withdrawn with nothing in its place |

Sigils compress these: `!` covers certified and fiat-warranted, `+`
narrows to fiat the agent held itself (so it says what `-- authority:
assistant` would), bare is asserted, and `?` needs no verbose form —
open is open.

## Two shapes you'll meet

A struck-through label — `~~AX~~: claim text` — is a retraction left
visible in place; `grep AX` still finds it.

A ledger too large for one readable list is split into **theories**, one
file each, headed by the theories it stands on and the vocabulary its
claims may use. A claim's theory is fixed by the words its text needs,
not by the turn that produced it: `SKILL.kb/theories.md`.

A closed ring — `AB <- CD` and `CD <- AB` — is mutual support, which is
no support at all. Nothing rejects it at entry; the ring stays `?` until
something outside it lands.

Render a ledger as a list, one claim per line, in ASCII (`<-`).

Why the notation is shaped this way, and where to argue with it:
`design.md`.
