---
type: "Template"
title: "Checkpoint Memory Evaluation"
description: "Template for checkpoint-bounded re-entry, update, evidence, and action memory evaluation."
tags: ["alphax", "template", "memory"]
---
# Checkpoint Memory Evaluation

## Generated Artifact Frontmatter

```yaml
---
type: "Checkpoint Evaluation"
title: "Checkpoint Memory Evaluation"
description: "Evaluation of remembered state across a checkpoint."
date: "<YYYY-MM-DD>"
actor: "alphaX"
kind: "checkpoint_memory_evaluation"
tags: ["alphax", "memory", "checkpoint"]
---
```

```yaml
scope:
  surface: "<project|source|conversation>"
  checkpoint: "<re-entry|handoff|freeze|release|project-review|source-iteration>"
  evidence_cutoff: "<time/commit/event>"
  loop: checkpoint_memory_evaluation

p0:
  current: "<one sentence>"
  boundary: "<write/read decision boundary>"
  next_action: "<one action or evidenced no-op>"

evidence_used:
  live_source: []
  local_alphaX: []
  external_source: []
  user_decision: []
  command_or_artifact: []
  prior_memory_note: []

remembered_evidence:
  source: "<memory|handoff|.alphaX|chat|none>"
  cutoff: "<declared cutoff>"
  status: "<current|stale|conflicting|unknown>"
  confidence: "<high|medium|low>"
  provenance: "<pointer>"
  conflict_with_live_source: "<none|describe>"

Call rubric:
  pass: evidence concrete and checkpoint-allowed
  partial: evidence exists but state/boundary/owner/verification gap remains
  fail: evidence missing, stale, post-cutoff without disclosure, or not action-supporting

evaluation:
  re-entry memory: {call: "<pass|partial|fail>", evidence: [], gap: "<gap>"}
  update memory: {call: "<pass|partial|fail>", evidence: [], gap: "<gap>"}
  evidence memory: {call: "<pass|partial|fail>", evidence: [], gap: "<gap>"}
  action memory: {call: "<pass|partial|fail>", evidence: [], gap: "<gap>"}

result:
  decision: "<decision or none>"
  source_implication: "<source change candidate or none>"
  parked: []
  unverified_claims: []
  next_checkpoint: "<checkpoint>"

boundary:
  runtime_backend_used: no
  interpretation_owner: alphaX
  approvals_needed: []
  do_not_do_now: []
```
