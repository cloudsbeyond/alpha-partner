---
type: "Reference"
title: "Non-Coding L0-L4"
description: "Non-coding formal-development coverage, minimum L0-L4 shape, L4 evidence carriers, and few-shot examples for research, SOPs, workflows, content products, knowledge assets, reviews, and decision memos."
tags: ["formal-development", "non-coding", "l0-l4", "validation"]
---
# Non-Coding L0-L4 / 非编码场景

Load this file for research, operating SOPs, organization workflows, content
products, knowledge assets, review systems, decision memos, or any change whose
L3 carrier is a repeatable non-code execution artifact.

```yaml
coverage:
  examples: [research service, operating SOP, organization workflow, content product, knowledge asset, review rubric, decision memo]
  rule: non-code execution still needs L3 execution artifacts and L4 validation evidence
  non_goal: do not treat lack of code as lack of formal-development structure
```

Minimum non-coding shape:

```yaml
non_coding_minimum_shape:
  l0_product:
    carrier: README.md + PRD.md
    example: research memo service for investment calls
  l1_architecture:
    carrier: docs/workflow.md
    example: intake -> evidence collection -> synthesis -> review -> decision
  l2_contract:
    carrier: docs/research-rubric.md
    example: evidence standard, inference boundary, source freshness rule, review checklist
  l3_execution:
    carrier: templates/research-memo.md + docs/workflow.md#review-step
    example: repeatable memo template and review operation
  l4_validation:
    carrier: docs/reviews/2026-07-07-sample-memo-review.md
    example: sample audit against rubric with residual risk
```

Non-coding L4 carriers:

```yaml
non_coding_l4_carriers:
  - review checklist
  - rubric scoring
  - sample output audit
  - dry run or rehearsal record
  - decision log
  - stakeholder review note
  - before/after comparison
  - residual risk memo
```

Minimal non-coding L4:

```yaml
expectation: research memo separates evidence, inference, decision, and residual risk
refs:
  l0: [README.md#research-service, PRD.md#p0-scope]
  l2: [docs/research-rubric.md#evidence-standard]
  l3: [templates/research-memo.md, docs/workflow.md#review-step]
evidence:
  review: docs/reviews/2026-07-07-sample-memo-review.md
  sample: outputs/sample-research-memo.md
result: partial
residual_risk: two claims still lack primary-source evidence
```

Non-coding few-shot:

```yaml
examples:
  - artifact: README describes research service users and decision boundary
    layer: L0
  - artifact: docs/workflow.md defines intake, evidence, synthesis, review
    layer: L1
  - artifact: docs/research-rubric.md defines freshness and inference rules
    layer: L2
  - artifact: templates/research-memo.md provides repeatable memo sections
    layer: L3
  - artifact: docs/reviews/sample-memo-review.md scores a memo against rubric
    layer: L4
  - artifact: review note adds a new product promise
    layer: drift
    action: return to L0 instead of treating review as source of truth
```
