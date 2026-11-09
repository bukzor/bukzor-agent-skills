---
managed-by: Skill(llm-subtask)
status: done
required-reading:
  - llm-subtask/SKILL.md
  - llm-subtask/jsonschema/todo.jsonschema.yaml
  - llm-subtask/bin/llm-subtask-todo
  - llm-subtask/bin/llm-subtask-idea
---

# `llm-subtask` creators birth files as `status: template`, untitled

**Origin:** coordinator session in `~/claude/deadlock` (2026-11-09). Never stage or commit (`llm-kb/uv.lock`
is unrelated dirt); scratch in this repo's `trash/`.

## Problem Statement

`llm-subtask-todo` / `llm-subtask-idea` / `llm-subtask-init`: (1) new files keep `status: template`
(hidden from `claude-open-tasks-list`); (2) `--title` never lands (scripts
replace `Example * Title`, skeleton says `# Task Title` / `# Idea Title`);
(3) suspect: each run clobbers the project's `*.kb/CLAUDE.md`. Fix minimally;
test if a convention exists. Schema review: should `status` gain in-progress
(2 of ~65 files use `active`)? Coordinator: decline. Count stuck `template`s.

## Steps

- [x] Reproduce at HEAD in `trash/x`: all three bugs confirmed.
- [x] Find working-tree edits (mtime 16:31:16, before this brief) fixing 1+2.
- [x] Verify bug 3 is damage, not an upgrade path; fix it in both scripts.
- [x] Regression check vs fixed and HEAD scripts; shellcheck.
- [x] Status census, stuck-`template` list, `active` provenance.

## Decisions

- Keep the found edits for 1+2 (verified correct). `not-started` for todos
  (schema: "no work artifacts exist yet"); `open` for ideas, since an idea
  is never "started", and `open` is the schema's idea-and-task default.
- Bug 3: `[ -e F ] || cp ...` (seed only if missing). Of 7 project
  `*.kb/CLAUDE.md` that differ from skeleton, 4 carry a deliberate local
  `requires: Skill(llm-subtask)` frontmatter a run would wipe; the overwrite
  only buys refreshing a stale one-line usage hint. Refresh belongs to an
  explicit command, not to every task creation.
- No committed test: the repo has no convention for skill `bin/` scripts
  (only Python `*_test.py` in `llm-claims-kb`/`llm-kb` libs). The ad-hoc
  check stays at `trash/verify-creators.sh`.

## Final report

**Files:** `llm-subtask/bin/llm-subtask-{todo,idea}` (+3/-2 lines each vs HEAD).
**Before:** `status: template`, heading `# Task Title`/`# Idea Title`, local
`CLAUDE.md` overwritten. **After:** `status: not-started`/`open`, heading
`# <title>` (safe with `&`, `/`, `\`; bash 5.3), `CLAUDE.md` seeded only if absent.
**Tests:** `trash/verify-creators.sh` gives 10/10 ok on the fix and 8/10 FAIL
on HEAD (the 2 passes are seed-when-missing, which HEAD also does).
Shellcheck (uvx shellcheck-py) clean.

**Schema verdict: decline; no change.** Evidence: 68 top-level task files
(107 with nested `.kb/`) under `~/repo ~/claude ~/.claude`, trash pruned. Real
`status: active` uses are 3, not 2: deadlock `todo.kb/2026-11-05-000-*`,
deadlock `.claude/todo.md`, windows-forensics `.claude/todo.md`. All 3 sit
exactly where an agent had to overwrite a creator- or init-born `template`
(`template` was never committed; the 11-05 file's frontmatter is the bare
skeleton pair). So the "demand" is bug-1 fallout: the agent was forced to
pick a word and reached past the vocabulary. With valid statuses at birth
that moment disappears, and the staleness argument still holds. An unknown
value already degrades safely (shown as open, plus a warning). No other
extension has ROI.

**Stuck at `template` (non-skeleton, outside trash): 0.** Bug 1's damage
was absorbed by hand-edits (3 of them to the off-vocabulary `active`), not
left as hidden tasks.

### `llm-subtask-init`

**File:** `llm-subtask/bin/llm-subtask-init` (+5/-5 vs HEAD), same pattern as
the creators. The fresh `todo.md` gets its skeleton content with
`status: template` swapped for `status: open`, and both `*.kb/CLAUDE.md` are
`[ -e F ] || cp ...`. An existing `todo.md` was already left alone.

**Status `open`, justified:** `todo.md` is a long-lived list container, not
a single task, so `not-started` ("no work artifacts exist yet") goes false
the moment the first item lands, and nothing would ever flip it. `open` is
the schema's plain "eligible" value and equals absence, which matches the
field: across 19 real `.claude/todo.md` (trash pruned), 16 have no status,
2 say `open`, and 1 says `active` (windows-forensics). Deadlock's
`todo.md` changed from `active` to `open` during this session, not by me.

**Before (HEAD):** a fresh `todo.md` was born `status: template`, which
`claude-open-tasks-list` SKIPs, so every task added to it stayed hidden.
Each run also overwrote both `*.kb/CLAUDE.md`. **After:** `status: open`,
the rest identical to the skeleton, and local `CLAUDE.md` edits survive.

**Tests:** `trash/verify-creators.sh`, extended with 7 init checks (fresh dir
plus a dir with local edits and an existing `todo.md`): 17/17 ok. With HEAD's
init, 3 of the 7 init checks FAIL (status, both CLAUDE.md). The other 4 pass
on HEAD as expected: body identity, fresh seeding, and the existing
`todo.md` untouched. Shellcheck clean.

**New consequence, out of scope:** now that a fresh `todo.md` is visible,
its skeleton placeholders (`- [ ] First task`, `- [ ] subtask 3`) appear
in the enumerator as 2 open tasks until someone edits them. That is loud and
self-correcting, which the enumerator's own policy prefers ("a task wrongly
shown beats one wrongly hidden"). The real fix is a skeleton `todo.md`
with no placeholder tasks.
