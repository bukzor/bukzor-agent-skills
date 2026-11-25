# Sub-agent handoffs for quality passes on claim ledgers

Each file here is one sub-agent's unit of work toward the parent plan,
`../2026-11-25-000-Quality-passes-for-claim-ledgers.md`. It carries both
directions of the handoff: the coordinator's brief, then the agent's own record
and report. Belongs here: work one agent can finish in one sitting (≤60 min),
scoped to named files. Does not belong: design (the fleet ledger,
`docs/dev/claims.kb/design.claims.kb/authorship.kb/`), or work spanning waves
(split it).

A handoff file holds only what has no other home: what the unit was asked,
how far it got, what it chose and still doubts. Design, interfaces and
findings live in their own homes, and a handoff file links to them, never
copies them.

## Protocol

1. The coordinator writes the file before launch, named
   `YYYY-MM-DD-NNN-slug.md`: frontmatter `required-reading:` (this file, the
   doc sections that govern the unit, the interfaces it consumes by path)
   and `blocked-by:`; a **Problem Statement** (goal, scope as a file list,
   decisions already made for it). The launch prompt is only "do the task in
   PATH".
2. The agent works from the file and keeps it current: **Steps** as
   checkboxes, marked `[~]` on starting one and `[x]` on finishing it, so an
   interrupted unit can resume where it stopped; **Decisions** with reasons;
   **Open Questions**. At the end, a **Final report**: check results,
   deviations from the brief, and where each result lives (the paths that
   define an interface, the doc a finding went into). `status:` stays
   `open` while it works; at the end it sets `status: done`, commits its
   unit, and replies with the path only.
3. While open, a later instruction is an in-place edit of the brief, and the
   message is just "reread PATH". Once done, the file is a frozen record:
   nobody updates it, and a correction is a new unit.

## Every agent, every task

- Read first: `~/.claude/CLAUDE.md`, the repo's `CLAUDE.md`, the `CLAUDE.md` of
  each skill you touch, then the brief's `required-reading:`. Skills you edit
  are live: `~/.claude/skills/*` symlink into this repo.
- Stay inside the brief's file list. Sibling agents, and the user's other
  sessions, run concurrently on other files; never edit theirs or the parent
  plan. Files already dirty or untracked when you start are someone else's:
  leave them, and list any that needed your change in Open Questions.
- Write each finding into its home, the doc your scope names. When there is
  none, the Final report is its home; name the gap in Open Questions.
- Frozen records stay as written: devlogs, ADRs, other migrations' entries,
  case studies, done handoff files, checked-off todo items. They record what
  was true when written; a path that has since moved is not a defect in them.
- Standing text you add -- a rule a future session must obey -- enters marked
  `> [!DRAFT] agent-authored YYYY-MM-DD, vetoable` (`~/.claude/CLAUDE.md`,
  Values).
- Stage your scope's paths as you finish each step (`git add PATHS`). Before
  handing back, commit them and your handoff file with
  `git commit-files PATHS -- -m MSG` (`~/.claude/reference.kb/git/commit.md`;
  pass both sides of a rename). Siblings share the index: never commit bare,
  and never stage, unstage or commit a path outside your scope. On an
  `index.lock` collision, retry. Don't push; the coordinator does.
- Finish with `llm.kb-validate` and `llm-kb/bin/llm.kb-validate-links` (not
  on PATH) on the trees you touched, no new errors.
- Run builds and checks in the foreground. Never end your turn waiting on a
  background job or monitor: if a sibling must land first, say so in your
  report and stop; the coordinator resumes you.
- Scratch goes in the repo-root `trash/`.
- The brief (frontmatter inputs, Problem Statement) is the coordinator's;
  edit only your own sections, in place, ≤60 lines.
