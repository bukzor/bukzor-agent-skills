---
name: deformalize
description: "Agent MUST load when asked to make a formal account -- a claim ledger, usually /formalize's output -- readable in plain English, or to check such an account against a runnable witness."
---

# /deformalize \<paths\>

Take the very-formal account at the paths -- normally `/formalize`'s
output -- and add what it needs to be read: a glossary, and
plain-English successor theories built on it. Escalate to a runnable
witness only when the account needs one.

This is not a port; it is a probe. Reification -- in any of its forms,
prose or code -- is where a formal account's slid-over seams surface, so
what breaks in the source is the primary finding, not a footnote.

## The formal side stays formal

`/formalize` delivers a formal account and keeps it formal -- the
vocabulary is what lets a claim pin anything down, and an account
rewritten to dodge it pins down proportionally less. `/deformalize`
never rewrites the source; it adds a reading path beside it.

## The primary path: glossary, then successor theory

1. **Glossary.** A glossary is a set of claims, each taking the
   very-formal theory as a prior and defining one plain-English
   alternative to one of its terms. Record the definitions the owner
   asked for; rename aggressively wherever a plain name is equally
   accurate -- a renamed term needs no entry. No further ritual: this is
   the whole of the apparatus for now.
2. **Successor theory.** The plain-English restatement takes the
   glossary as its prior, never the formal theory directly -- so the
   glossary is the only place a formal term is ever cashed out, and the
   only place that needs revisiting when a term's plain name changes.

Deliver both per `Skill(llm-claims)`; file to `Skill(llm-claims-kb)`
only once the account earns keeping.

## Escalating to a runnable witness

Plain-old-Python is the third rung, reached when a claim needs a demo
that would fail if the claim were false -- not the default path.

1. **Plain-old-Python.** Boring, obvious code: stdlib-flavored,
   dataclasses and functions, names in plain words. Jargon lives in the
   docstring at its definition site, never in the API -- the glossary
   above is the reading aid; the code doesn't re-derive it.
2. **The file order is the theory order.** Each section uses only names
   defined above it, so truncating at any section banner leaves a
   working program. In multi-module form: the import graph respects the
   source's poset, and a test checks it.
3. **One law, one check.** Each law becomes the smallest demo or test
   that would fail if the law were false -- a witness, not a
   restatement. A law you can't check in ~50 lines isn't thereby wrong,
   but say why not, in place.

## The review step

When a witness runs -- prose or code -- review it against the source,
claim by claim: does the witness show what the source asserts? Every
mismatch is adjudicated out loud, one of two ways -- the account was
wrong (propose the edit to the source, saying what changed) or the
witness is wrong (fix it, saying why). No silent repair in either
direction; a mismatch smoothed over is a finding destroyed. Expect the
strict-reading failures to be the valuable ones: a demo that only passes
under a weaker premise has found the source's missing premise.

## Lifecycle (code only)

Draft code in `trash/` -- it is a sketch until it survives the review
step. A `verify:` target cannot live in scratch: if the witness earns
keeping, promote it to a real project home (pyproject, real modules,
real test suite), name its tests after the claims they witness, and
wire the source's `verify:` lines to them. Promotion is itself an
escalation of enforcement grade, and expect that escalation to find
another round of cracks -- budget for it.

The glossary and the successor theory have no such lifecycle -- they are
ready the moment they are written, and filing them to disk is the same
optional step `/formalize`'s own output takes.

The reasoning behind everything above, and the place to argue with it:
`design.claims.md`.
