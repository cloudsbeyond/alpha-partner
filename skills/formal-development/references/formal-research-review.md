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
route_owner: formal-development
route_id: formal-research-review
carrier_kind: parent-routed-profile
shared_governance_contract: skills/formal-development/SKILL.md#formal-review-routes
layer_boundary: L3 research artifact review and L4 evidence only
project_truth: current target project source, research contracts, and research materials
```

Apply the parent shared governance for route selection, `delegate|managed`
mode semantics, normalized evidence, authority, one-way knowledge mapping, and
stop behavior. This profile supplies only research-specific target, coverage,
finding, validation, egress, and failure rules.

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

Route a clear L3 artifact defect to `l3-research-fix`. Route a mismatch with the
research rubric or evidence contract to `l2-research-contract-drift`; route a
method or workflow ambiguity to `l1-research-design-question`; route a scope,
publication, decision, or acceptance ambiguity to `l0-owner-decision`. A review
may recommend a route but cannot approve its own finding or mutate L0-L2.

## Research Authority Extensions / 研究权限扩展

```yaml
research_authority_extensions:
  research_material_egress: human-owner-required-for-managed
  publication_or_decision: human-owner
```

The parent contract retains finding acceptance, external-write, human
acceptance, and automatic-promotion authority. Passing research checks, source
agreement, model consensus, or a complete material manifest remains validation
evidence only.

## One-Way Knowledge Mapping / 单向知识映射

```yaml
research_knowledge_extensions:
  private_research_material: promotion-forbidden
  unpublished_data: promotion-forbidden
  raw_model_output: promotion-forbidden
```

Apply the parent one-way knowledge mapping. This profile creates no Wiki or
knowledge carrier and adds no writeback path. Never promote concrete project
paths, private research material, raw sessions, credentials, unpublished data,
or raw model output into Alpha Partner Source.

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
