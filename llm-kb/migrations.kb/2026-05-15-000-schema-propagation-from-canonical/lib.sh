# shellcheck shell=bash
# lib.sh: the category table, derived rather than declared.
#
# A category has a canonical exactly when the skills repo publishes
# <skill>/jsonschema/<category>.jsonschema.yaml. That file IS the
# registration -- there is no list to keep in sync, so publishing a
# canonical enrolls it in this guard and retiring one un-enrolls it.
#
# (Until 2026-08-21 this was a nine-row categories.tsv in the one-shot
# 2026-08-21-000 migration. It had fallen nine categories behind the
# filesystem, which is the failure mode a hand-maintained list has.)
#
# Callers must set HERE to this directory before sourcing.

export SKILLS_REPO="$HOME/repo/github.com/bukzor/bukzor-agent-skills"
# A plain stub uses only `$ref`, which means the same thing in every
# dialect, so it declares the better-tooled draft-07 meta-schema; see
# llm-kb/references/schema-reuse.md.
export MODELINE='# yaml-language-server: $schema=https://json-schema.org/draft-07/schema'

# category<TAB>skill, one row per published canonical.
table() {
  local f skill category
  for f in "$SKILLS_REPO"/*/jsonschema/*.jsonschema.yaml; do
    skill="$(basename "$(dirname "$(dirname "$f")")")"
    category="$(basename "$f" .jsonschema.yaml)"
    printf '%s\t%s\n' "$category" "$skill"
  done
}

skill_of() {
  table | awk -v category="$1" '$1 == category { print $2; found = 1 }
    END { if (!found) exit 1 }'
}

canonical_uri() {
  echo "skill://$(skill_of "$1")/jsonschema/$1.jsonschema.yaml"
}

canonical_stub() {
  printf '%s\n$ref: "%s"\n' "$MODELINE" "$(canonical_uri "$1")"
}

# Every authored collection under the roots, as <dir>. Prunes:
#   .git, node_modules, trash        -- never source
#   *.bak, *.old                     -- snapshots, not consumers
#   .claude/worktrees, *--replication-run
#     -- copies of the skills repo itself; fixing them there fixes
#        nothing, and they re-diverge on every respawn.
collections() {
  find "$@" \
    \( -name .git -o -name node_modules -o -name trash \
       -o -name '*.bak' -o -name '*.old' \
       -o -name worktrees -o -name '*--replication-run' \) -prune -o \
    -type d -name '*.kb' -print
}

export -f table skill_of canonical_uri canonical_stub collections
