# When Editing a CLAUDE.md

You're writing or modifying any `CLAUDE.md` in a kb-using project.

Run both CLAUDE.md passes -- they catch complementary failures:

- **Enumeration** -- sections that duplicate `ls -RF`.
  `../../quality-passes.kb/claudemd-enumeration.md`.
- **Completeness** -- missing the rules a maintainer needs to make
  decisions (what belongs / what doesn't / when to add).
  `../../quality-passes.kb/claudemd-completeness.md`.

In short: a `CLAUDE.md` is a maintenance guide. It must tell a
maintainer what belongs and must not duplicate `ls`. The two passes
defend the two boundaries.
