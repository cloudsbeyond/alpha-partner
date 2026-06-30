---
type: "SOP"
title: "Project Work"
description: "Project work trigger contract, scope guard, and assistance procedure."
tags: ["alphax", "project-work", "sop"]
---
# Project Work

```yaml
scope: project work
target: one concrete project, document, product question, research task, or engineering problem
alpha_partner_source: read-only

target_project_owns:
  - source of truth
  - ignored .alphaX/ data following docs/local-alphaX-schema.md

allowed_writes:
  - target project files when user asked to change that project
  - target .alphaX/ surfaces allowed by docs/local-alphaX-schema.md
  - OS temp dir
  - conversation

forbidden_writes:
  - source checkout .alphaX/process/ for project process data
  - alpha-partner tracked source unless user switches to source work
  - target tracked AGENTS.md alphaX pointer or versioned .gitignore edit
  - target .alphaX/AGENTS.md or catch-all reports directory

reentry:
  read: [alphaX/project-work/context-reloader.md, live target source, target .alphaX/ per schema when present]
  rule: live project source wins over stale .alphaX/ data

not_for:
  handoff_merge_release_freeze_or_claimed_completion: use project review first
```
