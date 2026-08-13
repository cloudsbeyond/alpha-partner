---
type: Reference
title: Mode And Evidence
description: Approved OCR mode selection, review evidence, routing, stop conditions, and downstream composition for formal code review.
---

# Mode And Evidence

Apply the shared governance in
`skills/formal-development/SKILL.md#formal-review-routes` first. This file
specializes that contract for OCR execution, code targets, file coverage,
code findings, validation commands, and code-specific failure classes.

## Mode Selection

Select exactly one mode for each review. Delegation is the default; managed
mode requires an explicit independent-model review request. Never silently
change delegation to managed or managed to delegation.

### Delegation Mode

Use delegation for routine local and project-bound work.

```bash
ocr delegate preview --format json [--from BASE --to HEAD | --commit SHA]
ocr delegate rule --format json REVIEWABLE_FILE...
```

Let OCR resolve review targets, exclusions, and applicable rules. Read the
bounded diff and current project context, account for every previewed file,
and produce structured findings. Do not require an OCR-side model endpoint.

### Managed Mode

Use managed mode only when all of these conditions are true:

- The user or project contract explicitly requests independent-model review.
- The configured model endpoint is already approved for the target code.
- `ocr llm test` succeeds in the current environment.
- The requested target and context satisfy the project's data boundary.

```bash
ocr llm test
ocr review --audience agent --background-file BOUNDED_CONTEXT.md \
  [--from BASE --to HEAD | --commit SHA]
```

If the selected mode fails, stop that review path and report its failure class.
Keep credentials in approved environment or OCR configuration surfaces; never
write them to the project or Alpha Partner Source.

## Context And Artifact Boundary

Resolve the repository, nearest `AGENTS.md`, review target, live diff, and
current formal-development path before OCR. Use a bounded summary with
project-relative references, not copied PRDs, architecture, contracts, source
files, transcripts, or hidden reasoning.

```yaml
objective: string
prd_refs: [project-relative product or requirement reference]
yaml_refs: [project-relative architecture, schema, registry, or contract reference]
review_target: workspace|range|commit
base: resolved-ref-or-null
head: resolved-ref
authority_and_data_boundary: string
```

If formal context is absent but implementation review remains meaningful, state
the missing contract context as a limitation. Do not infer absent requirements.

Use the target project's existing review convention for durable local artifacts.
If none exists and alphaX local data is allowed, use ignored
`.alphaX/reviews/formal-code-review/`. Never write concrete target project
facts or raw review sessions into Alpha Partner Source.

## Normalized Review Contract

Every run reports:

```yaml
review:
  mode: delegate|managed
  target: workspace|range|commit
  base: resolved-ref-or-null
  head: resolved-ref
  ocr_version: observed-version
  rules_source: built-in-or-project-relative-rule-path
  coverage:
    total_files: integer
    reviewed_files: integer
    skipped_files: [project-relative-path-and-reason]
    coverage_rate: number
  findings:
    - path: project-relative-path
      line: integer-or-unresolved
      severity: critical|high|medium|low
      category: bug|security|performance|maintainability|test|documentation|other
      claim: bounded-finding
      evidence: current-source-or-contract-reference
      route: l3-fix|l2-contract-drift|l1-architecture-question|l0-owner-decision
      status: confirmed|rejected|needs-evidence
  validation:
    commands: [fresh-project-check]
    results: [exit-status-and-covered-claim]
  residual_risk: [unverified-or-uncovered-risk]
```

Treat raw model reasoning, credentials, unredacted logs, and temporary private
code snippets as non-durable evidence. Keep a finding as `needs-evidence` until
current source or contract support confirms it. Omit low-value likely false
positives from the user-facing result; they do not count as confirmed findings
or proof that the reviewed area is defect-free.

## Finding Routing

- Route a clear implementation defect against a current contract to `l3-fix`.
- Route a code/contract mismatch with uncertain responsibility to
  `l2-contract-drift` and stop automatic fixing.
- Route a system-boundary ambiguity to `l1-architecture-question`.
- Route a product-scope or acceptance ambiguity to `l0-owner-decision`.
- Apply fixes only when the user requested implementation or explicitly
  approved the proposed review fixes.
- After fixes, rerun the relevant OCR target and fresh project validation
  before claiming resolution.

## Failure Classes And Stop Conditions

| Failure class | Stop condition |
| --- | --- |
| `ocr-cli-missing` | The local `ocr` executable is unavailable |
| `ocr-plugin-missing` | The requested Codex OCR skill is unavailable and no approved CLI fallback is in scope |
| `review-target-unresolved` | Repository, diff base/head, commit, or workspace target cannot be resolved |
| `contract-context-missing` | The requested claim depends on absent or contradictory L0-L2 context |
| `managed-llm-unapproved` | Managed mode lacks an approved code/data boundary |
| `managed-llm-unreachable` | `ocr llm test` fails |
| `review-coverage-incomplete` | A previewed file is neither reviewed nor explicitly skipped with a reason |
| `review-finding-unverified` | A material finding lacks current source or contract support |
| `source-drift` | Project source changes after target/context capture and before evidence closeout |
| `knowledge-promotion-not-confirmed` | A derived use-case update lacks Audit/Confirm approval |

No failure class authorizes mode fallback, source mutation, credential changes,
external comments, or knowledge promotion.

## Downstream Skill References

- Use `verification-before-completion` after review and any fixes; OCR output
  does not replace tests, lint, build, or project-specific validation.
- Use `gh-address-comments` only when actionable GitHub review threads exist;
  do not reply or resolve threads without explicit write authority.
- Use `gh-fix-ci` only for failing GitHub Actions checks and keep CI root-cause
  evidence separate from OCR suggestions.
- Use `alphax-project-closeout` to record the review artifact and validation
  evidence in the current completion state; owner acceptance remains explicit.
- Use `record-replay-refine` only after a stable repeated workflow has a real
  recording artifact; an ordinary OCR session is not Record & Replay proof.
- Use `agent-devops-health` to audit installation and behavior evidence when
  its canonical source is extended; do not edit its generated plugin package.
