---
managed-by: Skill(llm-subtask)
related-effort: ~/repo/github.com/bukzor/prototype.chatfs/.claude/todo.kb/2026-07-13-000-graduation-and-integration.kb/2026-07-13-005-design-kb-reconciliation-and-graduation-adr.md
cost-benefit-sweh:
  timebox:
    "@value": 6.0
    rationale: >
      Convention design + validator support, not a big build: cross-kb
      reference form, symlink semantics, traversal-scope rule, plus the
      llm-design-kb policy rider. Overrun signals over-engineering —
      the downstream consumer is proceeding on interim conventions
      regardless.
    confidence: tentative
  benefit-2w:
    "@value": 1.0
    rationale: >
      prototype.chatfs's design-entry graduation is the live consumer;
      it uses interim conventions meanwhile, so payoff is correctness
      and tooling, not unblocking.
    confidence: tentative
---

# Cross-kb cooperation conventions (monorepo-ish multi-kb repos)

**Priority:** Medium
**Complexity:** Medium (design-heavy, code-light)
**Context:** Raised 2026-07-13 planning prototype.chatfs's graduation
(incubator design entries → package-scoped kbs; project design.kb keeps
seams only). The repo already runs multiple kbs per subsystem de facto
(crate-scoped technical-policy.kb, incubator design.kbs, per-package
dev.kbs); what's missing is codified conventions for kbs that cooperate
across subpaths. Type specimen of the failure mode: prototype.chatfs's
`stack-split.md` — a project-level doc asserting subsystem internals,
drifted silently.

## Problem Statement

When one repo hosts many kbs, three mechanics are unowned:

1. **Content sharing.** Symlinks work (can't drift in content; already
   used for shared jsonschema files and mirrored entries) but dangle on
   moves — detectable via `find -xtype l`, undetected today.
2. **Cross-kb references.** Frontmatter refs (`why:`, `blocked-by:`) are
   bare same-kb slugs; crossing kb boundaries needs a defined form
   (relative path?) and validator support (overlaps
   `2026-06-03-000-validate-path-references.md`).
3. **Maintenance traversal scope.** "Find affected docs" passes don't
   know which kbs are in scope for a change — needs a rule or manifest.

And one policy question: can generic llm-kb mechanics cover the
llm-design-kb case? Hypothesis (2026-07-13): yes for 1–3; llm-design-kb
adds only a thin layer-crossing policy (a subsystem kb's mission/goals
link upward into parent goals/requirements; a parent 040 states seams
between subsystems, never their internals — "designed pieces have
designs" self-similarity).

## Interim conventions (in force downstream until this lands)

Symlinks for shared files; relative paths for cross-kb references;
repo-wide backlink grep on any move/delete. Declared 2026-07-13 in
prototype.chatfs's graduation umbrella.

## Implementation Steps

- [ ] Decide cross-kb reference form + teach `llm.kb-validate` to resolve
      it (with `2026-06-03-000-validate-path-references.md`).
- [ ] Symlink conventions: when to mirror vs reference; `find -xtype l`
      in validation.
- [ ] Traversal-scope rule for maintenance passes (manifest vs
      discovery-by-glob).
- [ ] llm-design-kb rider: layer-crossing policy + seams-only rule for
      parent kbs (document in that skill; it has no `.claude/` of its
      own today).
- [ ] Reconcile the interim conventions: bless, adjust, or migrate what
      downstream did under them.

## Open Questions

- Does the "one home per fact" rule need tooling (duplication
  detection), or does convention + review suffice?

## Success Criteria

- [ ] A repo with N cooperating kbs has a documented answer for sharing,
      referencing, and traversal — and `llm.kb-validate` enforces the
      referencing part.
- [ ] prototype.chatfs's graduated entries validate under the blessed
      conventions with no dangling links.
