#!/bin/bash
# validate.sh: report every design-tower `why:` item that is not a resolving
# `.md` path. Read-only. Exits 1 on any finding. See why_paths.py.
set -euo pipefail
exec "$(dirname "$(readlink -f "$0")")/why_paths.py" validate "$@"
