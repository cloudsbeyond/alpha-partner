#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"

mkdir -p \
  "$ROOT/.alphaX/local" \
  "$ROOT/.alphaX/process/loop-reports" \
  "$ROOT/.alphaX/process/pilots" \
  "$ROOT/.alphaX/process/review-feedback" \
  "$ROOT/.alphaX/process/source-work-candidates"

write_if_missing() {
  local path="$1"
  if [ -e "$path" ]; then
    printf 'kept: %s\n' "${path#$ROOT/}"
    cat >/dev/null
    return 0
  fi

  mkdir -p "$(dirname "$path")"
  cat >"$path"
  printf 'created: %s\n' "${path#$ROOT/}"
}

write_if_missing "$ROOT/.alphaX/manifest.yaml" <<'EOF'
schema_version: 1
owner: local
kind: alphaX_local_data
created_by: scripts/init-local-alphaX.sh
source_contract: AGENTS.md
local:
  directory: .alphaX/local
process:
  directory: .alphaX/process
EOF

write_if_missing "$ROOT/.alphaX/local/README.md" <<'EOF'
# alphaX Local Data

Machine-local and user-local clues for this checkout.

Allowed:

- local path aliases;
- quasi-static project metadata;
- local project map;
- local pilot queue.
- resident agent-runtime-services endpoint config.

Do not commit this directory. Live project source wins over this data.
EOF

write_if_missing "$ROOT/.alphaX/local/agent-runtime-services.json" <<'EOF'
{
  "agentRuntimeServices": {
    "baseUrl": "http://127.0.0.1:8765/"
  }
}
EOF

write_if_missing "$ROOT/.alphaX/process/README.md" <<'EOF'
# alphaX Process Data

Local alphaX process traces for this checkout.

Allowed:

- focus radar;
- session ledger;
- decision notes;
- source review backlog;
- review feedback;
- source work candidates;
- loop reports;
- pilot evidence.

Do not store raw hidden model chain-of-thought, secrets, or private transcript
content here. Do not commit this directory.
EOF

write_if_missing "$ROOT/.alphaX/local/project-paths.md" <<'EOF'
# Local Project Paths

schema_version: 1

Use this file for machine-local aliases. Keep private paths here, not in the
GitHub-tracked source.

| Alias | Path |
| --- | --- |
| `{alpha-partner}` | `<path-to-this-checkout>` |
EOF

write_if_missing "$ROOT/.alphaX/local/project-meta-index.yaml" <<'EOF'
schema_version: 1
owner: local
kind: quasi_static_project_meta
projects: []
EOF

write_if_missing "$ROOT/.alphaX/local/pilot-candidates.md" <<'EOF'
# Local Pilot Candidates

schema_version: 1

Record local candidate projects only when needed. Keep private project details
out of the GitHub-tracked source.
EOF

write_if_missing "$ROOT/.alphaX/local/private-patterns.txt" <<'EOF'
# One private literal per line.
# scripts/verify-alpha-source.sh fails if any non-comment line appears in the
# GitHub-tracked source tree. Keep this file ignored.
EOF

write_if_missing "$ROOT/.alphaX/process/session-ledger.md" <<'EOF'
# Local Session Ledger

schema_version: 1

Record local alphaX sessions when a durable local trace is useful.
EOF

write_if_missing "$ROOT/.alphaX/process/focus-radar.md" <<'EOF'
# Local Focus Radar

schema_version: 1

Record local focus and risk snapshots when needed.
EOF

write_if_missing "$ROOT/.alphaX/process/decision-log.md" <<'EOF'
# Local Decision Log

schema_version: 1

Record local decisions, unverified claims, and rationale when needed.
EOF

write_if_missing "$ROOT/.alphaX/process/source-review-backlog.md" <<'EOF'
# Local Source Review Backlog

schema_version: 1

Record local source review todos and unsettled review consensus when needed.
EOF

printf 'Local alphaX data initialized under %s\n' "$ROOT/.alphaX"
