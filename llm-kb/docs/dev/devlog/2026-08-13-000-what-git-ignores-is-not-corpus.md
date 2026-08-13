# Devlog: 2026-08-13 -- what git ignores is not corpus

## Focus

`llm.kb-validate .` at a repo root reported 13 errors, 12 of them from a
half-renamed ledger parked in gitignored `trash/` months ago. The
operator: *"that's not great ergonomics."* A red count that never means
anything is worse than no count -- it teaches the reader to skip the
count. Discovery now filters through git, and the day's remaining three
corrections all came from the operator reading the patch.

## Decisions

### Scratch is what git says it is; naming a path overrides that

What the walk *discovers* is filtered by `.gitignore`. A `.kb/` under
`trash/` or `node_modules/` is somebody's scratch. A path named on the
command line is validated whatever git thinks of it -- asking is asking
-- which is what keeps a deliberately-ignored corpus (generated output,
a ledger drafted in `trash/` before it earns a home) reachable.

**Alternatives considered:** a `--no-ignore` flag. The command line
already carries the intent; a flag would ask the user to say twice what
naming the path says once.

### No fail-soft, no swallowed stderr

The first implementation captured git's stderr and returned "nothing is
ignored" on any exit above 1. The operator: *"please take care to not
failsoft nor suppress stderr where there would (otherwise) be relevant
errors printed to terminal."* Now the only message that stays off the
terminal is the one that *is* an answer rather than an error -- `fatal:
not a git repository`, pinned in a named constant so a git rewording
fails the tests rather than users. Everything else git says is written
through, and then raised.

This paid for itself within the hour: see below.

### Ask each path its own repository

The operator asked whether `git rev-parse --show-toplevel` would beat
the hand-rolled walk up for a `.git`. It would -- it is git's own
discovery, and this machine already breaks the walk's assumptions, since
`git-localhost-store` relocates `.git` and leaves a symlink. But the
argument goes one step further: `check-ignore` performs that discovery
itself, so the right move was deleting the probe, not improving it.

The same change fixed a crash the fail-soft had been hiding.
`check-ignore` refuses a pathspec inside a submodule --

    fatal: Pathspec '.../mod/thing.md' is in submodule 'mod'

-- and one batched query anchored at the directory being expanded hands
it exactly that, for any submodule holding `.kb/` collections below a
name that isn't itself a `.kb`. Anchored per path, the submodule answers
for its own contents and its own `.gitignore` governs inside it. `-q`
leaves the answer in the exit code, so no output is parsed.

Fail-soft did not prevent this bug; it prevented *finding* it.

### `glob_prune` names the step, and the rewrite it implies is not worth it

`without_children` -> `outermost` -> `glob_prune`, the last being the
operator's, after find(1) `-prune`: universal vocabulary, and it names
the step rather than the residue. The name is a promise the code cannot
keep -- `-prune` stops the descent, this only declines to pass results
on, because the `**` glob has already paid for the walk. The docstring
says so.

Making it literal was measured and dropped (`.claude/todo.md`):
discovery is 7% of runtime (144ms glob of a ~2000ms run; the rest is
YAML plus jsonschema over 366 files), pruning saves ~70ms, and deciding
descent means asking git per directory visited -- hundreds of execs
against today's 97. It subtracts nothing either: `corpus` must stay for
the nested branch, and "asking is asking" becomes a flag threaded
through the walk.

## Verification

- 13 tests pass, four of them new: an ignored collection skipped, an
  ignored collection named on the command line validated, everything
  validated outside a repository, and a submodule asked about its own
  contents (a gitlink via `git add mod`, no clone, no protocol flag).
  A fifth plants an unreadable `.git` and asserts the raise.
- pyright: 0 errors, 0 warnings, 0 notes.
- Repo root: 0 errors, down from 13; 17 files under `trash/` stopped
  counting. `trash/aborted-git-mv` named explicitly still reports its 12.
- `~/.claude`, whose `sessions.kb` is a gitlink: walks without fatal,
  and reaches inside the submodule.

## References

- `lib/python/llmd/frontmatter_validate.py`: `ignored_by_git`, `corpus`,
  `glob_prune`
- Commits: `646e8f7`, `895c8ec`, `8c5ee24`, `a051195`, `6d65b97`,
  `9ebc50c`
