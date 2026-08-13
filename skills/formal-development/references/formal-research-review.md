---
type: "Profile"
title: "Formal Research Review"
description: "Lightweight non-coding formal-development profile for dual-mode review of bounded research artifacts with normalized evidence, human authority, and one-way derived knowledge boundaries."
tags: ["formal-development", "research", "review", "non-coding", "l3-l4"]
---
# Formal Research Review / 形式化研究评审

Use this profile when a formal-development research route needs an explicit
review of L3 research artifacts and normalized L4 evidence. It is a profile of
`formal-development`, not a standalone skill, model gateway, research runtime,
or acceptance system.

```yaml
profile: formal-research-review
parent_skill: formal-development
layer_boundary: L3 research artifact review and L4 evidence only
default_mode: delegate
managed_mode_requires_explicit_request: true
silent_mode_fallback: forbidden
shared_mode_contract: skills/formal-code-review/references/mode-and-evidence.md
shared_knowledge_authority_contract: skills/formal-code-review/references/use-cases/authority-and-promotion.md
project_truth: current target project source, research contracts, and research materials
```

The shared contract supplies the `delegate|managed` selection rule, evidence
discipline, routing direction, no-fallback rule, and stop semantics. Its OCR
commands, code target schema, file coverage fields, and code-specific failure
classes do not apply to research. Use the research carriers and normalized
envelope below.

## Mode Selection / 模式选择

### Delegation Mode

Use delegation for routine project-bound research review. The current host or
an explicitly delegated reviewer reads only the bounded materials authorized by
the project and requires no separately configured managed-model endpoint.

### Managed Mode

Run an independent managed research review only when every gate is proven:

```yaml
managed_research_gates:
  explicit_managed_request: required
  explicit_model_endpoint: required
  endpoint_reachability: required
  research_material_egress_authorization: required
  bounded_material_manifest: required
```

Authorization must cover the actual material classes sent, including source
documents, excerpts, datasets, notes, citations, and bounded background
context. Repository or code egress approval does not imply research-material
egress approval. Never infer approval from endpoint configuration or a prior
review. If any gate is absent, stop managed review with the exact gap; do not
fall back to delegation silently.

## Research Target And Coverage / 研究对象与覆盖

Resolve the current target instructions, L0-L2 research path, review question,
material manifest, freshness boundary, and exclusions before reviewing.

```yaml
research_target:
  question: bounded-review-question
  contract_refs: [project-relative-L0-L2-reference]
  material_manifest:
    - ref: project-relative-path-or-approved-source-id
      material_class: paper|dataset|interview|note|memo|other
      included: true|false
      reason: bounded-inclusion-or-exclusion-reason
  freshness_cutoff: observed-date-or-null
  authority_and_data_boundary: bounded-statement
```

Account for every declared material as reviewed or excluded with a reason.
Discovery, a search result, metadata, or a citation without a successful content
read is missing evidence, not reviewed material.

## Normalized Evidence Contract / 证据归一化合同

```yaml
research_review:
  mode: delegate|managed
  target: bounded-question-or-artifact-set
  coverage:
    declared_materials: integer
    reviewed_materials: integer
    excluded_materials: [reference-and-reason]
    coverage_rate: number
  findings:
    - claim: bounded-review-finding
      observed_evidence: [current-material-reference]
      inference: bounded-inference-or-null
      missing_evidence: [required-but-unavailable-evidence]
      confidence: high|medium|low
      unverified_claims: [claim-not-yet-supported]
      route: l3-research-fix|l2-research-contract-drift|l1-research-design-question|l0-owner-decision
      status: confirmed|rejected|needs-evidence
  validation:
    methods: [freshness-check|citation-check|counterevidence-check|rubric-check|reproduction|other]
    results: [covered-claim-and-result]
  residual_risk: [unverified-or-uncovered-risk]
```

```yaml
evidence_normalization:
  required_fields: [observed_evidence, inference, missing_evidence, confidence, unverified_claims]
  raw_model_reasoning_is_evidence: false
  review_output_is_acceptance: false
```

Route a clear L3 artifact defect to `l3-research-fix`. Route a mismatch with the
research rubric or evidence contract to `l2-research-contract-drift`; route a
method or workflow ambiguity to `l1-research-design-question`; route a scope,
publication, decision, or acceptance ambiguity to `l0-owner-decision`. A review
may recommend a route but cannot approve its own finding or mutate L0-L2.

## Human Authority / 人工权限

```yaml
human_authority:
  finding_acceptance: required
  research_material_egress: required-for-managed
  external_write_or_comment: required
  publication_or_decision: required
  human_acceptance: required
  automatic_fix_or_promotion: forbidden
```

Passing review checks, source agreement, model consensus, or a complete material
manifest is validation evidence only. It does not authorize changing research
claims, publishing a memo, making a project decision, or accepting completion.

## One-Way Knowledge Mapping / 单向知识映射

Reuse the shared knowledge authority contract for promotion gates and prohibited
content. This profile does not create another Wiki or knowledge carrier. If the
target project already uses a Wiki or derived knowledge map, preserve this
absolute direction:

```text
project truth -> local research review evidence -> sanitized pattern
```

```yaml
knowledge_mapping:
  authority: derived-map-not-source
  backlinks_only: true
  project_writeback_or_decision_authority: forbidden
  promotion: Audit -> Confirm -> Apply
  current_project_verification: required
```

The map may retain sanitized reusable patterns and backlinks to the current
project evidence. It cannot become a requirement, create a finding, decide for
the project, or write changes back. Never put concrete project paths, private
research material, raw sessions, credentials, unpublished data, or raw model
output into Alpha Partner Source.

## Failure Classes / 失败分类

| Failure class | Stop condition |
| --- | --- |
| `research-target-unresolved` | The question, artifact set, or L0-L2 research context cannot be bounded |
| `research-material-unread` | A material required for the finding was not successfully read |
| `research-coverage-incomplete` | A declared material is neither reviewed nor excluded with a reason |
| `research-finding-unverified` | A material finding lacks current observed evidence |
| `managed-model-endpoint-unapproved` | Managed mode lacks an explicitly approved model endpoint |
| `managed-research-egress-unapproved` | Managed mode lacks authorization for the bounded research materials |
| `managed-model-unreachable` | The approved endpoint fails its current reachability check |
| `research-source-drift` | Materials or contracts change after capture and before closeout |
| `knowledge-promotion-not-confirmed` | A derived mapping update lacks Audit/Confirm approval |

No failure authorizes mode fallback, material egress, source mutation, external
writes, publication, human acceptance, or knowledge promotion.
