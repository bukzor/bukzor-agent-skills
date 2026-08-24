---
managed-by: Skill(llm-subtask)
status: active
---

- [ ] Record the scoped-bare-`claims.kb` naming convention in SKILL.md
      ("Layout" and "What this is not"): when a ledger lives in a
      subject's sub-scope (e.g. `sources.kb/X.kb/claims.md` +
      `claims.kb/`), the collection takes its bare category name — the
      scope supplies the subject; `<name>.claims.kb` remains the form
      where a subject token is needed. Both claims skills already rule
      shape-over-name, so this is a naming addendum, not a semantics
      change. Ruled by the user 2026-08-24; rationale in
      `~/claude/meta-reasoning/docs/dev/devlog/2026-08-24-000-kb-nesting-conventions-ruled----breakdowns-live-under-their-source.md`;
      first worked instance is that repo's
      `sources.kb/design-discussion-transcript.kb/claims.kb/`.
  - [ ] Resolve the slot tension this surfaces: `bin/llm-claims-kb-graph`
        asserts the `X.md` beside `X.kb/` is a defining claim (frontmatter
        required; `ledger.py` `read_claim`), but llm-kb gives that slot to
        the prose roll-up — so the tool now errors on both worked ledgers
        (`claims.md`, `multi-design-merge.claim.md`). Either the tool
        learns to skip/accept a prose roll-up at the top slot, or the
        skill rules that a ledger's top `.md` is a defining claim and
        llm-kb's roll-up goes elsewhere. Predates 2026-08-24 (failed
        identically at the old flat path); surfaced by the normalization
        pass.
