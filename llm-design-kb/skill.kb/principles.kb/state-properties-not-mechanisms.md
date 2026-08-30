# State Properties, Not Mechanisms

A requirement or design entry names what must be true, never how it
happens to be achieved today. "Enforced deterministically" is a
property; "compiles to hooks" is a mechanism — and naming the
mechanism at a layer above the one that implements it locks the
whole entry to a tool, a version, or a vendor that the property never
needed. This applies to entry titles as much as to bodies; a title
that encodes a mechanism has already made the mistake, no matter how
carefully the prose below hedges it.

The mechanism still needs documenting — it belongs in the specific,
lower-layer entry that actually implements the property, referenced
by name from the property-level entry, never restated there.
