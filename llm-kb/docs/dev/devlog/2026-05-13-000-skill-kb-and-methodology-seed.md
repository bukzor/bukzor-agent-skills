# 2026-05-13: SKILL.kb/ audit infrastructure + methodology kb seed

## Focus

Convert SKILL.md rules into triggered actions. Apply llm-kb to itself
in `docs/dev/`.

## What Happened

Seeded `docs/dev/` methodology kb from a same-day case-study
(har-browse rust-port scope-refactor). Distilled post-mortem procedure,
concept definitions (case-study, failure-mode, procedure, principle),
plus case-study schema.

Built `SKILL.kb/` runtime infrastructure visible to every consumer via
`ls -RF SKILL.kb/must-read/`:
- `must-read/{before,after,when}/` triggers
- `self-audit.kb/` -- 13 proactive quality checks
- `procedures.kb/` -- run-self-audits aggregator, promote-to-collection,
  enumerate-and-categorize, stub-missing-entry

Meta-review of `post-mortem.md` produced seven critiques. Four
generalized into `SKILL.kb/` as triggered actions (step-0 → concrete
bookends; cascade bound; closing reconciliation; capture-first
trigger). Three were post-mortem-specific (goals-at-top, capture-first
ordering, inline shapes) and landed when `post-mortem.md` was rewritten
to capture-only.

## Decisions

- **Triggers point to one aggregator.** Both
  `after/creating-or-editing-kb-files.md` and
  `before/marking-kb-work-done.md` route to `run-self-audits.md`,
  which assigns urgency tiers (blocking / required-when-applicable /
  situational) and per-audit applicability conditions.

- **`self-audit.kb/` over `quality-checks.kb/`.** "Self-" puts
  ownership on the agent; "audit" is stronger than "check"; filename
  composes as imperative ("audit X").

- **No symlinks for trigger files.** Relative paths in linked
  procedures would resolve from the symlink's apparent location, not
  the target's. Tiny duplication preferred over silent path breakage.

- **Bloat audit pinned to Claude-audience stance.** Don't talk down or
  explain what Claude already knows. Audience-mismatched content
  *relocates* (to a maintainer file, creating one if absent) rather
  than gets cut.

- **200k tokens is the capture-first trigger.** Hitting 200k usually
  means crossing 300k before wrap. The trigger does a
  case-study-worthy preflight before routing to capture.

- **Post-mortem split.** `post-mortem.md` is capture-only (run while
  context is decaying). `reconcile-case-study.md` is the editorial
  pass (run by a separate fresh-context agent). Case-study `status:`
  frontmatter tracks lifecycle: absent = `raw`,  `reconciled` when
  distillation complete. Named partial-states added as patterns
  recur.

## Next Session

- Run `reconcile-case-study.md` on the seed case-study; populate
  `failure-modes.kb/` and `principles.kb/`; extract
  `procedures.kb/scope-refactor.md` from the embedded method.
- Resolve validator quirk: `SKILL.kb/SKILL.jsonschema.yaml` exists
  but isn't auto-matched to `SKILL.kb/self-audit.md` (1 warning).
- Route `after/distilling-from-a-raw-source.md` through
  `run-self-audits.md` for its generic audit portion.
