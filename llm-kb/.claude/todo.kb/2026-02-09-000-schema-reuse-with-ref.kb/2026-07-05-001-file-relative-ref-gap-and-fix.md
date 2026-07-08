# File-relative `$ref`: gap confirmed, fixed (2026-07-05)

Reproduced the failure directly: a schema with
`$ref: "../jsonschema/common.yaml#/definitions/why"`, loaded and validated
via the real `validate_against_schema`, raises

    _WrappedReferencingError: Unresolvable: ../jsonschema/common.yaml#/definitions/why

**Fragment resolution (`#/definitions/...`) itself is free** — `referencing`
does RFC 3986 relative-URI resolution (`urljoin` against a base) and
JSON-Pointer fragments natively, confirmed with a synthetic `file://`
example outside the validator. The gap was that our validator never gave a
loaded schema a base URI to resolve *against*:

1. `load_schema()` just `yaml.safe_load`ed the path — no `$id`, so
   `self._base_uri == ''`. `urljoin('', '../jsonschema/common.yaml')`
   yields the same bare relative string, which nothing knows how to fetch.
2. `_retrieve_skill()` only handled `skill://` URIs (raised `ValueError`
   otherwise) — even with a base URI, a resolved `file://...` URI wouldn't
   be retrievable.

**Fix, implemented same day** (same TDD pattern as the `skill://` work):
`load_schema()` now injects a `file://` `$id` (the schema's own absolute
path) when one isn't already declared; `_retrieve_skill()` was renamed
`_retrieve_schema()` and dispatches on URI scheme (`skill://` vs `file://`)
rather than only handling `skill://`. Red-green confirmed — the
file-relative test (`DescribeFileRelativeRefResolution`) failed with
exactly the predicted `Unresolvable: common.yaml#/definitions/why` error
before the fix, passed after. Full suite (3 tests) green;
`bin/llm.kb-validate .` against the real repo still reported 0 errors
across all 65 files (no regression).
