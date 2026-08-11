---
type: Reference
title: Pattern Schema
description: Required bounded fields for future formal code review derived pattern pages.
---

# Pattern Schema

Use this schema only for a future pattern that passed the promotion gate in
`authority-and-promotion.md`. Do not create a validated pattern page without
qualifying evidence.

```yaml
pattern_id: stable-kebab-case
status: validated|stale|superseded
applicability: [bounded-condition]
non_applicability: [bounded-condition]
source_refs: [generic-source-or-public-upstream-reference]
validation_evidence: [sanitized-direct-evidence]
review_mode: delegate|managed|both
failure_classes: [stable-failure-class]
residual_risk: [remaining-risk]
```
