# Creating a New .kb Collection

When creating a `.kb/` collection from scratch, follow this procedure.
Structural decisions made up front determine how usable the collection is
for future agents.

## Plan: enumerate and categorize

Run `../SKILL.kb/procedures.kb/enumerate-and-categorize.md` to list every
item the collection will hold and categorize them by type. The procedure
also covers the flat-`.md` fallback for small collections.

Skipping this step is the most common cause of under-scoped collections
that need restructuring later.

## Write: one thing per file

Each item in a `.kb/` is its own `.md`. Use kebab-case names descriptive
enough that a future agent can guess the file's content from its name.
Don't number unless items are inherently ordered.

Each `$CATEGORY.kb/` requires a `CLAUDE.md` that describes what belongs in
the directory and what does not. The `CLAUDE.md` is a maintenance guide,
not an enumeration of contents -- never list the files that happen to be
present, since `ls` does that better.

For a worked example of layout, see `complete-example.md`.

## Review: four quality passes

After writing initial content, run each of these passes. Each one targets
a common failure mode and prescribes a remediation.

### Pass 1: enumeration completeness

Re-list the "things" you intended to capture. Are all of them actually
persisted as files?

If anything is missing, write it. If anything is half-described in prose
that could be expanded into its own item, expand it.

### Pass 2: per-file scope

Open each `.md` and ask: does this file describe one thing, or several?
A file describing several things -- typically signaled by parallel `##` or
`###` sections describing items of the same kind -- should be promoted to
a sub-`.kb/` with one item per file.

The 50-token threshold is a useful trip wire: if any single item inside a
multi-item file exceeds ~50 tokens of explanation, promote unconditionally.
Below that threshold, judgement applies.

### Pass 3: schema potential

For each `.kb/` directory, ask: do the items within share attributes that
would be useful to expose as machine-readable metadata (status,
last-updated, severity, owner, etc.)?

If yes, design a `$CATEGORY.jsonschema.yaml` for the collection and add
frontmatter to each item file. Validate with `bin/llm.kb-validate`. If
the schema is non-trivial, see `schema-design.md`.

If no, leave the items prose-only. Schema isn't free; the structure
should pay its weight in queryability.

### Pass 4: validation

Run `bin/llm.kb-validate <path>` and resolve any errors before considering
the collection complete. The validator catches frontmatter schema
violations and structural issues -- manual auditing here wastes tokens and
misses real problems.

## When in doubt

If you're uncertain whether something belongs as a flat `.md` or as a
sub-`.kb/`, lean toward `.kb/`. The kb form is forgiving -- a `.kb/` with
two items reads almost identically to a flat `.md` with two `##`
sections, but the kb form scales without restructuring when more items
arrive. Going from `.md` to `.kb/` later requires renaming, splitting,
and writing a new `CLAUDE.md`, so paying that cost up front when you
expect even modest growth is usually worth it.
