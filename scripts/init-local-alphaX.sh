#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"

mkdir -p \
  "$ROOT/.alphaX/local" \
  "$ROOT/.alphaX/process/applied-runs" \
  "$ROOT/.alphaX/process/judgment-replays" \
  "$ROOT/.alphaX/process/loop-reports" \
  "$ROOT/.alphaX/process/pilots" \
  "$ROOT/.alphaX/process/review-feedback" \
  "$ROOT/.alphaX/process/source-evolution-candidates" \
  "$ROOT/.alphaX/process/source-work-candidates" \
  "$ROOT/.alphaX/process/thinking-notes"

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

write_if_missing "$ROOT/.alphaX/index.md" <<'EOF'
# alphaX Local Data Index

# Subdirectory

- [local](local/index.md) - Machine-local and user-local clues for this source checkout.
- [process](process/index.md) - Local alphaX process traces for this source checkout.
EOF

write_if_missing "$ROOT/.alphaX/local/README.md" <<'EOF'
---
type: "Guide"
title: "alphaX Local Data"
description: "Machine-local and user-local clues for this source checkout."
tags: ["alphax", "local-data"]
---

# alphaX Local Data

Machine-local and user-local clues for this source checkout.

Allowed:

- local path aliases;
- quasi-static project metadata;
- local project map;
- local pilot queue.

Do not commit this directory. Live project source wins over this data.
EOF

write_if_missing "$ROOT/.alphaX/local/index.md" <<'EOF'
# Guide

- [alphaX Local Data](README.md) - Machine-local and user-local clues for this source checkout.
- [Local Pilot Candidates](pilot-candidates.md) - Local candidate projects for alphaX pilots.
- [Local Project Paths](project-paths.md) - Machine-local path aliases for this source checkout.

# Data

- [project-meta-index](project-meta-index.yaml) - Quasi-static local project metadata.
- [private-patterns](private-patterns.txt) - Local private literals excluded from tracked source.
EOF

write_if_missing "$ROOT/.alphaX/process/README.md" <<'EOF'
---
type: "Guide"
title: "alphaX Process Data"
description: "Local alphaX process traces for this source checkout."
tags: ["alphax", "process-data"]
---

# alphaX Process Data

Local alphaX process traces for this source checkout.

Allowed:

- focus radar;
- session ledger;
- decision notes;
- source review backlog;
- review feedback;
- source work candidates;
- source evolution candidates;
- applied runs;
- judgment replays;
- thinking notes;
- loop reports;
- pilot evidence.

Do not store raw hidden model chain-of-thought, secrets, or private transcript
content here. Do not commit this directory.
EOF

write_if_missing "$ROOT/.alphaX/process/index.md" <<'EOF'
# Guide

- [alphaX Process Data](README.md) - Local alphaX process traces for this source checkout.

# Process Data

- [Local Decision Log](decision-log.md) - Local decisions, unverified claims, and rationale.
- [Local Focus Radar](focus-radar.md) - Local focus and risk snapshots.
- [Local Session Ledger](session-ledger.md) - Local alphaX session ledger.
- [Local Source Review Backlog](source-review-backlog.md) - Local source review todos and unsettled consensus.

# Process Directories

- [Applied Runs](applied-runs/) - Applied source/project/research traces that calibrate alphaX mechanisms.
- [Judgment Replays](judgment-replays/) - Replay packets for source-evolution claims.
- [Loop Reports](loop-reports/) - Manual loop reports.
- [Pilots](pilots/) - Pilot evidence.
- [Review Feedback](review-feedback/) - Sanitized mechanism feedback.
- [Source Evolution Candidates](source-evolution-candidates/) - PDCA and owner-review source evolution candidates.
- [Source Work Candidates](source-work-candidates/) - Candidate source edits before acceptance.
- [Thinking Notes](thinking-notes/) - Review thinking notes and freeze inputs.
EOF

write_if_missing "$ROOT/.alphaX/local/project-paths.md" <<'EOF'
---
type: "Local Data"
title: "Local Project Paths"
description: "Machine-local path aliases for this source checkout."
tags: ["alphax", "local-data", "paths"]
---

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
---
type: "Local Data"
title: "Local Pilot Candidates"
description: "Local candidate projects for alphaX pilots."
tags: ["alphax", "local-data", "pilots"]
---

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
---
type: "Process Data"
title: "Local Session Ledger"
description: "Local alphaX sessions recorded when a durable trace is useful."
tags: ["alphax", "process-data", "ledger"]
---

# Local Session Ledger

schema_version: 1

Record local alphaX sessions when a durable local trace is useful.
EOF

write_if_missing "$ROOT/.alphaX/process/focus-radar.md" <<'EOF'
---
type: "Process Data"
title: "Local Focus Radar"
description: "Local focus and risk snapshots recorded when needed."
tags: ["alphax", "process-data", "risk"]
---

# Local Focus Radar

schema_version: 1

Record local focus and risk snapshots when needed.
EOF

write_if_missing "$ROOT/.alphaX/process/decision-log.md" <<'EOF'
---
type: "Process Data"
title: "Local Decision Log"
description: "Local decisions, unverified claims, and rationale recorded when needed."
tags: ["alphax", "process-data", "decisions"]
---

# Local Decision Log

schema_version: 1

Record local decisions, unverified claims, and rationale when needed.
EOF

write_if_missing "$ROOT/.alphaX/process/source-review-backlog.md" <<'EOF'
---
type: "Process Data"
title: "Local Source Review Backlog"
description: "Local source review todos and unsettled consensus."
tags: ["alphax", "process-data", "source-review"]
---

# Local Source Review Backlog

schema_version: 1

Record local source review todos and unsettled review consensus when needed.
EOF

printf 'Local alphaX data initialized under %s\n' "$ROOT/.alphaX"
