# Devlog: 2026-08-20 — The standing pair is renamed to its propositions

## Focus

Naming the pair that 001 introduced. `Color(sense, content)` was
built and verified that morning; reading it back, every value needed
a legend — `sense: contested` says which question is open only if you
already know what `sense` asks. The sweep renamed the class, both
coordinates, the failure state, one label, and two claim files.

## Findings

- **A coordinate name should be a proposition, not a category.**
  `Disposition(live, upheld)` reads as answers: `live` is true,
  `upheld` is unknown. `Color(sense, content)` read as two category
  names whose values were the answer to an unstated question. Same
  structure, and the printout stops needing a glossary.
- **`content` was the ledger's most plain-English-polluted word.**
  Six ordinary uses in `strata.claims.kb` — "the content of the
  ruling", "a phrase with content", "the mathematical content of",
  "the claim's own content". Nothing disambiguates the stipulated
  sense from the ordinary one at the point of reading.
- **`moot` is ambiguous exactly where it must not be.** Not generic
  ambiguity: the American sense is "irrelevant", the legal and
  British sense is "debatable, open to argument" — and the second
  lands precisely on `contested`, the sibling value in the same
  two-coordinate system. A word whose two readings name two values of
  one pair cannot name either.
- **The corpus evidence I first gathered against `live` was wrong.**
  I counted seven collisions in the ledger. Four are the *verb* —
  "the values live in", "does this claim live in", "references live
  in prose" — a different part of speech, which no reader confuses
  with a predicate. The three adjectival uses (`live reference`,
  `live schema`, `live target`) all mean "actually in force", which
  is the same predicate, not a competing one.
- **`collapse` was already native; `moot` was the orphan.** The
  engine had `collapse()` the function and `sense-collapse` the
  ontology word before this session. `moot` named the resulting state
  and nothing else. Using `collapsed` for the state buys one word
  family — verb, ontology entry, derived property, value — in place
  of a noun with no relatives.

## Decisions

### The pair is `Disposition(live: Tri, upheld: Tri)`

**Rationale:** the user's argument settled it: a property name is not
separable from the type it hangs on, so `Reference.live` and
`Claim.live` meaning different things is no obstacle — the two being
*analogous at their respective types* is a reason to share the name.
That reframes the corpus check. The question is not "is this word
used elsewhere" but "would using it elsewhere signal a violation",
which is SHOULD_OWN's test, filed in `llm-claims/` today by a peer
session.
**Alternatives considered:** keeping `sense`/`content` (rejected:
`content` fails the plain-English test hardest of any word in the
ledger); naming the coordinate from its negative pole, `moot`
(rejected above); `in-force`/`standing` (rejected: `standing` is the
whole structure's name, and reusing it for a coordinate of itself is
the confusion the rename exists to end).

### The invariant weakens from biconditional to implication

**Rationale:** the old rule was `content is None` **iff**
`sense == "out"`. Only one half was load-bearing — that no value is
both collapsed *and* settled on the merits, which is what makes the
collapsed/defeated exclusion structural rather than a precedence
rule. The other half refused `Color("contested", None)`, a state that
under the new encoding is `(UNKNOWN, UNKNOWN)`: legal, reachable, and
meaning "the subject is disputed and so is the merit". Nothing was
lost, because under the old scheme `content` was present unless
`sense` was `out`.
**Alternatives considered:** keeping the biconditional (rejected: it
would forbid a state the model wants); dropping the assertion
entirely (rejected: mutation shows it is the only thing holding the
exclusion — see Verification).

### `Tri` replaces `str | None`

**Rationale:** `unknown` becomes a value rather than an absence, so
the type says what the encoding used to leave to a convention. The
one thing `None` bought — telling apart "disputed" from "does not
arise" — is bought better by the other coordinate: `(UNKNOWN,
UNKNOWN)` is a dispute, `(FALSE, UNKNOWN)` is a question that does
not arise. The distinction was never in `content` alone, which is why
reading it alone misled.

### `verdict`, not `content-act`

**Rationale:** `verdict` was already in `standing.md`'s ontology. The
compound `content-act` existed only to point at the coordinate, and
had no basis once `content` left. `ABSORB`'s file is
`a-collapsed-claim-absorbs-verdicts.md`.

## Conventions Established

- **A stipulated word is checked against the corpus for part of
  speech, not just spelling.** A verb and a predicate spelled the same
  are not a collision; counting them as one nearly cost this rename
  its best candidate.
- **`SENSE` → `SPLIT`, and prefix-freedom is checked at rename
  time.** `SPLIT` shares no prefix with `STATUS`, `STANCE`,
  `STANDING`, or any other label in the ledger — the property `grep`
  and the flattener both depend on.

## Verification

- 66 tests green; `black` clean; `llm.kb-validate` 95 files 0 errors;
  link check 110 files 0 broken; `llm-claims-kb-mentions` 0 unimported
  mentions.
- **The new invariant is witnessed.** Injecting `self.upheld is TRUE`
  in place of `self.upheld is not UNKNOWN` leaves
  `test_a_collapsed_claim_answers_no_truth_question` failing with DID
  NOT RAISE — 1 failed, 65 passed. Reverted; 66 pass. The test now
  witnesses both refusals, `(FALSE, FALSE)` and `(FALSE, TRUE)`,
  rather than only the one a single value would catch.
- **The error message was assessed, not just its existence.**
  `Disposition(live=FALSE, upheld=TRUE): a collapsed claim has no
  truth question to answer` carries the offending value and states
  the rule. The old text, `content is absent exactly where sense is
  out`, made the reader re-derive a biconditional to learn which half
  they had broken.
- All seven valid combinations were re-checked reachable by building
  a record per combination (`trash/enumerate-dispositions.py`), not
  by reasoning about the constructor.
- The per-claim `verify:` sweep runs green over 41 claims but one:
  `data-representation.kb/every-structure-lands-in-every-target.md`
  names a test that does not exist. **Pre-existing**, and already
  carried in `.claude/todo.md` as the live instance of the `verify:`
  notation defect.

## Cross-checked against today's ownership rulings

Three peer sessions filed `llm-claims/design.claims.kb/ownership.kb/`
today, including PLAIN ("a plain-English double culls or narrows")
and SHOULD_OWN ("a word is owned where use signals violation"). This
rename was argued on exactly those grounds, so it was checked against
them rather than assumed compatible:

- **PLAIN does not fire.** It governs *doubles* — one word two
  theories both stipulate. `llm-claims-kb-ownership` reports `0
  contending`, and none of `live`, `upheld`, `disposition`, or
  `collapse` appears anywhere in its output.
- **SHOULD_OWN passes, by its own mechanization.** The test is
  concentration across theories. `disposition` occurs in four files,
  all `standing` — tighter than `presupposition`, an accepted
  ownership. `upheld` and `collapse` match `presupposition`'s profile
  exactly.
- **`live`'s spread decomposes to zero downward trespasses.** Its
  out-of-theory occurrences are the verb (`reference.md`,
  `genre.kb/confinement-is-the-syntactic-half.md`), one `CLAUDE.md`
  maintenance note (exempt by the ledger's own filing rule), and
  adjectival uses in `genre.kb`, `fleet.kb`, and
  `data-representation` — every one of which has `standing` among its
  priors, so each is licensed by reach. No theory at or below
  `standing` uses it as a name. The counterfactual holds too: `live`
  turning up in `record.kb` or `history.kb` *would* signal a
  violation, since liveness is computed from a fixpoint those
  theories cannot see.

## Open Questions

- Whether `Mapping[str, Edge]` should widen to several edges per
  edge-claim. Recommended; the single-edge shape is an artifact of
  the first witness, not a ruling.
- Whether to lift the *into* half of the edge stratification — one
  assertion. Recommended. The *out of* half is not, yet: it wants an
  approximation fixpoint first.
- Whether `stale-when:` should lift to non-defining claims, so
  stipulation tripwires have a structural home. Recommended.
- HOME stays open, unmoved by this session: it now cites
  `live-and-upheld-are-judged-separately.md` and says "which is what
  not being live means", but the ruling it asks for is untouched.

## References

- `docs/dev/devlog/2026-08-20-001-Standing-becomes-a-pair--presupposition-edges-become-claims.md`
  — built the pair this entry renames. Its `Color`/`sense`/`content`
  vocabulary is provenance and was deliberately left standing there,
  as were `SENSE` mentions in `strata.replication.run.kb/`.
- `llm-claims/design.claims.kb/ownership.kb/what-decides-a-word-should-be-owned.md`
  (SHOULD_OWN) and `a-plain-english-double-culls-or-narrows.md`
  (PLAIN) — the law this rename was checked against, filed the same
  day by peer sessions.
- `.claude/todo.kb/2026-08-18-000-Lean-port-of-the-engine-tower.md` —
  still postponed, and by its own condition: the standing theory's
  vocabulary moved again today.
