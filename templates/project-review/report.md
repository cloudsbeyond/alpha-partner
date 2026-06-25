# Project Review Report

date: `<YYYY-MM-DD>`
project: `<project key or path>`
actor: `alphaX`
kind: `project_review`
trigger: `<explicit user trigger or suggested trigger>`
scope: `project review`
followup_state: `<initial_review|cleanup_requested|cleanup_merged|post_cleanup_handoffable|not_applicable>`
confidence: `<high|medium|low>`

## P0 Main Line

`<one sentence describing the project outcome being reviewed>`

## Scope

- reviewed_claims:
  - `<claim, acceptance criterion, handoff assertion, or release criterion>`
- out_of_scope:
  - `<what this review intentionally did not inspect>`
- write_boundary_used:
  - `<conversation only | project .alphaX/reports | project .alphaX/project-context.md | project files by user request>`

## Sources Read

- `<file, command, diff, issue, spec, test, build log, screenshot, or artifact>`

## Evidence Map

| Claim | Evidence | Status |
| --- | --- | --- |
| `<claim>` | `<file/command/artifact>` | `<supported|partial|unsupported|not checked>` |

## Completion State

- implementation_state: `<not-found|partial|implemented|not-reviewed>`
- validation_state: `<not-run|failed|partial|passed|not-applicable>`
- integration_state: `<local-only|branch-only|merged|released|not-reviewed>`
- completion_call: `<blocked|needs-owner-decision|handoffable|mergeable|publishable|insufficient-evidence>`
- state_conflicts: `<none or conflicting states that prevent a stronger call>`

## Lifecycle Hygiene

- release_or_publication_claim: `<yes|no>`
- lifecycle_hygiene_trigger: `<pr-or-merge|handoff|freeze|release|publication|open-source-readiness|stale-alphaX|noisy-alphaX|not checked>`
- remote_state: `<remote URL, visibility, default branch, commit shape, or not checked>`
- public_metadata: `<description/topics/license/readme posture or not applicable>`
- tracked_tree_state: `<clean|dirty|mixed|not checked>`
- ignored_alphaX_state: `<absent|compact|append-only-noisy|contains-risk|not checked>`
- compaction_needed: `<yes|no|not checked>`
- unfrozen_evidence_preserved: `<yes|no|not applicable|not checked>`

## Findings

- `<P0|P1|P2|P3>` `<finding with evidence and impact>`

## Drift Markers

- `<source, spec, test, handoff, .alphaX, or implementation drift>`

## Missing Evidence

- `<validation, source, artifact, or decision still missing>`

## Engineering Call

`<blocked|needs-owner-decision|handoffable|mergeable|publishable|insufficient-evidence>`

## Next Action

`<one concrete next action>`

## Review Feedback Closeout

- mechanism_feedback_observed: `<yes|no>`
- review_feedback_backwrite: `<written|not-needed|deferred>`
- review_feedback_pointer: `<target .alphaX report, alphaX .alphaX/process/review-feedback note, or n/a>`
- open_closeout_item: `<if mechanism_feedback_observed is yes and review_feedback_backwrite is deferred, write a sanitized note or state why no note is needed before handoff>`

## Unverified Claims

- `<claim not yet proven by reviewed evidence>`
