---
managed-by: Skill(llm-subtask)
required-reading:
  - ~/.claude/skills/llm-collab/SKILL.md
  - ~/.claude/skills/llm-collab/skeleton/
suggested-reading:
  - ~/.claude/skills/llm.kb/SKILL.md
related-effort: ~/repo/github.com/bukzor/prototype.chatfs/.claude/todo.kb/2026-01-02-000-harmonize-with-llm-skills.md
cost-benefit-sweh:
  timebox:
    "@value": 3.0
    rationale: |
      Move docs/, create design.kb/ skeleton, update init script,
      update references.kb/ docs. Pending user sign-off on
      tentative steps. Self-classified High priority, Medium
      complexity. ~3h.
    confidence: tentative
  benefit-2w:
    "@value": 0.5
    rationale: |
      Defines the `milestones.kb/` pattern in skeleton — unblocks
      prototype.chatfs `docs/dev/milestones.kb/` creation. ~$50
      of unblock-chain value.
    confidence: tentative
  cost-of-delay-2w:
    "@value": 0.2
    rationale: |
      Self-classified "blocks prototype.chatfs milestones.kb
      creation." Each 2w of delay keeps that downstream item
      blocked too. Cross-repo gating.
    confidence: tentative
---

# Update skeleton to match docs/dev/ pattern from git-partial

**Priority:** High
**Complexity:** Medium
**Context:** Modern pattern established in ~/repo/github.com/bukzor/git-partial.prototyping

## Problem Statement

The llm-collab skeleton has inconsistent documentation structure:
- Some developer docs at docs/ level (adr/, devlog/, architecture/)
- Some in docs/dev/ (old monolithic files: design-rationale.md, technical-design.md, development-plan.md)
- Doesn't match modern pattern where docs/dev/ contains ALL developer-facing docs

Modern pattern reserves docs/ for user-facing documentation.

## Current Situation

**Skeleton structure (old):**
```
docs/
  adr/
    README.md  (removed devlog/README.md already)
    CLAUDE.md ✓
    YYYY-MM-DD-000-example-decision.md
  architecture/
    overview.md
  dev/
    design-rationale.md
    technical-design.md
    development-plan.md
    devlog/  (empty)
  devlog/
    CLAUDE.md ✓
    YYYY-MM-DD-000-example-entry.md
  examples/
  milestones/
```

**Modern pattern (from git-partial):**
```
docs/
  examples/  (user-facing)
  dev/
    adr/
      CLAUDE.md
      YYYY-MM-DD-000-example-decision.md
    devlog/
      CLAUDE.md
      YYYY-MM-DD-000-example-entry.md
    design.kb/
      CLAUDE.md (to be created)
    milestones.kb/
      CLAUDE.md (pattern exists, not in skeleton)
```

## Proposed Solution

1. Move developer docs under docs/dev/
2. Remove old monolithic files (replaced by design.kb/ pattern)
3. Remove docs/architecture/ (replaced by design.kb/)
4. Update llm-collab-init script
5. Update references.kb/ documentation

## Implementation Steps

- [ ] Move skeleton templates to docs/dev/
  - [ ] mv docs/adr docs/dev/ (if not already done)
  - [ ] mv docs/devlog docs/dev/ (if not already done)
  - [ ] rm docs/dev/design-rationale.md
  - [ ] rm docs/dev/technical-design.md
  - [ ] rm docs/dev/development-plan.md
  - [ ] rm -r docs/architecture
  - [ ] rm -r docs/milestones
- [ ] Create design.kb/ skeleton template
  - [ ] Create skeleton/docs/dev/design.kb/CLAUDE.md explaining pattern
  - [ ] Don't create subdirectories - let projects create what they need
- [ ] Update llm-collab-init script
  - [ ] Change mkdir to create docs/dev/{adr,devlog,design.kb}
  - [ ] Update file copy paths to docs/dev/
  - [ ] Remove docs/architecture/overview.md creation
- [ ] Update references.kb/ documentation
  - [ ] Update file-types.kb/ to document design.kb/ pattern
  - [ ] Remove/update design-rationale.md, technical-design.md, development-plan.md references
  - [ ] Update new-project-setup-checklist.md
- [ ] Update skeleton/ROADMAP.md template to point to docs/dev/milestones.kb/

## Open Questions

- Should design.kb/ CLAUDE.md provide example category names, or be completely generic?
- Keep architecture.md file type reference for legacy projects, or remove entirely?

## Success Criteria

- [ ] All developer-facing docs are under docs/dev/
- [ ] docs/ reserved for user-facing docs (examples/, future guides/)
- [ ] llm-collab-init creates correct structure
- [ ] references.kb/ accurately documents modern pattern
- [ ] No references to removed files (architecture/, old dev/ monoliths)

## Notes

**⚠️ IMPORTANT:** Implementation steps above are tentative and unreviewed by user.
Must confirm with user before executing any changes to the skeleton structure.

Related work:
- Already updated devlog/README.md → devlog/CLAUDE.md with workaround frontmatter
- Already removed static "Recent Entries" sections (ls as source of truth)
- git-partial repo now uses this pattern successfully

## Progress (2026-07-06)

The bulk of "Implementation Steps" was already done by an earlier,
unlogged pass — verified against the actual skeleton on disk, not just
this file's checklist (which had drifted stale and understated
reality):

- `docs/dev/{adr,devlog,design,technical-policy.kb}/` all exist;
  `docs/architecture/`, `docs/milestones/`, and the old monolithic
  `design-rationale.md`/`technical-design.md`/`development-plan.md`
  files are already gone.
- `llm-collab-init` already creates the `docs/dev/` structure and
  self-migrates `docs/adr` → `docs/dev/adr`, `docs/devlog` →
  `docs/dev/devlog` for existing projects.
- Design docs landed as `docs/dev/design/` (plain, not `design.kb/`
  as this file proposed) plus a separate `docs/dev/technical-policy.kb/`
  — a finer split than originally planned, superseding the "Create
  design.kb/ skeleton template" step.

What was genuinely still broken — three places never updated when the
`docs/dev/` move happened, found by tracing what `llm-collab-init`
actually creates against what other files assume:
- `bin/llm-collab-session-start` read from the pre-migration
  `docs/adr`/`docs/devlog` paths, so on any already-migrated project
  (i.e. every project `llm-collab-init` produces today) it silently
  showed no devlog/ADR context at all. Its own "Quick commands" output
  also named nonexistent scripts (`new-adr.sh` etc.) instead of the
  real `llm-collab-adr`/`llm-collab-devlog`/`llm-subtask-todo`. Fixed;
  verified end-to-end with a fresh `llm-collab-init` + `llm-collab-session-start`
  run — latest devlog now correctly surfaces.
- `references.kb/file-types.kb/ADRs.md` and `devlog.md` still declared
  `docs/adr/`/`docs/devlog/` in frontmatter and a since-removed
  `scripts/new-adr.sh`; `devlog.md`'s template links pointed at the
  pre-migration skeleton path. Fixed.
- `skeleton/docs/dev/devlog/README.md` was stale leftover cruft (static
  "Recent Entries: None yet") contradicting the CLAUDE.md-is-canonical,
  ls-is-source-of-truth convention this file's own Notes section says
  was already adopted — no sibling dir (`adr/`, `design/`,
  `technical-policy.kb/`) has one, and `TESTING.md`'s skeleton
  integrity check never expected it. Deleted.

## Progress (2026-07-06, continued) — `docs/milestones/` reference resolved

Corrected the earlier note above: the milestones location was **not**
actually an open pattern question — the ADR
(`docs/dev/adr/2025-12-11-001-separate-user-facing-and-developer-facing-documentation.md`)
and the `llm-kb` migration entry
(`llm-kb/migrations.kb/2025-12-11-000-docs-dev-separation-with-auto-migration.md`)
already both name the target consistently: `docs/dev/milestones.kb/`,
parallel to `design.kb/`. The only thing stale was
`references.kb/file-types.kb/ROADMAP.md`, which still pointed at the
pre-decision `docs/milestones/`. Fixed (path + heading updated to
`docs/dev/milestones.kb/`, with a citation to the ADR).

**Still genuinely open** — unlike `design/` and `technical-policy.kb/`,
no milestones.kb skeleton exists yet. The *destination path* is settled
and documented everywhere consistently; what remains is implementation:

- [ ] Build `skeleton/docs/dev/milestones.kb/` template (`CLAUDE.md`)
      + `llm-collab-init` wiring (create on init, migrate existing)
- [ ] `complete-example/`-style example-update step (this todo defined
      none; see the parallel llm-kb rename todo,
      `llm-kb/.claude/todo.kb/2026-01-02-000-complete-d-to-kb-rename.md`)

## Scoping pass (2026-07-19)

Checked whether `llm-design-kb` (new skill, didn't exist when this
todo was filed) already covers the `milestones.kb/` pattern this item
wants, per the 2026-07-18 session log's speculation. It does not:
`llm-design-kb` is scoped to `design.kb/` only (goals/requirements/
design/decisions), no `milestones.kb/` concept anywhere in it. Not
superseded — this item is still needed as originally scoped. The
"⚠️ user sign-off" gate on Implementation Steps still stands; not
executing the restructuring itself this pass.
