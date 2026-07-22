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

delivery_scope:
  intended_outcome: "<project-native outcome; distinguish repository change, release artifact, and target-environment acceptance when relevant>"
  responsibility_lane:
    source_of_truth: "<source|contract|artifact|environment|decision>"
    owner: "<human|agent|shared|external>"
    acceptance_gate: "<evidence or decision that clears this lane>"
    release_authority: "<owner|not-applicable>"
  adjacent_work: "<same lane|split|sequence + reason>"
  external_evidence_boundary:
    required_evidence: []
    provider: "<target environment|external owner|none>"
    available_now: "<yes|no|not-needed>"
    smallest_fail_closed_carrier: "<existing check or artifact|missing|not-needed>"
    decision: "<continue|hold + evidence-bound reason>"

delivery_loop:
  current_state: "<intake|clarify|design|implement|review|validate|handoff|reflect>"
  target_artifact_or_decision: "<file|doc|contract|diff|test|decision|none>"
  next_action: "<one concrete action or decision needed next>"
  advance_hold_or_rework: "<advance|hold|rework + evidence-bound reason>"
  gate:
    owner: "<human|agent|shared>"
    reason: "<L0-L2 decision|architecture/data/permission/security risk|merge/release/publication|external document refresh|durable memory|L3-L4 execution|none>"
    status: "<open|cleared|blocked|not-needed>"
  validation_method: "<test|command|artifact|review|user decision|missing>"
  validation_evidence: []
  feedback_route: "<how comments/findings/failures change the next artifact or action>"
  feedback_to_rework:
    responsible_boundary: "<L0|L1|L2|L3|L4|not L0-L4|unknown>"
    rework_items: []
    changed_artifacts: []
    validation_method: "<test|command|artifact|review|user decision|missing>"
    validation_evidence: []
    open_residue: []
  rework_state:
    closed: []
    remaining: []
  memory_candidate_quality:
    category: "<reusable-boundary-judgment|verified-project-fact|action-changing-evidence|none>"
    decision: "<candidate|park-unverified|park-one-off|park-private|park-noisy|park-non-actionable|none>"
    verification_path: []

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
