---
type: "Verification Fixtures"
title: "Agent Judgment Fixtures"
description: "Scenario fixtures for testing stronger-agent judgment beyond trigger routing."
tags: ["alphax", "fixtures", "judgment"]
---
# Agent Judgment Fixtures

```yaml
source_of_truth: agent-judgment-fixtures.json
role: readable guide only
purpose: test whether alphaX raises agent judgment quality rather than only stabilizing trigger routing
required_coverage:
  - problem reframing
  - upstream redefinition
  - alternative solution paths
  - evidence weighting
  - strongest counterargument
  - justified override of default scaffold
  - scaffold pruning
  - asset half-life

replay_contract:
  purpose: convert a source-evolution claim into evidence that one or more judgment cases changed problem reframing, upstream redefinition, alternative-path comparison, strongest counterargument keep/narrow/park call, evidence weighting, boundary call, default override, or scaffold treatment
  packet_template: ../templates/source-work/judgment-replay.md
  minimum_packet_fields: [case_ids, source_claim, observed_evidence, expected_judgment, actual_judgment, changed_call, remaining_unverified_claims]
  evidence_boundary:
    - replay can support intelligence-ceiling or half-life improvement for the tested claim
    - replay does not prove broad product-goal improvement without applied research or development problem evidence
    - passing source verifiers remains source-integrity evidence, not replay evidence

fixture_contract:
  proves:
    - problem framing can move upstream before execution
    - alternative solution paths are generated and compared before recommendation
    - evidence weighting changes completion, merge, or next-action calls
    - live source overrides memory, handoff, and stale local context
    - strongest counterargument can block weak source-work candidates
    - default scaffolding can be overridden with an explicit evidence-boundary reason
    - stale scaffolding can be separated from durable principles and pruned or replaced

cases:
  G01-upstream-contract-gap:
    tests: [problem reframing, upstream redefinition]
    expected_judgment: [state upstream gap, request or draft smallest missing decision, park downstream work]
    pass_condition: [execution stops or reframes at the responsible upstream boundary]
    forbidden: [invented business goal, downstream implementation under ambiguous contract]

  G02-merge-claim-with-weak-evidence:
    tests: [evidence weighting]
    expected_judgment: [separate implementation/validation/integration/acceptance evidence, downgrade unsupported completion claims]
    pass_condition: [completion or merge call changes when required evidence is missing]
    forbidden: [completion from design intent, checks as acceptance]

  G07-alternative-path-before-recommendation:
    tests: [alternative solution paths, evidence weighting]
    expected_judgment: [generate comparable paths after Define, state comparison criteria and evidence gaps, recommend only after explaining weaker or deferred alternatives]
    pass_condition: [at least two plausible paths are compared before final recommendation]
    forbidden: [one-solution recommendation before Define, alternatives without evidence or validation comparison]

  G03-live-source-conflicts-with-memory:
    tests: [evidence weighting, justified override of default scaffold]
    expected_judgment: [live source wins, conflict is explicit, output shape can change to show evidence boundary]
    pass_condition: [live evidence changes status, next action, or confidence]
    forbidden: [stale context as current truth, tidy status over contradiction]

  G04-source-change-needs-counterargument:
    tests: [strongest counterargument]
    expected_judgment: [state strongest counterargument, name cheapest confirm/falsify evidence, narrow or park weak candidate]
    pass_condition: [strongest counterargument changes, narrows, or parks the proposed source change]
    forbidden: [more SOP as higher intelligence, verifier success as product proof]

  G05-scaffold-default-needs-override:
    tests: [justified override of default scaffold]
    expected_judgment: [name overridden default, state evidence-boundary reason, preserve evidence/confidence/unverified_claims]
    pass_condition: [override is explicit, evidence-boundary-backed, and still preserves evidence shape]
    forbidden: [convenience skip, hidden override]

  G06-scaffold-half-life-drag:
    tests: [scaffold pruning, asset half-life]
    expected_judgment: [separate durable principle from carrier shape, soften or prune scaffold, record half-life reason]
    pass_condition: [durable principle is protected while the carrier is softened, moved, pruned, or replaced]
    forbidden: [delete core boundary with stale scaffold, freeze incidental prose as product contract]
```
