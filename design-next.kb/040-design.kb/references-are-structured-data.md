---
why:
  - ../030-requirements.kb/filesystem-as-database.md
  - ../030-requirements.kb/validators-outlive-migrations.md
status: proposal
---

# References Are Structured Data

Knowledge edges live in frontmatter as data. A loosely-structured
`references:` map — kebab-slug relation label to list of targets, in
cross-reference notation — carries every association that isn't a
load directive:

```yaml
references:
  prior-art:
    - ../030-requirements.kb/filesystem-as-database.md
  see-also:
    - https://en.wikipedia.org/wiki/Application_profile
```

Labels are kebab-slugs, matching every other identifier in the tower
(frontmatter keys, filenames, `kb-spec.md`'s own naming rule) — not
free strings. A label too nuanced for a slug belongs in the entry's
prose, not forced into the map.

Two regimes, one lifecycle:

- **Loose**: any label, any resolvable target. Capture-first —
  existence precedes usage. Validators walk the map mechanically
  (every target resolves) with no understanding of labels.
- **Hardened**: a label that recurs and gains tooling graduates to a
  schema-defined top-level key with validated semantics (`why:`,
  `premises:` are already this). Same physics as flat-file →
  collection: structure hardens under demonstrated pressure. No
  separate registry tracks hardened labels — the promoted key's own
  schema entry is the record; a registry would only restate it.

`requires:` stays a top-level directive: it commands loading and is
mechanically enforceable; `references:` asserts relations and
commands nothing. V1's `depends:` retires *into* a `references:`
label — the relation survives, structure kept, label made explicit
where `depends:` left it implied.

If accepted: `kb-spec.md` gains a references bullet beside
directives; the `depends:` migration ships its doctor check; the
meta-schema validates the map shape (label → list, always a list)
once for all collections.
