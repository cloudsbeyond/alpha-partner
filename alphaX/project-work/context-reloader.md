---
type: "SOP"
title: "Context Reloader"
description: "Project re-entry SOP for live source and project-local objective data."
tags: ["alphax", "context", "sop"]
---
# Context Reloader

```yaml
identity:
  name: Context Reloader
  kind: alphaX function/SOP
  principle: function, not project store
  output: report-first re-entry

not:
  - centralized Project Context directory
  - project spec, roadmap, ADR, contract, changelog, or test plan
  - scheduler, notification system, dashboard, or automation loop
  - dependency imposed on third-party projects

source_priority:
  - target AGENTS.md, README, specs, contracts, tests, changelog, live git state
  - target ignored .alphaX/project-context.md as context only
  - optional target ignored .alphaX/* only when referenced by project-context.md or required by review depth
  - current command output and validation evidence
  - optional source checkout ignored .alphaX/local/project-meta-index.yaml for quasi-static clues
  - other-agent feedback as context input only

project_local_objective_data:
  schema: docs/local-alphaX-schema.md
  default: .alphaX/project-context.md is the current reload baseline
  optional: evidence, decision, or durable-review files only when referenced or needed
  rule: context, not control
  must_not_replace: versioned source of truth
  should_avoid: broader alphaX risk judgment, goal calibration, raw logs, or project-source copies

callable_truth_source_rule:
  usable_when: claim has a source, command, artifact, URL, or explicit decision pointer that can drive a next action or review call
  downgrade_when: pointer is stale, narrative-only, copied source, private dump, or lacks a verification path
  live_source_priority: target versioned source and current command output still win

source_process_data_boundary:
  belongs_to: alpha-partner ignored .alphaX/process/
  project_work_read: false
  project_review_exception: sanitized mechanism feedback only; no project facts
  not: target project state or raw hidden model chain-of-thought

project_meta_index:
  path: source checkout ignored .alphaX/local/project-meta-index.yaml
  allowed: [project key, path alias, local context path, alphaX relationship, source-of-truth anchors]
  forbidden: [current branch, PR status, active P0, live risks, private transcripts, implementation status, acceptance state]

sop:
  - receive alphaX trigger
  - identify project and project key
  - read target instructions and live git/source state
  - read .alphaX/project-context.md when present as context, not control
  - read target .alphaX/* optional files only when referenced or required by review depth
  - consult source checkout ignored .alphaX/local/project-meta-index.yaml only for quasi-static clues
  - separate live facts, project-local objective data, source-local clues, historical evidence, unverified claims
  - produce report-first output
  - write back only with explicit approval and only into target-owned surfaces

staleness_rule:
  .alphaX/project-context.md: reload starting point, not current-state guarantee
  optional_extensions: lower-priority evidence, decision, or review pointers; not default truth
  conflict: live project source wins; .alphaX becomes stale evidence

split_rule:
  stay_in_project_context: current baseline, active risks, open items, compact latest review snapshot
  split_out_only_for: reusable evidence, durable owner decisions, or explicit persistent review artifacts
```
