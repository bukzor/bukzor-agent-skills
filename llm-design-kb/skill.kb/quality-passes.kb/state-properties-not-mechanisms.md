# State Properties, Not Mechanisms

A requirement or architecture claim names what must be true, never how it
happens to be achieved today. "Enforced deterministically" is a property;
"compiles to hooks" is a mechanism -- and naming the mechanism above the rung
that implements it locks the claim to a tool, a version, or a vendor that the
property never needed.

Walk each requirement and architecture claim, title first: a title that
encodes a mechanism has made the mistake however carefully the prose below
hedges it. A finding is any tool, format, or vendor named where a property
would answer the rung's question.

Repair: restate the property. The mechanism still needs documenting: it
belongs in the lower-rung claim that implements the property, which the
property-level claim names, never restates.

The general rule, for every rung: `each-rung-says-only-what-its-question-asks.md`.
