# Devlog: 2026-07-06 -- caller-cwd resolution for relative args

## Focus

`bin/llm.kb-validate` resolved relative path arguments against the skill
directory, not the caller's cwd -- the launcher `cd`s to the repo root
(for `python -m` package context) before passing `"$@"` through. From an
unrelated project, `llm.kb-validate some.kb/` silently validated nothing
("0 files, 0 errors"), and the no-arg default validated the *skill's own
tree* instead of the caller's project. Found in real use: a consumer
project's schema violation reported ✅ until run by absolute path.

## Decisions

### Absolutize args in the launcher, before the cd

`realpath` each argument that exists on disk; leave non-path args (and
nonexistent paths, which the module should diagnose itself) untouched.
No-arg invocations now pass `$PWD` explicitly, preserving the documented
"validate current directory" default from the caller's perspective.

**Alternatives considered:** teaching the python module an env var for
the original cwd -- more moving parts for the same result; the confusion
is created by the launcher's `cd`, so the launcher is where it belongs.

## Verification

- `shellcheck bin/llm.kb-validate`: clean.
- From a consumer project: no-arg run walks that project (63 files); a
  relative dir arg validates just that collection; a known frontmatter
  violation reports ❌ where it previously reported "0 files, 0 errors".

## Follow-up

The silent "0 files" on a nonexistent/empty target is what masked this
bug; a "no .kb files found under <path>" warning would have surfaced it
immediately.
