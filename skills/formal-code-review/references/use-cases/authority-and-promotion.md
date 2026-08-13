---
type: Reference
title: Authority And Promotion
description: One-way derived knowledge authority and audited promotion rules for formal code review use cases.
---

# Authority And Promotion

Apply the shared authority and one-way knowledge mapping in
`skills/formal-development/SKILL.md#formal-review-routes` first. This page
specializes those rules for the code-review use-case map below; it is not a
shared contract for sibling review routes.

```yaml
knowledge_authority:
  carrier: skills/formal-code-review/references/use-cases/
  flow: project truth -> local review evidence -> sanitized pattern
  promotion: Audit -> Confirm -> Apply
  automatic_ocr_rule_generation: forbidden
  automatic_knowledge_promotion: forbidden
```

## Authority Boundary

The only knowledge carrier is
`skills/formal-code-review/references/use-cases/`. It is a Source-owned,
skill-scoped derived knowledge map, not an alphaX-root Wiki and not a second
project truth surface.

```text
project truth -> local review evidence -> sanitized pattern
```

Project truth remains the current target project's source and contracts. A
use-case page may suggest a check, but it must link back to current target
evidence for verification. It cannot create a defect claim, redefine L0-L2,
write to a target project, or generate an OCR rule automatically.

## Promotion Gate

Use this one-way sequence: `Audit -> Confirm -> Apply`.

- Audit direct validation evidence and reusable applicability.
- Confirm the sanitized scope and explicitly approved update.
- Apply only the confirmed generic pattern to this use-case map.

Promote only when a real use supplied direct validation evidence, the pattern
is reusable beyond one task, and each claim links to current generic Source
contracts or public upstream documentation. When current project evidence does
not support a suggested pattern, report `unknown`.

## Prohibited Content And Actions

Forbid concrete project paths, project status, pilot evidence, transcripts,
credentials, secrets, raw model reasoning, raw model output, private logs, and
unredacted review sessions in Alpha Partner Source. Forbid automatic OCR rule
generation and automatic knowledge promotion. Do not pre-populate speculative
or validated pattern pages; add a future page only after the promotion gate is
satisfied.
