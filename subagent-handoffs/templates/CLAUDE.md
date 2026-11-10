# Sub-agent handoffs for {{the parent plan's goal}}

Each file here is one sub-agent's unit of work toward the parent plan,
`../{{plan}}.md`. It carries both directions of the handoff: the coordinator's
brief, then the agent's own record and report. Belongs here: work one agent
can finish in one sitting (≤60 min), scoped to named files. Does not belong:
design (`{{the project's design docs}}`), or work spanning waves (split it).

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
   {{path}}".
2. The agent works from the file and keeps it current: **Steps** as
   checkboxes, marked `[~]` on starting one and `[x]` on finishing it, so an
   interrupted unit can resume where it stopped; **Decisions** with reasons;
   **Open Questions**. At the end, a **Final report**: check results,
   deviations from the brief, and where each result lives (the paths that
   define an interface, the doc a finding went into). `status:` stays
   `open` while it works; at the end it sets `status: done`, commits its
   unit, and replies with the path only.
3. While open, a later instruction is an in-place edit of the brief, and the
   message is just "reread {{path}}". Once done, the file is a frozen record:
   nobody updates it, and a correction is a new unit.

## Every agent, every task

- Read first: {{global and repo instructions, style/test conventions}}, then
  the brief's `required-reading:`.
- Stay inside the brief's file list. Sibling agents run concurrently on
  other files; never edit theirs or the parent plan.
- Write each finding into its home, the doc your scope names. When there is
  none, the Final report is its home; name the gap in Open Questions.
- An interface you produce is documented where it is defined (docstrings,
  types, schema), not restated in your report.
- Stage your scope's paths as you finish each step (`git add {{paths}}`).
  Before handing back, commit them and your handoff file with a
  path-scoped commit (`{{git commit-files PATHS -- -m MSG}}`), per
  {{the project's commit conventions}}. Siblings share the index: never
  commit bare, and never stage, unstage or commit a path outside your
  scope. On an `index.lock` collision, retry.
- {{Project rules: language/runtime limits, test layout, size limits.}}
- Finish with {{the project's checks}} on the files you touched, clean.
- {{Environment workarounds, added as agents discover them.}}
- Run builds and checks in the foreground. Never end your turn waiting on a
  background job or monitor: if a sibling must land first, say so in your
  report and stop; the coordinator resumes you.
- Scratch goes in {{the repo's scratch dir}}.
- The brief (frontmatter inputs, Problem Statement) is the coordinator's;
  edit only your own sections, in place, ≤60 lines.
