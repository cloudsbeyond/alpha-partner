---
type: "SOP"
title: "Intelligence Ceiling And Asset Half-Life"
description: "Source-work governance for raising alphaX judgment quality while keeping durable assets separate from short-lived scaffolding."
tags: ["alphax", "source-work", "governance"]
---
# Intelligence Ceiling And Asset Half-Life

```yaml
scope: source work
product_goal: enable agents to autonomously solve more high-value research and development problems under explicit evidence, scope, data, and human authority boundaries
source_evolution_goal: raise alphaX intelligence ceiling and extend Alpha Partner Source asset half-life

goal_boundary:
  product_goal_role: external outcome alphaX serves in project work, research, review, and engineering collaboration
  source_evolution_goal_role: internal self-iteration target for Alpha Partner Source and alphaX mechanism iteration
  rule: do not present intelligence ceiling or asset half-life as the product goal; use them to improve alphaX's ability to serve the product goal
  narrative_boundary: product goal is the external outcome; intelligence ceiling and asset half-life are source self-iteration axes
  proof_boundary:
    product_goal_progress_requires: applied research or development problem evidence
    source_evolution_progress_requires: judgment replay, applied run, or half-life evidence tied to a source mechanism

first_principles:
  amplify_judgment:
    meaning: source work should help stronger agents frame better problems, weigh evidence, challenge assumptions, and stop wrong-layer work
    not: adding more process steps, routing branches, or safer-looking templates by default
  preserve_authority:
    meaning: stronger agent capability must stay bounded by scope, write, data, decision, and human authority rules
    not: autonomous control, hidden state, external publication, or background action
  keep_current_truth_current:
    meaning: live source and direct evidence beat memory, handoff, summaries, and stale local context
    not: treating persistent memory as a source of truth
  separate_lifetimes:
    meaning: durable principles and short-lived scaffolding must be governed differently
    not: flattening all YAML fields, templates, triggers, fixtures, and verifier strings into equal source contracts

source_layers:
  root_contract_rule: AGENTS.md carries only the compact layer map and pointer; detailed governance lives here
  core_principles:
    expected_half_life: 10y_plus
    examples: [evidence fields, scope boundaries, data boundary, decision boundary, live-source priority, wrong-layer guard, false-completion guard]
    governance: thin, hard, rarely changed, protected from operational defaults
  cognitive_frameworks:
    expected_half_life: 5y_to_10y
    examples: [D0-D3, thinking loop, research loop, evidence-strength rubric, checkpoint memory dimensions, durable failure pathology concepts]
    governance: evolve from applied evidence, project reviews, and judgment fixtures
  operational_scaffolding:
    expected_half_life: 2y_to_5y_or_less
    examples: [intent buckets, trigger phrases, must-read lists, minimum outputs, template shapes, routing fixture details]
    governance: default replaceable, depreciable, and pruneable
  implementation_carriers:
    expected_half_life: current_tooling
    examples: [shell scripts, node parsers, Markdown/YAML shape, generated index implementation, string verifier checks]
    governance: freely replace when source integrity, data boundary, and semantic intent remain protected

source_work_pdca:
  plan:
    - state which intelligence-ceiling signal or half-life signal the change is meant to improve
    - classify the affected mechanism layer before editing
    - pick the responsible source boundary; do not patch downstream scaffolding when the core contract is ambiguous
    - choose the smallest source surface that can carry the durable rule
    - for creative input batches, create an insight catcher candidate ledger before tracked source changes
  do:
    - prefer clarifying source contracts, cognitive examples, or judgment fixtures over adding process volume
    - keep operational scaffolding explicit as defaults, not product identity
    - keep runtime, scheduler, connector, backend, and always-on identity outside P0 unless a later accepted contract proves they are required
  check:
    proof_boundary:
      - passing verifiers proves source integrity, not intelligence-ceiling improvement
      - docs or governance text prove intent, not behavior change
      - product-goal improvement requires applied research or development problem evidence
      - intelligence-ceiling improvement requires a judgment-case-set replay or applied run that changes problem reframing, upstream redefinition, alternative-path comparison, evidence weighting, boundary call, default override, or the keep/narrow/park call after strongest counterargument
      - asset half-life improvement requires evidence that a durable principle was separated from, or protected against, short-lived scaffolding
    judgment_replay:
      - select the smallest relevant case set from docs/agent-judgment-fixtures.json
      - record replay evidence with templates/source-work/judgment-replay.md when claiming intelligence-ceiling or half-life improvement
      - pass only when the replay changes problem reframing, upstream redefinition, alternative-path comparison, evidence weighting, boundary call, default override, scaffold treatment, or the keep/narrow/park call after strongest counterargument for the tested claim
      - keep the claim local to the tested case set; do not generalize replay success into product-goal completion
    applied_evidence_policy:
      - do not accumulate count-based samples after current judgment cases are covered
      - add another applied trace only when it covers an uncovered judgment case, exercises a materially different high-value research or development problem, exposes a concrete source mechanism gap, or is explicitly requested for owner review
      - if a new applied run satisfies existing mechanisms without changing the judgment call, treat it as weak negative evidence for adding more source
      - if repeated runs bypass a scaffold while satisfying core evidence and authority rules, open a pruning candidate for that scaffold
    convergence_gate:
      - stop the PDCA loop at owner review when three consecutive cycles recommend no tracked source change, add no new materially different external or project-bound evidence, and expose no concrete source-mechanism blocker
      - do not restart by switching to another internal alignment surface; restart only for owner review, new materially different high-value research or development evidence, an uncovered judgment case, a repeated source-mechanism gap, or a concrete verifier/source-map blockage
      - if an active goal keeps prompting after the gate is met, report the stop decision and pending owner decision instead of adding tracked source or more local process notes
    insight_catcher:
      first_deliverable: templates/source-work/insight-catcher.md
      deliverable_kind: disposition-tracked candidate ledger plus judgment trace
      required_status_values: [covered, partial, absent, parked-with-reason]
      decompose_rule: split one external input into atomic reusable mechanism candidates before grading; when a candidate is not yet a transferable mechanism, apply problem-decomposer to reach it rather than grading the raw input
      evidence_before_source: tracked source changes require disposition_status, source_decision reason, vision-value alignment, and at least one judgment replay case
      trace_is_asset: preserve omissions, narrowing corrections, parking reasons, and why the classification changed in ignored .alphaX/process/
      no_silent_loss: every identified mechanism candidate must appear in the trace with an explicit status
      no_narrowing_as_complete: partial implementation must stay partial until the stated gap is closed by source evidence or replay
      parking_honesty: covered requires real current-source evidence; otherwise use partial or parked-with-reason
      data_boundary: tracked source must stay decoupled from external article facts, private paths, ignored process records, and local plugin or runtime assets
      vision_value_gate: a patch-candidate requires alignment to at least one intelligence_ceiling_signals or half_life_signals entry; record source_value high|medium|low from that alignment; a candidate that aligns to no vision signal must be parked or marked no-change instead of becoming a patch-candidate
      source_value_tiers:
        rule: grade source_value by what judgment call the candidate changes, not by how reusable or novel it sounds
        high: changes a material judgment call in replay, for example the keep/park/patch decision, an evidence-weight-driven action or completion call, a boundary or authority call, the landing_layer or smallest_source_surface, or a default scaffold overridden with an evidence-boundary reason
        medium: strengthens an existing judgment or reduces drift risk without changing the core call, for example making an existing signal easier to apply, clarifying an already accepted boundary, or improving traceability for future replay
        low: local clarity only and cannot alone justify a patch-candidate, for example wording polish, index or router readability, or cosmetic fixture phrasing
      landing_rule: every keep names the target source layer (core_principles, cognitive_frameworks, operational_scaffolding, implementation_carriers) and the smallest source surface before a tracked patch, so a durable rule does not land on the wrong layer
      exit_gates:
        hard_stop_owner_gate:
          when: tracked source write, external publication, risky operation, durable memory update, or source-of-truth change needs approval
          action: stop at owner review with per-mechanism decision
        convergence_stop:
          when: three consecutive rounds have no new external evidence, no tracked change, and no new owner instruction
          action: stop at owner review; scope switching does not count as progress
        diminishing_return_stop:
          when: a new round produces no disposition-state transition
          action: stop as no_state_transition and ask owner whether further polish is worth it
    intelligence_ceiling_signals:
      - better problem reframing
      - alternative solution paths are generated and compared before recommendation
      - strongest counterargument is represented
      - evidence weight changes the action or completion call
      - upstream redefinition is surfaced when downstream work would patch symptoms
      - default scaffolding can be overridden with an evidence-boundary reason
      - scenario fixtures in docs/agent-judgment-fixtures.json cover the claim being made
    half_life_signals:
      - core principles are thinner or clearer
      - scaffolding is more replaceable or easier to prune
      - verifier protects boundary, consistency, and source integrity instead of incidental prose shape
      - no project facts, private paths, runtime dependencies, or hidden chain-of-thought enter tracked source
    required_commands:
      - bash scripts/verify-alpha-source.sh
      - bash scripts/verify-local-alphaX.sh when local alphaX data changed
      - git diff --check
  act:
    - keep the change only if the check shows a concrete improvement signal
    - label the change as candidate, not complete, when proof_boundary evidence is missing
    - if replay fails, narrow the source change, park it, or move it back to ignored process notes
    - park future-useful but unproven ideas in ignored .alphaX/process/
    - record what helped, what got in the way, and what was unused
    - decide the next cycle from evidence rather than completing a prewritten roadmap

pruning:
  rule: operational scaffolding must earn its keep; core principles must not be deleted merely because a current carrier rarely references them
  weak_negative_signal: lack of use in one run
  stronger_negative_signals:
    - repeated applied runs bypass the scaffold while still satisfying core evidence and authority rules
    - scaffold causes wrong-layer work, excessive conservatism, stale context acceptance, or false confidence
    - verifier string checks block valid source improvements while not protecting a boundary or consistency contract
  prune_actions:
    - soften exact wording into semantic or structural checks
    - move a rule from P0 to default guidance
    - split durable concept from current output shape
    - delete only when replacement evidence is stronger than nostalgia for the old carrier

offline_semantic_verifier_boundary:
  status: future_candidate
  can_be_amplifier_if:
    - it checks core and cognitive-framework semantics
    - it remains offline, explicit, and human-invoked
    - it improves boundary, evidence, or judgment review beyond string checks
  becomes_scope_creep_if:
    - it introduces scheduler, connector, backend, always-on watcher, hidden state, or autonomous publication
    - it treats generated semantic scores as human acceptance
```
