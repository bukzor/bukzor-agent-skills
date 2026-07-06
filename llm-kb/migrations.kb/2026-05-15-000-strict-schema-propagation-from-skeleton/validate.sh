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
    category="${schema%%.*}"   # todo | ideas
    if [[ ! -f "$dst" ]]; then
      # MISSING is only drift when the skill actually authors this
      # category. A consumer-only skill legitimately omits the schema.
      if [[ -d "$skill_claude/$category.kb" || -f "$skill_claude/$category.md" ]]; then
        printf 'MISSING %s\n' "$dst"
      fi
    elif ! diff -q "$src" "$dst" >/dev/null 2>&1; then
      printf 'DIFFER  %s\n' "$dst"
    fi
  done
done
