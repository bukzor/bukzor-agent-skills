# llm-collab owns peer-session coordination

**Date:** 2026-09-19
**Status:** Proposed -- the reclaim of the `llm-collab` name and the
protocol's content are agent-authored from the owner's framing
("cross-pollination ... without burning rubber sending messages willy
nilly"; "perhaps we should reclaim that name"). Vetoable.

## Context

Several claude-code sessions were live at once on overlapping work.
The owner wanted findings to cross between them without a message
mesh. A prior session had already audited the message channel
(`~/.claude/sessions.kb/penguin.kb/decide-the-inbound-peer-message-channel.md`,
2026-08-13): three inbound messages cost a third of a context window,
the owner called the channel "uncontrollable", and the session's
recommendation -- keep the repo as the bus; treat an inbound message
as a ticket -- was "not persisted anywhere enforceable."

`llm-collab` existed as "LLM-Collaborative Documentation": ADR and
devlog patterns, a skeleton, helper scripts, and a `references.kb/`.
Its description fired only on ADR/devlog writing. Its body was ~200
lines, paid in full on every load.

## Decision

1. `llm-collab` is the domain *collaboration among agents and humans
   across sessions*. The sequential case (baton-passing in time) and
   the concurrent case (peers live at once) are two occasions in one
   domain, not two skills (`authorship.kb/one-skill-beats-two-that-overlap.md`,
   `skills-are-domains-occasions-are-triggers.md`).
2. The body is a stance (standing, able-to-say, precedence) plus the
   bank stanza. Occasion-gated content moves to
   `skill.kb/must-read.kb/`:
   - `before/writing-an-ADR-or-devlog-entry.md` -- the incumbent body,
     paths corrected, marketing sections dropped.
   - `when/peer-sessions-work-overlapping-ground.md` -- the digest is
     the `sessions.kb/` entry; pull at checkpoints; contradictions go
     to the user; fan-in for dense overlap.
   - `before/sending-a-peer-message.md` -- three admissible kinds
     (pointer, conflict, hand-off); one per peer per checkpoint;
     delivery is not uptake.
   - `after/receiving-a-peer-message.md` -- ticket, not conversation.
3. The description names the founding occasions in the owner's words:
   related sessions live, cross-pollinating, a peer message arriving
   or about to be sent, and the ADR/devlog clause unchanged.

## Incumbent parts and their fates

| Part | Placement | Name | Route | Schedule |
|---|---|---|---|---|
| description's ADR/devlog clause | kept in description | kept | none needed | now |
| principles 1-6 | `before/writing-an-ADR-or-devlog-entry.md` | kept | bank listing on load | now |
| Quick Reference, Detailed References | same entry, paths made relative to skill root | kept | same | now |
| Status / Adaptation Guidelines / Success Indicators / Design Goals | nowhere -- obviated: they addressed a reader deciding whether to adopt, which the description already settles | -- | none: no invoker acts on them | now |
| `<https:references.kb/...>` links | rewritten as paths | -- | -- | now |
| `bin/`, `skeleton/`, `references.kb/`, `.claude/` | untouched | -- | -- | -- |
| deeper reform of the ADR/devlog entry (stance form, trim) | -- | -- | -- | later, on a tripwire: the entry misfires or an invoker complains of its length |

## Alternatives Considered

### New skill `llm-peer-collab` (or `claude-peer-collab`)
- **Pros:** no reform of the incumbent; smaller diff.
- **Cons:** two skills named collab; an invoker decides which before
  reading either. `claude-` prefix is wrong too: only the mechanics
  section is Claude-Code-specific, and it is named as situational.

### Personal `~/.claude/must-read.kb/` entries, no skill
- **Pros:** binds every session without a load.
- **Cons:** not portable to the fleet; the 2026-08-13 session named
  this home and it never happened, which is evidence the personal bank
  is not where the fleet's protocols get written.

### A new digest file format for peers
- **Cons:** `sessions.kb/` entries already are the per-session digest
  the owner reads; a second file per session is a second thing to keep
  current.

## Consequences

**Positive:**
- The 2026-08-13 protocol has an enforceable home.
- `llm-collab` loads at ~40 lines instead of ~200; ADR guidance is paid
  only when the ADR occasion fires.

**Negative:**
- Per-session digests now carry a peer-facing burden (findings as
  signed claims, overlap, wants) that `sessions.kb/CLAUDE.md` and
  `.template.md` do not yet mention. Follow-up in that repo.
- `ListAgents`, `SendMessage`, `notify_when_idle` are named in the
  bank; a consumer on another harness reads them as situational.

## Related

- `~/.claude/sessions.kb/penguin.kb/decide-the-inbound-peer-message-channel.md`
- `~/.claude/CLAUDE.md`, "Standing Defaults": durable deliberation
  lives in the filesystem -- the same rule, applied to agents.
- `2026-08-28-000-A-skill-states-a-stance--not-a-procedure.md`
