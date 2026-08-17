---
type: "SOP"
title: "Source Review"
description: "Source review contract for improving alphaX source and mechanisms."
tags: ["alphax", "source-review", "sop"]
---
# Source Review

```yaml
scope: source review
target: Alpha Partner Source and alphaX mechanisms
goal: improve alphaX itself
not: project delivery review
external_projects: do not read or modify

checks:
  - contract drift
  - stale local process state
  - unsupported claims
  - scaffolding-to-use imbalance
  - weak assumptions
  - source governance risk
  - intelligence-ceiling suppression
  - asset half-life drag
  - source-integrity proof mistaken for intelligence-ceiling or product-goal proof

read:
  - AGENTS.md
  - alphaX/source-work/intelligence-ceiling-half-life.md
  - relevant Alpha Partner Source files
  - .alphaX/process/focus-radar.md when present
  - .alphaX/process/session-ledger.md when present
  - .alphaX/process/decision-log.md when present
  - .alphaX/process/source-review-backlog.md when present
  - .alphaX/local/project-paths.md only as local alias registry

run:
  - bash scripts/verify-alpha-source.sh

verifier_evidence:
  required_output:
    status: current | historical | missing
    evidence: completed tool event, exact saved-result reference, or none
    result: observed result for current or historical; not_observed for missing
  current: use only when the completed verifier tool event is present
  historical: use only when an exact saved verifier result was actually read; label its date or source
  missing: use when neither current nor historical evidence exists; do not claim that the verifier ran, failed, or was blocked

output:
  - verifier evidence with status, evidence, and result
  - source/mechanism risks with evidence and confidence
  - layer call when a mechanism mixes durable principle, cognitive framework, operational scaffold, or implementation carrier
  - intelligence-ceiling and half-life impact when relevant
  - proof boundary when a claimed improvement is supported only by docs or passing checks
  - drift markers
  - source-work candidates or review-feedback notes when useful
  - handoff update when applicable
  - Spec Checkpoint when source discussion grew or drifted

candidate_outputs:
  - source-work candidate
  - verifier or boundary fix
  - contract simplification
  - judgment fixture or pruning candidate
  - stale-process correction
  - evidence-backed objection to claimed source readiness

does_not_decide:
  text: does not decide whether a target project is handoffable, mergeable, releasable, or complete

persistence:
  tracked_edits: never unless user switches to source work
  notes: source checkout ignored .alphaX/process/
```
