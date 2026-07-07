---
type: "Reference"
title: "Layer Glossary"
description: "Shared L0-L4 terminology, goals, non-goals, carriers, anti-examples, and few-shot classification for formal-development reviews."
tags: ["formal-development", "l0-l4", "glossary", "few-shot"]
---
# Layer Glossary / 层级术语

Load this file only when layer terminology or classification is ambiguous.
For scenario-specific minimum shapes, prefer `coding-l0-l4.md` or
`non-coding-l0-l4.md` directly.

```yaml
l0_product_intent:
  term_zh: 产品意图层
  goal: define why this exists, who it serves, what P0 problem it solves, value boundary, scope, and non-goals
  non_goal: [define architecture, prescribe implementation files, claim validation or acceptance]
  carriers: [README.md, product narrative, PRD.md]
  examples: [product narrative, P0 scope, non-goals, owner boundary]
  anti_examples: [test fixture redefining product promise, changelog silently adding P0 scope]

l1_architecture_narrative:
  term_zh: 架构叙事层
  goal: explain organization, flow, objects, states, authority, and boundaries
  non_goal: [change product promise, encode every field-level contract, implement behavior]
  carriers: [architecture/README.md, workflow.md, blueprint, sequence narrative]
  examples: [adapter boundary, request lifecycle, intake-to-review workflow]
  anti_examples: [architecture doc adding absent customer segment, implementation notes replacing boundary]

l2_formal_contract:
  term_zh: 形式化契约层
  goal: make L1 claims verifiable with explicit input, output, state, acceptance, or review constraints
  non_goal: [become full implementation, rely only on vague prose, override L0 or L1]
  carriers: [schema, protocol, concept registry, rubric, checklist, decision table, contract snapshot]
  examples: [JSON schema, protocol contract, evidence rubric, pass/partial/fail decision table]
  anti_examples: [checklist that only says looks good, code behavior as only contract without upstream ref]

l3_execution:
  term_zh: 执行或实现组织层
  goal: realize L2 through repeatable execution artifacts, either code or non-code operations
  non_goal: [invent product promises, rewrite architecture or contracts silently, claim validation without L4 evidence]
  carriers: [src/, adapters/, fixtures, templates, SOP steps, operating worksheet, migration script]
  examples: [module realizing schema, template realizing rubric, operating worksheet]
  anti_examples: [code adds field absent from L2, template changes review standard without updating rubric]

l4_validation_evidence:
  term_zh: 验证证据层
  goal: prove, partially prove, or falsify whether L3 conforms to L0/L1/L2 and claimed completion state
  non_goal: [replace human acceptance, approve merge or publication by itself, create new requirements]
  carriers: [test result, harness output, CI result, AI Contract Index, review checklist, rubric score, sample audit, residual risk memo]
  examples: [contract test result, rubric review, sample audit, dry-run notes]
  anti_examples: [passing tests presented as product acceptance, review notes changing L0 instead of reporting drift]
```

Few-shot classification:

```yaml
examples:
  - artifact: README explains who uses the workflow and what problem it solves
    layer: L0
    reason: defines user, problem, value boundary, and product promise
  - artifact: architecture/README shows lifecycle, states, and adapter boundary
    layer: L1
    reason: explains organization and boundary
  - artifact: concept-registry.yaml defines required object fields
    layer: L2
    reason: makes architecture claims verifiable
  - artifact: src/import/request.ts parses and stores the contract object
    layer: L3
    reason: concrete implementation realizes L2
  - artifact: test-results/import-request.json records contract test output
    layer: L4
    reason: evidence for whether L3 conforms to L2
  - artifact: docs/research-rubric.md defines evidence freshness and inference boundary
    layer: L2
    reason: non-code review contract
  - artifact: templates/research-memo.md gives repeatable memo sections
    layer: L3
    reason: non-code execution artifact realizing L2
  - artifact: docs/reviews/sample-memo-review.md scores a memo against the rubric
    layer: L4
    reason: validation evidence for a non-code L3 output
  - artifact: test adds a required field because implementation needs it
    layer: drift
    reason: route back to L2 before treating it as valid
  - artifact: passing CI is used to claim product acceptance
    layer: invalid_upgrade
    reason: L4 proves validation evidence only; acceptance is separate
```
