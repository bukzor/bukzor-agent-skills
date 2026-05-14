# Self-audit: bloat

## Audience

**The reader is Claude.** Don't talk down. Skip what Claude already
knows: tool-flag semantics, common-usage commentary, generic
programming concepts, restated definitions, moral framing
("don't be sloppy"). Write as if briefing a peer.

**Identify *which* Claude.** Architectural notes ("X runs in a
separate agent," "this could be extracted later," "currently
overloaded with Y") belong in maintainer files, not in actor-facing
triggers and procedures.

## Goal

Each file states its point in the fewest lines that preserve clarity
for a Claude reader.

## Procedure

For each file you just wrote or edited:

> Could a Claude reader make the same correct decisions with fewer
> lines?

Look specifically for:

- Conversational intros that restate the title or the goal.
- Explanations of things Claude already knows (flag semantics,
  unix usage, restated definitions, "X is bad because Y").
- Audience mismatch: notes meant for a reader other than this
  file's audience.
- "What this is not" sections defending against misuse the
  procedure doesn't actually invite.
- Example menus where one in-line example would suffice.
- Recovery branches that restate the same fix under different
  headings.
- "Related" sections linking files that don't change the action.

## Recovery

Cut. Exception: audience-mismatched content **relocates** to a file
with the right audience (create the destination if absent). Don't
delete content that has no other home but needs an audience.

If a file still feels expansive after cutting, the trigger is
probably too abstract -- sharpen the question and the hedges fall
away.
