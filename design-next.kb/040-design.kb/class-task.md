---
why:
  - ../030-requirements.kb/filesystem-as-database.md
  - ../030-requirements.kb/dated-records-are-primitive.md
  - kb-spec.md
---

# Class: Task

Work items and their lifecycle. A task is a linked node
(`kb-spec.md`), and its weight is a per-task consequence of
elaboration need, never a store choice. The gradual-elaboration plan
grows each task only as the work demands — starting from no durable
write at all (a task may live and die in conversation):

1. **Line** — a line in its contract's synthesis (`- [ ]` in the
   working set; a plain bullet in the option pool). Cheapest durable
   capture: one line takes note of a tangent without taking the
   tangent.
2. **File** — a collection entry, when the task outgrows its line
   (multi-step, own frontmatter, outlives a session). The line
   becomes the entry's pointer, in place.
3. **Task kb** — a sibling `$slug.kb/` elaborating the entry, whose
   synthesis file is the task itself.

The plan is self-similar: the working-set/collection relation
(`todo.md` : `todo.kb/`) is the spec's synthesis/elaboration relation
(`$slug.md` : `$slug.kb/`), and entries inside a task kb are afforded
the same steps. Work grows a task *tree* on demand, complexity
minimized to what the work requires.

## Two contracts

- **Obligation** — committed work: the `todo.md`/`todo.kb/` pair.
  Sweeps must surface it (silent loss is the v1 invisible-work
  failure); disposition is explicit — done or won't-do.
- **Option** — recorded, uncommitted: the `ideas.md`/`ideas.kb/`
  pair. Sweeps must never nag it; forgetting is a valid end state.
  An option activates when it would ease or obviate committed work,
  or when its cost would be more-than-amortized across several tasks
  it facilitates — value coupling to the obligation set, not a
  schedule.

Each contract is a full synthesis pair — the spec's one-to-one
`$name.md` : `$name.kb/` relation — and no section break exists:
v1's `## Later` retires into `ideas.md`, its one real job having
been to hold the option pool. Contract-awareness in tooling is the
line form at line grain (`- [ ]` means obligation wherever it
appears — see Schema-level rules) and filename dispatch at
collection grain. Crossing the contract boundary is orthogonal to
elaboration weight — a line moves between synthesis files, gaining
or losing its checkbox; a file moves between collections.

## Horizon and priority

Horizon is the obligations' total order, nothing else: "far out" is
"near the bottom" — no horizon field, no named buckets. The ordering
is the content; that is why a working set is not "merely a listing"
(`ls` is the index; the order is not). Deferral gated on a condition
(a date, "after X ships") is trigger-shaped, not far-horizon: a
deferred task names its wake condition in frontmatter, per
`../../llm-triggers/design.kb/040-design.kb/task-deferral.md`.

The option pool has no standing order — options are consulted, not
scheduled. Contract symmetry is at the pair level (same relation,
same elaboration steps); the syntheses specialize differently.
`todo.md` is the working set: a `- [ ]` checklist, complete over
open entries (an absent line is invisible work), its order the
content as above. `ideas.md` is the pool's roll-up: prose or plain
bullets — one-line pitches, pointers into `ideas.kb/` where they
earn their place — with no checkboxes (nothing for one to mean),
no order semantics, and no completeness mandate: a synthesis is
never its collection's index (`kb-spec.md`), `ls ideas.kb/` is that
index, and forgetting is a valid end state. The options' priority
signal is ratings-driven batch reevaluation (commit / retire /
keep), the read-side that
`../070-future-work.kb/task-priority-frontmatter.md` serves; v1's
wsjf metrics originated in the ideas.kb schema for exactly this.
That entry also holds the deferred frontmatter successor to hand
ordering; `../070-future-work.kb/task-synthesis-drift-check.md`
holds the deferred line↔entry consistency check.

**Why not a horizon field, or more buckets:** frontmatter cannot
reach line grain, and every named bucket (`## Someday`, `## Blocked`)
erodes the total order that makes the working set contentful —
blockage is per-task state, and conditional deferral is
trigger-shaped. Even the contract boundary is structural
(`ideas.md`), not positional.

**Why not a likelihood scale:** sweeps need a binary — nag or
don't — which the contract split already answers. Finer grades
are ratings, consulted at reevaluation time; a standing likelihood
number on every task would be false precision with no reader.

## Scope

A **project** is any directory that owns a task-class instance —
project boundaries follow the work's ownership, not git's: one git
repository may contain several projects, and a project need not be a
repository root.

- Per-project instances are canonical for project-owned work: a task
  belongs to the project whose work it tracks, wherever it was
  noticed. A parent project points at a sub-project's items with
  breadcrumb lines; details are never duplicated upward.
- The global scope (v1 `sessions.kb/`) is the same class instanced
  at operator level: each entry is a task node for a line of work
  spanning or outliving any one project, with dated-record naming
  like any collection entry and dated addenda in its elaboration kb.
  Its per-instance conventions are defined, not deviant: per-machine
  subdirectories (a session tracks in-progress working state —
  worktrees, branches, uncommitted files — which exists per-machine)
  and `cwd:` frontmatter as the project edge. Entries point, never
  copy, down into project stores; disposition is the obligation
  contract — deleted when absorbed.
- A working set is per-instance optional: present where an ordering
  has a consumer. The global scope has none today — `ls` and the
  sweep tooling serve it.
- Cross-scope enumeration is convention plus shell: stable
  frontmatter, naming, and layout are the core's whole commitment.
  External consumers (the open-tasks sweep, task-archeology's
  `wsjf-rank`) prove the conventions suffice; `kb query` stays
  behind `../070-future-work.kb/structured-query.md`'s trigger.

## Schema-level rules

V1's proven ones, plus the elaboration plan's own:

- `- [ ]` is the only task-shaped line, and it means obligation
  wherever it appears; enumeration sweeps key off it exactly. Two
  doctor checks fall out: a bare-`-` task bullet in a working set is
  the v1 "invisible work" failure, and a checkbox in an option
  synthesis is a miscategorized obligation — both mechanically
  detectable.
- Existence-is-signal: a file in a task collection counts regardless
  of its bullets.
- Enumeration is the union of bracketed lines in synthesis files
  and files in task collections; a pointer line is its entry's
  synthesis-file presence, not a second task. Contract dispatch is
  the bracket at line grain and the filename at collection grain:
  everything nag-worthy is exactly enumerable, and only obligations
  nag. Line-grain options are the one loose spot (plain bullets) —
  their read-back is the wholesale reevaluation pass, not a sweep.
- The engine defaults to the lightest sufficient step — v1 evidence
  says agents default heavyweight.
