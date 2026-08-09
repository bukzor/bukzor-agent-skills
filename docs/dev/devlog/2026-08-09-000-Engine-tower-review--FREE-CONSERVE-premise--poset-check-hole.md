# Devlog: 2026-08-09 — Engine-tower review: FREE_CONSERVE premise, poset-check hole

## Focus

Two-pass review of `docs/dev/design-incubators/engine_tower/` — another
agent's rewrite of this session's pedagogical Python sketch of the
strata tower — plus its claim ledger `docs/dev/strata.ledger.kb/`.

## Decisions

### FREE_CONSERVE requires confinement, not just monotonicity

**Rationale:** The ledger claim `genre.kb/one-sort-buys-conservativity-for-free.md`
argued conservativity from monotone growth alone. That gives only one
direction (old standing cannot fall); the other direction (old standing
cannot rise) needs confinement — extension evidence concludes only on
the genre's own entries; premises may cite anything. The verify suite's
own `test_an_unconfined_extension_breaks_conservation` is the
counterexample: one appended unconfined row breaks conservation.
Fixed the claim body, `why:` (added `confinement-is-the-syntactic-half.md`),
and widened `verify:` to all of `tests/test_genre.py` (commit a03c7ec).
Sharpened OBLIGATION (`tower.kb/what-remains-to-prove.md`) to match:
the proof-grade theorem is **monotone + confined ⇒ conservative**.
**Alternatives considered:** Leaving OBLIGATION vague ("conservativity
holds") — rejected; the missing premise is exactly what a proof
assistant would force you to state, so state it now.

### Poset-check hole: relative imports evaded the STRATA witness

**Rationale:** `tests/test_tower.py::internal_imports` only matched
`from engine_tower.X import ...`; both `from .sibling import name`
(module set, `level` set) and `from . import sibling` (`module=None`)
slipped through. Since house style (`reference.kb/python/`) prefers
explicit-relative imports, following style would have stepped straight
through the hole. Fixed to cover both forms (commit 7e1a5e5).
**Alternatives considered:** Forbidding relative imports in the
incubator — rejected; the witness should observe the code, not
legislate its style.

### Adopted from the other agent, verified

- `genre.confined()` predicate + `test_fixpoint.py` witnesses for
  KNASTER / WARM_START / OVERSHOOT (commit 1724cf8) — checked the
  overshoot math by hand (ring a↔b with root retracted: descent keeps
  {a,b}, lfp from ∅ is ∅); correct.
- `standing.py` decoupled from `reference.Edge` via `type Attack` —
  keeps the module poset honest.
- Single-file `verify:` per claim with hand-mirrored PRIORS table and
  an "update both together" comment — deliberate; left as is, with a
  possible pair-witness alternative parked in todo.kb.

## Conventions Established

- `verify:` commands are file-scoped so `-k` selectors don't leak
  across test modules (test_fixpoint names must not match
  ASYMMETRY/APPROX selectors).
- Instance witnesses are tooling grade: they move no standing to
  `bare`; OBLIGATION names the proof-grade step and stands `open`.
- The incubator's first commit imports the reviewed sketch verbatim so
  the rewrite delta is inspectable.

## Open Questions

- Typecheck wiring for the incubator (pyright is clean only from the
  project root; 25 spurious import errors from repo root) — parked in
  `.claude/todo.kb/2026-08-09-000-engine-tower-incubator-follow-ups.md`.

## References

- `docs/dev/strata.ledger.md` and `docs/dev/strata.ledger.kb/` — the ledger under review
- `docs/dev/design-incubators/engine_tower/` — the uv project; 27/27 tests pass
- Commits: c0ceef6, f6b2116, 2a09d93, 8e8a727 (rewrite); a03c7ec, 7e1a5e5 (review fixes); 1724cf8, c370a52 (responses)
- `trash/engine_tower.py` — the original sketch, superseded by the verbatim import in f6b2116
