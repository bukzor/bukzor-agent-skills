# Devlog: 2026-08-20 — License and standing collapse into one relation

## Focus

The user read the ownership decision tables and challenged five
points. Four became amendments; one was held. The collapse that came
out of the first challenge shrank the law enough that the corpus scan
it had been blocking could finally be written.

## The challenge that mattered

> doesn't 'owner' **imply** standing, inherently? or rather: how can
> an owner be an owner but lack standing?

It does, and the account had two places that said otherwise. The
tables had a "silent violation" cell: a position barred from a word
whose owner no one could prosecute there — a rule with nothing behind
it. It came from computing license (`reach`) and standing
(`answerable`) by separate rules and then intersecting them.

Two distinct causes:

- **Foreign ledgers**, ~1675 of 1854 raw rows, and not a real
  disposition at all: `owner` was a fleet-global function while
  SORT_REACH says namespaces are per-ledger. Fixed by giving `owner` a
  namespace argument. The same string in two ledgers is two names.
- **Cousins and nephews**, real, and *created* by the user's own
  ANSWERABLE_IS_LOCAL ruling (sibling-only) rather than closed by it.

Taking the ruling together with the principle gives one predicate:

> A finding is a sibling, without an import, saying the word.

So REACH is now **the ledger less the owner's siblings; a sibling
enters by importing**, and license and standing partition the ledger
between them. THREE_MOVES' three regions survive as consequences —
none of interior, ancestors, or importers' interiors is a sibling —
and `witness_moves` runs that containment so the amendment provably
lost nothing. TRESPASS drops from three conjuncts to two.
ANSWERABLE_IS_LOCAL dissolved: the ruling is recorded as REACH's
`authority:`, and the question file is gone.

Measured cost before ruling: 2 nephew occurrences, 0 cousins. The
amendment was bought for coherence, not cleanup — said so in the
claim.

## The other four

- **CONTENTION** (renamed from SINGLE_VALUED). The user: "doesn't that
  rather imply two owners? which should be an error, charged back to
  both stipulations." Right, and it relocates the disposition from the
  occurrence to the stipulation — both of them. "Undefined" described
  the formalism's gap; "contention" describes the corpus's fault and
  names who answers for it.
- **OUTERMOST_WINS held**, against a well-aimed push for innermost-wins
  ("the most-specific-scope that's in scope should win"). The reply
  that settled it: `ontology:` is a word list, ownership is exclusion,
  and the *gloss* already resolves by proximity — so innermost-wins
  would not change which sense a reader takes, it would newly bar the
  inner theory's siblings. And it is unimplementable: shadowing asks
  the checker to tell two senses of one string apart. `uniquify` covers
  a genuinely different sense; culling the outer entry covers a genuine
  intent to narrow. Checked the field first: all six nested pairs are
  plain re-listing, `tower.kb` re-listing 'tower' among them.
- **SHOULD_OWN** got the user's goal-relative definition — own a word
  whose appearance in another theory would signal a concerns violation.
  That killed the build already approved for it: extending
  `trash/term-of-art.py`'s Zipf scoring to unowned words targets
  *reader comprehension*, and the user's test is *distributional*. Said
  so before building, and re-aimed at concentration across theories.
- **Two `kinship` functions** — one in the law, one in the scan, with
  different arities. The user: "this smells like the tool should be
  modified to match the theory." Fixed by deleting the scan's copy
  entirely; see below.

## Built

`llm-claims-kb-ownership` now imports `ownership.py` and runs it. The
scan keeps the adapter — reading ledgers off disk, deciding what a
claim *says* — and defines no law of its own; its private `kinship`
is gone, and `contended()` asks the law's `owner` to raise rather than
restating the rule. Two new modes:

- `--trespass`, the scan four claims had been witnessed on fixtures
  and never run against the corpus: **252 trespasses over 121
  stipulations**, 88 of them in `strata.claims.kb`. The heaviest are
  'state' (8), 'theory' (8), 'claim' (6), 'map' (6), 'standing' (6) —
  which is SCREENING's warning and SHOULD_OWN's plain-English
  population, arriving as data. The ownership theory's own words are
  on the list: 'answerable', 'reach', 'sort', 'force', all trespassed
  by `good-smells.kb` and `stance.kb`.
- `--candidates`, SHOULD_OWN's first mechanization, both directions:
  49 owned words are ambient (>4 theories), 19 unowned words
  concentrate (>=8 uses in 1 theory). Precision is good on the cull
  side and about 2/3 on the own side — `phi`, `defeated`, `wrestled`
  are noise. It is a proposal queue and says so.

## Left open

The 252-finding docket is not adjudicated; that is its own pass, and
the `--candidates` cull list is the right order to work it in.
DIRECT_ONLY? survives with a much smaller stake — imports now license
one population only. EXPOSITION? lost its ownership stake entirely and
stays open as a writing question.
