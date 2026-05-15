# Self-audit: bloat

## Frame

**The reader is Claude.** Bloat is anything Claude already knows or
that targets the wrong audience for this file.

- Skip tool-flag semantics, common-usage commentary, restated
  definitions, moral framing ("don't be sloppy"). Brief a peer.
- Identify *which* Claude. Architectural notes ("X runs in a
  separate agent," "this could be extracted later") target a
  maintainer; runtime triggers and procedures target the actor.
  Misaddressed content is bloat at the wrong file even when it's
  earning its keep at the right one.

## Goal

Each file states its point in the fewest lines that preserve clarity
for its intended Claude reader.

## Procedure

For each file you just wrote or edited:

> Could a Claude reader at this file's audience make the same
> correct decisions with fewer lines?

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
