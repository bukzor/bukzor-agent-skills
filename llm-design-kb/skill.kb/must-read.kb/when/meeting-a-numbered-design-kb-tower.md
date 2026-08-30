# When meeting a numbered design.kb tower

You have found `010-mission.kb/`, `020-goals.kb/`, `040-design.kb/` or
their siblings -- a design tower written before this skill kept its
records as claim ledgers. Two things are true at once: the tower is
still legal, and it is no longer what a new record looks like.

## Nothing migrates on a schedule

The numbered format keeps working. Its entries validate against
`../../../jsonschema/layer-entry.jsonschema.yaml`, which stays in place
for exactly this reason, and `technical-policy.jsonschema.yaml` beside
it likewise. Do not convert a tower you merely walked past, and do not
open a migration as a task of its own unless the owner asked for one.

Modernization is per-instance and opportunistic: if you are already
working inside a tower and the work touches an entry anyway, convert
what you touched. Otherwise leave it.

## What maps to what

The tower is the ledger with standing erased. Each correspondence
recovers something the tower could not record:

| Numbered tower | Ledger |
|---|---|
| `0NN-<rung>.kb/` | `<rung>.md` beside `<rung>.kb/` -- a theory; the digits go, the order lives in `why:` |
| `040-design.kb/` | `architecture.kb/` -- `design.kb/design.kb/` would repeat the word its container supplies |
| `why:` frontmatter | `why:` frontmatter, unchanged -- the field this skill contributed to the claim schema |
| an entry that reads as settled | a claim with a `standing:` naming who settled it, which the tower had nowhere to say |
| `070-future-work.kb/` | `?` claims where nothing is decided, `todo: true` where something is decided and unbuilt -- each filed under the rung it concerns, not in a bucket |
| an inline "why not X" note | a struck sibling claim carrying `verdict:` and its ground |
| an alternatives listing | the decision-point shape: `$ITEM.md` poses the question, `$ITEM.kb/` holds one file per candidate |
| `> [!TODO]` | `todo: true` |
| `> [!QUESTION]` | `standing: open` |
| auxiliary `background.kb/` | an auxiliary theory beside the rungs -- unchanged in kind, now a claim like any other |

## Converting one entry

1. Give it `label:` (upper snake, naming the locus of contention, not
   the current conclusion) and `standing:`. Standing is the honest
   answer to *who decided this*: `user` if the owner ruled it, `agent`
   if a previous session inferred it, `open` if nobody has.
   Reconstructing that from a tower is guesswork -- when you cannot
   tell, `agent` is the truthful default, because it invites the veto
   the tower silently skipped.
2. Leave `why:` alone. It already means what the ledger means by it.
3. Move it to the rung whose question it answers, renaming the
   collection as it goes.

The entry's prose needs no rewrite: `Skill(llm-claims-kb)`'s claim
bodies are the same cold prose the tower already held.

## Leaving a tower half-converted

Legal and expected. A ledger and a tower can sit in one project, and a
`why:` crossing between them resolves the same way. What must not
happen is a *third* home for the same claim -- convert an entry or
leave it, never copy it.
