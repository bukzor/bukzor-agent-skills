# When a design claim overlaps an ADR, a devlog, or a CLAUDE.md

Four records with four jobs. The overlap is real but the division is
clean, and the test is what a reader would come looking for:

- **The design ledger** holds what is *currently* true or committed,
  with its standing: who decided it and what it rests on. Present
  tense, or `todo:` for a decided future state.
- **An ADR** holds the record of one ruling -- its context, the
  options weighed, the date. A claim whose ruling has an ADR cites it
  as `authority:` rather than restating it.
- **A devlog** holds the narrative: what happened in a session, in
  what order, and what it felt like to find out. Nothing in the ledger
  should read as narrative; if a claim's prose has past-tense dated
  sentences, they belong here instead.
- **A CLAUDE.md** orients an agent arriving cold -- where things are,
  where a new file goes. It says what a claim cannot, and never
  duplicates one.

Two rules follow, and they are what this file is for:

- **Never copy a commitment between records.** Cite across instead.
  Two copies drift, and the reader trusts the wrong one.
- **A ruling recorded in an ADR still needs its claim.** The ADR says
  what was decided that day; the claim says what binds today. When a
  later ruling supersedes it, the claim gains a `verdict:` and the ADR
  stays exactly as written -- it was never wrong about its own day.

Whether the ledger's `verdict:` and `authority:` fields have made the
ADR redundant is an open question in this fleet, not settled here.
Keep writing both until it closes.
