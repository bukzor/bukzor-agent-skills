---
label: NESTING
standing: agent
why:
  - a-theory-is-defined-by-a-claim.md
  - ../good-smells.kb/bare-form-stays-legal.md
  - ../good-smells.kb/survives-dumb-media-and-tools.md
---

# Containment is indentation, and it nests without limit

A claim written under another reads in every word that one stipulates.
That is the whole of theory membership: no `theory:` field, no grouping
header, no fixed two levels of claim-inside-theory -- a claim carrying
an `ontology:` is a theory, and what is indented under it is confined to
those words. The shape is the same at every depth and recurses as far as
the writer needs.

Indentation was already the cheapest structure a chat can carry: it
survives dumb media, needs no parser, and its all-defaults case is the
flat list, so nothing written before this nests wrongly. The alternative
was a membership field on every claim, which pays a token on every line
to say what a two-space indent says once, and still cannot express a
theory inside a theory.

`<-` stays orthogonal: indentation is sense, arrows are support. A prior
is what you cite when the words you need sit beside you rather than
above.
