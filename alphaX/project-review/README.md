---
type: "SOP"
title: "Project Review"
description: "Project review contract for judging one project's delivery evidence."
tags: ["alphax", "project-review", "sop"]
---
# Project Review

```yaml
scope: project review
target: one concrete project's claimed delivery state
goal: decide what reviewed evidence supports
calls: [blocked, needs-owner-decision, handoffable, mergeable, publishable, insufficient-evidence]
not: alphaX source governance review

next_action_options:
  - fix implementation
  - run or add validation
  - compact stale project-local .alphaX/ data
  - defer or ask owner decision
  - hand off, merge, release, or publish when evidence supports it

read:
  target_project:
    - instructions
    - README
    - specs
    - contracts
    - schemas
    - tests
    - changelog
    - issue notes
    - source files
    - current diff
    - git status
    - commits
    - build output
    - validation logs
  optional_context:
    - target ignored .alphaX/project-context.md
    - other target .alphaX files only when referenced or required by review depth

forbidden:
  - write Alpha Partner Source
  - replace target source of truth, spec, ADR, changelog, or approval flow
  - implement fixes without scope switch
  - store secrets, private transcripts, hidden chain-of-thought, or broad alphaX governance judgment inside target

procedure:
  - identify root, branch, working tree, instruction files
  - list reviewed claims
  - map each claim to evidence or missing evidence
  - run smallest safe validation
  - use templates/project-review/report.md

completion_fields:
  implementation_state: [not-found, partial, implemented, not-reviewed]
  validation_state: [not-run, failed, partial, passed, not-applicable]
  integration_state: [local-only, branch-only, merged, released, not-reviewed]
  completion_call: [blocked, needs-owner-decision, handoffable, mergeable, publishable, insufficient-evidence]

Escalation Gate:
  default_review_mode: compact
  compact_required: [reviewed claims, sources read, evidence map, completion state, findings, missing evidence, unverified_claims, confidence, next action]
  full_lifecycle_triggers:
    - PR/merge/handoff/freeze/release/publication/open-source readiness claim
    - stale, noisy, or decision-bearing target .alphaX/ evidence
    - public metadata, license, remote/default-branch, tag, package, generated artifact, or release-state risk
    - repeated-surface parity risk
    - data-boundary or private-source leakage risk
  review_mode: compact|full-lifecycle

lifecycle_hygiene:
  compact_only_unless_triggered: true
  preserve: [current baseline, durable decisions, evidence pointers, unfrozen evidence, open decisions, next actions, local-only warnings]
  archive_or_remove: [command transcripts, obsolete phase logs, duplicated source facts, stale paths, superseded names unless anti-drift sentinel]

output:
  order: [findings, completion state, drift markers, missing evidence, lifecycle hygiene gaps, unverified_claims, next action]
  persistence:
    default: conversation first; update target .alphaX/project-context.md only when useful and allowed
    optional: split to target .alphaX/ only by docs/local-alphaX-schema.md boundaries
  alpha_partner_exception: sanitized mechanism review-feedback only
```
