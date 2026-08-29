# Persisting the reviewed ledger

You arrive here with a reviewed ledger (`../SKILL.md`: encode, then
review). This file maps it onto disk. The invariant: every claim,
open, and residue ends the session in a home a cold agent will find,
and the operation ends at a commit — uncommitted clarity is one crash
from gone.

## Filing stance

Work with what disk already holds — verify, amend, reword, sharpen;
mint as a last resort. Prefer the homes that already exist; where a
residue has none, mint the smallest one that holds it — a single file
beats a structure, and either beats evaporation. What's banned is only the *parallel* home:
a second place for something that already has a place — the two
drift, and the reader trusts the wrong one.

## Homes, by ecosystem

- Claims-ledger projects (`Skill(llm-claims-kb)`): the mapping is
  that skill's table — standing to `standing:`, strikes to `verdict:`
  with the ground and the acceptance quoted in `authority:`, arrows
  to `why:`; the roll-up carries the re-entry section.
  `Skill(llm-claims)`'s session-ending rule already obliges this
  serialization — this operation adds the rest.
- Session-register projects (`Skill(llm-sessions)`, discussion
  registers): the register entry is the narrative address — a pointer
  plus the name, not a second copy.
- Plain projects: ADRs hold results, and their "options considered"
  section holds reversals; README or HACKING holds lenses; the
  tracker holds discharge routes.

## Where each residue lands

- **Results and reversals** — a decision record: claims ledger, ADR,
  design doc. Reversals land *beside the winner* — the decision-point
  shape (`skill://llm-kb#decision-points`): `$ITEM.md` states the
  resolution and why, `$ITEM.kb/` holds one file per candidate,
  chosen and declined alike.
- **Lenses** — the project's methodology home (playbook, HACKING, a
  principles file), each citing the session's own artifact as its
  worked instance.
- **Opens** — a discharge route apiece, in the project's task system:
  the task, its trigger if it's dormant, and where its context lives.
  An open without a route is a decision silently delegated to
  amnesia.
- **The narrative address** — a pointer to where the full story can
  be re-mined: session id, transcript, PR, register entry, incident
  doc. A pointer, never a copy.

## The re-entry path

Written last — it indexes everything filed above. Fluency is
restorable, not storable, so this is a **reading order for a cold
agent**: what to load, in what sequence, placed where that agent will
look first (the roll-up, the README, the CLAUDE.md). Include the
warning that the struck and declined records are load-bearing, not
debris; a cold reader skips them by instinct and then re-litigates
them by accident.

## Verify, then commit

Follow your own re-entry path reading only what's on disk; anywhere
you reach for something missing, that is the gap. A project's own
health gate (frontmatter validation, quote and link checking) covers
the mechanical half; the reading-order half is yours alone. Then
commit.

## Anti-patterns

- **The narrative dump.** A transcript-shaped copy nobody will
  reload; the address beats it at a thousandth the size.
- **Persisting the journey as the state.** Render the final framing;
  the journey lives in the reversals and at the address.
- **Polishing the persisted.** Anything already on disk can be
  sharpened later, by anyone; spend the wrap-up on what only this
  session holds.
