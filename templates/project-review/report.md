---
type: "Template"
title: "Project Review Report"
description: "Report template for reviewing project claims, evidence, drift, lifecycle hygiene, and next action."
tags: ["alphax", "template", "project-review"]
---
# Project Review Report

## Generated Report Frontmatter

```yaml
---
type: "Project Review Report"
title: "Project Review Report"
description: "Review of one project's claims, evidence, drift, lifecycle hygiene, and next action."
date: "<YYYY-MM-DD>"
project: "<project key or path>"
actor: "alphaX"
kind: "project_review"
trigger: "<explicit trigger>"
scope: "project review"
review_mode: "<compact|full-lifecycle>"
confidence: "<high|medium|low>"
tags: ["alphax", "project-review", "report"]
---
```

```yaml
p0_main_line: "<project outcome being reviewed>"

review_mode:
  value: "<compact|full-lifecycle>"
  escalation_trigger: "<none|pr-or-merge|handoff|freeze|release|publication|open-source-readiness|stale-alphaX|noisy-alphaX|public-metadata|parity-risk|data-boundary-risk>"
  compact_required_fields: [claims, sources, evidence_map, completion_state, findings, missing_evidence, unverified_claims, confidence, next_action]

scope:
  reviewed_claims: []
  out_of_scope: []
  write_boundary_used: "<conversation only|project .alphaX/project-context.md|project .alphaX/reviews/|project files by request>"

sources_read:
  files: []
  commands: []
  diffs: []
  issues_or_specs: []
  tests_or_build_logs: []
  artifacts: []

evidence_map:
  - claim: "<claim>"
    evidence: "<file|command|artifact|missing>"
    status: "<supported|partial|unsupported|not checked>"

completion_state:
  implementation_state: "<not-found|partial|implemented|not-reviewed>"
  validation_state: "<not-run|failed|partial|passed|not-applicable>"
  integration_state: "<local-only|branch-only|merged|released|not-reviewed>"
  acceptance_state: "<not-reviewed|missing|partial|owner-accepted|user-validated|not-applicable>"
  completion_call: "<blocked|needs-owner-decision|handoffable|mergeable|publishable|insufficient-evidence>"
  state_conflicts: []

delivery_flow_state:
  personal_execution_speed: "<not claimed|claimed|evidenced|not-reviewed>"
  project_delivery_cycle: "<not claimed|blocked|improved|not-reviewed>"
  rework_or_regression_risk: "<none found|risk|not-reviewed>"
  review_consensus: "<missing|partial|owner-aligned|not-applicable|not-reviewed>"
  handoff_readiness: "<blocked|handoffable|not-reviewed>"

Project Lifecycle Hygiene:
  required_when: review_mode == full-lifecycle
  lifecycle_hygiene_trigger: "<pr-or-merge|handoff|freeze|release|publication|open-source-readiness|stale-alphaX|noisy-alphaX|not checked>"
  Trigger Signals:
    pr_merge_handoff_freeze_release_publication_open_source: "<yes|no>"
    target_alphaX_used_as_evidence: "<yes|no>"
    target_alphaX_stale_or_noisy: "<yes|no>"
  source_and_evidence_state:
    target_root: "<path>"
    branch: "<branch>"
    working_tree: "<clean|dirty|mixed|not checked>"
    generated_outputs: []
    private_path_or_secret_scan: "<clean|risk|not checked>"
    validation_commands: []
    passing_evidence: []
    missing_evidence: []
    parity_checks: []
  release_or_publication_state:
    remote_url: "<url|not checked>"
    visibility: "<private|public|not checked>"
    default_branch: "<branch|not checked>"
    tags: []
    readme_license_metadata: "<ok|gap|not checked>"
  local_alphaX_state:
    present_and_ignored: "<yes|no|not checked>"
    current_summary_present: "<yes|no|not checked>"
    optional_extensions_used: []
    append_only_logs_too_noisy: "<yes|no|not checked>"
    unfrozen evidence: "<preserved|missing|not applicable|not checked>"
    compaction_needed: "<yes|no|not checked>"
    boundary_call: "<project-context baseline ok|split evidence|split decisions|durable review artifact needed|do not persist>"
  compaction_rule:
    preserve: [current baseline, durable decisions, evidence pointers, unfrozen evidence, open decisions, next actions, local-only warnings]
    remove_or_summarize: [command transcripts, obsolete phase logs, duplicated source facts, stale paths, superseded names unless anti-drift sentinel]

findings:
  - severity: "<P0|P1|P2|P3>"
    finding: "<finding>"
    evidence: "<pointer>"
    impact: "<impact>"

drift_markers: []
missing_evidence: []
engineering_call: "<blocked|needs-owner-decision|handoffable|mergeable|publishable|insufficient-evidence>"
next_action: "<one concrete action>"

review_feedback_closeout:
  mechanism_feedback_observed: "<yes|no>"
  review_feedback_backwrite: "<written|not-needed|deferred>"
  review_feedback_pointer: "<pointer|n/a>"
  open_closeout_item: "<item|none>"

unverified_claims: []
```
