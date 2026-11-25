# Self-audit: one home

## Goal

Each conclusion, and its reasoning, is stated in one file that everything else
links to ([ONE_HOME]): no copy left to drift, and no cut that removes the last
statement of something.

## When to run

After writing, editing, or cutting any kb file -- `CLAUDE.md` files and trigger
banks included.

## Procedure

- **Copies.** For each file you wrote or edited, grep a distinctive clause of
  it (not a word) across the repo. A second hit that restates, rather than
  naming the act and linking, is a finding: keep the home, cut the other down to
  the act and a link.
- **Losses.** Before committing a cut, grep each removed phrase that carried
  content -- a scope item, a constraint, a named example. No surviving hit
  means the cut lost it: move it where it belongs, or say in the commit that it
  was meant to go.

[ONE_HOME]: ../../../docs/dev/claims.kb/design.claims.kb/principles.kb/one-home.md
