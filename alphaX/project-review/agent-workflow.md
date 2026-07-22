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
  acceptance_state: [not-reviewed, missing, partial, owner-accepted, user-validated, not-applicable]
  completion_call: [blocked, needs-owner-decision, handoffable, mergeable, publishable, insufficient-evidence]

delivery_flow_boundary:
  use_when: productivity, AI-native, handoff, merge, release, or claimed-completion evidence is being judged
  distinguish: [personal_execution_speed, project_delivery_cycle, rework_or_regression_risk, review_consensus, handoff_readiness]
  rule: faster local execution or generated output is not project delivery progress without validation, review, handoff, and acceptance evidence

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
  closeout_asset_hygiene:
    use_when: a full-lifecycle merge, handoff, freeze, release, or publication review includes Git or generated-output cleanup
    inspect: [worktrees, branches, stashes, ordinary untracked files, ignored or generated outputs]
    classify: [authoritative source, durable project evidence, reproducible output, temporary safety copy, unresolved unique content]
    deletion_gate:
      allow_when:
        - live-source coverage is proven by ancestry, tree equivalence, content equivalence, or another direct repository-specific check
        - durable logic, provenance, decisions, and evidence pointers have an explicit owning target surface
        - generated outputs are proven reproducible or their release authority is preserved by the target project
      hold_when:
        - unique content, authority, reproducibility, or absorption destination remains unresolved
    absorption_rule: preserve the reusable judgment and project evidence in their owning source or allowed project-local review surface; do not retain binary copies merely because cleanup produced them
    temporary_safety_copy:
      role: optional transaction guard for an authorized destructive cleanup, not a durable archive or new project data surface
      disposal_gate: delete after logical absorption, clean-state verification, and confirmation that no unresolved unique content depends on it
      anti_pattern: leaving a recovery directory indefinitely after its transaction has closed

output:
  order: [findings, completion state, drift markers, missing evidence, lifecycle hygiene gaps, unverified_claims, next action]
  persistence:
    default: conversation first; update target .alphaX/project-context.md only when useful and allowed
    optional: split to target .alphaX/ only by docs/local-alphaX-schema.md boundaries
  alpha_partner_exception: sanitized mechanism review-feedback only
```
