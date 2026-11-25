---
label: LAYOUT
standing: user
todo: true
why:
  - quality-passes-run-at-occasions.md
  - the-pass-collection-is-quality-passes.md
  - skill-kb-is-a-collection-of-kbs.md
  - occasions-bind-without-llm-triggers.md
authority:
  address: 59b55f01
  words: 'agreed: PASS_NAME, PASS_AT_OCCASION, SMOOTHING, LAYOUT'
  about: the per-skill layout of quality passes
---

# Each Skill Keeps Its Passes, Their Occasions, and a Sweep

A skill keeps its quality passes in `skill.kb/quality-passes.kb/`, their
occasions in `skill.kb/must-read.kb/`, and one sweep that runs them in tiers. A
skill layered on another runs the base skill's sweep first, citing it
(`llm-design-kb` on `llm-claims-kb` on `llm-kb`).
