---
type: Reference
title: Separate Review Coverage From Path Accountability
description: Keep OCR review coverage distinct from complete changed-path accountability when delegation preview excludes files.
---

# Separate Review Coverage From Path Accountability

```yaml
pattern_id: separate-review-coverage-from-path-accountability
status: validated
applicability:
  - delegate mode where the current OCR preview partitions changed paths into reviewable and excluded sets
  - reviews where excluded contract or documentation paths are read by the host as context
non_applicability:
  - managed review without equivalent preview-level reviewable and excluded path evidence
  - claims about extension support that are not re-established by the current OCR preview and version
  - claims that path accounting proves semantic completeness or defect absence
source_refs:
  - skills/formal-code-review/SKILL.md#Workflow
  - skills/formal-code-review/references/mode-and-evidence.md#Delegation-Mode
  - skills/formal-code-review/references/mode-and-evidence.md#Normalized-Review-Contract
  - skills/formal-code-review/references/mode-and-evidence.md#Failure-Classes-And-Stop-Conditions
  - skills/formal-code-review/references/use-cases/authority-and-promotion.md#Authority-Boundary
validation_evidence:
  - sanitized real delegate run: 21 changed paths, 5 OCR-reviewable and reviewed, 16 excluded as unsupported_ext, 21 explicitly accounted
  - the excluded Markdown paths informed host context review but received no OCR rule coverage
review_mode: delegate
failure_classes:
  - review-coverage-incomplete
residual_risk:
  - OCR support and exclusions can change by version, configuration, and project rules
  - full path accountability does not prove equal review depth, semantic completeness, or defect absence
  - host context reading must never be represented as OCR review or OCR rule coverage
```

## When To Use

Use this pattern only when the current delegation preview excludes one or more
changed paths, or when review evidence could otherwise conflate host context
reading with OCR review. The current preview is authoritative for the run's
reviewable and excluded sets; do not infer a permanent extension-support rule
from an earlier run.

## Evidence Accounting

Preserve every previewed `(path,status)` pair. Partition the full set into paths
reviewed with resolved OCR rules and paths explicitly skipped with the current
preview reason. Resolve OCR rules only for the preview-selected reviewable set.
An unaccounted previewed path is `review-coverage-incomplete`.

## Report Separate Facts

Report these as distinct facts when the preview supplies the required counts:

- OCR-reviewed changed-path coverage: OCR-reviewed paths divided by all changed
  paths in the preview.
- OCR reviewable-set coverage: OCR-reviewed paths divided by paths selected as
  reviewable by the current preview.
- Changed-path accountability: reviewed plus explicitly skipped paths divided
  by all changed paths in the preview.

Do not collapse these measures into one success percentage or use full
accountability to imply full OCR coverage.

## Host-Context Boundary

The host may read an excluded contract or documentation path as current context
for source-verifiable judgment. The path remains skipped for OCR and has no OCR
rule coverage. State both facts explicitly.

## Interpretation Limits

Re-establish extension support and exclusion reasons from the current OCR
preview and observed version. Complete path accountability does not prove equal
review depth, semantic completeness, defect absence, or independent review of
excluded paths. Retain those limits as residual risk.

## Authority Boundary

This pattern is an advisory evidence-accounting check. It cannot generate OCR
rules, create a target-project defect claim, redefine L0-L2, write project
truth, or substitute for current project source and contracts.
