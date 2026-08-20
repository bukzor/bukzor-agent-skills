# Devlog: 2026-08-20 — Correct SENSE's certificate and vocabulary

## Focus

The user read SENSE in its flattened form and asked whether it was
correct. Three defects, all in the same claim, all invisible in the
file and obvious on the one line.

## Findings

- **`certified(CHECK)` covered a third of the claim.** SENSE commits
  to three things; `-k "moot_propagates"` selected one test, one
  instance of one of them. The headline — no interval at all — was
  witnessed by a test that carries the SENSE label and that the
  pattern did not select. The third commitment, seeding from *surely*
  defeated only, had no witness anywhere: swapping `claims - upper`
  for `claims - lower` in `color()` passed the whole suite. Now it
  fails one test by name, and SENSE's `verify:` runs all three.
- **`dissolved` is not a word of this theory.** The engine's verdicts
  are accepted/certified/rejected/retracted. `dissolved` lives in the
  notation ledger (`llm-claims/design.claims.kb`), which a
  proper-noun-free theory cannot cite, and in `question.md` in the
  other sense — a dissolved *question*. The sentence also carried
  `key: value` frontmatter shape below the representation seam.
  Removed from the claim and from `moot()`'s docstring; the Lean
  brief's trigger now says "moot claim" for the same reason.
- **"A verdict on it judges the framing" contradicted ABSORB.** A
  verdict on a moot claim is dropped, not reinterpreted, and mootness
  is computed rather than issued (FORCE). The sentence described a
  move the algebra does not have. Deleted rather than reworded —
  what remains is what is checked.

## Decisions

### The sigil and the certificate are not in tension

**Rationale:** `SENSE+` is the agent's act; `certified(CHECK)` is the
checker's. Two assessors, two addresses — the act algebra's own
reading. The schema's "a certified claim's standing is bare" is the
case where the check is the *only* act. So SENSE keeps `agent`: the
commitment that mootness is a color outside the order rather than a
point in it is a modelling choice with a live alternative, and that is
what a judge is for.
**Consequence:** the flattened line is a fair summary of the file,
which is what made the other three defects visible from it.

## Conventions Established

- A claim's `verify:` must select every commitment the body makes, or
  the body must shrink to what the check covers. A `-k` pattern that
  names one bullet of three is a checker's act asserting more than it
  checked.

## References

- `docs/dev/devlog/2026-08-18-002-File-the-derived-results-as-claims.md`
  — filed SENSE; its open question about SENSE's standing is answered
  above.
