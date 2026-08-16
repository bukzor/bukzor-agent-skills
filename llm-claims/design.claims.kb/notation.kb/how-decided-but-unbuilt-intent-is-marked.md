---
label: DECIDED_UNBUILT
standing: open
why:
  - ../notation.md
---

# How Decided-but-Unbuilt Intent Is Marked

How does the notation mark a claim that is decided but not yet
built -- the `llm-discourse-graph` `TODO!` analogue? Open.

`?` already covers *disputed* claims; what's missing is tense on a claim
nobody disputes. `formalize/design.claims.kb/purpose.kb/`'s AUTOCHECK and
EXTRACT are the live instance: both ruled `user`, neither built, and the
distinction lives only in a sentence of body prose today -- nothing in
the frontmatter says "decided, not yet real."

One shape is on the table, and it is a strawman, not a decision: a token
between sigil and colon, `AUTOCHECK! todo: there's an autochecker`,
keeping the label stable across the status change (a `-TODO` suffix
would break every `why:`/`<-` reference on the day it ships). It has not
been argued for past that one property, and the `.kb` file form has no
counterpart at all -- no frontmatter field, `verify:` the nearest
neighbor and not actually the same thing.

An answer would settle: what the marker is (a status suffix like
`certified(CHECK)`, a frontmatter field, something else), whether it
takes the same shape in-chat and in `Skill(llm-claims-kb)`, and whether
it belongs to this notation at all rather than to `Skill(llm-subtask)`,
which already schedules undone work.
