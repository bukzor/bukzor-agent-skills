---
managed-by: Skill(llm-subtask)
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
  - [ ] Record the slot ruling with it: the `X.md` beside a ledger's
        `X.kb/` is both the roll-up and the defining claim — one file,
        claim frontmatter over roll-up prose. llm-kb's validator and
        `references/frontmatter-outside-a-collection.md` already state
        it; this SKILL.md half-says it ("its entry point, carrying the
        poset") and should say it outright.
