---
label: AGENT_COMMIT
standing: user
why:
  - ../../requirements.kb/unit-diff.md
  - ../../requirements.kb/resume.md
authority:
  address: "97605ccb"
  words: "sub-agents should be encouraged to git-add (with paths) as they work [...] git-commit-files before handback"
---

# Each agent commits its own unit

An agent stages its scope's paths as it works and commits them,
path-scoped, before it hands back. The coordinator then reviews the
unit's commits as it would a human collaborator's: keep them, reset
them, fix them up, or ask the agent for further commits. Separate
agents make separate commits, so each commit's author is the agent
that did the work.

> [!@bukzor] 97605ccb
>
> i think sub-agents should be encouraged to git-add (with paths) as
> they work. And, perhaps use git-commit-files before handback? then
> user/coordinator can reset, or commit --fixup, or request further
> commits -- all the things we might do in a human collaboration. and
> the idea that we get separate commits from separte agents (rather
> than one committing another's work) seems like a good smell?

> [!DRAFT] 97605ccb
>
> Staging as it works also serves RESUME: after an interruption, the
> index holds the unit's finished edits and the working tree its edit
> in flight. Concurrent agents share one index, so every add and
> commit names its paths; a bare commit would sweep a sibling's staged
> work into this unit.
