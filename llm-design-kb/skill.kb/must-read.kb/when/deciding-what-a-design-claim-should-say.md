# When deciding what a design claim should say

> [!DRAFT] agent-authored 2026-11-25, vetoable: the split into passes and
> decision lenses, and the pointer to the file form's passes.

The lenses in `../../quality-passes.kb/` are about how any design record is
written, not about what any one project decided, so they apply to a record you did not write as readily as to
one you are drafting. The file form's own passes are `Skill(llm-claims-kb)`'s
[writing-a-claim-file]; this skill adds three, due while you write:

- [each-rung] -- you are writing any claim, highest rungs first, and reaching
  for detail its question does not ask.
- [state-properties] -- you are writing a requirement or an architecture claim
  and reaching for *how* it works. The rung below is where mechanism goes;
  confinement will report it if you don't.
- [regression-proof] -- you found an error in a claim and want to explain it
  in the claim. Sharpen the claim instead; the narrative is the devlog's.

Three decision lenses beside them judge the decision a claim records, not the
record:

- [evaluate-uses] -- you are about to keep, change, or retire something that
  serves more than one purpose. Enumerate the uses first; a single verdict on a
  bundle is wrong for at least one of them.
- [shared-shape] -- two collections look alike and merging them is tempting.
  Share the shape, not the identity.
- [residue] -- you are asking whether something should exist. Ask what remains
  once its substitutes are accounted for.

[writing-a-claim-file]: ../../../../llm-claims-kb/skill.kb/must-read.kb/before/writing-a-claim-file.md
[each-rung]: ../../quality-passes.kb/each-rung-says-only-what-its-question-asks.md
[state-properties]: ../../quality-passes.kb/state-properties-not-mechanisms.md
[regression-proof]: ../../quality-passes.kb/regression-proof-with-principles-not-narrative.md
[evaluate-uses]: ../../quality-passes.kb/evaluate-uses-independently.md
[shared-shape]: ../../quality-passes.kb/shared-shape-separate-semantics.md
[residue]: ../../quality-passes.kb/test-the-residue-not-the-bundle.md
