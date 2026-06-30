---
type: "SOP"
title: "Agent-Native Activation"
description: "Machine-facing activation and context reconstruction contract."
tags: ["alphax", "activation", "sop"]
---
# Agent-Native Activation

```yaml
principle: user triggers; alphaX reconstructs context

minimal_triggers:
  engage: ["alphaX engage", "Engage Alpha Partner", "Proceed in Alpha Partner mode"]
  problem_decomposition: ["What are we actually trying to solve?", "step back to the real problem"]
  reentry_risk: ["alphaX restore this project context", "alphaX review risks"]
  project_review: ["alphaX run project review", "check whether claimed work is implemented"]
  loops: ["alphaX daily radar", "alphaX source drift check", "alphaX false completion check", "alphaX nudge check"]

invocation_contract:
  map_with: docs/agent-invocation-contract.md
  fixtures: docs/agent-trigger-fixtures.json
  readable_guide: docs/agent-trigger-fixtures.md
  rule: classify intent, read required source, inspect live evidence, then call state/risk/completion

agent_responsibility:
  do_not_first: ask user to restate the scene
  first_inspect:
    - cwd and project files
    - target AGENTS.md, README, specs, contracts, changelog, issues
    - target .alphaX/project-context.md when present
    - target .alphaX/evidence.md or .alphaX/decisions.md when referenced
    - git status, branch, recent commits, changed files
    - provided links, attachments, files
    - relevant memory entries when prior context matters
  first_output:
    - inferred project/conversation surface
    - inferred P0
    - primary loop
    - source of truth found
    - missing evidence
    - next concrete move
  ask_user_only_when: first pass cannot resolve target, boundary, or source of truth

helpers:
  context_snapshot: scripts/context-snapshot.sh [/path/to/project]
  target_project_review: alphaX/project-review/README.md

project_local_data:
  create_after: repeated project use
  guide: templates/project-work/local-pointer.md
  default_install: target .git/info/exclude
  schema: docs/local-alphaX-schema.md
  expansion_rule: start with index.md and project-context.md; create optional files only when they reduce reload ambiguity or preserve evidence/review boundaries
  forbid:
    - target tracked AGENTS.md alphaX pointer
    - target versioned .gitignore edit
    - copying Alpha Partner Source into target repo
    - target .alphaX/AGENTS.md or default reports directory

proactive_nudge_boundary:
  allowed_active_invocation_signals: [stale next action, unresolved high-risk decision, uncommitted project objective data, source drift, false completion, explicit focus/risk concern]
  outside_session_requires_approval: [schedule, destination, observed sources, privacy boundary, cooldown, stop condition]

boundary:
  - short trigger is user work; context reconstruction is agent work
  - project source of truth overrides partner defaults
  - durable memory, publication, risky operations, destructive commands, and secrets require approval
```
