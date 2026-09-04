# A trigger commands loading only; the bootstrap reads must-read://SCOPE

**Date:** 2026-09-04
**Status:** Accepted -- the stanza text and the `must-read://` spelling
are the owner's rulings (2026-09-04, drafting session in
`~/claude/triggers/`). The rationale for declining a `run:` directive
is agent-authored, from a debate the owner set up and took the con
side of; it stands vetoable.

## Context

The "Required Reading" stanza every host CLAUDE.md carries was
imperative prose: a FIRST-action `ls -RF` order, a numbered
review-the-banks procedure, and a warning. The owner rewrote it as a
vocabulary -- four definitions (occasion, trigger, installed, `before`)
and a list of the sources triggers arrive from -- and spelled the
bootstrap in the shape of a `triggers:` entry:

```
- before: your first tool call
  action: Bash("llm-must-read-ls ~")
```

`action:` is not a key the field has. `triggers-field.md` specifies one
directive, `read:`, and `kb-spec.md` calls it "the only load
directive". Conforming the bootstrap therefore forced the question the
owner put directly:

> "there's no syntax to specify a script, a tool call?"
> "i want to directly give a CLI command/tool call as the action"

and, once a scheme was on the table:

> "is it so very different from: read: Bash(llm-must-read-ls ~)"

## Decision

1. The stanza is a vocabulary. Its lead is one obligation ("Continually
   monitor for installed triggers' occasions; take the action when one
   arrives"); a Definitions section carries the terms; an Installation
   section lists the sources. Canonical text: `llm-must-read-kb/SKILL.md`,
   "Adoption". Rationale clauses were struck: they only strengthen the
   normative, and the owner ruled that the instruction suffices.
2. The bootstrap is a load: `read: must-read://$SCOPE`. The scheme's
   floor meaning is a definition in the stanza itself:
   `must-read://DIR` means `Bash(llm-must-read-ls DIR)`. `$SCOPE` is `~`
   for a personal home, `.` for a project.
3. `read:` remains the only directive. No `run:`, and no `Bash(...)`
   handle as a read target.
4. `llm-triggers-lint` accepts a hyphen in a scheme name (`[\w-]+://`);
   it had spelled schemes as `\w+` and fell through to path resolution.

## Alternatives Considered

### `run:` directive, system-evaluated
- **Pros:** one hop from occasion to command; evaluable by a hook rather
  than by the agent, which is more deterministic; matches the runtime's
  own primitive (a hook is a condition and a command).
- **Cons:** see Rationale. Also passes the floor test -- an agent can
  interpret it -- so the floor is not what excludes it.

### `read: Bash(llm-must-read-ls ~)`
- **Pros:** lints clean today (the handle regex accepts any `Word(...)`
  and skips resolution); no scheme to teach.
- **Cons:** the same as `run:` under mechanical evaluation, since the
  target is a shell string; the lint acceptance is a regex accident, not
  a sanctioned form.

### `read: ~/.claude/must-read.kb/` (a directory target)
- **Pros:** no new syntax at all.
- **Cons:** underdefined -- "read a directory" could mean every file, and
  the reader would be inferred from the path's shape, which the owner
  named as code-as-prompt.

### `bank://DIR`
- Identical in mechanism to `must-read://DIR`; the owner's name matches
  the bank and the lister, and takes the lister's own search-root
  argument.

### Leave `action:` as prose
- Nothing lints it. It only resembled the syntax.

## Rationale (agent-authored, vetoable)

At the floor, in a trusted CLAUDE.md, today, `must-read://~` and
`Bash(llm-must-read-ls ~)` are the same: same tool call, one line of
teaching either way. The difference is two properties.

- **Parameter, not program.** In `must-read://X`, X is data handed to
  one fixed, user-owned, read-only reader. In `Bash(cmd)`, cmd is a
  program. Triggers are content: they ride in cloned repos and installed
  plugins. A hook that evaluates the first from any carrier can only
  list; a hook that evaluates the second can do anything, with no model
  and no permission prompt in the loop. Commands are config; hooks are
  where config runs commands. The property holds only if a shim passes X
  as an argument vector, never through a shell.
- **Meaning outlives mechanism.** The scheme says what is wanted. Rename
  the lister, or land on a consumer without it, and the trigger still
  means the same thing and any reader can satisfy it, including a hook
  that already injected the result. `Bash(...)` says how; when the how
  is gone, so is the trigger. The same property is why one can be linted
  for a directory that exists and the other cannot.

Disconfirmers, recorded so the ruling can be revisited on evidence:

- If the adapter never ships, the first property buys nothing and the
  scheme is an indirection paid for a future. `Bash()` would then be the
  more honest spelling.
- If per-purpose hooks ("inject the date", "inject git status")
  proliferate in settings.json, "one authoring format" has become false
  and `run:` earns its place. Count on 2026-09-04: two hooks, both
  generic infrastructure (Bash preamble, session-start binpatch).

Two corrections made during the debate, kept here so they are not
re-derived: the adapter binding for "before your first tool call" is a
PreToolUse shim gated on the first call, not SessionStart -- a
`claude --print` question makes no tool call, so the condition never
holds there and SessionStart would over-fire on arrival. Re-injecting
the index after compaction is a distinct trigger (`after: compaction`),
not a virtue of binding this one early.

## Consequences

**Positive:**
- The bootstrap is in the field's syntax and lints.
- One directive survives; the safety boundary between content and
  config is explicit and named.
- The stanza dropped from about 1000 bytes of imperative prose to 841
  bytes of vocabulary, in the hottest text the fleet loads.

**Negative:**
- An arbitrary command at an arbitrary occasion costs two hops: a
  trigger that reads a body, and a body that says run it.
- `llm-must-read-ls` lives in the owner's `~/bin`, not in this skill; an
  adopter of the canonical stanza does not get its reader. The Adoption
  text says so and names `ls -RF` as the same index. Follow-up: ship it
  under `llm-must-read-kb/bin/`, mirroring `llm-triggers/bin/`.

**Neutral:**
- A project CLAUDE.md loaded alongside a personal one that already
  carries the stanza needs only one frontmatter entry
  (`before: your first tool call` / `read: must-read://.`), since the
  definitions are already installed. Not yet ruled; the Adoption text
  still gives the full stanza for every scope.
- `bank-format.md` still names `ls -RF` as the listing command. Whether
  it should name the lister instead is open.

## Related

- `llm-triggers/design.kb/040-design.kb/triggers-field.md` -- the one
  directive.
- `llm-triggers/design.kb/040-design.kb/floor.md`,
  `condition-vocabulary.md`, `claude-code-adapter.md`.
- `design-next.kb/040-design.kb/kb-spec.md` -- "the only load directive".
- ad8001e (2026-09-04) -- a trigger binds from its listing onward; the
  prior stanza change.
- `~/.claude/CLAUDE.md`, "Required Reading: Triggers" -- the deployed
  instance.
