---
why:
  - filesystem-as-database
  - validators-outlive-migrations
status: proposal
blocked-on: discussion
---

# References Are Structured Data

Knowledge edges live in frontmatter as data. A loosely-structured
`references:` map — free-form relation label to list of targets, in
cross-reference notation — carries every association that isn't a
load directive:

```yaml
references:
  "prior art":
    - ../030-requirements.kb/filesystem-as-database.md
  "see also":
    - https://en.wikipedia.org/wiki/Application_profile
```

Two regimes, one lifecycle:

- **Loose**: any label, any resolvable target. Capture-first —
  existence precedes usage. Validators walk the map mechanically
  (every target resolves) with no understanding of labels.
- **Hardened**: a label that recurs and gains tooling graduates to a
  schema-defined top-level key with validated semantics (`why:`,
  `premises:` are already this). Same physics as flat-file →
  collection: structure hardens under demonstrated pressure.

`requires:` stays a top-level directive: it commands loading and is
mechanically enforceable; `references:` asserts relations and
commands nothing. V1's `depends:` retires *into* a `references:`
label — the relation survives, structure kept, label made explicit
where `depends:` left it implied.

If accepted: `kb-spec.md` gains a references bullet beside
directives; the `depends:` migration ships its doctor check; the
meta-schema validates the map shape (label → list, always a list)
once for all collections.

Open: label grammar (free strings vs kebab slugs); whether hardened
labels get a registry.
