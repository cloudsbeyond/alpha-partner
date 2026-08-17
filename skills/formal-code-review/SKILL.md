---
name: formal-code-review
description: "Use when formal code review / 形式化代码审查 is requested; when OCR review is needed inside formal development; for delegation review, independent-model review, branch, commit, or workspace review with L0-L4 routing; or when review evidence is needed for alphaX closeout."
---

# Formal Code Review

## Core Contract

```yaml
route_owner: formal-development
route_id: formal-code-review
carrier_kind: independently-triggerable-skill
shared_governance_contract: skills/formal-development/SKILL.md#formal-review-routes
code_execution_contract: references/mode-and-evidence.md
code_knowledge_map: references/use-cases/
layer_boundary: L3 review and L4 evidence only
project_truth: current target project source and contracts
scope_default: project-work
scope_upgrade: project-review only when the user explicitly requests completion, merge, release, handoff, or claimed-implementation judgment
scope_non_upgrade_signals: [formal code review, review this branch, findings, validation gaps]
```

## Workflow

1. Resolve scope, repository, nearest AGENTS.md, target, diff, and current
   contract refs. Keep ordinary formal code review in `project-work`; the word
   "review" and a blocked/rework result do not satisfy the scope-upgrade rule.
2. Apply the parent shared governance and select exactly one mode.
3. Read `references/mode-and-evidence.md` before executing OCR.
4. Account for every previewed file and verify material findings from current source.
5. Route findings without changing L0-L2. A missing or ambiguous P0/L0-L2
   requirement returns to that layer's owner as an upstream decision; it is
   never an `l3-fix`. Use `l3-fix` only when current implementation violates
   an already-owned L0-L2 contract.
6. Run fresh project validation after approved fixes.
7. Report evidence, missing evidence, and a distinct residual-risk statement.
   Zero reviewable code, zero OCR coverage, or no executable validation remains
   residual risk even when every available document was inspected.

## Knowledge Boundary

Read `references/use-cases/authority-and-promotion.md` only when evaluating a reusable pattern. Never load a use-case page as a project requirement or OCR rule.
