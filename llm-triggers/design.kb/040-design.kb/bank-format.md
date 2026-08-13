---
why:
  - ../../../design-next.kb/030-requirements.kb/judgment-triggers-remain-scannable.md
  - floor.md
---

# Bank Format

A trigger bank is an ordinary kb collection — the subsystem cites
`Skill(llm-kb)`'s spec one-way and adds no collection concepts of its
own. What it fixes beyond the base spec:

- **Juncture directories** partition the bank by when a trigger
  fires: `before/`, `after/`, `when/`. Filename plus juncture verb
  read as the full trigger phrase.
- **Filename is the index.** The bank is consumed as a listing
  (`ls -RF`); a body loads only when its trigger matches
  (`floor.md`).
- **Body is the payload.** Whatever delivery strength a consumer
  achieves — scan-time read, injected context, deny reason — the
  content delivered is the file body: one authoring format at every
  enforcement level.

V1's `llm-must-read-kb` documents the working instance of this
format (naming grammar, symlink aliasing, topical nesting,
composition with `procedures.kb/`); those conventions carry forward
unless an entry here says otherwise, and that skill folds into this
subsystem at the v2 build
(`../../../design-next.kb/040-design.kb/core-and-classes.md`).
