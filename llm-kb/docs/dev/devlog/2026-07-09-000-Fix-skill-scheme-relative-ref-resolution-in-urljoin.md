# Devlog: 2026-07-09 — Fix skill-scheme relative-ref resolution in urljoin

## Focus

Root-cause a real `llm.kb-validate` failure reported against
`prototype.chatfs/.claude/ideas.kb`: a `skill://ideas` stub schema with a
file-relative `$ref: todo.jsonschema.yaml` blew up with a four-deep chained
traceback ending in `Unsupported $ref scheme ...: todo.jsonschema.yaml`.

## Decisions

### Register `skill` with `urllib.parse.uses_relative`/`uses_netloc`

**Rationale:** `referencing`'s `Resolver.lookup()` always sets the base URI
for further `$ref` resolution to the literal retrieval key (the URI a
schema was fetched by) — never to that resource's own embedded `$id`.
Verified this empirically against bare `referencing`+`jsonschema` before
touching this repo's code. That means a schema reached via `skill://...`
can only have its own relative `$ref`s resolve correctly if `skill://` is
itself treated as a hierarchical scheme by `urljoin` — the same way
`file://` already is. Python's `urllib.parse.urljoin` only knows a fixed
set of schemes are hierarchical; `skill` wasn't in it, so
`urljoin("skill://ideas/stub.jsonschema.yaml", "todo.jsonschema.yaml")`
silently returned `"todo.jsonschema.yaml"` unchanged instead of joining —
no error at the join site, just a bad URI a few frames of library code
later. Fixed at `frontmatter_validate.py` module scope: append `'skill'`
to both `urllib.parse.uses_relative` and `uses_netloc` once, at import
time.

**Alternatives considered:**
- Inject a `file://` `$id` into resources loaded via `_retrieve_schema`'s
  `skill://` branch (mirroring what `load_schema` already does for the
  root schema). Rejected: proved empirically that an embedded `$id` is
  never consulted for this — `Resolver.lookup` uses the retrieval key,
  not `resource.id()`, as the next base URI.
- Redirect `_retrieve_schema`'s `skill://` branch to return a synthetic
  `{"$ref": "file://<resolved-path>"}` wrapper, forcing a second `$ref`
  hop that lands on a real `file://` URI. This does work for whole-file
  refs, but breaks the existing (tested) fragment case
  (`skill://.../shared.jsonschema.yaml#/definitions/why`), because the
  JSON-pointer fragment gets applied to the wrapper object instead of the
  real content. Rejected in favor of the `urllib.parse` fix, which fixes
  both cases with no architecture change.

## Conventions Established

- When a custom URI scheme needs relative-`$ref` support under
  `jsonschema`/`referencing`, register it with
  `urllib.parse.uses_relative`/`uses_netloc` rather than trying to inject
  `$id` — `$id` on a `$ref`-fetched (non-root) resource is not honored as
  a new resolution base by `referencing`.

## Open Questions

- The nested-traceback noise (`Unretrievable` → `Unresolvable` →
  `_WrappedReferencingError`, each explicitly chained with `from error` in
  library code) is not fixable from our own raise site — there's nothing
  to suppress there. If it recurs for a genuinely bad `$ref` scheme, the
  clean fix is to catch once at `iter_schema_errors`/`validate_against_schema`
  and re-raise a single message `from None`. Not done now since it's no
  longer the common case.

## References

- `docs/dev/adr/2026-05-18-000-skill-uri-scheme.md` — the ADR whose own
  worked example (`$ref: y.yaml` beside `$id: skill://llm-kb/a/x.yaml`
  resolving to `skill://llm-kb/a/y.yaml`) this fix makes actually true.
- `lib/python/llmd/frontmatter_validate.py`, `frontmatter_validate_test.py`
  — the fix and its regression test
  (`it_resolves_a_file_relative_ref_inside_a_skill_owned_stub`).
