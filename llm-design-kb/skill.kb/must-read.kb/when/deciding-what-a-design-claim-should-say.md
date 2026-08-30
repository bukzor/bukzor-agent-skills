# When deciding what a design claim should say

Five authorship lenses, in `../../principles.kb/`. They are about how
any design record is written, not about what any one project decided,
so they apply to a record you did not write as readily as to one you
are drafting. Read the ones whose occasion you are in:

- **`state-properties-not-mechanisms.md`** -- you are writing a
  requirement or an architecture claim and reaching for *how* it works.
  The rung below is where mechanism goes; confinement will report it
  if you don't.
- **`evaluate-uses-independently.md`** -- you are about to keep,
  change, or retire something that serves more than one purpose.
  Enumerate the uses first; a single verdict on a bundle is wrong for
  at least one of them.
- **`shared-shape-separate-semantics.md`** -- two collections look
  alike and merging them is tempting. Share the shape, not the
  identity.
- **`test-the-residue-not-the-bundle.md`** -- you are asking whether
  something should exist. Ask what remains once its substitutes are
  accounted for.
- **`regression-proof-with-principles-not-narrative.md`** -- you found
  an error in an entry and want to explain it in the entry. Sharpen
  the claim instead; the narrative is the devlog's.
