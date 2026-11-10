---
label: CLEANUP
standing: user
why:
  - tense.md
  - ../goals.kb/review.md
authority:
  address: "97605ccb"
  words: "we intend to git-rm the 'done' handoffs during project cleanup, after we're fully satisfied on review"
---

# Done handoff files live until review is over

A done handoff file exists only for review. Once the plan's success
criteria pass and the user is fully satisfied on review, cleanup
records the plan's commit range in the plan and `git rm`s the plan's
handoff collection. Its record stays in git.

> [!@bukzor] 97605ccb
>
> on tense: it may be worth saying that we intend to git-rm the 'done'
> handoffs during project cleanup, after we're fully satisfied on
> review.
