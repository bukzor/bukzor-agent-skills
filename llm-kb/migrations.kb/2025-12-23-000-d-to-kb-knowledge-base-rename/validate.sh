#!/bin/bash
# validate.sh: list .d/ directories and hint at whether each should
# (probably) be a .kb/. Read-only; the user judges each case.
#
# Output format:
#   <hint>  <path>  <entry-count>
#
# Hint values:
#   kb-like        — contains YYYY-MM-DD-NNN-*.md files, or has sibling .kb/ dirs
#   config-like    — contains .conf/.cfg/.sh/.yaml without the date-prefix shape
#   template-like  — path includes template/skeleton/copier
#   unknown        — doesn't match the above

set -uo pipefail

ROOTS=("$HOME/repo" "$HOME/.claude" "$HOME/claude")

while IFS= read -r -d '' d; do
  # Skip subtrees we never want to consider
  case "$d" in
    */.git/*|*/node_modules/*|*/trash/*) continue;;
    *.kb/*|*.kb) continue;;  # already-kb
  esac

  count=$(find "$d" -maxdepth 1 -type f 2>/dev/null | wc -l)

  hint="unknown"
  case "$d" in
    */template*|*/skeleton*|*/copier*) hint="template-like" ;;
  esac

  if [[ "$hint" == "unknown" ]]; then
    # Date-prefixed entries → kb-like
    if find "$d" -maxdepth 1 -name '????-??-??-???-*.md' 2>/dev/null | head -1 | grep -q .; then
      hint="kb-like"
    fi
  fi

  if [[ "$hint" == "unknown" ]]; then
    parent=$(dirname "$d")
    if find "$parent" -maxdepth 1 -type d -name '*.kb' 2>/dev/null | head -1 | grep -q .; then
      hint="kb-like"
    fi
  fi

  if [[ "$hint" == "unknown" ]]; then
    # Look for non-markdown content suggesting config-style use
    if find "$d" -maxdepth 1 -type f \( -name '*.conf' -o -name '*.cfg' -o -name '*.sh' -o -name '*.yaml' -o -name '*.toml' \) 2>/dev/null | head -1 | grep -q .; then
      hint="config-like"
    fi
  fi

  printf '%-14s  %s  (%d entries)\n' "$hint" "$d" "$count"
done < <(find "${ROOTS[@]}" -type d -name '*.d' -print0 2>/dev/null) | sort
