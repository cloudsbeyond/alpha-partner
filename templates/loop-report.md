---
type: "Template"
title: "Loop Report"
description: "Template for manual-trigger loops and proactive nudge candidates."
tags: ["alphax", "template", "loop"]
---
# Loop Report

```yaml
generated_frontmatter:
  type: Loop Report
  title: Loop Report
  date: "<YYYY-MM-DD>"
  actor: alphaX
  kind: loop_report

loop:
  name: "<loop name>"
  trigger: "<trigger>"
  surface: "<project|source|conversation>"

p0:
  loop_purpose: "<one sentence>"
  project_main_line: "<one sentence or n/a>"

evidence:
  files_inspected: []
  commands_run: []
  external_sources: []

findings:
  proven: []
  not_proven: []
  drift_or_risk: []

nudge_candidate:
  should_push: "<yes|no>"
  reason: "<evidence-backed reason>"
  urgency: "<low|medium|high>"
  channel: "<active invocation|proposed external channel>"
  cooldown: "<cooldown>"

recommendation:
  next_focus_move: "<one action>"
  needs_human_decision: "<yes|no + decision>"
  do_not_do_now: []

boundary:
  read_only: "<yes|no>"
  writes_performed: []
  approvals_needed: []
  stop_condition: "<condition>"
```
