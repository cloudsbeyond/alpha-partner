---
type: "Architecture"
title: "Formal Code Review Integration"
description: "Approved design for composing alphaX formal development with Open Code Review, validation, PR feedback, closeout, and a skill-scoped derived knowledge map."
tags: ["alphax", "formal-development", "code-review", "open-code-review", "validation"]
---
# Formal Code Review Integration

## Status And Scope

This document records the owner-approved design and current local validation
state for integrating Alibaba Open Code Review (`ocr`) into alphaX
formal-development work. The Source candidate and delegation flow are validated
locally. This does not establish accepted publication, installed AlphaX parity,
fresh F11 live replay, managed-model behavior, or owner/product acceptance.

```yaml
design_status: approved
implementation_status: validated-local
managed_mode_evidence: guarded-unproven
managed_mode_failure_class: managed-llm-unapproved
primary_scope: Alpha Partner Source work
integration_owner: skills/formal-code-review
external_dependencies:
  - Open Code Review Codex plugin
  - local ocr CLI
optional_downstream_integrations:
  - verification-before-completion
  - GitHub PR comment handling
  - GitHub Actions CI diagnosis
  - alphaX project closeout
```

## Goal And Non-Goals

Goal: add a reusable bridge that reviews L3 code against current project
context and returns bounded L4 review evidence without changing L0-L2 authority.

Non-goals:

- Do not make alphaX a code-review runtime, model gateway, or knowledge base.
- Do not copy or fork the upstream Open Code Review plugin.
- Do not let review output rewrite product narrative, PRD, architecture, or
  formal contracts.
- Do not treat OCR findings, passing tests, or CI status as human acceptance.
- Do not enable automatic fixes, PR comments, merge blocking, or code egress by
  default.
- Do not introduce an alphaX-root `wiki/` or a second project truth surface.

## P0 Flow

```text
project product narrative + PRD + architecture + formal contracts
  -> alphaX formal-development confirms the active L0-L2 path
  -> alphax:formal-code-review selects one explicit OCR mode
  -> OCR reviews the bounded L3 target
  -> findings are verified and routed to the responsible layer
  -> tests and project checks produce additional L4 evidence
  -> optional PR/CI handling and alphaX closeout consume the evidence
```

The bridge is downstream-only. A missing or contradictory L0-L2 path produces
questions or a review packet; it does not authorize the bridge to invent review
requirements.

## Ownership And Composition

| Surface | Responsibility | Authority boundary |
| --- | --- | --- |
| Target project source | Product intent, architecture, contracts, code, tests | Sole project truth |
| `alphax:formal-development` | Route changes through the existing L0-L4 chain | May identify drift; does not replace project truth |
| `alphax:formal-code-review` | Select OCR mode, bound context, normalize findings and evidence | L3/L4 only |
| Open Code Review plugin and CLI | Deterministic file/rule selection and review execution | External replaceable carrier |
| Verification workflow | Run current project commands and read complete results | Proves only the covered validation claims |
| GitHub workflows | Read or address PR comments and diagnose CI when requested | External writes require explicit authority |
| alphaX closeout | Classify current completion state from evidence | Cannot promote to owner acceptance |

`formal-code-review` is a Source skill packaged by the alphaX plugin. The Open
Code Review, Superpowers, GitHub, and CoXX plugins stay separately versioned.
The bridge refers to their public skill contracts when installed and otherwise
falls back only to the documented local CLI path. It never patches generated
marketplace or cache copies.

## Dual-Mode Policy

### Delegation Mode

Delegation is the default for routine local and project-bound work.

```bash
ocr delegate preview --format json [--from BASE --to HEAD | --commit SHA]
ocr delegate rule --format json REVIEWABLE_FILE...
```

OCR provides review target resolution, exclusions, and applicable rules. The
host Codex agent reads the bounded diffs and current project context, accounts
for every previewed file, and produces structured findings. Delegation requires
no OCR-side model endpoint.

### Managed Mode

Managed mode is an explicit independent-model review path.

```bash
ocr llm test
ocr review --audience agent --background-file BOUNDED_CONTEXT.md \
  [--from BASE --to HEAD | --commit SHA]
```

Managed mode runs only when all of the following are true:

- the user or project contract explicitly requests independent-model review;
- the configured model endpoint is already approved for the target code;
- `ocr llm test` succeeds in the current environment;
- the requested target and context satisfy the project's data boundary.

The bridge never silently changes delegation to managed or managed to
delegation. Failure in the selected mode stops that review path and reports the
failure class. Credentials remain in approved environment or OCR configuration
surfaces and are never written to project or Alpha Partner Source.

## Context Boundary

The bridge first resolves the real repository, nearest `AGENTS.md`, review
target, live diff, and current formal-development path. Background context is a
bounded summary with project-relative references, not a copy of complete PRD,
architecture, contracts, source files, transcripts, or hidden reasoning.

Minimum context:

```yaml
objective: string
prd_refs: [project-relative product or requirement reference]
yaml_refs: [project-relative architecture, schema, registry, or contract reference]
review_target: workspace|range|commit
base: resolved-ref-or-null
head: resolved-ref
authority_and_data_boundary: string
```

If formal context is absent but code review is still meaningful, the bridge may
review implementation defects with the missing contract context stated as a
limitation. It must not infer absent requirements.

## Review And Evidence Contract

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

Raw model reasoning, credentials, unredacted logs, and temporary private code
snippets are not durable evidence. A finding without current source or contract
support remains `needs-evidence`. Low-value likely false positives are omitted
from the user-facing result but still count neither as confirmed findings nor as
proof that the reviewed area is defect-free.

When a durable local review artifact is needed, use the target project's
existing review convention. If none exists and alphaX local data is allowed,
use ignored `.alphaX/reviews/formal-code-review/`. Never write concrete target
project facts or raw review sessions into Alpha Partner Source.

## Finding Routing

- A clear implementation defect against a current contract routes to an L3 fix.
- A code/contract mismatch with uncertain responsibility routes to L2 contract
  drift and stops automatic fixing.
- A system-boundary ambiguity routes to an L1 architecture question.
- A product-scope or acceptance ambiguity routes to an L0 owner decision.
- Fixes occur only when the user requested implementation or explicitly
  approved the proposed review fixes.
- After fixes, rerun the relevant OCR target and fresh project validation before
  claiming resolution.

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

## Skill-Scoped Derived Knowledge Map

Long-lived reusable patterns belong to `formal-code-review`, not to the alphaX
product root. The allowed carrier is:

```text
skills/formal-code-review/references/use-cases/
  index.md
  validated-pattern.md
```

This is a small derived knowledge map maintained with source-first Wiki
discipline. It is not an alphaX-root Wiki and is not a project truth surface.
The LLM Wiki tooling may audit, index, or refresh these pages, but it is not a
runtime dependency and cannot update them without `Audit -> Confirm -> Apply`.

Promotion criteria:

- a real use produced direct validation evidence;
- the pattern is reusable beyond one task;
- the page contains only sanitized generic knowledge;
- every claim links to current generic Source contracts or public upstream
  documentation;
- concrete project paths, status, pilot evidence, transcripts, secrets, and raw
  model output have been removed;
- the update scope receives explicit confirmation.

Knowledge flow is absolute and one-way:

```text
target project truth
  -> target-local review evidence
  -> sanitized and independently checked generic pattern
  -> formal-code-review use-case map
```

During later reviews, a use-case page may suggest a check and must link back to
the current target project for verification. It cannot generate an OCR rule,
create a defect claim, change L0-L2, or write to the target project. When no
current project evidence supports the pattern, the result is `unknown`.

Do not pre-populate speculative pages. Create the index and promotion contract
with the skill, then add pattern pages only after qualifying evidence exists.

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

## Planned Source Changes

Implementation should make the smallest coherent Source delta:

1. Add `skills/formal-code-review/SKILL.md` with dual-mode routing, evidence,
   failure, and stop contracts.
2. Add a focused reference for mode/evidence details and the empty use-case map
   index plus promotion contract.
3. Update `formal-development` to route coding L3/L4 review through the bridge
   when applicable without making OCR mandatory for all projects.
4. Register the skill in the invocation contract, session runbook, operating
   system, Source map, plugin metadata, generated indexes, and trigger fixtures.
5. Extend Source/plugin tests to cover discovery, packaging, default delegation,
   explicit managed mode, no silent fallback, evidence fields, and knowledge
   authority boundaries.
6. Build and verify a dirty candidate package before acceptance. After a clean
   accepted Source commit, install through the one-way publication path and
   verify package/marketplace/cache parity.
7. Add the upstream OCR marketplace and CLI only after source design and tests
   are ready; verify delegation behavior and the managed-mode credential gate
   separately.

## Verification Plan

Source verification:

```bash
python3 -m unittest discover -s tests -v
node scripts/generate-alphaX-indexes.mjs --check
bash scripts/verify-alpha-source.sh
python3 scripts/alphax_plugin.py verify-source
```

Skill validation must check frontmatter and resource references with the current
`skill-creator` validator. Plugin tests must prove the new Source skill appears
byte-identically in generated packages.

Behavior fixtures must cover at least:

- a routine formal-development code change selects delegation mode;
- an explicit independent-model request selects managed mode;
- managed preflight failure stops without falling back;
- missing contract context produces a bounded limitation rather than invented
  requirements;
- all previewed files are reviewed or explicitly skipped;
- review findings route to L3, L2, L1, or L0 without crossing authority;
- durable artifacts exclude secrets, raw reasoning, and concrete project facts
  from Alpha Partner Source;
- a use-case candidate without qualifying evidence is not promoted.

Installation and live behavior are separate evidence layers. Static Source and
package checks cannot prove that OCR executed, the managed model was approved,
or a real review improved project outcomes.

## Acceptance Criteria

The integration is complete only when:

- the bridge skill and all planned references are present in canonical Source;
- trigger, Source, skill, package, and parity checks pass;
- the OCR CLI and Codex plugin are installed from their declared upstream;
- a fresh delegation-mode review proves target coverage and normalized output;
- managed mode either passes against an explicitly approved endpoint or is
  reported as guarded-unproven with the exact missing owner evidence;
- formal-development and closeout preserve the L0-L2/L3-L4 boundary;
- the use-case map exists under the bridge references and contains no
  speculative or project-private page;
- residual risks and external proof gaps remain explicit.
