---
type: "SOP"
title: "Source Work"
description: "Source work scope, write boundary, and verification requirements."
tags: ["alphax", "source-work", "sop"]
---
# Source Work

```yaml
scope: source work
target: Alpha Partner Source or alphaX function

use_when_changing:
  - AGENTS.md contract
  - scopes, SOPs, templates, skills, docs, scripts, verifiers
  - plugin packaging that carries invocation behavior
  - open-source boundary or local .alphaX/ governance

write_boundary:
  tracked_source: allowed only for accepted source work
  local_process_notes: source checkout .alphaX/process/
  forbidden: project facts in GitHub-tracked source

verify:
  source_changed:
    - bash scripts/verify-alpha-source.sh
    - git diff --check
  local_alphaX_initialized_or_used:
    - bash scripts/verify-local-alphaX.sh

not_for:
  source review: audit first, then switch scope before edits
```
