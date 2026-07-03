---
type: "Template"
title: "Project Loop Packet"
description: "Template for real project, repo, document, implementation, review, or artifact work."
tags: ["alphax", "template", "project-work"]
---
# Project Loop Packet

```yaml
generated_frontmatter:
  type: Project Packet
  title: Project Loop Packet
  date: "<YYYY-MM-DD>"
  actor: alphaX
  kind: project_loop_packet
  scope: project work

project_surface:
  name: "<project>"
  path_or_link: "<path|url>"
  source_of_truth: []
  branch_or_doc_state: "<state>"

p0_main_line: "<one sentence>"
work_type: "<discovery|spec|implementation|review|reflection>"

boundary:
  layer: "<L0|L1|L2|L3|L4|not L0-L4>"
  owner: "<human|agent|shared>"
  missing_upstream_decision: "<none|decision>"

evidence_to_inspect:
  files: []
  commands: []
  links: []
  tests: []
  docs: []
  memory_entries: []

partner_stance: "<frame options|challenge assumptions|implement|review risks|collect evidence|simplify|preserve decision>"
acceptance: "<what proves project improved or next decision clarified>"

loop_verification:
  clear_goal: "<yes|no + goal>"
  scoped_authority: "<human|agent|shared|missing>"
  independent_sensor: "<test|command|artifact|user decision|metric|missing>"
  feedback_to_next_action: "<what changes after evidence>"
  cost_or_stop_boundary: "<cost limit or stop condition>"

spec_checkpoint:
  P0 Main Line: "<one sentence>"
  This Round Pruned: []
  Kept But Deferred: []
  To Confirm: []

verification:
  commands: []
  source_checks: []
  review_evidence: []
  user_acceptance: []
```
