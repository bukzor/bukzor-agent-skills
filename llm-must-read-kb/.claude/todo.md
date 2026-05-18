---
managed-by: Skill(llm-subtask)
cost-benefit-sweh:
  timebox:
    "@value": 1.5
    rationale: |
      File-level estimate for a 2-item rollup. Write
      references/create-new-trigger.md procedure + a small side item.
      The procedure itself unblocks the /must-read slash command.
  benefit-2w:
    "@value": 1.5
    rationale: |
      Procedure is shared by both manual and slash-command paths, so
      it removes a coordination cost. Unblocking the /must-read command
      returns trigger-creation ergonomics.
---

- [ ] Write `references/create-new-trigger.md` (canonical trigger-file creation procedure; blocker for the slash command)
- [ ] todo.kb/2026-05-15-000-must-read-slash-command.md
