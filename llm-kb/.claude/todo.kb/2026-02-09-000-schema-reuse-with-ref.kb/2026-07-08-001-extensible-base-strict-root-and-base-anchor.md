# Progress (2026-07-08): extensible base via strict-root/#base convention

Extension was documented-but-blocked: canonical top-level
`additionalProperties: false` rejected any consumer-added field even
through `$ref` conjunction, and the fix-on-first-need plan would have
forced the first extender into a cross-repo canonical edit. Adopted the
two-entry-point convention (user's design, superseding a
close-every-stub proposal): canonical content lives in `$defs: base:`
(open, `$anchor: base`); the document root is the strict entry point,
`$ref: "#/$defs/base"` + `unevaluatedProperties: false`. Plain stubs are
untouched -- they ref the root and stay strict; closure is stated once,
in the canonical, so no stub can forget it. An extender refs
`...jsonschema.yaml#base`, adds `properties:`, and closes itself with
`unevaluatedProperties: false` -- purely local. Required bumping the
canonicals to the 2020-12 dialect (draft-07 ignores `$ref` siblings;
the validator already ran 2020-12) and `definitions:` -> `$defs:` (no
live consumer referenced the old `#/definitions/sweh-value` pointer).
Verified end-to-end through llm.kb-validate, file-relative and
skill://, both `#base` and `#/$defs/base` forms. Documented in
`references/schema-reuse.md`; policy record in the propagation
migration entry.
