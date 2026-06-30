---
type: "Template"
title: "Research Loop Packet"
description: "Template for evidence work that improves decisions or collaboration methods."
tags: ["alphax", "template", "research"]
---
# Research Loop Packet

```yaml
generated_frontmatter:
  type: Research Packet
  title: Research Loop Packet
  date: "<YYYY-MM-DD>"
  actor: alphaX
  kind: research_loop_packet

question: "<project-linked or collaboration-bottleneck question>"
p0_relevance: "<how this changes project R&D, thinking, alphaX, or agent-native practice>"

source_plan:
  allowed: [official docs, research papers, engineering blogs, product docs, local project files, memory entries when prior context matters]
  prefer_primary_sources: true

evidence:
  - source: "<url|path>"
    source_type: "<official|paper|engineering-blog|product-doc|local|memory>"
    observed_claim: "<claim>"
    mechanism_or_failure_mode: "<mechanism>"
    confidence: "<high|medium|low>"
    local_implication: "<implication>"

synthesis:
  observation: []
  inference: []
  judgment: []
  decision_candidate: []

partner_challenge: "<strongest counterargument or risk>"
output_destination: "<evidence-index|local process data|project note|memory candidate|none>"
verification: "<how research changed decision, question, experiment, or practice>"
```
