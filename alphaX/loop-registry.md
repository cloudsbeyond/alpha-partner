---
type: "SOP"
title: "Loop Registry"
description: "Manual-trigger loop registry for alphaX recurring checks and reports."
tags: ["alphax", "loops", "sop"]
---
# Loop Registry

```yaml
principle: loops protect attention; they do not replace judgment
default_boundary:
  mode: manual-trigger
  writes: read-only unless approved
  forbid_without_approval: [schedule, hosted routine, private watcher, repo modification, external post, destructive operation]

loop_quality_gate:
  required: [clear_goal, scoped_authority, independent_sensor, feedback_to_next_action, cost_or_stop_boundary]
  fail_call: keep report-first, define missing evidence, or park the loop
  rule: repeated execution is not improvement unless an independent sensor can change the next action

source_inspiration:
  - Claude Code /loop
  - Claude Code Routines
  - Boris-style report loops
  - alphaX uses report-first loops before execution

observation_boundary:
  allowed_active_session_signals: [project state, recent diffs, failing checks, stale ledger entries, unresolved decisions, repeated interruptions, explicit user work surfaces]
  forbidden_without_approval: [cross-app private data collection, centralized super-app scraping, private chat processing, background watchers]

loops:
  L1_daily_focus_radar:
    trigger: alphaX daily radar
    purpose: focus/risk view and next work block
    inputs: [focus-radar, session-ledger, context-snapshot, target instructions, target .alphaX/project-context.md, optional target .alphaX/* when referenced]
    output: compact focus/risk report
    approval_needed_for: [writing project files, scheduling, publishing]

  L2_source_drift_watch:
    trigger: alphaX source drift check
    purpose: source-of-truth drift scan
    route: project target => alphaX/project-review/agent-workflow.md; alphaX target => alphaX/source-review/agent-workflow.md

  L3_false_completion_watch:
    trigger: alphaX false completion check
    purpose: separate proven claims, missing evidence, needed acceptance
    route: project target => alphaX/project-review/agent-workflow.md; alphaX target => alphaX/source-review/agent-workflow.md

  L4_pr_ci_watch:
    trigger: alphaX PR CI watch
    purpose: read repo/PR CI, stale branch, flaky tests, rebase risk
    required_input: explicit repo_or_pr_url
    approval_needed_for: [push, rebase, CI modification, PR comment]

  L5_research_intake:
    trigger: alphaX research intake
    purpose: map primary external signals to local collaboration mechanisms
    default_sources: [official docs, papers, engineering blogs, primary product docs]
    write_source_only_by_request: true

  L6_proactive_nudge_experiment:
    trigger: alphaX nudge check
    purpose: propose low-intrusion reminder/risk/focus candidate
    allowed_signals: [unresolved high-risk decisions, stale next action, missing manual acceptance, explicit focus degradation]
    output: candidate nudge with evidence, reason, urgency, channel
    approval_needed_for: [cron, host automation, Slack, Feishu, email, app notification, cross-app data]

  L7_alphaX_self_critique:
    trigger: alphaX self-critique
    purpose: find internally consistent but unverified alphaX claims
    allowed_signals: [contract claim without evidence, process claim without evidence, value claim without cross-day test, meta-only ledger, unused rules]
    output: suspect claim, why unverified, cheapest confirm/falsify evidence
    writes: none unless user switches to source work

upgrade_gate:
  required_before_schedule_or_push: [manual value proven, explicit scope, source list, read/write boundary, independent verification sensor, observation signals, feedback-to-next-action path, stop condition, destination, cooldown, cost/privacy review, human approval]

parking_lot:
  - background-agent swarms
  - hosted routines
  - Slack/Feishu posting
  - automatic PR repair
  - autonomous rebase/merge
  - scheduled private transcript processing
  - cross-app behavior learning
```
