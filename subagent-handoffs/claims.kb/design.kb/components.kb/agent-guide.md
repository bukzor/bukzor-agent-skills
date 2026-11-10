---
label: AGENT_GUIDE
standing: agent
why:
  - ../architecture.kb/homes.md
  - ../architecture.kb/commits.md
  - ../architecture.kb/steps.md
---

# `templates/CLAUDE.md`: the agents' protocol

Copied into each plan's handoff collection, where Claude Code loads it
whenever an agent reads a file there. So it holds the protocol from
the agent's side and every rule all of the plan's agents share,
written once instead of into each brief.

Its git rules name a path-scoped commit command, `git commit-files
PATHS`, as a placeholder: a project without that tool substitutes any
commit that takes its paths from the index and leaves a sibling's
staged changes alone.
