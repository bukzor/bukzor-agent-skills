---
label: GUIDE_HOME
standing: user
why:
  - what-becomes-of-llm-discourse-graph.md
---

# Where the Migration Guide and Its Trigger Live

Both live in `llm-discourse-graph` itself: the guide under
`skill.kb/`, and a `must-read.kb/when/` trigger pointing at it.

The warrant is routing, not tidiness. An agent that meets an
old-format directory loads `llm-discourse-graph`, because that is
what the directory is; whatever it needs to read next has to be
reachable from there.
