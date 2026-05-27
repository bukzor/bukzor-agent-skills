#!/bin/bash
# validate.sh: report files where `<anthropic-skill-ownership ...>`
# appears as a declaration — anchored at line start, not embedded in
# prose or quoted as text.
#
# Excludes:
#   - ADRs (history; legitimate references)
#   - .claude/projects/ session logs (immutable transcripts)
#   - trash/ folders (backups, scratch)
#   - migrations.kb/ entries (this convention is itself the subject)
#
# Read-only. Idempotent.

set -uo pipefail

ROOTS=("$HOME/repo/github.com/bukzor" "$HOME/.claude" "$HOME/claude")

# `^<anthropic-skill-ownership` — at column 0 to exclude indented quotation.
grep -rlE '^<anthropic-skill-ownership' "${ROOTS[@]}" 2>/dev/null | \
  grep -vE '/docs/dev/adr/|/\.claude/projects/|/\.claude/file-history/|/trash/|/migrations\.kb/' | \
  grep -vE '\.swp$'
