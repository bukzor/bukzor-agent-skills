---
name: llm-must-read-kb
description: "Agent MUST load for must-read.kb/ directories and prescribed-access trigger banks"
---
--- # workaround: anthropics/claude-code#13005
setup: |
    Adopting a `must-read.kb/` requires TWO things in the host CLAUDE.md.

    1. Frontmatter declaring the dependency:

    ```yaml
    --- # workaround: anthropics/claude-code#13003
    depends:
        - Skill(llm-must-read-kb)
    ```

    2. A "Required Reading" stanza wiring the agent to the trigger bank.
       See "Adoption" in the skill body for the exact text.
---

# Must-Read Trigger Banks

Extends `Skill(llm-kb)` with a **prescribed access pattern**: a `.kb/`
whose entries are consulted by *triggered conditional read*, not by free
query. Filename names the trigger; body holds the directives.

A plain `.kb/` is access-pattern-agnostic — readers decide when and how
to load. A `must-read.kb/` is not: the host CLAUDE.md instructs the
agent to scan filenames during planning, match them against the current
situation, and read matched bodies before the named action.

## The Innovation: Prescribed Access

The pattern works because filenames are *cheap to scan* and *expensive
to ignore*:

1. Agent runs `ls -RF must-read.kb/` once at session start.
2. The listing becomes a passive index of all trigger conditions.
3. Before any action (and continuously while planning), the agent
   mentally walks the listing and asks: *does any trigger fire here?*
4. On match, the agent reads that file's body and applies it before
   proceeding.

No tool-call hook, no startup tax beyond the `ls`. Bodies stay unloaded
until their trigger fires. The directory IS the index.

## Anatomy

```
must-read.kb/
├── before/
│   └── $TRIGGER.md         ─ read+act BEFORE the named action
├── after/
│   └── $TRIGGER.md         ─ read AFTER the named event completes
└── when/
    └── $TRIGGER.md         ─ read WHEN the situational match fires
```

All three subdirs are optional. Topical sub-grouping is allowed when a
trigger family grows (see "Nesting").

## Trigger Junctures

The three subdirs encode *when* the read fires. Pick by the directive's
relationship to the named situation:

| Subdir | Semantics | Example |
|---|---|---|
| `before/` | Hard precondition. Read MUST complete *and* prescribed actions MUST run before the named action. | `before/ANY-shell-commands.md` |
| `after/` | Read on completion of the named event. Typically for cleanup, audits, or post-mortems. | `after/an-unexpected-Bash()-tool-call-failure.md` |
| `when/` | Read when a situational predicate holds mid-task. Fuzzier triggers. | `when/evaluating-a-contested-or-subjective-position.md` |

`before/` creates an action dependency: the read is sequenced *before*
the triggered action — not parallel, not deferred.

## Trigger File Format

Each file is a small markdown directive. Recommended template:

```markdown
# {Before|After|When} {restated trigger}

{1–2 sentences naming the situation in author's own words. Helps the
agent confirm the match before reading further.}

## {Directive section(s)}

{Rules, examples, anti-patterns. Code blocks where useful.}

## When NOT to trigger   ← recommended for `when/`, optional elsewhere

- {edge cases that look like the trigger but aren't}
```

**Conventions:**

- **H1 restates the trigger** with the juncture verb (`# Before X`,
  `# After X`, `# When X`). Files are often opened standalone; the H1
  must self-orient the reader.
- **Keep bodies short.** A trigger file that exceeds ~50 lines is a
  signal that the method belongs in a shared `procedures.kb/` (see
  "Composition with procedures.kb/").
- **State the trigger condition in prose**, even though the filename
  encodes it. Filenames slug; bodies disambiguate.

## Naming

Filename + parent-dir verb = full trigger phrase.

```
before/ANY-shell-commands.md          →  "Before ANY shell commands"
when/cwd-starts-with-wsl.localhost.md →  "When cwd starts with wsl.localhost"
after/distilling-from-a-raw-source.md →  "After distilling from a raw source"
```

Rules:

- Kebab-case slug; descriptive enough that filename alone signals match.
- Use `ANY-` prefix for unconditional triggers within a juncture (e.g.
  `before/ANY-shell-commands.md` fires for every shell command).
- Verb tense in the slug should compose with the juncture: `before/`
  pairs with gerunds (`making-code-changes`), `after/` with nouns or
  past events (`an-unexpected-Bash-failure`), `when/` with predicates
  (`user-instructions-are-inconsistent`).

## Nesting

Topical subdirs are allowed when a trigger family grows past ~3 files:

```
must-read.kb/before/git/
must-read.kb/before/git/ANY-git-command.md
must-read.kb/before/git/commit.md
must-read.kb/before/lazy-loading/
must-read.kb/before/lazy-loading/skills.md
must-read.kb/before/lazy-loading/commands.md
```

The juncture verb (`before`/`after`/`when`) stays at the top; nested
dirs add a topic axis. Don't sub-nest `.kb/` directories — the trigger
slug, not the directory shape, carries the categorization.

## Aliasing

When one body serves multiple triggers, symlink:

```
before/contradicting-a-previous-response.md
  → ../when/evaluating-a-contested-or-subjective-position.md
```

Both filenames remain individually scannable in the index; the body
lives in one place. Prefer symlinks over duplication; duplication drifts.

## Composition with `procedures.kb/`

When a trigger's method is shared across triggers, or long enough to
deserve its own file, factor it out:

```
SKILL.kb/
├── must-read/
│   ├── before/marking-kb-work-done.md   ─ "run the validation pass"
│   └── after/creating-or-editing-kb-files.md  ─ "run the audit pass"
└── procedures.kb/
    ├── self-audit.kb/
    │   ├── audit-claudemd-enumeration.md
    │   └── audit-per-file-scope.md
    └── validation.md
```

Trigger file says **when**; procedure file says **how**. The trigger
references the procedure by path. Multiple triggers can reference one
procedure (deduplication).

## Scopes (Homes)

The pattern installs at three scopes:

| Scope | Location | Purpose |
|---|---|---|
| Personal | `~/.claude/must-read.kb/` | User's own rules across all projects |
| Project | `$REPO/.claude/must-read.kb/` | Project-specific triggers, versioned with the code |
| Skill | `$SKILL/SKILL.kb/must-read.kb/` | Triggers bundled with a skill; consumers inherit them on load |

All three coexist; each scope ships its own `must-read.kb/`. The agent
scans every reachable one during planning. Same-named triggers across
scopes are not deduplicated — each trigger file is independent.

> **Open question (deferred):** the existing personal home is
> `~/.claude/must-read.d/` and the existing skill-level home is
> `SKILL.kb/must-read/` (no `.kb` suffix). Migration to
> `must-read.kb/` is pending; this skill prescribes the target name.

## Adoption

Each scope's host CLAUDE.md needs a "Required Reading" stanza. The
canonical text:

```markdown
# Required Reading

> IMPERATIVE:
>
> Your FIRST action in every conversation MUST be:
> `Bash("ls -RF $PATH/must-read.kb")`

While planning, before taking ANY action:

1. Mentally review the must-read paths — filenames specify when to
   read each file.
2. Evaluate whether any of the triggers match your situation.
3. When a trigger condition matches, you MUST read that file.
   - `before/` creates a dependency: the read MUST complete before
     related actions. These operations are NOT independent — they
     MUST be executed sequentially.

> WARNING: You WILL FAIL your tasks if you do not properly make use
> of these files.
```

`$PATH` is whichever scope's `must-read.kb/` this CLAUDE.md governs.
For a personal home, hardcode the absolute path. For a project or
skill home, the relative path suffices.

## When to Use

Good fit:

- Rules that apply only to *some* actions, not all sessions.
- Directives the agent forgets when not foregrounded.
- Conventions whose full text is too large to inline in CLAUDE.md.
- Cross-cutting concerns (shell hygiene, commit etiquette, language
  style) that fire in many contexts.

Poor fit:

- One-shot project orientation → put in CLAUDE.md directly.
- Decision rationale or history → use ADR (`Skill(llm-collab)`).
- Living design knowledge → use `design.kb/` (`Skill(llm-design-kb)`).
- Always-applicable rules → inline in CLAUDE.md; trigger banks add
  overhead the agent must traverse every plan.

## Relationship to `Skill(llm-kb)`

A `must-read.kb/` is a regular `.kb/` — same naming, promotion, and
maintenance rules apply. This skill **specializes** the parent pattern
by:

1. Fixing the top-level structure (`before/`/`after/`/`when/`
   subdirs).
2. Prescribing the access pattern (scan-and-trigger, not free query).
3. Treating filenames as the index, not just identifiers.

When the prescribed access pattern is not wanted, use a plain `.kb/`
instead. The two are not interchangeable: a regular `.kb/` will not be
read on the trigger cadence, and a `must-read.kb/` is overkill for
content readers will query on their own.
