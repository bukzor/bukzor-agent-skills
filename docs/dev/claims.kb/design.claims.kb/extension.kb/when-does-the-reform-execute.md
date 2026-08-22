---
label: EXECUTION
standing: user
why:
  - what-becomes-of-llm-discourse-graph.md
  - what-the-successor-is-called.md
  - migration-plan.md
---

# When Does the Reform Execute?

**"Decide and record" was the whole deliverable of the 2026-08-16/17
batch; execution is its own work item, and it runs as a
build-beside-and-swap.** Ruled 2026-08-22 by @bukzor, who supplied the
route the question was missing.

The route, in the user's own steps:

- Build `llm-discourse-graph-v2` directly against the description
  already in use: "use the discourse-graph ontology but in the
  claims-kb format".
- When third-party review determines it succeeded, replace the old one
  -- `git rm -r` the old and commit, then `git mv` the new into the
  vacated path and commit.

The gate is review, not a date. The user asked whether it could be
taken care of "real quick" today; nothing here commits to that, and
nothing forbids it.

`-v2` is scaffolding, not a successor: it is a path to build at while
the old one still works, and the second commit spends it. SUCCESSOR is
untouched -- the end state is `llm-discourse-graph`, at the same path,
which is exactly what that second commit restores, and what GUIDE_HOME
needs in order to route anyone.

The two commits are the point of splitting them. A single rename
commit would ask a reader to diff a skill against its replacement;
a removal followed by a placement says what actually happened.

What makes the reform small enough to build in one sitting is that
the description has already been run: for a week or two the user has
been invoking `/llm-claims-kb /llm-discourse-graph -- use the
discourse-graph ontology but in the claims-kb format` by hand and
getting what they wanted. The skill is being written down, not
designed.
