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

export SKILLS_REPO="${SKILLS_REPO:-$HOME/repo/github.com/bukzor/bukzor-agent-skills}"
# A plain stub uses only `$ref`, which means the same thing in every
# dialect, so it declares the better-tooled draft-07 meta-schema; see
# llm-kb/references/schema-reuse.md.
export MODELINE='# yaml-language-server: $schema=https://json-schema.org/draft-07/schema'

# category<TAB>skill, one row per published canonical.
#
# A canonical only counts if its skill:// form actually resolves --
# SKILLS_HOME/<skill>/jsonschema/<category>.jsonschema.yaml, where
# SKILLS_HOME is ~/.claude/skills. Publishing under a repo subdirectory
# that is not installed there would otherwise mint stubs that reference
# a URI nothing can retrieve, silently, for a whole category.
#
# This is not hypothetical bookkeeping: `design-next.kb/` publishes a
# canonical and has no SKILL.md. It resolves only because it happens to
# be installed anyway. The next such directory might not be.
#
# Computed once at source time, not per call. validate.sh asks
# skill_of() a question per collection directory -- thousands of times
# across the roots -- and rebuilding the table each time cost minutes.
# A guard slow enough to skip is a guard that gets skipped.
build_table() {
  local f skill category
  for f in "$SKILLS_REPO"/*/jsonschema/*.jsonschema.yaml; do
    skill="$(basename "$(dirname "$(dirname "$f")")")"
    category="$(basename "$f" .jsonschema.yaml)"
    if [[ ! -f "$HOME/.claude/skills/$skill/jsonschema/$category.jsonschema.yaml" ]]; then
      echo >&2 "WARNING: $skill/jsonschema/$category.jsonschema.yaml is published" \
        "but skill://$skill/ does not resolve; not enrolling $category"
      continue
    fi
    printf '%s\t%s\n' "$category" "$skill"
  done
}
export SCHEMA_TABLE="${SCHEMA_TABLE:-$(build_table)}"

table() {
  printf '%s\n' "$SCHEMA_TABLE"
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

export -f build_table table skill_of canonical_uri canonical_stub collections
