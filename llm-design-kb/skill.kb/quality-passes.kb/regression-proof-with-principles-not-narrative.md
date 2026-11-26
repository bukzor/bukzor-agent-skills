# Regression-Proof With Principles, Not Narrative

A design claim states current understanding, forward-facing. When a gap or
error surfaces in one, the fix belongs in the *principle* -- a sharper, more
checkable claim or `why:` -- never in a paragraph narrating what went wrong
and when it was corrected. "We used to think X; we now think Y because Z
happened" is history: a devlog's, or an ADR's.

Walk each claim's prose for past-tense, dated, or self-referential
sentences. One is a finding if removing it leaves the claim just as
actionable. A declined option's `verdict:` and its ground are not narrative:
they say what binds now.

Repair: cut the sentence. If it carried a real regression risk, that risk
is a missing or too-loose principle: write or sharpen that instead.
