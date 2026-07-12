---
why:
  - session-continuity
  - authorship-boundary
trigger: Engine core (new/validate/promote/doctor) has landed and is in daily use.
---

# Transcript Distillation

V1's `llm-chat-librarian` pipeline (digest → survey → segment →
assess → extract → index) becomes an engine capability: turning raw
conversation exports and oversized session transcripts into kb
entries with provenance. Same for the post-mortem flow (incident →
distilled failure-modes/principles).

Distilled output is Claude-authored by definition, so every extracted
entry carries provenance frontmatter (source, endorsement) per the
authorship boundary — extraction surfaces candidates; the operator's
acceptance is what promotes them to knowledge.
