---
label: LABEL_FORMATS
standing: user
authority: "@bukzor 2026-08-31, ruling: 'when mentioning a claim it's valid (and probably recommended) to omit the suffix, and valid to omit the sigil. The only place where a claim-label must be fully qualified is the definition site. As such, a claim object has two name renderings: just the label, and the fully-qualified, definition label.'"
why:
  - the-sigil-signs-the-judge.md
  - how-decided-but-unbuilt-intent-is-marked.md
  - ../good-smells.kb/names-outlive-contents.md
---

# A Claim Has Two Name Renderings

A claim's name renders two ways, and which one is licensed depends on
one thing: whether the name sits at the definition site.

- The **qualified** rendering -- label, sigil, and any `(todo)` -- is
  required at the definition site, the line or file that states the
  claim. That is the one place the standing is not a copy.
- The **bare** rendering -- the label alone -- is licensed everywhere
  else, and is the recommended default for prose that merely names a
  claim.

A mention carrying a sigil is carrying a cache of data owned elsewhere,
and it goes stale on the day the claim is re-signed -- which is exactly
the day someone is reading to find out what changed. So the copy is
legal but not free: take it where the warrant-mix is the point, as in an
arrow clause read at a glance (`XY <- AB! CD?`), and skip it where the
sentence only needs the locus.

What the permission does not reach is the definition site itself. Bare
is a mark, not the absence of one -- it asserts that no judge was needed
-- so a definition with the sigil dropped is not unmarked but wrong,
claiming a judgment nobody made. The four marks exhaust the space
(the-sigil-signs-the-judge.md); none of them is silence.

The file form already ruled this way and the chat notation was the
straggler: `why:` entries are bare references "never carrying a copied
sigil", and `llm-claims-kb-flatten` computes the sigils it prints in
arrow clauses from each cited claim's own file rather than reading them
from the citation. Prose scanners follow the same rule --
`llm-claims-kb-mentions` matches the bare label, since bare is the
mention form.

The declined alternative was to require the qualified form everywhere,
which reads as rigor and buys a corpus of standing-copies that no tool
updates: one re-signing would leave the fleet disagreeing with itself
about who ruled a claim, with no way to tell the stale copies from the
deliberate ones.
