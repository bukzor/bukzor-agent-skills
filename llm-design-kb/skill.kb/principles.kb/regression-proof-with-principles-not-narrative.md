# Regression-Proof With Principles, Not Narrative

A design entry states current understanding, forward-facing — this
skill's "Alternatives Considered" rule already says so. The corollary
that's easy to miss: when a gap or error surfaces in an entry, the
fix belongs in the *principle* (a sharper, more checkable why:
requirement or goal), never in a paragraph narrating what went wrong
and when it was corrected. "We used to think X; we now think Y
because Z happened" is history — an ADR's job, not a design tower's.

The tell: if removing every past-tense, dated, or self-referential
sentence from an entry would leave it just as actionable, those
sentences were narrative, not design content. Cut them; if they
contained a real regression risk, that risk is a missing or
too-loose principle — write or sharpen that instead.
