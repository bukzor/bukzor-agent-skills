---
label: GUARD_ROOTS
standing: open
why:
  - a-home-rooted-sweep-sees-almost-nothing.md
---

# What Roots Does a Guard Run Over?

A recurring migration's `validate.sh` needs a list of trees to check.
`~` does not work. The candidates:

- enumerate the repositories -- `~/repo/*/*/*` and `~/claude/*` -- and
  accept that a new repo is invisible until someone adds it;
- run per-repository, from each repo's own hook, and accept that a repo
  nobody commits to is never checked;
- ask an existing survey tool for the repository list, and check what
  it returns.

The third has prior art the user pointed at:
`~/claude/homedir-archeology` is a real package
(`bukzor_homedir_archeology.survey.find()`) that already owns the
noise-pruning -- `trash/`, `node_modules/`, venvs, build caches -- in
one place, and is installed editable into the `$HOME` uv workspace.
`~/.claude/must-read.kb/when/surveying-the-homedir-for-an-artifact-type.md`
already forbids writing a new scanner instead of using it.

That makes the third option the one to beat, but it is not yet ruled:
what survey returns is a file list, and a guard wants a repository
list.
