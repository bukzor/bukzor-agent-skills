# Decisions (2026-07-09): task-graph relations -- `blocked-by` field, hierarchy as sub-kb

First real extender of the strict-root/`#base` convention (chatfs
`.claude/todo.kb/`), which forced the per-field placement calls the
2026-07-07 conformance sweep had parked ("rename / drop / extend"). Modeled
task-graph relations by splitting them across three mechanisms rather than
adding one frontmatter field per name a consumer happened to invent:

- **Hard dependency -> canonical `blocked-by`** (array), added to the
  llm-subtask base `$defs.base`. Generic task vocabulary for a skill named
  *subtask*; pairs with the existing `status: blocked` (that marks a task
  blocked, this names what blocks it). Rejected `requires` -- overloaded by
  the read-first `requires:` directive and `required-reading` -- and
  `depends-on` as ambiguous on hard-vs-soft. Prior art is uniform: Jira "is
  blocked by", Linear "blocked by", GitHub "blocked by". chatfs renamed its
  `depends`/`depends-on` usages to it.
- **Parent / subtask-of -> sub-kb nesting**, no field. Hierarchy is a
  separate axis from dependency links (Jira and Linear both treat
  sub-issues as distinct from relations), and the llm-kb
  document+sub-collection pattern already expresses containment
  structurally: parent `<stem>.md` + `<stem>.kb/` children + a one-line
  `<stem>.jsonschema.yaml` stub. chatfs moved its one `parent:`-bearing file
  under the parent's `.kb/` and dropped the field. `ls` is the discovery
  surface, so no back-pointer is needed.
- **Soft link -> existing `related-effort`** (= prior art's "relates to").
  No new field. If plural informative links arise, generalize
  `related-effort` to a `related`/`see-also` list; deferred until a real
  case appears.
- **`supersedes-question-from` -> consumer-local `#base` extender** (chatfs
  only). Not general enough to bless in the base; the extension pattern
  exists precisely for this. Audit for promotion if it recurs elsewhere.

`blocked-by` went to `todo.jsonschema.yaml` only, not `ideas` -- no idea
data needs it and ideas is already the lighter schema (no `closeout`). The
todo/ideas near-duplication (should `ideas` just `$ref` `todo`?) stays an
open smell. Verified: `llm.kb-validate` green on chatfs `.claude` (33
files); the additive base change regressed no other consumer.
