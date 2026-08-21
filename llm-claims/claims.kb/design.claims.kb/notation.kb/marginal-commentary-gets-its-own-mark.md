---
label: MARGIN
standing: user
why:
  - containment-is-indentation.md
---

# Marginal Commentary Gets Its Own Mark

A sub-bullet opened with `//` is commentary about its parent claim, not
containment: it takes no label, no sigil, and does not travel with the
claim when it is re-rendered, filed, or flushed.

The mark is load-bearing, not decorative: `containment-is-indentation.md`
already makes a labelled child mean "confined to this theory," so an
unmarked, unlabelled child would be ambiguous — commentary, or a claim
whose label got dropped by accident. `//` disambiguates and greps
(`grep -n '\* //'` finds every note in a render) at the cost of one
punctuation mark.

Declined: `#`. It reads as a heading-of-a-heading in most markdown
where a bullet is a list item, so it renders wrong more often than the
ambiguity it would have resolved.
