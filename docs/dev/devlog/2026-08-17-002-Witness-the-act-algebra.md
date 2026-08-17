# Devlog: 2026-08-17 — Witness the act algebra

## Focus

Mechanize the two unwitnessed act-algebra laws (EXPLICIT's
contravention fold, the moot color behind `verdict: dissolved`) in
`engine_tower`, run the stack over a real ledger, and wire `verify:`
lines so ACT, FORCE, EXPLICIT, ONE_WAY, REIFY graduate from
user-ruled prose to certified. Brief:
`.claude/todo.kb/2026-08-17-000-Witness-the-act-algebra--contravention-fold-and-moot-color-in-engine-tower.md`
(now `status: done`, residue recorded there).

## Decisions

### The fold is record-wise, not grounded

**Rationale:** EXPLICIT says "an act leaves the effective set only
when an *admitted* act targets it" — admitted, not effective. A
strike already in the record is not undone by later striking its
striker; every subtraction is an addition to the record, so
once-struck stays struck and the fold's outcome is
order-independent. Reinstatement lives one level up, in the interval
calculus: clashing effective acts attack each other mutually, so a
one-or-two-assessor clash computes to the same contested interval
through the existing `grounded`, and litigation is one move (strike
the rejection, the acceptance stands un-attacked).
**Alternatives considered:** a grounded-style fold at the act level
(effective acts strike; strikes of strikers reinstate). Rejected as
reading "admitted" to mean "effective", and as duplicating DEFEAT's
machinery below the layer that feeds it.

### Moot absorbs before the truth-order pass

**Rationale:** the "never both defeated and dissolved" exclusion must
be a theorem, so `color()` drops content-acts on moot claims before
recomputing the interval — the moot claim is never in the truth
order to lose. Moot seeds from surely-defeated presupposition
targets only (a merely contested presupposition collapses nothing
yet), and propagates as an lfp so collapse chains.
**Alternatives considered:** a precedence rule ("moot wins over
defeated") — that is the schema constraint the criterion forbids,
restated in code. The exhaustive
`test_moot_absorbs_content_acts` (512 small records) checks the
derivation, not the precedence.

### Desugaring lives in the test file

**Rationale:** the tower's own discipline
(`test_the_modules_are_exactly_the_theories`) admits no new src
module, and data-representation is non-code by design; the brief's
open question already said incubator-until-proven. So
`tests/test_data_representation.py` reads
`llm-claims/design.claims.kb` (52 files) itself: `standing:` in
{agent, user} is the signing assessor's one act, `verify:` a
checker's, and `bare`/`open` desugar to *no act* — they name no
judge, so they pass through as claim states rather than judgments.
Decode reproduces every file's written fields, and the composed
stack colors every negative-verdict claim out, everything else in —
stored equals computed below the tripwires.

## Conventions Established

- Verdict polarity in `contest()`: `accepted`/`certified` affirm,
  every other word takes standing away; clash = opposite polarity,
  so two different negative words (retracted vs rejected) agree
  rather than contest.
- `Act.address` is REIFY's content-address (assessor, target,
  occasion); `effective()` asserts one act per address and
  occasion-well-foundedness of `strikes`.
- `strikes` is enumeration-only; contravention by description stays
  a syntax seam (noted in the `Act` docstring), per the brief's
  COMPREHEND question.

## Open Questions

- No strata claim states the sense-collapse law, so the moot tests
  are cited by no `verify:`; WITHDRAWN's `dissolved` word
  (llm-claims ledger) is the natural carrier if the user wants one.
- `llm-claims-kb-graph` flags a fleet citation cycle (pre-existing
  since b7b89c0): `discourse-graph-is-the-continuous-presentation`
  <-> `the-discourse-graph-never-evaluates`. Wants a direction
  ruling.

## References

- `docs/dev/strata.claims.kb/standing.kb/` — ACT, FORCE, EXPLICIT,
  ONE_WAY (ruled b7b89c0); `data-representation.kb/` — REIFY, SUGAR.
- `docs/dev/design-incubators/engine_tower/` — `standing.py` act
  layer; `tests/test_standing.py`, `tests/test_data_representation.py`.
- Both ledger tests were validated by mutation (polarity widened;
  fold dropping user acts) — each caught, then reverted.
