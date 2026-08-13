# Progress (2026-07-07/08): complete-example refactor + yaml-language-server verification

Extracted the duplicated `status` (enum `decided`/`pending`) and `budget`
(number) field definitions into `complete-example/jsonschema/status.jsonschema.yaml`
and `complete-example/jsonschema/budget.jsonschema.yaml`, following the
default pattern (whole-file `$ref`, no fragment). Three consumers now
point at them: `decorations.jsonschema.yaml` and `food.jsonschema.yaml`
(both fields, same-directory relative path) and
`food.kb/cake.jsonschema.yaml` (`status` only, one directory deeper --
demonstrates `../jsonschema/...` resolution). `bin/llm.kb-validate
complete-example` still reports 0 errors across all 20 files after the
refactor. `references/complete-example.md` gained a "What to Notice"
paragraph pointing at the new `jsonschema/` subdirectory.

yaml-language-server verification: no interactive editor session is
available in this environment, so this was verified via a generic-tool
proxy rather than an actual editor. Loaded `decorations.jsonschema.yaml`
with `jsonschema.RefResolver` (the legacy resolver, which auto-fetches
`file://` URIs via `urlopen` with **no custom retrieve callback** --
the same generic mechanism a tool like yaml-language-server relies on
for plain file-relative `$ref`, as opposed to our own `_retrieve_schema`).
Confirmed it resolves the `$ref` chain and correctly accepts valid data
and rejects invalid `status`/`budget` values. This validates the
technical claim in `references/schema-reuse.md` ("a generic tool
resolves plain file-relative `$ref`s out of the box"); it is not a
substitute for opening the files in an actual editor with the YAML
extension installed, which remains a manual follow-up if stronger
confidence is wanted.
