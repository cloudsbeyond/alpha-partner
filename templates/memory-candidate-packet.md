---
type: "Template"
title: "Memory Candidate Packet"
description: "Template for reviewable memory candidates before durable memory updates."
tags: ["alphax", "template", "memory"]
---
# Memory Candidate Packet

```yaml
generated_frontmatter:
  type: Memory Candidate
  title: Memory Candidate Packet
  date: "<YYYY-MM-DD>"
  actor: alphaX
  kind: memory_candidate

rule: do not update durable memory unless user explicitly asks

candidate:
  statement: "<one concise sentence>"
  allowed_category: "<reusable-boundary-judgment|verified-project-fact|action-changing-evidence|none>"
  evidence:
    - "<file|source link|command|test|conversation decision|repeated pattern>"
  verification_path: []
  update_or_expiry_rule: "<when to refresh, downgrade, or delete>"
  scope: "<global|repo|project-family|workflow-type|Alpha Partner Source>"
  stability: "<stable default|likely drift|re-check before use|one-off not memory>"
  risk_of_remembering: "<over-application failure mode>"
  reject_if:
    - unverified
    - one-off
    - private
    - noisy
    - chat-only
    - not actionable
  proposed_action: "<keep local|add process data|ask user for durable memory|discard>"
  user_approval: "<explicit approval pointer or none>"
```
