---
status: complete
kind: one-shot
scope: |
  Any `*.jsonschema.yaml` that is a **symlink** rather than a file. It
  becomes a real file holding the `$ref` its link target implies:
  `skill://<skill>/<path>` when the link crossed into
  `~/.claude/skills/`, the link's own relative path when it stayed inside
  its tree.

  Not in scope: symlinked markdown (`must-read.kb/` has two). Prose has no
  `$ref`; a symlink is the only dedup those have, and it is the right one.

  Not in scope: the `~/.claude/skills/*` symlinks themselves. Those are
  the skill *installation* mechanism -- 29 directory links that make
  `skill://` resolvable in the first place. They are not a dedup hack and
  have no `$ref` form.
depends-on:
  - 2026-07-07-000-schema-copies-to-ref-stubs.md
related-todo: ~/.claude/skills/llm-kb/.claude/todo.kb/2026-08-21-000-ref-rollout-beyond-todo-ideas.md
why: |
  A symlink is a third form of the same pre-`$ref` dedup, and the census
  behind 2026-08-21-000 missed all 30 of them: it swept for *copies*, and
  a symlink is not a copy. Only a `-type l` sweep finds them.

  Symlinks look strictly better than copies -- they cannot drift -- so the
  instinct is to leave them. Three reasons not to:

  1. **They cannot extend.** A symlink is all-or-nothing: the consumer
     gets the canonical exactly, or forks it into a full copy. A `$ref`
     stub is one line away from becoming an extender that `$ref`s `#base`
     and adds a field. Every symlink here is a fork waiting to happen.
  2. **They break silently on rename.** Five of the thirty pointed at
     `llm-discourse-graph/schemas/`, renamed to `jsonschema/` at some
     point. Nothing reported it. A dangling `skill://` ref is a loud
     retrieval error; a dangling symlink is a file that is merely absent.
  3. **They do not survive copying.** Archive, `cp -r` without `-d`, or a
     tarball turns a symlink back into the copy it was avoiding -- the
     pattern reinstalls itself, exactly as with `skeleton/`.
---

# Schema symlinks to $ref stubs

## Transformation

For each `find <roots> -type l -name '*.jsonschema.yaml'`:

1. Read the link target.
2. If it points inside `~/.claude/skills/<skill>/`, the replacement ref is
   `skill://<skill>/<rest>`. Otherwise it is the link target verbatim --
   a file-relative `$ref` resolves against the stub's own `file://` base,
   so the relative path that was correct as a link is correct as a ref.
3. Assert the target exists; skip and report if not.
4. `unlink`, then write the two-line house stub.
5. `llm.kb-validate` the affected trees.

Idempotent: a real file is not `-type l`, so a second run finds nothing.

Deliberately *not* rewritten to `skill://`: the two in-tree relative
links (`prototype.chatfs`, and the `--replication-run` clone). A
replication clone that reached out to the real skills tree would stop
being a replication of anything.

## Applied

2026-08-21: all 30, across 7 repos. Zero skipped.

| site | n | ref form |
| --- | --- | --- |
| `bukzor.samsung-debloat` `forensic-{sources,analyses}.kb/` | 13 | relative |
| `summer-programming-project` `2026/.plan/` | 5 | `skill://llm-discourse-graph/` |
| `scratch.vim-work` `docs/sources/2026-03-02-*.kb/` | 5 | `skill://llm-discourse-graph/` |
| `meta-reasoning` `plans.kb/` | 3 | relative |
| `~/.claude/claude-alignment-2026-04-29.kb/` | 2 | relative |
| `prototype.chatfs` `packages/chatfs-cli/design.kb/` | 1 | relative |
| `bukzor-agent-skills--replication-run` | 1 | relative |

## Verification

Behavior-neutral where the link was live, repairing where it was not.
Measured, not assumed -- the symlinks were restored and re-validated to
establish each baseline before the stubs went back:

- `bukzor.samsung-debloat`: 244 files, 0 errors.
- `~/.claude/claude-alignment-2026-04-29.kb`: 36 files, 0 errors.
- `meta-reasoning/plans.kb`: 15 files, 0 errors.
- `summer-programming-project/2026/.plan`: **41 errors before, 41 after**
  -- identical. That drift is pre-existing and belongs to the DIVERGED
  backlog under 2026-08-21-000, not to this entry.
- `scratch.vim-work`: **44 errors before, 15 after.** All 44 files were
  failing because the schema did not resolve at all; 29 of them conform
  and had simply never been checked. The remaining 15 were a *second*
  instance of the same defect one level down -- see Follow-up; since
  fixed to 0.
- `prototype.chatfs/packages/chatfs-cli/design.kb`: 2 errors, both the
  `canonical-conversation-graph` `why:` slugs left deliberately
  unresolved by 2026-08-21-002. Not caused here.

## Follow-up

**The 15 newly-exposed `scratch.vim-work` errors are resolved**
(`scratch.vim-work` b4658bf): 44 files, 0 errors. Judged, and the verdict
was not the expected one -- none of them were content drift.

All 15 shared one cause, and it was `No schema found`, not a schema
violation. `llm.kb-validate` resolves a schema *strictly* as a sibling of
the `.kb/` it governs (`schema_for()` in `frontmatter_validate.py`: walk
up hive partitions, then require `<category>.jsonschema.yaml` beside the
directory). There is no inheritance from an ancestor scope. The two
elaborated questions -- `config-debug-hell.kb/` and `distro-alignment.kb/`
-- are legitimate nested scopes per `Skill(llm-discourse-graph)` §Scoping
and hierarchy, each with its own `claims.kb/` etc., and *none* of those
nested scopes had a sibling schema. The pre-`$ref` symlinks had only ever
been placed at the graph root.

Fixed by cause: 7 house stubs, one per nested collection, identical in
form to the 5 at the root. Zero frontmatter edited. The archived
2026-03-02 capture validates exactly as authored -- no extender was
needed, and no case arose for freezing a file as unfixable history.

Why it hid for months: while the root symlinks dangled, all 44 files
failed identically, so the 15 with a *second*, independent defect were
indistinguishable from the 29 that were merely unreadable.

Generalizes past this tree. A symlink-era graph gets schema links at its
root because that is where the author was standing; every scope
elaborated later is silently unvalidated. Worth a `-type d -name '*.kb'`
sweep for collection directories lacking a sibling schema -- that finds
this class directly, where a `-type l` sweep cannot.

Proposal, not applied (canonicals are out of scope here):
`llm-discourse-graph/SKILL.md` §Scoping and hierarchy says a sub-scope
"may contain any of this skill's collection types" without saying each
one needs its own schema file beside it. One sentence there prevents the
next instance.

The house stub keeps a `# yaml-language-server: $schema=...draft-07...`
first line, matching the 18 stubs written under 2026-08-21-000. It is
stale on every one of them: the referenced canonicals are 2020-12. Worth
one sweep, not worth diverging here.
