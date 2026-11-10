---
label: UNIT_COMMIT
standing: user
verdict: superseded
why:
  - ../../requirements.kb/unit-diff.md
---

# The coordinator commits each unit on receipt

The coordinator commits each unit's scope paths when the unit's report
arrives, and sub-agents never touch the index.

Superseded by AGENT_COMMIT (`agent-commit.md`). It gave one commit per
unit, but under the coordinator's hand: one party
committing another's work, with no commit until the agent was done,
so nothing of a unit in flight survived as history.
