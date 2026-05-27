#!/bin/bash
# validate.sh: compare each skill's .claude/{todo,ideas}.jsonschema.yaml
# against the canonical skeleton; report MISSING or DIFFER.
#
# Read-only. Idempotent.

set -uo pipefail

SKILLS_ROOT="$HOME/repo/github.com/bukzor/bukzor-agent-skills"
SKEL="$SKILLS_ROOT/llm-subtask/skeleton/.claude"

for skill_claude in "$SKILLS_ROOT"/*/.claude; do
  # Skip skeleton itself (it IS the source of truth)
  case "$skill_claude" in
    "$SKILLS_ROOT/llm-subtask/skeleton/.claude") continue;;
  esac

  for schema in todo.jsonschema.yaml ideas.jsonschema.yaml; do
    src="$SKEL/$schema"
    dst="$skill_claude/$schema"
    [[ -f "$src" ]] || continue
    if [[ ! -f "$dst" ]]; then
      printf 'MISSING %s\n' "$dst"
    elif ! diff -q "$src" "$dst" >/dev/null 2>&1; then
      printf 'DIFFER  %s\n' "$dst"
    fi
  done
done
