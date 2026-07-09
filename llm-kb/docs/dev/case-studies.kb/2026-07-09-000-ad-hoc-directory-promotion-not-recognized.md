---
date: 2026-07-09
failure-modes:
  - promotion-signals-assume-flat-file-origin
---

# Ad hoc directory promotion not recognized

A prior session had asked an agent to bring `todo.kb/reunify-dotfiles/`
(an ad hoc directory of one-file-per-task, missing the `.kb` suffix, a
date-prefix matching its `todo.kb/` siblings, and a top-level pointer
file) into "proper llm-kb form." The user reported:

> above is my attempt to get "reunify dotfiles" into standard sub-kb
> form. i'm not sure it's done right though.

> does llm-kb not explain this pattern sufficiently? i tried to refer to
> it several times but agent seemed oblivious
>
> "this pattern" being the breakdown from X.md to X.kb/ when X.md
> becomes a listing
> initially I had a todo.kb/reunify-dotfiles/{todo files}.md, and I
> asked agent to put things in proper llm-kb form. they were seemingly
> mystified and i eventually had to do it myself.

Investigating (in a fresh session), I confirmed the user's own rename
was already correct in every load-bearing way — schema validated clean,
cross-references resolved — modulo two stale path references left over
from the rename, which I fixed. I then checked why the earlier agent
couldn't do this itself: SKILL.md's "Promotion Signals" section only
gave triggers for one starting shape — a flat `.md` file exhibiting
listing signals (plural filename, parallel sections, per-item growth
pressure). The user's starting point was a directory, already split
into one file per task. None of the documented signals named that
shape, so there was nothing for the agent to pattern-match against —
not a case of ignoring the skill, but of the skill only teaching one
instance of the pattern instead of the pattern itself.

The user's diagnosis, once the gap was found:

> we should demote the promotion material to a minor procedural note,
> and promote *the pattern* as primary. it's much more important that
> agent internalize the pattern than have the procedure for promotion
> spelled out.

Acted on directly — see
`../adr/2026-07-09-000-Promote-pattern-recognition-over-promotion-procedure-in-SKILL-md.md`.
