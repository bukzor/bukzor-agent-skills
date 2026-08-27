# Recommendation (2026-08-23): no -- the guard's roots do not include `~`; derive the dotfiles collections from the `$HOME` git index instead

## The mechanism, re-derived (the brief's framing is wrong in a load-bearing way)

`$HOME` **is** the dotfiles working tree: `git -C ~ rev-parse
--show-toplevel` is `/home/bukzor`, `origin` is `git@github.com:bukzor/dotfiles.git`,
and `~/.git` is a symlink into `~/.local/state/git-localhost-store/`. `~/.vim`
is a real directory at the top of that tree, not a symlink and not an install
target; `.vim/.claude/{ideas,todo}.jsonschema.yaml` are tracked files.

There is also a *second, independent checkout* at
`~/repo/github.com/bukzor/dotfiles` (its own git dir, same branch name
`svelte-crostini`), and that is the copy the guard walks. So the brief is right
that coverage is accidental, and wrong about what the accident produces:

| | live `$HOME` tree | clone under `~/repo` |
|---|---|---|
| `.vim/.claude/todo.jsonschema.yaml` | draft-07 stub, `$ref: skill://llm-subtask/...` | same stub at HEAD; **working tree** holds a full 2020-12 copy, uncommitted |
| `.vim/.claude/ideas.jsonschema.yaml` | stub | same, uncommitted overwrite |
| HEAD | `5b6aa7b` | `82e1a8e`, a strict ancestor -- behind |
| seen by the guard | no | yes |

`git merge-base --is-ancestor 82e1a8e HEAD` succeeds: the clone is behind, not
divergent. But staleness is not what the guard is reporting. `git status` in the
clone shows nine `M` schema files plus two untracked ones, all stamped
2026-08-22 14:03, and `git diff` shows the direction: a committed
`$ref` stub replaced by a hand-rolled full copy. That is the signature of the
2026-08-22 schema blast -- "add schemas where missing" read as "make every
collection have a schema" -- whose revert never reached this clone. So the
committed content here is *already correct*; the seven `dotfiles` findings among
the guard's fifteen are unreverted blast damage sitting in a working tree, not
ghosts of an old commit. The repair is `git checkout` in that clone (plus a
judgment on the two untracked files), not a prune rule.

The accident is still not giving us coverage: the tree it stands in for is
invisible, and live `$HOME` is clean.

## The gain from adding `~`: three directories, zero findings

`collections()` under `~` minus `collections()` under the three current roots is
exactly three entries, and that set is the entire benefit:

    /home/bukzor/.vim/.claude/ideas.kb
    /home/bukzor/.vim/.claude/todo.kb
    /home/bukzor/.vim/testing.kb

`./validate.sh ~/.vim` exits 0, clean. The first two already carry canonical
stubs; `testing` has no published canonical, so the guard is vacuous on it by
construction. Net new findings from adding `~`: **zero**.

## The cost: a 3x walk that ends in `ERROR(1)` and an empty report

| measurement | roots `~/repo ~/claude ~/.claude` | root `~` |
|---|---|---|
| `collections()` alone (warm) | 2.9 s | 16.0 s |
| full `validate.sh` | 10.8 s | 17.3 s |
| directories walked (post-prune) | 71,805 | 221,290 |
| collections found | 627 | 630 |
| findings on stdout | 15 | **0 -- report lost** |
| exit | 1 (findings) | 1 (`ERROR(1)`, crash) |

The crash is the decisive number. Forty-two `Permission denied` lines come from
root-owned container overlay dirs (`~/.local/share/containers/storage/overlay/*/work/work`,
`~/.solargraph/0/overlay/...`). `find` exits 1; `report="$(collections ... | sort
| xargs ...)"` inherits it under `pipefail`; `errexit` fires the `ERR` trap. The
guard prints nothing and exits 1 -- indistinguishable at a glance from "found
findings", which is the worst possible failure shape for a recurring guard.

What `~` drags in, by directory count outside the current roots: `.local`
65,246 (of which `state/git-localhost-store` alone is 28,106 -- every repo's git
dir, invisible to the `-name .git` prune because it is *not* named `.git`),
`.opam` 36,655, `.cache` 23,952, `prefix` 12,225, `.bun` 11,884, `.volta` 5,764,
`chats` 4,612, `.npm` 3,129, `.pyenv` 2,444, `books` 2,357, `.rustup` 1,927,
`.cargo` 1,858, `.vscode` 1,772. 41 GB excluding the three roots. The walk *is*
prune-aware, but a prune list adequate here would have to name every one of those
plus a `-readable` predicate, and would grow with every tool the owner installs.

## Portability

The three current roots are owner-defined conventions, created the same way on
every host by the dotfiles setup. `~` is defined by the *operating system and
the toolchain*, and this host is ChromeOS Crostini: podman overlay stores,
`~/Downloads` and `~/GoogleDrive` symlinked into `/mnt/chromeos` (unfollowed
today only because `find` defaults to `-P`; any later `-L` turns that into a
network-mount hang). A `~`-rooted guard behaves differently per machine, and its
prune list must be maintained per machine. A fleet guard should not be the most
host-dependent thing in the fleet.

## The cheap positive change: register the enumeration, don't inline it

Enumerate the `$HOME` tree's collections from its own git index rather than by
walking it:

    git -C "$HOME" ls-files | sed -n 's,\(^.*\.kb\)/.*,\1,p' | sort -u

Twenty collections, **18 ms**, including all three otherwise-invisible ones and
none of the 149,485 extra directories. It is *derived*, not declared -- the same
property that made globbing published canonicals beat `categories.tsv` -- and the
manifest is one the owner already maintains for unrelated reasons, so it cannot
fall behind the way a hand-written root list did. On a host where `$HOME` is not
a git checkout it yields nothing and the guard degrades to today's behavior
rather than crashing.

Inlined into `lib.sh`, though, that one-liner is a new homedir-wide artifact
scan, and `must-read.kb/when/surveying-the-homedir-for-an-artifact-type.md`
governs those: don't write a new script, and *"only add a new named
function/subcommand if the survey is going to be rerun -- and if so, add it to
`survey.py` (+ a subcommand in `cli.py`)"*. A guard that runs daily is the
definition of rerun. So the enumeration belongs in the package:
`home_git_collections()` in `bukzor_homedir_archeology/survey.py`, a
`collections` subcommand in `cli.py`, and the guard calls the CLI.

Why the git index and not that package's own `find()` engine -- measured today:

| instrument | `.kb` dirs | wall | crash |
|---|---|---|---|
| guard `collections()`, three roots | 660 | 5.4 s | no |
| guard `collections()`, root `~` | 630 | 16.0 s | `ERROR(1)` |
| `survey.find -path '*.kb/*'`, reduced to dirnames | 733 (81 of them `*--replication-run`) | 3.0 s | no |
| `git -C ~ ls-files` | 20, of which 3 novel | 18 ms | no |

- **`survey.find()` cannot see the three collections either.** Its prune list
  drops every top-level dotdir except `.claude`
  (`-regex '^\./(\.[^/]*|prefix)$' -not -name .claude -prune`), so `./.vim` is
  never walked: of the 733 collections it returns, zero are under `.vim`. The
  shared engine is strictly better than a raw `~` walk -- 3.0 s against 16.0 s,
  no permission errors, prune list maintained by someone else -- and still
  misses exactly the gap this ruling is about.
- **Both instruments enumerate files; the guard checks directories.** Six
  collections today hold no regular file at their own level
  (`dotfiles/.claude/sessions.kb`, `ideation.epistemics/.claude/todo.kb`, four
  more), and no file-derived list can contain them. That may well be an
  improvement -- an empty collection has no frontmatter to validate, so
  `MISSING` on it is a false positive of the species lane -003 owns -- but it is
  a behavior change riding along with a coverage change, and the verdict should
  say whether it is wanted.

The `~` row above was measured 2026-08-23; the three-root row is today's, and
the 627 in the cost table is that day's figure for the same command. 89 `.kb`
directories under the three roots carry an mtime inside those four days --
drift arriving at exactly the rate ruling #4's schedule argument assumes.

The cost of routing through the package is a new dependency direction: fleet
infrastructure in bukzor-agent-skills calling a personal project under
`~/claude`, needing `uv` on `PATH` in an anacron environment. Smaller than it
looks -- the guard already requires `yq`, so "pure bash" is not the status quo --
but it has to fail loudly: if the subcommand is unavailable the guard prints
`SKIPPED` with a reason on stderr and continues at three roots. Silently
narrowing coverage is the failure this ruling exists to prevent.

If the owner rejects that direction, the fallback is declared rather than
derived: add `$HOME/.vim` to `ROOTS`. Three collections, no new dependency,
portable because dotfiles creates `.vim` on every host -- and the
`categories.tsv` failure mode re-created knowingly, blind to the next collection
someone puts at `~/.config/foo.kb`.

Priced honestly either way: today it finds zero new findings, so it is
insurance, not repair.

Two subordinate observations for whichever lane owns guard edits: the stale
`dotfiles` clone deserves the `*--replication-run` treatment (prune it, or
prefer the live tree), and the `-name .git` prune silently misses
`git-localhost-store` git dirs on this host.

## The declined alternative: add `~`, steelmanned

The strongest case for `~` does not rest on today's findings, and I should not
pretend it does. A guard's value is *coverage by construction*: three roots
chosen because that is where drift was last found is the categories.tsv failure
mode wearing a different hat, and "zero findings today" is evidence the fleet is
currently clean, not evidence the root is worthless. The next collection someone
creates at `~/.config/foo/.kb` or `~/lvim/.claude/` is invisible under my
recommendation and visible under theirs. The 17 seconds and the 42 permission
errors are ordinary engineering (`-readable`, a prune list), not intrinsic
objections, and a guard scoped to avoid a fixable bug is a guard shaped by its
implementation rather than its purpose.

I think that argument is right about the *goal* and wrong about the *instrument*.
Coverage-by-construction over the dotfiles tree is exactly what the git index
gives, in milliseconds instead of 16 s, with a manifest that is maintained for
other reasons and is identical on every host. `~` buys the same coverage plus an
unbounded, per-machine prune list -- the declared-list failure the roll-up
already hit once. If the owner rules for `~` anyway, the minimum viable form is
`~` plus `-readable` plus a prune list naming at least `.local`, `.cache`,
`.opam`, `prefix`, `.bun`, `.volta`, `.npm`, `.pyenv`, `.rustup`, `.cargo`,
`.vscode`, `chats`, `books` -- and the `ERROR(1)` crash must be fixed first, or
the widened guard reports nothing at all.

## Verdict

**No `~`. `$HOME/.vim` joins `ROOTS`** (user, 2026-08-27).

The package registration is declined for now -- agent's call, recorded
here, veto by editing this file. Doing both gives the guard two sources
for the same three directories, and the must-read's trigger for a named
`survey.py` function is that *the survey is going to be rerun*, which a
`ROOTS` entry does not satisfy. Revisit on the first `.kb` that appears
in the homedir outside `repo/`, `claude/`, `.claude/`, `.vim/`: that is
the evidence the declared list has begun to rot, and the git index is
waiting.

The edit belongs to whichever lane owns `validate.sh`, and the new
entry carries a comment saying why `.vim` is a root -- an unexplained
root is what the next sweeper deletes.
