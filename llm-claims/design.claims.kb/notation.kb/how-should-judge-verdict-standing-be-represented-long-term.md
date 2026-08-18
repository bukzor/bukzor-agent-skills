---
label: GRAIN
standing: open
why:
  - the-sigil-signs-the-judge.md
  - ../purpose.kb/the-format-must-hold-whatever-is-actually-true.md
  - ../purpose.kb/forced-misrepresentation-is-the-failure-mode.md
  - a-verdict-names-what-the-judge-ruled.md
  - ../../../docs/dev/strata.claims.kb/standing.md
  - ../../../docs/dev/strata.claims.kb/data-representation.md
---

# How Should Judge/Verdict/Standing Be Represented, Long-Term?

The two gaps FLEXIBLE and RATIONAL name -- a claim two assessors
judge differently, and a verdict finer than a small discrete set --
are answered in ruled law, not open here: verdicts are an
assessor-keyed map (ASSESSOR), values are cuts of a continuous
commitment space, re-cut when usage demands (STATUS), and scalar
`standing:` is licensed as the one-entry sugar of that map (SUGAR).
A row's `standing:`/`verdict:`/`authority:` triple already reads as
one judgment act -- issuer, ruled value, occasion -- and the schema
already holds two acts of different sorts on one claim, spelled
field-per-sort: the human's in `standing:`+`authority:`, a
checker's in `verify:` (strata's DEFEAT carries both). What this
question still asks is presentation, three parameters:

- KEY -- the spelling of the map once a second assessor *of the
  same sort* writes (CASCADE's `$all` plus RFC 7396 merge-patch, or
  otherwise), and the collision lint that trips the widening. That
  lint is armed: `engine_tower`'s ledger test resugars each claim
  from its acts and asserts one signing act, so the day a second
  same-sort assessor signs one, the test fails and this parameter
  comes due.
- CUT -- which discrete words the written value uses, and when a
  word escalates to the truth/certainty/utility triple; entangled
  with HEDGE_FORM, which the same map would close in the same
  stroke.
- CACHE -- when a computed, stance-indexed standing is cached and
  stamped (COMPUTED's discipline). The defeat fixpoint runs over a
  real ledger; the evidence operator whose least fixpoint *is*
  standing does not, and until it does this parameter is acceptance
  debt.

`how-should-judge-verdict-standing-be-represented-long-term.kb/`
holds one file per prior design bearing on this -- read them as
coordinates in this parameter space, not rivals: MECHANIZED is the
semantics the rest presuppose, and CONVERGE is every parameter held
at its minimum behind a tripwire, ON_DEMAND applied here. Rule by
editing this file's `standing:`; when it closes, rewrite this as
the answer and keep the `.kb/` as the record of roads not taken.
