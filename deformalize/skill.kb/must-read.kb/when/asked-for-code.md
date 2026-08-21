# Asked for Code

When the request is for runnable code specifically -- not just a
plain-English reading -- escalate past the glossary and successor
theory to a plain-old-Python witness. This is the pre-2026-08-15 shape
of `/deformalize`, still exactly right when code is actually wanted.

## Plain-old-Python

1. **Plain-old-Python.** Boring, obvious code: stdlib-flavored,
   dataclasses and functions, names in plain words. Jargon lives in the
   docstring at its definition site, never in the API -- the glossary
   is the reading aid; the code doesn't re-derive it.
2. **The file order is the theory order.** Each section uses only names
   defined above it, so truncating at any section banner leaves a
   working program. In multi-module form: the import graph respects the
   source's poset, and a test checks it.
3. **One law, one check.** Each law becomes the smallest demo or test
   that would fail if the law were false -- a witness, not a
   restatement. A law you can't check in ~50 lines isn't thereby wrong,
   but say why not, in place.

Run the review step (`../../../SKILL.md`) against what comes out.

## Lifecycle

Draft in `trash/` -- it is a sketch until it survives the review step.
A `verify:` target cannot live in scratch: if the witness earns
keeping, promote it to a real project home (pyproject, real modules,
real test suite), name its tests after the claims they witness, and
wire the source's `verify:` lines to them. Promotion is itself an
escalation of enforcement grade, and expect that escalation to find
another round of cracks -- budget for it.

This lifecycle is code-specific. The glossary and the successor theory
have none -- they are ready the moment they are written.
