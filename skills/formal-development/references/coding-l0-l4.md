---
type: "Reference"
title: "Coding L0-L4"
description: "Coding formal-development coverage, minimum L0-L4 shape, L4 evidence carriers, and few-shot examples for software, scripts, plugins, apps, services, data pipelines, and agent runtime work."
tags: ["formal-development", "coding", "l0-l4", "validation"]
---
# Coding L0-L4 / 编码场景

Load this file for software, scripts, plugins, apps, services, data pipelines,
agent runtime work, or any change whose L3 carrier is code.

```yaml
coverage:
  examples: [product, tool, plugin, script, service, frontend app, data pipeline, agent workflow]
  rule: product intent must pass through architecture narrative and contracts before code claims completion
  non_goal: do not turn every local code edit into a full L0-L4 redesign
```

Minimum coding shape:

```yaml
coding_minimum_shape:
  l0_product:
    carrier: README.md + PRD.md
    example: import workflow for external source requests
  l1_architecture:
    carrier: architecture/README.md
    example: request lifecycle, source adapter boundary, authority model
  l2_contract:
    carrier: architecture/concept-registry.yaml#import_request
    example: required source, authority, and scope fields
  l3_execution:
    carrier: src/import/request.ts + src/import/adapters/github.ts
    example: concrete module and adapter implementation
  l4_validation:
    carrier: npm test -- import-request + test-results/import-request.json
    example: contract test and artifact
```

Coding L4 carriers:

```yaml
coding_l4_carriers:
  - test command
  - contract test
  - harness
  - CI result
  - AI Contract Index
  - fixture comparison
  - runtime or manual acceptance artifact
```

Minimal coding L4:

```yaml
expectation: import request preserves source, authority, and scope fields
refs:
  l0: [README.md#import-workflow, PRD.md#p0-scope]
  l2: [architecture/concept-registry.yaml#import_request]
  l3: [src/import/request.ts]
evidence:
  command: npm test -- import-request
  artifact: test-results/import-request.json
result: pass
residual_risk: manual product acceptance not yet complete
```

Coding few-shot:

```yaml
examples:
  - artifact: README section explaining why import workflow exists
    layer: L0
  - artifact: architecture/README lifecycle and adapter boundary
    layer: L1
  - artifact: JSON schema or concept registry for import_request
    layer: L2
  - artifact: src/import/request.ts and github adapter
    layer: L3
  - artifact: saved contract test output
    layer: L4
  - artifact: implementation adds a new required field absent from schema
    layer: drift
    action: return to L2 before accepting implementation
```
