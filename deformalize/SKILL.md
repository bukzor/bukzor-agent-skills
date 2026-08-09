---
name: deformalize
description: "Agent MUST load when asked to make dense formal material (a claim ledger, a mathematical text, a theory write-up) concrete, executable, or plain enough to poke with a stick, or to check such an account against runnable code."
---

# /deformalize \<paths\>

Take the formal content at the paths -- a claim ledger, a dense
mathematical text, a theory write-up -- and produce its plain-old-code
representation: runnable Python the owner can read and poke with a
stick, with the formal vocabulary demoted to internal detail.

This is not a port; it is a probe. Reification is where a formal
account's slid-over seams surface, so what the code breaks in the
source is the primary finding, not a footnote.

## The output contract

1. **Plain-old-Python.** Boring, obvious code: stdlib-flavored,
   dataclasses and functions, names in plain words. The jargon lives
   in the docstring at its definition site -- so every formal term
   has exactly one place where it is cashed out -- and nowhere in the
   API.
2. **The file order is the theory order.** Each section uses only
   names defined above it, so truncating at any section banner leaves
   a working program -- the source's dependency structure made
   literal. In multi-module form the same law is "the import graph
   respects the source's poset", and a test checks it; the
   single-file form should self-test its truncatability too.
3. **One law, one check.** Each law becomes the smallest demo or test
   that would fail if the law were false -- a witness, not a
   restatement. A law you can't check in ~50 lines isn't thereby
   wrong, but say why not, in place: "not mechanically checkable,
   because X" is part of the account.
4. **The jargon table.** Deliver a source-term -> code-object mapping
   alongside the code. It is the reading aid the whole exercise was
   bought for; an unmapped term means an unreified idea.

## The review step

When the code runs, review the pair, claim by claim: does the witness
show what the source asserts? Every mismatch is adjudicated out loud,
one of two ways -- the account was wrong (propose the edit to the
source, saying what changed) or the code is wrong (fix it, saying
why). No silent repair in either direction; a mismatch smoothed over
is a finding destroyed. Expect the strict-reading failures to be the
valuable ones: a demo that only passes under a weaker premise has
found the source's missing premise.

The source edits this step accumulates are the owner's decisions to
make; present them for ruling: `Skill(review-open-questions)`.

## Lifecycle

Draft in `trash/` -- it is a sketch until it survives the review
step. But a `verify:` target cannot live in scratch: if the witness
earns keeping, promote it to a real project home (pyproject, real
modules, real test suite), name its tests after the claims they
witness, and wire the source's `verify:` lines to them. Promotion is
itself an escalation of enforcement grade, and expect that
escalation to find another round of cracks -- budget for it.
