# Devlog: 2026-08-18 — File the derived results as claims

## Focus

Two rulings from the user, both about the ledger rather than the code:
tests that assert something design-relevant should have a claim that
runs them, and the fleet citation cycle should be replaced by whatever
the correct non-circular reasoning is. Four new claims in
`standing.kb/`, one edge deleted in `fleet.kb/`, witnesses moved to
the claims they are about.

## Decisions

### Derived results are `bare`, not `agent`

**Rationale:** the user's correction, and it is structural.
`bare` names no judge, and a `verify:` line already desugars to a
checker's act — so a result that follows from its premises gets its
standing from the derivation and its evidence from the check. Signing
it `agent` would invent an assertor the claim does not need.
**Consequence:** this supersedes the first decision of
`2026-08-18-001` ("derived results get their own file, cited by no
claim"). The file stays separate; it is now cited.

### The bound is recorded at the claims, and stated once

**Rationale:** the Lean brief requires that a bounded check standing
in for a proof be recorded as debt at the claim it weakens. Each bare
claim says its `verify:` is quantification rather than proof; the
bound itself — three claims, five acts, four verdict words, acyclic
presupposition — is written once in `strata.claims.md` (Verify),
because four copies of it would drift.

### `standing`'s ontology gains three words

**Rationale:** `presupposition`, `sense-collapse`, `moot`. The
alternative was an auxiliary theory, which the ledger's own guidance
prefers to widening. Declined here because the moot color is an output
of the standing computation itself — `color()` returns it beside
in/contested/out — so the machinery is this theory's own, and a
nested theory would split the module the tower test pins to it for
nothing the ledger needs.

### The fleet cycle runs one way: UNEVALUATED ← CONTINUUM

**Rationale:** UNEVALUATED argues that the shipped schema is a lawless
cache, which needs CONTINUUM to say what the lawful reading would have
been; it also corrects CONTINUUM's porting note, and a claim that
corrects another stands downstream of it. CONTINUUM needed nothing
back: its "design, not shipped" caveat reads the live schema, which
the sentence already names. So the cite is dropped from `why:` and
from the prose, and the fact stands on its own evidence.
**Alternative considered:** keeping a prose forward-reference for
discoverability. Rejected — the ledger's rule is that inline cites are
mirrored in `why:`, and who-cites-me is what the graph is for.

## Conventions Established

- A test asserting something the design leans on carries a claim
  label in a trailing comment, the same way `test_standing.py` has
  always done — and the claim's `verify:` selects it. Two tests in
  `test_standing.py` had neither.
- A witness belongs to the claim it is about, not the claim that
  happened to adopt it: absorption left FORCE for ABSORB.
- Where a `-k` pattern is the selector, the test is named so the
  pattern reads as English at the claim: `-k "litigation"` picks up
  `test_litigation_is_one_move_in_any_record`.

## Findings

- **The sense-collapse law was implemented, witnessed, and stated
  nowhere.** `moot()` had two tests, neither carrying a label, and no
  claim in the strata ledger. The notation ledger's `dissolved`
  vocabulary (`llm-claims/design.claims.kb`, WITHDRAWN) is a different
  ledger and cannot be cited from a proper-noun-free theory. Filed as
  SENSE.
- **A claim can only run one command, so `-k` patterns now span two
  files.** ABSORB and EXPLICIT name both test files explicitly rather
  than sweeping the suite; the slowest of the nine act-algebra
  `verify:` lines is 1.8s wall.
- **STRATA ran one of the three tests that carry its label.**
  `test_the_declared_priors_are_a_poset` asserts the poset STRATA
  claims and no claim ran it; its `verify:` is now the whole file
  (0.2s).

## Open Questions

- SENSE stands `agent` — the collapse rule is a modeling commitment,
  not a consequence — and it is the one new claim inviting a veto.
- Whether the incubator's modules-are-theories check belongs to STRATA
  at all; it is a fact about the realization, not about the tower,
  and the ledger below the seam is supposed to be representation-free.

## References

- `docs/dev/devlog/2026-08-18-001-Quantify-the-derived-theorems.md` —
  the properties these claims file; its first decision is superseded
  above and its two open questions are answered.
- `.claude/todo.kb/2026-08-18-000-Lean-port-of-the-engine-tower.md` —
  the port now inherits nine engine-cited claims, not five.
