---
label: NON_CLAIM_TOKENS
standing: user
authority: "@bukzor 2026-09-01: 'My idea is: a listing of token-looking-but-not-token words, somewhere.' -- and, on the cost model: 'a positive is always actionable, regardless of whether it's false. But i'd think in a mature kb tree the rate of false positives goes to a long tail.'"
why:
  - a-claim-has-two-name-renderings.md
  - a-label-is-at-least-two-characters.md
---

# Non-Claim Tokens Are Enumerated, Not Inferred

A label-shaped token that cites no claim -- an acronym, a system name,
an `RFC` keyword -- is declared in the record, token by token. No
oracle infers the distinction from context.

Two inferences were tried, and both failed measurably:

- **Fleet membership** -- "a token is a label only if some discovered
  ledger defines it" -- makes the gate depend on what happens to sit
  on disk near the scanner: a template's example labels enter it, a
  single-ledger checkout starves it, and a typo'd or unledgered
  citation is silently presumed English, which is the one case the
  scan exists to catch.
- **Backtick quotation** -- "a backticked name is a literal" -- was an
  agent inference the corpus never obeyed: measured 2026-09-01,
  fourteen of the twenty-three backticked fleet labels are ordinary
  mentions wearing decoration.

Enumeration inverts the failure mode. An unlisted token surfaces as a
finding, and a positive is always actionable, regardless of whether it
is false: true, it is citation rot to repair; false, it costs one line
added to the list, once, visibly. In a mature tree the false-positive
rate goes to a long tail, because the list grows with new vocabulary,
not with new prose. Projected at twenty-one tokens before the scan was
repaired; built 2026-09-03, once backticks were read through
(BACKTICK_SCOPE), the whole burden past the LABEL_MIN floor is
forty-one tokens over twenty-three lists, thirty-four of them confined
to a single ledger. Five citations survived the seeding -- real labels
in unimported theories, which is the finding the gate was inverted to
surface.
