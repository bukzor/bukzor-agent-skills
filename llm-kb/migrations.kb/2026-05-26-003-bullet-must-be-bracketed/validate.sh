#!/bin/bash
# validate.sh: flag bare `-` bullets in inventoried task files.
# These bullets are invisible to claude-open-tasks-list and silently
# drop work from the prioritization queue.
#
# Read-only. Idempotent. Output format:
#   <path>:<line-no>:<content>
#
# A "bare bullet" is a line matching `^ *- [^[]` — dash-space followed
# by anything other than an opening bracket. Compliant lines like
# `- [ ]`, `- [x]`, `- [~]`, `- [-]` are excluded.

set -uo pipefail

# grep -P would be nicer but stay POSIX-ish: BRE with appropriate escapes.
# Pattern: ^[whitespace]*- [non-bracket] ... matches bare bullets only.
PATTERN='^ *- [^[]'

claude-open-tasks-list | grep '^## ' | sed 's/^## //' | \
  while IFS= read -r path; do
    [[ -f "$path" ]] || continue
    grep -nE "$PATTERN" "$path" 2>/dev/null | \
      sed "s|^|${path}:|"
  done
