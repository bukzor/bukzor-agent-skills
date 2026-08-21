# Findings (2026-08-21): homedir schema survey, and why this is two migrations

Surveyed every schema file in the homedir
(`cd ~/claude/homedir-archeology && uv run homedir-archeology jsonschemas`)
-- 309 files -- and evaluated them for duplication and unintentional
drift. Findings, then the three structural decisions this session made.

## The survey says: unfinished rollout, not a design problem

Seven clusters still use the pre-`$ref` copy pattern, and they are the
exact complement of the 2026-07-07 sweep's scope. That sweep hardcoded
`todo` and `ideas`; every category it did not name still copies. The
`$ref` infrastructure is mature and the conventions are written down --
nothing here needs inventing except in clusters 1 and 6.

Checked for latent closure bugs and found none: no 2020-12 keyword sits
under a draft-07 declaration where it would silently no-op, and no
`additionalProperties: false` is paired with a property-adding `allOf`.

Three files are *wrong*, not merely duplicated, and copying is what hid
them: ideation.physical-musings' todo copy admits `in-progress` (a status
the canonical deliberately omits, because a task either has an owner or
does not); two claim copies predate the verdict field; and
template.python-project seeds a stale snapshot into every repo made from
it.

## Decision: no `$schema:` in instance frontmatter

Asked whether instance files should carry `$schema:` alongside the
pointer they were assumed to have. First, a correction to the premise --
instances carry *no* schema pointer at all. The yaml-language-server
modeline appears only in schema files. Binding is positional and derived
(`frontmatter_validate.py`: `foo.kb/*.md` -> `../foo.jsonschema.yaml`).
Four reasons to leave it that way:

- It would be frontmatter *data*. Canonicals close with
  `unevaluatedProperties: false`, so every canonical would grow a
  `$schema` property purely to permit a pointer the directory already
  fixes.
- A derived binding cannot disagree with itself. A written pointer in N
  instances is N copies of one fact -- the precise pathology of the 21
  discourse copies, reintroduced at instance scale.
- `$schema` in an instance is not JSON Schema; it is a VS Code/ajv
  convention. `frontmatter_validate.py` does not honor it, so it would be
  inert.
- The editor-feedback argument does not survive either:
  yaml-language-server does not attach to markdown frontmatter. Buy that
  with a `yaml.schemas` glob mapping, which adds no data to any file.

Where `$schema` *is* right and underused is schema files themselves: 144
of 309 declare no dialect, and the house answer already exists
(`skill://llm-kb/jsonschema/dialect.jsonschema.yaml`, 12 files).

## Decision: two migrations plus one deferred amendment, not seven

The count that matters is transformations, not findings. Clusters 2, 4, 5
and 7 are one transformation -- the one already written as
`2026-07-07-000-schema-copies-to-ref-stubs`, whose only defect is a
hardcoded scope. Generalizing it with a category table beats three
siblings sharing a `migrate.sh`. Cluster 3 is a genuinely different
transformation (relocate the canonical, repoint dependents), so it gets
its own entry. Clusters 1 and 6 are not migrations at all: per
`migrations.kb/CLAUDE.md`, no transformation exists until the target is
decided, so they are todo work that unblocks a later migration.

The recurring guard `2026-05-15-000-schema-propagation-from-canonical`
needs its scope widened from todo/ideas to every category with a
canonical -- but *after* the generalized validator can back the wider
claim. Widening a `status: verified` guard's stated scope while its
`validate.sh` still checks two categories would make the entry lie.

## Non-obvious: what the frontier work actually has to settle

Cluster 1 (design-kb layer entries, 9 projects) is not mechanical. Real
disagreements, each with live data on both sides:

1. Is `why:` required? Five projects say yes, four say no. Picking
   "required" invalidates data in four projects.
2. `minItems: 1`? mitmproxy alone asserts it. Is `why: []` meaningful --
   a root goal has nothing above it?
3. What *is* a `why` entry? har-browse and design-next use paths;
   mitmproxy says slugs; meta-reasoning adds `aliases` holding claim
   labels. Three different reference systems wearing one field name.
4. Does the canonical own the layer tower (010-mission .. 070-future-work
   as fixed), or only the entry shape?
5. Are per-project extras (`tags`, `aliases`, design-next's
   `status`/`blocked-on`/`superseded-by` lifecycle) canonical or
   extensions?
6. Whether to canonicalize at all. `references/schema-reuse.md` warns
   about the extraction floor: a definition a reader can restate from
   memory costs more as a reference than as a copy, and
   `why: {type: array, items: {type: string}}` is arguably below it. That
   is a real argument against a canonical here and deserves adjudication
   rather than assumption.

Cluster 6 is smaller but genuinely undecided: `$ref` to
`/home/bukzor/.claude/sessions.jsonschema.yaml` is a machine-specific
absolute path with no scheme. Options are to move the schema into a skill
and use `skill://`, to teach the resolver a `home://`-style scheme, or to
accept the absolute path. Each has fallout beyond this one file.

One more unadjudicated tension, smaller than the above but not obvious:
should `template.python-project` ship stubs or self-contained copies? A
stub only resolves if the consumer has the skills installed. DRY says
stub; standalone-ness says copy. The 2026-07-07 sweep stubbed it as
"intent-free" without anyone deciding the general question.
