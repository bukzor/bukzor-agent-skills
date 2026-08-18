---
filename: docs/dev/devlog/YYYY-MM-DD-NNN-slug.md
audience: Future sessions
purpose: Narrative third place — process and decision-making that fit neither code comments nor commit messages
---

# devlog/ (The "When")

**Audience:** Future you, future Claude sessions

**Purpose:** The third place for narrative documentation of process — what
fits neither a code comment (it is not about the extant code) nor a commit
message (it spans or outlives one change): the concerns at hand, the
discussion and decision-making surrounding a change. Captures what diffs
can't — reasoning, principles, conventions.

**Must contain:**
- Decisions and their rationale (especially rejected alternatives)
- Conventions established and principles discovered
- Tradeoffs that shaped the approach

**Integration with task tracking:** Devlogs document work history. For active task tracking ("what's next"), use the subtask skill.

**File naming:** `YYYY-MM-DD-NNN-slug.md`
- `NNN` - Auto-incrementing 3-digit sequence (000, 001, ...)
- `slug` - Lowercase hyphenated title (e.g., `claude-md-instruction-optimization`)

**Create via:** `llm-collab-devlog --title "Entry title"` (add `-C <dir>` to target another directory)

**Templates:**
- [skeleton/docs/dev/devlog/YYYY-MM-DD-000-example-entry.md](../../skeleton/docs/dev/devlog/YYYY-MM-DD-000-example-entry.md)
- [skeleton/docs/dev/devlog/CLAUDE.md](../../skeleton/docs/dev/devlog/CLAUDE.md) - Directory guide
