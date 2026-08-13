# Stub a Missing Entry

When a kb file needs to reference something that doesn't exist yet -- a
concept, glossary entry, failure mode, principle, procedure -- the
correct response is to **stub** the missing entry rather than expanding
it fully or leaving the reference dangling.

## Goal

Every reference resolves; no cross-link cascade dominates the session.

## Procedure

1. Identify the target collection. A concept (a *thing* with shape)
   → `concepts.kb/`. A one-line word-to-meaning entry → `glossary.kb/`.
   A procedure → `procedures.kb/`. A principle → `principles.kb/`. Etc.

2. Create the collection if needed. Single-entry kb collections are
   fine; growth justifies more structure later. Include a `CLAUDE.md`
   describing what belongs (per the SKILL.md pattern).

3. Write the stub. One-line meaning + `TODO: expand`. Example:

   ```markdown
   # Concept: foo-bar

   The thing that happens when X meets Y under condition Z.

   TODO: expand once a second instance surfaces.
   ```

4. Verify the original reference resolves (the path now points at
   an existing file).

## Cascade bounding

If the stub *itself* introduces references that don't exist yet:

- Cap at one level deep this session. Stub the immediate
  cross-refs. Note any deeper TODOs inside the stubs themselves.
- The next pass (or the next agent) walks one level further.

If you stub more than two or three entries in a session, drop a note
in `.claude/todo.md` so the deeper layers aren't forgotten.
