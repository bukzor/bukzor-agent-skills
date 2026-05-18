---
managed-by: Skill(llm-subtask)
---

- [ ] .claude/ideas.kb/2026-04-17-000-llm-subtask-init-ignores-path-argument-uses-cwd.md
  - All bin/ scripts use CWD, agent naturally passes paths → mangled filenames or wrong repo
- [ ] todo.kb AND ideas.kb templates too boilerplate-heavy
  - Agent had to read 43 lines of placeholder then overwrite entirely
  - Simpler skeleton: title + frontmatter + blank sections, no [placeholder text]
  - ideas.kb template same problem — affects both llm-subtask and llm-collab
- [ ] Tier selection guidance too weak — agent defaults to heavyweight
  - Filed 10 individual ideas.kb entries when todo.md bullets were the right call
  - User had to correct: "this is very heavyweight, just use bullets"
  - Skill describes four tiers but doesn't push hard enough toward the lightest sufficient tier
  - Proposed heuristic: "batch of related lightweight feedback → todo.md bullets, not ideas.kb files"
  - policy note: "you may give additional detail via sub-bullets in todo.md"
- [ ] Guidance on which repo owns a todo in multi-repo setups
  - Financial todo started in bukzor-llc, belonged in evan-family
  - Skill doc has no advice for cross-repo task ownership

## Later

- [ ] todo.kb/2026-02-10-000 (Milestone/phase planning pattern gap) — discussion invited
