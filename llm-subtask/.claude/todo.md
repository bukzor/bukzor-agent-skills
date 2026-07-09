---
managed-by: Skill(llm-subtask)
cost-benefit-sweh:
  timebox:
    "@value": 2.5
    rationale: |
      Three inline improvement items: bin/ script CWD-vs-path bug
      (~1h, same root cause as llm-collab bug), todo.kb/ideas.kb
      template boilerplate trim (~0.5h, both skills affected), tier
      selection guidance push toward lightest tier (~1h, requires
      SKILL.md update with heuristic).
    confidence: tentative
  benefit-2w:
    "@value": 0.5
    rationale: |
      Per-session UX improvements affecting every llm-subtask
      invocation. Modest individual, flowing across all sessions
      that use the skill.
    confidence: tentative
  cost-of-delay-2w:
    "@value": 0.2
    rationale: |
      Each item is a per-session tax: bin/ scripts mangle filenames
      silently, templates waste agent attention, heavyweight tier
      defaults waste effort. Flowing taxes across all skill uses.
    confidence: tentative
---

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
  - Data point (2026-07-07, bukzor-agent-skills): monorepo with per-skill
    lists adopted breadcrumb checkboxes — root todo.md points at each
    subpath todo.md; session entries point at briefs; details never
    duplicated upward

## Later

- [ ] todo.kb/2026-02-10-000 (Milestone/phase planning pattern gap) — discussion invited
