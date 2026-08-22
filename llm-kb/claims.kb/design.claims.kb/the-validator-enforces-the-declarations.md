---
label: VALIDATE_ENFORCES
standing: user
why:
  - explicit-and-positional-must-agree.md
  - should-the-modeline-and-the-schema-key-agree.md
authority: "user, 2026-08-22: 'seems like we might should add several checks to llm.kb-validate along these lines'"
---

# The Validator Enforces the Declarations

`llm.kb-validate` is where a declaration rule becomes a rule. A
convention nothing checks is a convention that has already drifted --
the 318 stale modelines are the proof, and they accumulated in a corpus
whose validator ran on every commit and had nothing to say about them.

Each declaration claim lands as one check:

- an explicit selector that disagrees with positional binding;
- a modeline and a `$schema` key that name different dialects;
- a schema file declaring no dialect, if DIALECT_DECLARED rules that
  it must.

The third waits on its claim. The first two do not: both are errors
under claims already signed, and neither needs the corpus cleaned
first, because a check that fires on existing files is how the backlog
gets counted.
