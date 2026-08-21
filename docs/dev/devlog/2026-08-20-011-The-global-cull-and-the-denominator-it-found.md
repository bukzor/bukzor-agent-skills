# Devlog: 2026-08-20 — The global cull, and the denominator it found

## Focus

Yesterday's docket work drove trespasses to zero by repairing findings.
This turn went at the other side of the ledger, on the user's
instruction:

> do a global cull, all theories, based on SHOULD_OWN criteria.

All 267 `ontology:` entries in the fleet, judged one at a time against
the counterfactual: *if this word turned up in some other theory, would
that be evidence of a concerns violation?* Twenty-two came out.

## The measurement was wrong before the cull started

`--candidates` already had the SHOULD_OWN question, and its cull side
named 30 words. Reading them, the top of the list was `claim`, `ledger`,
`label`, `standing` — the words deliberately promoted to the ledger root
one turn earlier, precisely so the whole ledger could say them.

The scan was counting spread over a ledger. The law counts findings, and
a **root's interior is the ledger**: no in-ledger theory can trespass on
a root word, and a foreign ledger is out of jurisdiction. So a root
stipulation cannot generate a finding in any corpus, ever, and its
spread measures nothing at all. That is not a defect of the root
entries — it is what the promotion move buys, and it means the root
ontology is a glossary rather than a license.

Counted where the counterfactual actually lives — **outside the owner's
interior** — the cull side falls from 30 rows to 7, and the 7 survivors
are exactly the ones a person has to weigh.

## Spread carried by import is not spread

The 7 are `store`, `view`, `fixpoint`, `corpus`, `act`, `grade` — plus
`act` again in the other ledger. Every one is said by five to seven
theories outside its owner, and every one was kept.

A prior exists to be read in its own words. `fixpoint` is an auxiliary
theory, split off so `reference` and `standing` could cite one label
instead of restating a proof sketch; six theories saying `fixpoint` is
that split working, not the license failing. The raw number cannot tell
this apart from ambience, so it is evidence for the counterfactual and
never the ruling on it.

## What did come out, in three classes

**Six restatements of a word an ancestor already owns.** `stratum` and
`tower` in `tower.md` under `ENGINE`; `extension` in `genre.md`;
`enforcement` in `protocol.md`; `skill` in `authorship.md`; `design` in
`good-smells.md`. `OUTERMOST_WINS` made every one inert — they owned
nothing and added a line each. The inert count is now 0, and the foreign
double count fell 37 → 29 as a side effect.

**Five homonyms whose plain sense is unavoidable**, ranked by how many
theories outside the owner already say them innocently: `word` (8),
`ruling` (5), `update` (3), `review` (2), `agent` (1). `word` is the
sharpest: `HISTORY` means it exactly — a word in the free monoid of
updates — and eight strata say it meaning *a word*. `HISTORY` keeps
`log`, `fold`, `merge`, `branch`, `linearization`, which carry the same
content with no homonym.

**Eleven ordinary English words whose zero spread is an accident of
ledger size**, not concentration: `work`, `world`, `growth`, `peer`,
`blind`, `SKILL.md`, `force`, `job`, `project`, `criterion`, `context`.
Nothing said them outside their owner yet. `force` and `context` are
among the commonest words in this corpus and will.

`SKILL.md` is its own small lesson: a filename is always backticked in
prose, backticks are struck from speech, so the entry could never fire.
A stipulation on a literal is dead weight by construction.

## Two entries survived a cull I had already decided on

`domain` and `occasion` in `authorship.md` looked like plain English
beside `trigger`, which authorship also owns. Reading the claims killed
that: `DOMAINS` says "a skill is a domain of law; an occasion is a
trigger in the domain" — the three words are one law's three roles, and
culling two of them would have left the claim unable to state itself.
The count said cull; the sentence said keep.

## The own side had no defence against English

`f11n code`, working the strata rename, sent over the complementary
finding: `--candidates` gated the own side on one *sayer*, so a coinage
went invisible the moment a neighbour said it once — `sibling`, 24 uses,
excluded on that ground alone. The gate should be one *stipulator*.

It is, now. Loosening it exposed that the own side had never had any
defence against English at all: it immediately proposed `they`, `below`,
`itself`, `everything`. The ledger-local count had been suppressing them
by accident. The fix is a fleet-wide count — a word the other ledgers
say as freely is English, however hard this one leans on it — and the
own side settles at 22 proposals, most of them `ownership.kb`'s own
coinages, which it does not yet own.

## Left open

- The two idle imports are unchanged, and no cull stranded a new one.
  `data-structures` → `genre` went idle when `sort` left `genre.md` last
  turn; `GRAIN` → `data-representation` was idle before either sweep.
- The own side's 22 proposals are unactioned. The cull was the ask.
