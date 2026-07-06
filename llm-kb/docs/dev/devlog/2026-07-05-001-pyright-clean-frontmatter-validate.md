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

### `types.py` renamed to `_json_types.py`

**Rationale:** `bin/llm.kb-validate` is a symlink to
`frontmatter_validate.py` (per `docs/adr/2025-12-09-003`), run standalone
via `uv run --script` with no parent package. That path requires
inserting the module's own directory onto `sys.path`, at which point a
module literally named `types.py` would shadow the stdlib `types` module
for every other import in the process. Not a hypothetical: several
dependencies (e.g. `dataclasses`) reference `types` internally.

### Dual-mode import via `if TYPE_CHECKING: ... else: try/except`

**Rationale:** `frontmatter_validate.py` and `_jsonschema_adapter.py`
both need to work two ways: imported as `llmd.frontmatter_validate` (pytest,
other package consumers) and run standalone as `bin/llm.kb-validate`
(`__name__ == '__main__'`, no parent package — plain relative imports
raise `ImportError`). The runtime fix is an unremarkable
try-relative-except-sys.path-bootstrap. The type-checking wrinkle:
`basedpyright`'s `reportImplicitRelativeImport` flags the bare
(non-relative) import in the except-fallback as *always* wrong, since it
can't know that branch only executes in the no-package case. Wrapping the
whole thing in `if TYPE_CHECKING: <relative-only> else: <try/except>`
gives the checker the accurate (relative) view for type purposes while
the real dual-mode logic runs unanalyzed at runtime — confirmed empirically
that `basedpyright` does not lint inside the `TYPE_CHECKING`-false branch.

## Conventions Established

- **Ill-typed third-party boundary → its own small adapter module,** named
  for the library it wraps (`_jsonschema_adapter.py`), leading-underscore
  since it's an internal implementation seam, not public API.
- **Never name a sibling module after a stdlib module** (`types.py` →
  `_json_types.py`) when that module might ever be imported off a
  directly-inserted `sys.path` entry, even if today's import graph makes
  it seem safe.
- **`bin/` symlink scripts that gain internal sibling imports** need the
  `TYPE_CHECKING`-guarded dual-mode import pattern above, not just a bare
  try/except — otherwise the standalone-execution branch fails pyright's
  relative-import check even though it's correct at runtime.

## Verification

- `basedpyright` (repo root, whole tree): 0 errors, 0 warnings, 0 notes.
- `uv run pytest lib/python/llmd/frontmatter_validate_test.py`: 4 passed.
- `uv run bin/llm.kb-validate .` (standalone symlink path): 65 files,
  0 errors — matches pre-refactor baseline, confirming the dual-mode
  import fix didn't just satisfy the type checker but actually works.

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
