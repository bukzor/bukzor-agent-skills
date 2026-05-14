---
name: llm-kb
description: "Agent MUST load for .kb/ directories and structured multi-agent knowledge bases"
---
--- # workaround: anthropics/claude-code#13005
setup: |
    All projects that depend on this skill should have as `CLAUDE.md` frontmatter:

    ```yaml
    --- # workaround: anthropics/claude-code#13003
    requires:
        - Skill(llm-kb)
    ```
---

> **IMPERATIVE:**
>
> Your FIRST action when this skill loads MUST be:
> `Bash("ls -RF SKILL.kb/must-read/")`. Then read every entry whose trigger
> matches the work at hand.

The must-read entries link to audits in `SKILL.kb/self-audit.kb/` and
procedures in `SKILL.kb/procedures.kb/`; follow those links when triggers
fire. When adding new kb content of your own, browsing
`SKILL.kb/self-audit.kb/` directly is a cheap proactive check for relevant
quality concerns.

# llm.kb Pattern

Create structured knowledge bases using `.kb/` directory collections. Frontmatter
is optional, but if used, requires schema validation to prevent drift. Use when
organizing facts, tasks, or information for efficient LLM access across multiple
agents. Key principles: small focused files, CLAUDE.md for maintenance guidance
(never enumeration), summary files only when they add value beyond `ls`.

## Anatomy

```
$PROJECT/
├── CLAUDE.md ──────────────────── maintenance guide (root)
├── README.md ──────────────────── summary file (root scope)
├── $CATEGORY.jsonschema.yaml ─── schema
├── $CATEGORY.md ───────────────── summary file (category scope)
├── $CATEGORY.kb/
│   ├── CLAUDE.md ──────────────── maintenance guide (category)
│   ├── $ITEM.md ───────────────── content file
│   └── $NESTED.kb/
│       ├── CLAUDE.md ──────────── maintenance guide (nested)
│       └── $ITEM.md ───────────── content file
```

### Summary Files (README.md, $CATEGORY.md)

Summarize a scope to help readers decide whether to dive deeper.

- README.md -- root scope (the whole project or multiple `.kb/` collections)
- $CATEGORY.md -- category scope (summarizes `$CATEGORY.kb/`)

May describe themes, patterns, or even list contents -- whatever helps readers
avoid reading the directory. Omit when trivial (few items); `ls` suffices.

If present, requires frontmatter:
```yaml
last-updated: YYYY-MM-DD
```

### Maintenance Guides (CLAUDE.md)

Enable maintenance decisions, not content discovery. After reading, an agent
knows what belongs here -- not what's currently here.

- Root CLAUDE.md -- common principles (pushed up from per-directory guides)
- Per-directory CLAUDE.md -- category-specific guidance for that `.kb/`

Root CLAUDE.md must have:

- Frontmatter declaring this skill (see `setup:` above for exact format)
- An overview of available `.kb/` collections and their purpose

This ensures any agent working in the project loads the pattern and can
navigate to the right collection without exploring.

After reading `$CATEGORY.kb/CLAUDE.md`, agent must know:
- What belongs here (concept, not enumeration)
- What does NOT belong (boundaries)
- When to add/read files here

Content discovery is `ls`. Never enumerate in CLAUDE.md.

❌ "Tools: Goose, Aider..." / "PRs: #123, #456..." / "Contains: api.md, auth.md"

## Frontmatter Directives

CLAUDE.md files use frontmatter to give agents operational instructions. These are **action triggers**, not passive metadata.

- `requires:` -- Read these files before acting in this directory.
- `depends:` -- Read when relevant.

### Content Files ($ITEM.md in .kb/)

Individual items within collections. Each file represents one thing (one tool,
one decision, one task).

- Markdown prose, optionally with YAML frontmatter
- If frontmatter used, must conform to `$CATEGORY.jsonschema.yaml`

Create when adding a new item to a collection. The file IS the item; there's no
separate registry.

### Schema Files ($CATEGORY.jsonschema.yaml)

Validates frontmatter in `$CATEGORY.kb/*.md`. Prevents drift between files in the
same collection.

- Required if any content files in that collection use frontmatter
- Optional if content files are prose-only
- Skips CLAUDE.md files (maintenance guides don't need frontmatter)

Create when you want structured metadata on content files. Omit for prose-only
collections.

### Collections ($CATEGORY.kb/)

A directory holding homogeneous content files -- **same type of thing**.

- Each item is one file
- All files share the same schema (if using frontmatter)
- Related by type, not by tool/subject

Create when you have multiple items of the same kind. Use the `.kb/` suffix to
signal "this is a collection, use `ls` for contents."

Example: `tools.kb/` contains tool profiles; `features.kb/` contains feature
comparisons.

## Naming

Applies to `$CATEGORY` and `$ITEM` identifiers (directory and file names).

- Use kebab-case
- Be descriptive -- agent must know roughly the content from the filename
- Prepend digits if inherently ordered (e.g., `001-setup.md`, `002-config.md`)
- Zero-pad to twice the digits you expect to need

## When to Use

Good fit:

- Information with structure (metadata + explanation)
- Multiple categories of related content
- Future agents will maintain/extend
- LLMs will consume frequently

Poor fit:

- Simple flat information (single README suffices)
- One-time use
- No structured metadata needed

## Promotion Signals

Promote a single `.md` to a `.kb/` directory when any of these signals is
present:

- Plural filename -- `patterns.md`, `providers.md`, `alternatives.md`. The
  name signals a listing; the directory shape should follow.
- Parallel sections of the same type -- multiple `##` or `###` headings
  describing items of the same kind, even in prose form. Each section is one
  item; they belong in a `.kb/` as separate files. This applies regardless of
  whether the prose itself contains bullet lists.
- Listing-heavy content -- most of the file is a numbered list, table, or
  parallel enumeration of homogeneous items.
- Per-item growth pressure -- each item wants its own paragraph, frontmatter,
  or lifecycle (status, why:, last-updated), or any single item exceeds ~50
  tokens of explanation.

When you notice these, promote:

1. `$name.md` → `$singular.kb/` directory (rename to singular).
2. Each listed item → its own `.md` inside.
3. The former file's non-listing prose → either `$singular.md` (summary at
   parent scope) or `$singular.kb/CLAUDE.md` (maintenance guide for the new
   collection).

A fixed 2-4-item list of one-line entries is fine as prose. The signal is
*growth pressure*, not the mere presence of a list. Bullet lists for
short reference material (glossaries, shorthand) are also fine; the rule
targets parallel descriptions of items, not all uses of list syntax.

## Creating a Collection

When creating a `.kb` from scratch, **read `references/creating-a-new-kb.md`
before writing files.** It contains the full procedure and the four quality
passes (enumerate-and-categorize, persistence, per-file scope, schema
potential). The summary procedure here is for orientation only:

1. Ensure root CLAUDE.md meets requirements (see Maintenance Guides above)
2. Identify homogeneous categories → `$CATEGORY.kb/` directories
3. Design schemas for frontmatter → `$CATEGORY.jsonschema.yaml` (if using frontmatter)
4. Create per-directory CLAUDE.md guides
5. Create summary files (`$CATEGORY.md`) where they help
6. Populate content files
7. Validate with `bin/llm.kb-validate <path>`

## Reading Collections

Use category directories as query filters. Load entire categories in one
operation to save tokens and time:

```bash
head -n999 $CATEGORY.kb/*.md          # All items in category
head -n999 $CATEGORY.kb/**/*.md       # Including nested
grep -l "keyword" $CATEGORY.kb/*.md   # Search within category
```

This exploits small focused files -- loading 5 related files is faster than
searching one 500-line file.

## Tools Provided

### bin/llm.kb-validate

Purpose: catch frontmatter schema violations (error prevention).

Why offered: manual validation is error-prone and wastes tokens debugging
schema mismatches.

Usage:

```bash
bin/llm.kb-validate                  # Validate current directory (default)
bin/llm.kb-validate path/to/project  # Validate specific directory
bin/llm.kb-validate category.kb/     # Validate one category
bin/llm.kb-validate file.md          # Validate single file
```

Recursively finds and validates `.kb/` directories. Auto-detects schemas. Skips CLAUDE.md files.

Recommended: run `bin/llm.kb-validate` before committing changes.

## References

When creating a `.kb` from scratch, you must read
`references/creating-a-new-kb.md` before writing files.

Other references, load as relevant:

- `references/pattern-guide.md` - Complete pattern explanation
- `references/schema-design.md` - Schema design guidance
- `references/complete-example.md` - Worked example (birthday party planning)
- `references/splitting-large-docs.md` - Splitting heuristics

## Methodology kb (self-applied)

`docs/dev/` contains pre-distilled methodology this skill applies to itself:

- `procedures.kb/` -- step-by-step methods for recurring kb tasks
- `case-studies.kb/` -- narratives from instructive failures
- `concepts.kb/` -- structured definitions of recurring terms

`ls -RF docs/dev/procedures.kb/` lists procedures by task-shaped filename
(`post-mortem.md`, not `error-recovery-method.md`). Load one when its task
matches the user's request. Cross-referenced sibling collections
(`failure-modes.kb/`, `principles.kb/`, `glossary.kb/`) are seeded by
procedures as they're run; consult those when procedure files reference them.
