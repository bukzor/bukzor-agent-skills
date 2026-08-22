---
label: COHORT
standing: open
why:
  - when-does-the-reform-execute.md
---

# Which Other Skills Want the Same Reform?

`llm-discourse-graph` is the fleet's first extension of
`/llm-claims`, not necessarily its only one. @bukzor: "There may be
one or two other skills that are slated for the same kind of
treatment. Has `/llm-design-kb` undergone this transformation? I'm
pretty sure it should."

`/llm-design-kb` has not. It carries `principles.kb/`, `jsonschema/`,
and `references/`, and no ledger of any kind -- so its own design
commitments are unrecorded, and it cannot be an extension of a
notation it does not use.

Two questions, and only the second is open:

- Should `/llm-design-kb` keep a ledger? Yes, on the same warrant as
  every other skill that has one, and `llm-kb` just took that step
  itself. That much needs no ruling.
- Is that the same reform? Not obviously. `llm-discourse-graph` is
  being reformed because its *ontology* -- five node types, a
  truth-valued `status:`, a stored `likelihood` -- is what the claims
  format supersedes. `/llm-design-kb`'s `why:` is cited as prior art
  by the claim schema itself, so it may be an ancestor rather than a
  candidate for replacement.

Rule this: does `/llm-design-kb` become an extension of
`/llm-claims`, or does it merely gain a ledger like any other skill
and keep its own shape? And name the "one or two other skills" if
there are more.
