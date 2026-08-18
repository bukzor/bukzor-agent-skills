# Devlog: 2026-08-18 — Quantify the derived theorems

## Focus

The act algebra's *derived* results — moot absorption, one-pass
sufficiency, assessor invariance, litigation-in-one-move — rested on
an informal argument plus one exhaustive check over a strike-free,
two-claim, two-verdict domain. Take the cheap confidence rung named
in the Lean-port brief: hypothesis in the engine_tower incubator, and
four properties over generated strike-bearing records.
`tests/test_derived_theorems.py`, 5 properties, suite 45 → 50 tests
(0.13s → 4.7s).

## Decisions

### Derived results get their own file, cited by no claim

**Rationale:** the suite's rule is one ledger claim, one smallest
instance, named by that claim's `verify:`. A derived result is a
statement about *every* record, so the smallest instance is the wrong
witness for it and quantification is the right one. Separating them
keeps each `verify:` line fast (all five act-algebra lines still run
in ~0.2s) and keeps "this test witnesses this ruling" honest.
**Alternatives considered:** extending FORCE's and EXPLICIT's `-k`
patterns to sweep the new file in. Rejected for now — it conflates
ruled-claim witnesses with derived-result checks, and pays 5s per
claim. The user may want it anyway; the properties are named so no
existing `-k` pattern catches them by accident.

### The generator is checked for reach, not just used

**Rationale:** three of the four properties are conditioned on a
color (a moot claim, a defeated one). A generator that stopped
reaching one would leave them passing-and-silent, which is worse than
red. `test_the_generator_reaches_every_color` uses `hypothesis.find`
to demand each of moot/in/contested/out be constructible, so
vacuity fails loudly.

### Presupposition is generated acyclic

**Rationale:** edges run down a fixed claim order, matching the
tower's own poset discipline [STRATA]. A presupposition cycle would
make a claim's frame turn on its own defeat — a different subject,
and not one the ledger admits.

## Conventions Established

- Properties are `@settings(derandomize=True, database=None)`: a
  failing example must reproduce from the file alone, and no
  `.hypothesis/` directory appears in whatever cwd the agent ran
  `verify:` from.
- A stance is a named frozen dataclass (`Trusting`), never a lambda —
  a lambda's repr in a falsifying example (`lambda act: act.assessor
  in trusted`) omits the one thing needed to reproduce it.
- Every property's assertion message is self-labeling and states the
  transition, not just the values: `+u:q:2 accepted: {'q': 'moot',
  ...} -> {'q': 'contested', ...}`. The error has to carry the cause;
  pytest's own diff truncates the dicts that are the whole subject.

## Findings

- **A property whose act the stance discounts proves nothing.** The
  first draft drew the added act's assessor from all assessors while
  drawing the stance independently, so absorption passed under a
  mutation that should have broken it — the act often had no force to
  begin with. Fixed by drawing the assessor from the stance's own
  trusted set (`data.draw`).
- **`color()`'s second contest is redundant for the value.** Acts on
  a moot claim attack only that claim and each other, so dropping
  them removes whole components and no surviving claim's interval can
  move; defeat can only shrink, so the collapse cycle has no second
  round to find. This survives even the cross-claim mutation below —
  it is not a fact about the current attack rule. The second contest
  stays because it is what makes the never-both exclusion *derived*
  rather than a label-precedence rule; it earns its keep in the
  derivation, not in the output.

## Mutation validation

Four mutations, injected one at a time into `standing.py`, each
reverted (`git diff` on `src/` empty afterward):

- moot as a residual label (interval over every claim, "moot" last) —
  caught by absorption and by the fixpoint property.
- `contest` leaking across claims (every non-affirming act attacks
  every claim) — caught by absorption and litigation. *Not* caught by
  the fixpoint property, for the structural reason under Findings.
- clash restricted to distinct assessors (an assessor assumed
  self-consistent) — caught by assessor invariance alone.
- `effective`'s strike rule narrowed to same-issuer (`or` → `and`) —
  caught by litigation, and by assessor invariance.

## Open Questions

- Whether FORCE and EXPLICIT should cite the derived-theorem file
  alongside their minimal witnesses (see the first decision).
- The bounds are unrecorded debt if the Lean port ever lands: three
  claims, five acts, four verdict words, acyclic presupposition.

## References

- `.claude/todo.kb/2026-08-18-000-Lean-port-of-the-engine-tower.md` —
  the rung this discharges; its Notes now carry the four statements
  and the redundancy finding.
- `docs/dev/devlog/2026-08-17-002-Witness-the-act-algebra.md` — the
  informal arguments these quantify.
- `docs/dev/design-incubators/engine_tower/tests/test_derived_theorems.py`.
