---
type: "Template"
title: "Re-Entry Risk Packet"
description: "Template for project re-entry, focus recovery, and risk review."
tags: ["alphax", "template", "risk"]
---
# Re-Entry Risk Packet

```yaml
generated_frontmatter:
  type: Risk Packet
  title: Re-Entry Risk Packet
  date: "<YYYY-MM-DD>"
  actor: alphaX
  kind: reentry_risk_packet

surface:
  project_path_or_link: "<target>"
  trigger: "<trigger>"

p0:
  current_main_line: "<one sentence>"
  source_of_truth: []
  stop_condition: "<condition>"

current_state:
  live_files_or_commands_inspected: []
  latest_verified_evidence: []
  changed_since_last_checkpoint: []

top_risks:
  P1: []
  P2: []
  P3: []

focus_move:
  next_work_block_action: "<one action>"
  validation_or_acceptance_evidence: "<command|artifact|decision>"
  do_not_do_now: []

parking_lot:
  later: []
  waiting_on_user_decision: []
  research_only: []
```
