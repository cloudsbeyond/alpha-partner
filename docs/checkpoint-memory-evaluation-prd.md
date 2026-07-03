---
type: "PRD"
title: "Checkpoint Memory Evaluation PRD"
description: "Why/how contract for checkpoint memory evaluation without runtime dependency."
tags: ["alphax", "memory", "prd"]
---
# Checkpoint Memory Evaluation PRD

```yaml
objective: prove remembered/project-local state is current, evidence-backed, and action-guiding at checkpoints
p0_flow: checkpoint -> evidence-bounded state call -> memory quality evaluation -> next action
p0_dependency: no runtime, RPC, backend, scheduler, or persistent memory service

failure_modes_addressed:
  - stale summary re-entry
  - old decision kept after user changed direction
  - remembered state cited without evidence boundary
  - recap that does not change next action

P0 Capability Scope:
  adds: [one evaluation loop, one template]
  does_not_add: [runtime backend, storage adapter, global memory writes, scheduler, connector, approval engine]

evidence_inputs:
  - live source files, specs, contracts, tests, changelog, git state, command output
  - target ignored .alphaX/project-context.md when present
  - target ignored .alphaX/evidence.md or .alphaX/decisions.md when referenced
  - source checkout ignored .alphaX/process/ for source work/review only
  - explicit user decisions and acceptance notes
  - artifacts, URLs, attachments available in active invocation
  - prior memory notes only when host already provides them

conflict_rule:
  remembered_state: evidence to verify, not authority
  wins: live source and newer explicit user decisions

dimensions:
  re-entry memory: recover current P0, boundary, risks, next action
  update memory: downgrade or replace superseded direction, terms, conclusions
  evidence memory: trace judgments to files, commands, URLs, artifacts, user decisions
  action memory: turn current state into useful next action

memory_lifecycle:
  representation: state the claim, evidence pointer, action use, and confidence
  extraction_reason: map every candidate to re-entry, update, evidence, or action continuity
  retrieval_path: name where a future agent should find it and what trigger should retrieve it
  update_or_expiry_rule: state what newer evidence, decision, command, or time boundary makes it stale
  verification_method: require live source, command output, artifact, URL, or explicit user decision before reuse
```

## DynamicMem Reference And Borrowed Ideas

```yaml
research_anchor: https://arxiv.org/abs/2606.22877
borrow:
  - evaluate memory across checkpoints
  - test stable facts and changed facts
  - separate delivered evidence failures from final wording failures
  - ask current real state and next action at every checkpoint

adapt:
  DynamicMem quarterly checkpoints: project/source lifecycle checkpoints
  user profile facts: project claims, source decisions, risks, boundaries, evidence pointers, next actions
  remembered user correctness: [re-entry memory, update memory, evidence memory, action memory]
  evidence_cutoff: later evidence may update but must not be backdated

do_not_borrow:
  - personal-assistant taxonomy
  - exact dataset or scoring pipeline
  - infrastructure-before-evaluation assumption
```

## Rubric

```yaml
calls: [pass, partial, fail]
rule: pass requires non-empty checkpoint-allowed evidence

rubric:
  re-entry memory:
    pass: current P0, boundary, main risks, next action recovered
    partial: key boundary/risk/action still needs confirmation
    fail: repeats background or relies on stale/non-checkpoint evidence
  update memory:
    pass: superseded direction/term/claim visibly downgraded or replaced
    partial: new direction noticed but old claim still mixed in
    fail: old direction remains active after newer evidence or user decision
  evidence memory:
    pass: material judgments point to allowed evidence
    partial: important judgments weakly sourced
    fail: memory-only assertion or missing source pointer
  action memory:
    pass: concrete next action, validation, blocked decision, or evidenced no-op
    partial: plausible move with unclear owner/evidence/validation
    fail: history summary only

how_it_works:
  - choose surface and checkpoint
  - define evidence cutoff
  - inspect live source and available local data
  - separate observed evidence, inference, remembered state, missing evidence
  - fill templates/checkpoint-memory-evaluation.md
  - choose next action, source change, project review, or P1/P2 parking

acceptance_signals:
  - AGENTS.md states checkpoint evaluation executable without runtime dependency
  - alphaX/operating-system.md defines evidence-input loop
  - template records evidence, calls, gaps, next action
  - template records memory lifecycle, retrieval, expiry, and verification path
  - verifier requires PRD and template
  - local process report can evaluate source iterations when local data is used

deferred_decisions:
  - whether applied evidence justifies adapter or dedicated runtime
  - whether future release adds helper commands for evidence capture
  - which evidence fields become project-pilot convention
```
