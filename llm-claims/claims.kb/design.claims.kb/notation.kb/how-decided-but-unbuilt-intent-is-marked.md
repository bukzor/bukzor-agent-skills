---
label: DECIDED_UNBUILT
standing: user
authority: "@bukzor 2026-08-29, during the llm-design-kb reform: the pre-colon token was his strawman here; the frontmatter form his proposal -- 'the claim body *is* the built when. I think future: true is more honest. Or even todo: true, for homoiconicity's sake.'"
why:
  - ../notation.md
  - an-open-question-needs-no-new-mark.md
---

# How Decided-but-Unbuilt Intent Is Marked

A claim decided but not yet built takes one word, in the pre-colon
slot in chat -- `XY! todo: the island rule is ***` -- and as
`todo: true` in frontmatter. The body already states the future
state, so the mark restates nothing: when the state lands, drop the
token and the line is already the descriptive sentence; on disk,
delete the key (adding `verify:` if a check now exists) and the label
never moves.

Why each rejected shape lost:

- **A label affix** (`TODO-` prefix, `-TODO` suffix): breaks every
  `why:`/`<-` reference on the day the state ships -- the one day the
  record matters most -- and is illegal under the label pattern
  besides. The label names the locus, not the tense.
- **`verify:`-that-cannot-run**: not greppable data -- reading it as
  "unbuilt" requires running the check and expecting failure, a
  reading with no basis in the file; and it has no chat-compatible
  one-line form.
- **A structured suffix** (`-- built-when(CONDITION)`): everything
  past the first `:` is opaque prose, repeatedly ruled; and the
  condition would be a second copy of the body, drifting from it.
- **A second frontmatter field** (`built-when:`): same duplication --
  the claim body *is* the "built when".
- **`future: true`**: reads as a category, quietly re-minting the
  future-work bucket the design-kb reform dissolved; `todo` is one
  word across prose callout (`[!TODO]`), chat token, and frontmatter.

`const: true`, not boolean -- absent already means false, so no claim
on file needs migration (the same route `verdict:` shipped with).
Undecided work needs none of this: it is a plain `?` claim
(an-open-question-needs-no-new-mark.md), and scheduling remains
`Skill(llm-subtask)`'s job. The `formalize/` pair that motivated the
question -- decided, unbuilt, distinguishable only by body prose --
is the intended first consumer.
