#!/bin/bash
# validate.sh: find em-dash characters (U+2014) in inventory-visible
# markdown files. Read-only.
#
# Excludes session logs, .git/, node_modules/, and trash/.

set -uo pipefail

ROOTS=("$HOME/repo/github.com/bukzor" "$HOME/.claude" "$HOME/claude")

grep -rnP --include='*.md' --include='*.txt' '\x{2014}' "${ROOTS[@]}" 2>/dev/null | \
  grep -vE '/\.git/|/node_modules/|/\.claude/projects/|/\.claude/file-history/|/trash/'
