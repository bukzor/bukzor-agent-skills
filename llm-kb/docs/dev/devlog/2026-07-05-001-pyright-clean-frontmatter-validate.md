# Devlog: 2026-07-05 — pyright-clean frontmatter_validate

## Focus

Get `lib/python/llmd/frontmatter_validate.py` fully pyright-clean
(0 errors, 0 warnings under `basedpyright`, the repo's configured strict
checker), following on the file-relative `$ref` work earlier the same day.

## Decisions

### Isolate all `jsonschema`-touching code in `_jsonschema_adapter.py`

**Rationale:** `jsonschema` ships no `py.typed` marker. Any code touching
it directly infers as Unknown/Any throughout, and that Unknown-ness
propagates into every caller. Concentrating every `jsonschema` import and
the one genuinely-needed `extend()` call into a single, small module means
the rest of the codebase (`frontmatter_validate.py`) never imports
`jsonschema` at all — it only sees `_jsonschema_adapter.iter_schema_errors`,
fully typed.

**Alternatives considered:** `cast()` scattered at each `jsonschema`
touchpoint throughout `frontmatter_validate.py` directly — works
mechanically but spreads the "this library isn't typed" concern across
the whole file instead of quarantining it.

### Local `typings/jsonschema/` stub package (repo root)

**Rationale:** `basedpyright` doesn't just fail to infer types from an
unmarked library — it falls back to a *bundled* third-party stub (an old
typeshed `jsonschema` stub) that doesn't match the installed 4.26 API
(e.g. references a `_JsonParameter` type that doesn't exist in the real
package, requires `Any` where the real API doesn't). A project-local
`typings/` stub (pyright's default `stubPath`) takes precedence over the
bundled one and lets us declare only the ~4 names this repo actually
touches (`Draft202012Validator`, `TypeChecker`, `extend`,
`protocols.Validator`), correctly.

**Alternatives considered:** `cast()` everywhere without stubs — doesn't
work for the one case that matters most: `extend()`'s own import binding
is flagged Unknown regardless of what's done with its return value,
since the diagnostic attaches to the import statement itself, not any
downstream expression.

### `bin/llm.kb-validate` becomes a launcher script, not a symlink to the module

**Problem:** `frontmatter_validate.py` gained internal sibling imports
(`from ._jsonschema_adapter import ...`, `from .types import ...`) this
session. `bin/llm.kb-validate` was a symlink straight to that file (per
`docs/adr/2025-12-09-003`), so running it executed the module directly
as `__main__` with no parent package -- its own relative imports raised
`ImportError`.

**Decision:** `bin/llm.kb-validate` is now a small bash launcher
(replacing the symlink) that runs the module properly, as a real module:

```bash
cd "$here/.."
exec env PYTHONPATH="lib/python${PYTHONPATH:+:$PYTHONPATH}" \
  uv run python -m llmd.frontmatter_validate "$@"
```

`python -m llmd.frontmatter_validate` gives the module a correct
`__package__` (`llmd`), so every relative import inside it -- and inside
`_jsonschema_adapter.py`, which it imports -- just works, no
special-casing anywhere in the package's own source. `frontmatter_validate.py`
lost its `uv run --script` shebang and PEP 723 header (dead weight now
that nothing executes it directly; `llm-kb/pyproject.toml` already
declares the same deps and `uv run` picks them up from cwd) and its
executable bit, and gained a docstring note not to run it directly.

**Alternatives considered:** patch around the symlink at the Python
level -- `try: <relative import> except ImportError: <sys.path
bootstrap + absolute import>` inside `frontmatter_validate.py` itself,
guarded by `if TYPE_CHECKING:` so `basedpyright`'s
`reportImplicitRelativeImport` wouldn't flag the fallback branch.
Rejected: it solves the symlink's problem by complicating the module
instead of fixing the actual cause (running a package member as a
parentless script), and a bootstrap that inserts a module's own
directory onto `sys.path` for a bare import is one bad neighbor away
from shadowing a same-named stdlib module. `python -m` sidesteps the
entire class of problem for free.

## Conventions Established

- **Ill-typed third-party boundary → its own small adapter module,** named
  for the library it wraps (`_jsonschema_adapter.py`), leading-underscore
  since it's an internal implementation seam, not public API.
- **A `bin/` entry point for a package member is a launcher, not a
  symlink to the member itself**, the moment that member has internal
  sibling imports. `python -m pkg.module` (or the equivalent
  `runpy.run_module`) gives correct `__package__` for free; patching the
  module to tolerate being run parentless solves the wrong end of the
  problem.

## Verification

- `basedpyright` (repo root, whole tree): 0 errors, 0 warnings, 0 notes.
- `uv run pytest lib/python/llmd/frontmatter_validate_test.py`: 4 passed.
- `bin/llm.kb-validate .`, both from `llm-kb/` and from an unrelated cwd
  via absolute path: matches the pre-refactor baseline (0 errors across
  every real `.kb/` file).
- `shellcheck bin/llm.kb-validate`: clean.

## Filed

Upstream PR against typeshed (or jsonschema directly) to fix the stale
bundled stub's `_JsonParameter`/`extend()` gaps: tracked in
`.claude/todo.kb/2026-07-05-001-upstream-jsonschema-typeshed-stub-fix.md`.

## References

- `.claude/todo.kb/2026-02-09-000-schema-reuse-with-ref.md` — same-day
  earlier work (file-relative `$ref`) that motivated touching this file
  again for the typing pass.
- `docs/adr/2025-12-09-003-lib-python-pattern-for-testable-skill-scripts.md`
  — the `bin/` symlink convention this session had to preserve.
