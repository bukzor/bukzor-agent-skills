---
label: ACTS_ADOPTED
standing: open
why:
  - ../unify-the-format-with-the-stet-design-work.md
---

# Are Acts the Base, and Standing the Projection?

The stet design work replaced the single `standing:` field with an
append-only log of judgments, and made `standing:` a cache over it:

```yaml
standing: user
acts:
  - {source: agent, date: "2026-08-18", verdict: proposed, note: "offered with the alternative of leaving the kernel as a design incubator"}
  - {source: user,  date: "2026-08-18", verdict: accepted, note: "\"yep, exactly\""}
```

Its own claim for this -- ACT_LOG, in
`~/claude/meta-reasoning/claims.kb/plans.kb/` -- argues three things
this notation cannot currently do. A superseded judgment stays true,
because "the user accepted this on the 18th" is a historical fact that
a later reversal does not falsify, and both entries sit in the file in
order. Currency stops being stored: the last entry of a given source
is that source's current judgment, so no field can drift out of step
with it. And `standing:` where it disagrees with the log is a defect
rather than a second opinion.

Adoption would be additive and would migrate nothing: a claim with no
`acts:` is the degenerate case where `standing:` is the whole record,
which is every ledger in this fleet today.

Against adoption, argued honestly: this notation already puts the
judgment's provenance in `authority:` as a quotable sentence, which is
more readable than a verdict word and is what a reader actually cites;
and an append-only list in frontmatter is a log in the wrong place,
since git already holds every past judgment with its date and author.
The counter is that git holds them where no `grep` will find them.

Nobody has ruled. The user's prior: the older `standing:` is "less
descriptive, less accurate, and less helpful than the newer design(s)".
