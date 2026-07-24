---
name: llm-claim-ledger
description: "Conversational claim ledger. Agent MUST load on `claim *` marker commands, or when a conversation's claims churn (reversals, contested points, retractions)."
---

<!-- Core: verbatim-shared with the user's claude.ai preferences.
     Merge improvements in either direction by copy-pasting this block. -->

## Claim Ledger

When claims churn, start labeling:

* LC: we Label our Claims
* SG: trailing Sigils mark standing -- bare asserted, ? open, ! warranted
* XY <- LC! SG?: entailment, each premise's standing visible in place

Policy:

1. Labels: short mnemonics.
2. Claim set: union over chat, last wins.
3. Every claim, both parties: sound, open, or retracted. Open claims are debt, priced by what rests on them.
4. Governance is one line over labels: `claim accept: SG`

<!-- /Core -->

Everything below elaborates the core. Elaborate lazily: bare labels first;
sigils once standing starts to matter; verbose statuses once routes and
checks matter; flush only at a context boundary.

## Sigils

Compact standing, trailing the label — the label stays a greppable
prefix, so `grep XY` finds `XY`, `XY?`, `XY!`, and every reference:

| Sigil | Standing |
|---|---|
| bare | asserted — believed sound, unadjudicated |
| `?` | open — proposed, contested, or not yet stood behind |
| `!` | warranted — adjudicated by fiat, or certified by check |

Sigils go wherever the label goes: `XY <- AB! CD?` shows the premises'
warrant-mix exactly where weight is placed on them. `?` is the honest
out — finish the line now, upgrade in place when the judgment lands.

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
| `retracted` | withdrawn; supersession counts (last wins) |

Sigils compress these: `!` covers certified and fiat-warranted, bare
is asserted, and `?` needs no verbose form — open is open. Fiat
warrant and check warrant propagate alike: withdraw the stipulation or
invalidate the check, and retraction propagation applies downstream.

Policy:

- **Obligation is implicit.** Open claims need no debt declaration:
  each is obligated exactly to the extent conclusions rest on it, and
  the warrant-mix at point of use (`ZZ <- XY?`) shows where that is.
  Name routes at discharge or flush; never demand them at entry.
- **Retraction propagates.** On retracting `AB`, revisit every claim with
  `AB` as premise: re-derive it, retract it in turn, or restate it without
  the lost support. Tell the user what changed. Never silently keep a
  conclusion whose support vanished.
- **Last wins.** Restating a label supersedes its prior versions; the
  ledger is the surviving union over the whole chat.

## Commands

Marker commands (see `Skill(llm-subtask)` references/marker-commands.md);
also act on your own initiative — the core's "when claims churn" is the
trigger, not a user request:

- `claim list` — render the surviving ledger
- `claim: TEXT` or `claim XY: TEXT` — add a claim
- `claim accept: XY` — adjudicate warranted, the operator's call; mark `XY!`
- `claim contest: XY` — reopen; mark `XY?`
- `claim retract: XY` — retract and propagate
- `claim certify: XY` — name an executable check, run it; on success
  mark `certified(CHECK)`
- `claim flush` — end-of-context extraction (below)

Always render the ledger in a code fence — `<-` and `(ROUTE)` get mangled
as markdown/HTML otherwise.

## Flush

At session end, under context pressure, or on `claim flush` — serialize
claims *with their statuses*; a summary of conclusions is not a substitute
(it strips exactly the standing this ledger exists to preserve):

1. Render the full surviving ledger, code-fenced.
2. Open claims still carrying weight → `- [ ] discharge XY: ROUTE` in
   `.claude/todo.md`, naming the route now — brackets are load-bearing
   (`Skill(llm-subtask)`).
3. Claims worth keeping across sessions → `claims.kb/` nodes
   (`Skill(llm-discourse-graph)`); certified ones include enough check
   output to re-run.
4. Artifacts addressed to a fresh context (prompts, task files) carry
   obligations as instructions to verify, never as facts to inherit.

## Background

The semi-formal rung of a ladder: the core block alone runs in chat-only
environments; typed claim kernels and proof-transport systems are harder
rungs elsewhere. Same invariant throughout: every claim sound, open,
or retracted.
