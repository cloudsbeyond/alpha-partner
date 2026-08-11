---
name: formal-code-review
description: "Use when formal code review / 形式化代码审查 is requested; when OCR review is needed inside formal development; for delegation review, independent-model review, branch, commit, or workspace review with L0-L4 routing; or when review evidence is needed for alphaX closeout."
---

# Formal Code Review

## Core Contract

```yaml
default_mode: delegate
managed_mode_requires_explicit_request: true
silent_mode_fallback: forbidden
layer_boundary: L3 review and L4 evidence only
project_truth: current target project source and contracts
```

## Workflow

1. Resolve repository, nearest AGENTS.md, target, diff, and current contract refs.
2. Select exactly one mode; use delegation unless managed mode was explicit.
3. Read `references/mode-and-evidence.md` before executing OCR.
4. Account for every previewed file and verify material findings from current source.
5. Route findings without changing L0-L2.
6. Run fresh project validation after approved fixes.
7. Report evidence, missing evidence, and residual risk.

## Knowledge Boundary

Read `references/use-cases/authority-and-promotion.md` only when evaluating a reusable pattern. Never load a use-case page as a project requirement or OCR rule.
