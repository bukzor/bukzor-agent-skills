---
managed-by: Skill(llm-subtask)
cost-benefit-sweh:
  timebox:
    "@value": 2.0
    rationale: |
      Extract 7 failure modes + 7 principles, seed two new kbs, cross-link
      and mark case-study reconciled. Beyond 2h you're polishing the new
      kbs rather than promoting the case-study content; defer polish.
  benefit-2w:
    "@value": 1.0
    rationale: |
      Reference-grade artifacts; payoff is indirect (future lookups while
      debugging similar failure modes). Estimate ~3-4 lookups over 2
      weeks at ~15 min saved each = ~1h.
---

# Reconcile seed case-study (May 13 har-browse rust-port)

**Priority:** High
**Complexity:** Medium
**Context:** `docs/dev/case-studies.kb/2026-05-13-000-har-browse-rust-port-scope-refactor.md`

## Problem Statement

The seed case-study at `docs/dev/case-studies.kb/2026-05-13-000-...` is raw
(no `status: reconciled` frontmatter). It names 7 failure-mode aliases and
~7 principles, and embeds a multi-step scope-refactor method inline. None of
those are yet promoted to canonical entries. Until reconciled, `docs/dev/`
methodology kb is a half-finished bet: `failure-modes.kb/` and
`principles.kb/` don't exist, and procedures elsewhere can't cross-reference
canonical aliases.

## Proposed Solution

Run `docs/dev/procedures.kb/reconcile-case-study.md` against the seed
case-study. That procedure's steps drive the work below.

## Implementation Steps

- [ ] Seed `docs/dev/failure-modes.kb/` from the 7 perceived aliases
    - [ ] `container-thinking.md`
    - [ ] `action-bias.md`
    - [ ] `anchoring-on-first-framing.md`
    - [ ] `empty-directory-paralysis.md`
    - [ ] `title-based-classification.md`
    - [ ] `defensive-admission-without-recovery.md`
    - [ ] `where-thinking-exclusively.md`
    - [ ] Each entry: description, recognition prompt, corrective signals
        (verbatim), worked example, recovery, `mitigated-by:` / `eliminated-by:`
- [ ] Seed `docs/dev/principles.kb/` from the named principles
    - [ ] `content-thinking-not-container-thinking.md`
    - [ ] `title-scope-not-content-scope.md`
    - [ ] `smallest-relevant-scope-wins.md`
    - [ ] `empty-parent-dirs-are-valid.md`
    - [ ] `package-symmetry.md`
    - [ ] `split-equals-content-extraction.md`
    - [ ] `audit-is-a-deliverable.md`
- [ ] Extract `docs/dev/procedures.kb/scope-refactor.md` from the embedded
    method in the case-study (currently lives only as inline prose)
- [ ] Update case-study frontmatter to canonical aliases; add
    `status: reconciled`
- [ ] Cross-link failure-modes to procedures (mitigated-by) and to principles
- [ ] After distillation: run
    `SKILL.kb/must-read/after/distilling-from-a-raw-source.md` audits

## Open Questions

- Does `bloat.md`'s "Frame" stance (Audience-identification principle) belong
  in this `principles.kb/` seed, or wait for a second instance?
- Naming: stick with `post-mortem.md` (capture) + `reconcile-case-study.md`
  (distill), or rename to `capture-incident.md` / `distill-learnings.md`?

## Success Criteria

- [ ] `docs/dev/failure-modes.kb/` and `docs/dev/principles.kb/` exist and
  hold canonical entries for every alias / principle the case-study names
- [ ] `docs/dev/procedures.kb/scope-refactor.md` exists as a standalone
  procedure (the case-study no longer embeds the method)
- [ ] Seed case-study has `status: reconciled` and aligned aliases
- [ ] `bin/llm.kb-validate docs/dev/` clean
- [ ] No orphan references (`SKILL.kb/self-audit.kb/cross-references.md`
  passes)

## Notes

This is the originating work the May 13 devlog flagged as "Next Session." The
two sessions since have built infrastructure (SKILL.kb audit corpus,
skeleton-default schema centralization). This is the consequential next step.

Filename examples in `docs/dev/{CLAUDE.md, concepts.kb/procedure.md,
procedures.kb/CLAUDE.md}` already reference `scope-refactor.md` as a
"task-shaped filename" example — those examples become real once this todo
lands.

Run from a fresh context (per the post-mortem / reconcile-case-study split).
