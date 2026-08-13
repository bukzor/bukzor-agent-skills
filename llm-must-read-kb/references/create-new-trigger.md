# Creating a New Trigger File

Canonical procedure for adding one trigger to a `must-read.kb/`. Both
manual creation and the `/must-read` slash command follow these same
steps so they produce identical-shape artifacts. See `SKILL.md` for
the format this procedure produces; this file is the *how*, not the
*what*.

## Step 1: State the trigger condition in one sentence

Write the condition in plain prose first, independent of filenames or
juncture: "the agent is about to do X" / "X just happened" / "the
agent notices situation X mid-task." If you can't state it in one
sentence, it's not one trigger — split it.

This sentence becomes the body's opening line (see Step 5) and drives
Steps 2–3.

## Step 2: Pick the juncture

| The sentence says...                          | Juncture  |
|------------------------------------------------|-----------|
| "before/prevent the agent from doing X"         | `before/` |
| "after X happens/completes"                     | `after/`  |
| "when the agent notices/is in situation X"      | `when/`   |
| ambiguous, or reads as both a precondition and a situational check | ask (human) or default `when/` (command) |

Reference: `SKILL.md`'s "Trigger Junctures" table for the semantics of
each. `before/` is the strictest — it sequences a mandatory read+act
ahead of the triggered action, not just a suggestion.

## Step 3: Pick the scope (home)

| Scope    | Location                          | Choose when...                                  |
|----------|------------------------------------|--------------------------------------------------|
| Personal | `~/.claude/must-read.kb/`          | Rule applies across all projects, tied to the user's own habits/preferences. **Default.** |
| Project  | `$REPO/.claude/must-read.kb/`      | Rule is specific to this repo's conventions, versioned with its code. |
| Skill    | `$SKILL/SKILL.kb/must-read.kb/`    | Rule should bind every consumer of a skill, shipped with it. |

If invoked from inside a skill directory, don't infer skill scope
silently — skill-level triggers are sticky for every consumer and
should be a deliberate choice. Ask, or require an explicit flag.

## Step 4: Compose the filename slug

`{juncture}/{slug}.md`, optionally nested one topic level:
`{juncture}/{topic}/{slug}.md` once a topic family exceeds ~3 files
(see `SKILL.md` "Nesting").

Slug rules:

- Kebab-case, descriptive enough that the filename alone signals the
  match without opening the file.
- Verb form composes with the juncture — read the full trigger phrase
  aloud as `"{Before|After|When} {slug-with-dashes-as-spaces}"` and
  confirm it's a grammatical, self-orienting sentence:
  - `before/` → gerund or bare imperative-object: `making-code-changes`,
    `running-ANY-Bash-commands`
  - `after/` → noun phrase or past event: `an-unexpected-Bash()-tool-call-failure`
  - `when/` → predicate clause: `user-instructions-are-inconsistent-or-would-create-a-problem`
- Use an `ANY-` prefix when the trigger is unconditional within its
  juncture (fires for every instance of the action, not a specific
  case of it): `before/running-ANY-Bash-commands.md`.
- Check for an existing file with the same or overlapping condition
  before creating a new one (`ls` the juncture dir, or the topic
  subdir if nesting). If one exists and the new rule is really the
  same trigger with an additional directive, extend that file instead
  of creating a near-duplicate.
- Check whether the same body should also fire under a *different*
  phrasing (e.g., "before contradicting" and "when evaluating a
  contested claim" can be the same underlying rule). If so, this is an
  aliasing case — see Step 7 — not two independent files.

## Step 5: Write the body

Use this template:

```markdown
# {Before|After|When} {restated trigger, in the author's own words}

{1–2 sentences naming the situation. This is Step 1's sentence,
polished. Lets the agent confirm the match before reading further —
files are often opened standalone.}

## {Directive section(s)}

{Rules, examples, anti-patterns. Code blocks where useful. Keep this
concrete and actionable — a trigger file is consulted mid-task, not
studied.}

## When NOT to trigger

- {edge cases that look like a match but aren't}
```

The "When NOT to trigger" section is recommended for `when/` triggers
(their conditions are fuzzier and more prone to false positives) and
optional for `before/`/`after/` (their conditions are usually
unambiguous events).

**Length check:** if the body exceeds ~50 lines, stop and factor the
method out to a shared `procedures.kb/` file instead (see `SKILL.md`
"Composition with `procedures.kb/`"); the trigger file should say
*when*, a separate procedure file says *how*, and the trigger
references it by path. This keeps the directory scannable — a trigger
file is meant to be skimmed at plan time, not read in full every time.

## Step 6: Write the frontmatter

Two directives, both optional, per `Skill(llm-kb)`'s base convention
(this skill inherits rather than redefines them):

```yaml
---
requires:
    - path/to/file-that-must-be-read-first.md
depends:
    - Skill(some-skill)
---
```

- `requires:` — listed files/skills MUST be read before acting on
  *this* file's content. Use when the directive assumes background the
  agent might not have (e.g. a git commit trigger requiring the repo's
  git conventions doc first). Creates a hard sequencing dependency,
  same strength as the `before/` juncture itself.
- `depends:` — informational; read when relevant, not unconditionally
  required. Use for related-but-not-blocking context.
- Omit both if the body is fully self-contained.

## Step 7: Decide aliasing vs. new content

If Step 4 surfaced a case where the same body should fire under a
second trigger phrase, symlink rather than duplicate:

```bash
ln -s ../when/existing-trigger.md before/new-alias-name.md
```

Both filenames stay independently scannable in `ls -RF` output; the
body lives in one place and can't drift out of sync.

## Step 8: Verify

1. `ls -RF must-read.kb/` (or the relevant scope's equivalent) and
   confirm the new file appears where expected, correctly nested.
2. Read the new file cold, as if encountering it during planning for
   the first time: does the H1 alone let you confirm or reject a
   match without reading further? Does the body give a clear,
   executable action once matched?
3. If `requires:` was set, confirm every listed path/skill actually
   exists and is reachable from where an agent would be standing when
   the trigger fires.
4. If this created a new juncture-topic family (Step 4's nesting
   case), confirm the parent topic dir has no stray files left at the
   old flat location.

## Success criteria

- Exactly one new trigger file (or one new file + one new symlink, for
  aliasing) exists at the chosen scope and juncture.
- The filename + juncture read as a grammatical trigger phrase (Step
  4's self-check).
- The body matches the Step 5 template shape and is under ~50 lines.
- `requires:`/`depends:` are set only where genuinely needed, pointing
  at real, reachable targets.
