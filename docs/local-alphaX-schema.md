---
type: "Data Schema"
title: "Local alphaX Data Schema"
description: "Schema and bootstrap contract for ignored local .alphaX data."
tags: ["alphax", "schema", "local-data"]
---
# Local alphaX Data Schema

## Required Shape

```yaml
tracked_source_role: reusable alphaX function source
local_alphaX_role: ignored machine-local and process data
consistency_source: schema, not identical contents

source_checkout_shape:
  .alphaX/:
    index.md: local navigation
    manifest.yaml: schema anchor
    local/:
      index.md: navigation
      README.md: local data notes
      project-paths.md: private aliases
      project-meta-index.yaml: quasi-static clues
      pilot-candidates.md: local queue
      private-patterns.txt: literals forbidden in tracked source
    process/:
      index.md: navigation
      README.md: process notes
      decision-log.md: decisions
      focus-radar.md: focus/risk
      session-ledger.md: session trace
      source-review-backlog.md: source review queue
      applied-runs/: applied source/project/research traces
      judgment-replays/: source-evolution judgment replay packets
      loop-reports/: manual loop reports
      pilots/: pilot evidence
      publication-packets/: owner-gated publication decision packets and closeouts
      review-feedback/: sanitized mechanism feedback
      source-evolution-candidates/: PDCA and owner-review source evolution candidates
      source-work-candidates/: candidate source edits
      thinking-notes/: review thinking notes and freeze inputs

minimum_verified_shape:
  required: [manifest.yaml, local/README.md, process/README.md, process/applied-runs/, process/judgment-replays/, process/loop-reports/, process/pilots/, process/publication-packets/, process/publication-packets/README.md, process/review-feedback/, process/source-evolution-candidates/, process/source-work-candidates/, process/thinking-notes/]
  existing_local_data_rewrite_required: false

manifest.yaml:
  schema_version: 1
  owner: local
  kind: alphaX_local_data
  created_by: scripts/init-local-alphaX.sh
  source_contract: AGENTS.md
  local.directory: .alphaX/local
  process.directory: .alphaX/process
  forbid: [project status, paths, private facts]

local_data:
  stores: [path aliases, quasi-static project metadata, local project map, local pilot queue]
  must_remain_ignored: true

process_data:
  stores: [focus radar, session ledger, decisions, source review backlog, review feedback, source work candidates, source evolution candidates, applied runs, judgment replays, thinking notes, loop reports, pilot evidence, owner-gated publication packets]
  not: raw hidden model chain-of-thought
  root_files_allowed: [README.md, index.md, decision-log.md, focus-radar.md, session-ledger.md, source-review-backlog.md]
  publication_packets:
    path: .alphaX/process/publication-packets/<date>-<surface>/
    stores: [decision packet, execution runbook, review-packaging rationale, closeout]
    rule: side-effecting command plans must be marked closed/historical with do_not_execute after completion, supersession, or parking
```

## Target Project Shape

```yaml
target_project_shape:
  install: target .git/info/exclude
  role: ignored project-local context surface, not control surface
  minimum_files:
    .alphaX/index.md:
      role: local data contract and file map
      write: rare
      not: [current status, decisions, findings, reports]
    .alphaX/project-context.md:
      role: current reload baseline
      write: default
      stores: [identity, source anchors, current state, compact evidence, open items, active risks, latest review]
  optional_extensions:
    .alphaX/evidence.md:
      create_when: evidence pointers outgrow project-context.md
      role: pointer registry, not raw log store
    .alphaX/decisions.md:
      create_when: durable owner decisions need stable lookup
      role: project decision ledger
    .alphaX/reviews/:
      create_when: explicit durable local review or handoff artifact is needed
      role: compact artifacts, not default report dump
  forbidden:
    - .alphaX/AGENTS.md
    - .alphaX/reports/
    - copied Alpha Partner Source
    - target tracked AGENTS.md alphaX pointer
    - target versioned .gitignore edit

extension_file_boundaries:
  evidence.md:
    read: when referenced or review depth requires it
    not: [raw command output, copied source, transcripts, secrets]
  decisions.md:
    write: explicit durable user/project decisions only
    not: [agent preference, hidden rationale]
  reviews/:
    write: explicit persistent review artifacts only
    read: through project-context.md pointer first
    not: unbounded report directory

callable_truth_source_contract:
  usable_when:
    - a claim maps to a current source, command, artifact, URL, or explicit decision pointer
    - the pointer supports a concrete next action, review call, or verification step
    - live source priority and staleness are stated
  not_usable_when:
    - it is a narrative archive, copied source, raw transcript, or private project dump
    - it asserts current truth without a verification path
    - it becomes a control surface or approval flow

compaction_triggers:
  - PR/merge/handoff/freeze/release/publication/open-source readiness
  - stale project-context rewrite
  - evidence or decisions outgrow current reload baseline
  - repeated logs make re-entry harder
  - conflicting current-state pointers

compaction_requires_user_approval: true
preserve:
  - current baseline
  - durable decisions
  - evidence pointers
  - unfrozen decision evidence
  - open items
  - local-only warnings
archive_summarize_or_remove:
  - command transcripts
  - obsolete phase logs
  - superseded paths unless anti-drift sentinel
  - duplicated source facts
  - raw transcript content, secrets, private paths, hidden model chain-of-thought

invariants:
  - .alphaX/ ignored by Git
  - git ls-files '.alphaX/*' returns no paths
  - target project uses .git/info/exclude by default, not versioned .gitignore
  - tracked tree excludes local paths, project state, ledgers, pilot evidence, loop reports, transcripts, secrets
  - live source wins over compacted .alphaX/ context
  - index.md describes boundaries; project-context.md carries current reload state
  - optional extensions reduce ambiguity or bloat; they are not default catch-all storage

commands:
  init: bash scripts/init-local-alphaX.sh
  verify_local: bash scripts/verify-local-alphaX.sh
  verify_source: bash scripts/verify-alpha-source.sh
  detect_applied_run_candidates: bash scripts/detect-applied-run-candidates.sh

private_patterns:
  path: .alphaX/local/private-patterns.txt
  role: optional literal denylist checked by scripts/verify-alpha-source.sh
```
