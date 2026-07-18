# Complete Example

A working example lives at `complete-example/` in this skill directory.

## Scenario

Planning an 8-year-old's birthday party. The domain requires no technical
knowledge yet admits substantial decomposition: guests, food, games,
decorations, timeline.

## What to Notice

Nested decomposition: `food.kb/cake.kb/` demonstrates when a subcategory
warrants its own directory. Cake decisions (flavor, frosting, decorations) are
independent concerns that would clutter the parent directory.

Synthesis sibling for nested directories: `food.kb/cake.md` rolls up
`food.kb/cake.kb/` in a form suitable as a `food.kb/` member. It uses the same
frontmatter schema as `main-dishes.md` and `snacks.md`, so someone reading
`food.kb/` sees cake at the appropriate level without diving into `cake.kb/`.

Cross-cutting constraints: Emma's peanut allergy appears in `guests.kb/`
but affects decisions throughout `food.kb/`. The root CLAUDE.md flags this.

CLAUDE.md at each level: Each directory has guidance for what belongs
there and what doesn't. An agent can read `food.kb/CLAUDE.md` and know
immediately whether "paper plates" belongs here (no - that's `decorations.kb/`).

Schemas document frontmatter: Each `.jsonschema.yaml` file includes
`description:` entries that explain what each field means. Agents read the
schema to understand the data model, not redundant documentation in CLAUDE.md.

Synthesis files for overview: `decorations.md` rolls up theme and budget
without diving into individual items. Unlike `cake.md` (which is also a
`food.kb/` member), `decorations.md` sits at the root as a pure overview.

Schema reuse via `$ref`: `decorations.jsonschema.yaml` and
`food.jsonschema.yaml` both need a `status`/`budget` pair; `food.kb/cake.jsonschema.yaml`
needs `status` alone. Rather than duplicate those field definitions,
all three `$ref` shared files in `jsonschema/` (`jsonschema/status.jsonschema.yaml`,
`jsonschema/budget.jsonschema.yaml`) -- file-relative, no fragment. See
`references/schema-reuse.md` for the general pattern.

## Exploring

```bash
# See the structure
find complete-example -type f -name '*.md' | head -20

# Read all CLAUDE.md files to understand organization
cat complete-example/**/CLAUDE.md

# See how constraints propagate
grep -r "peanut" complete-example/
```
