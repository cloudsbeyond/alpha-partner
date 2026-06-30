---
type: "Failure Modes"
title: "Agent Failure Modes"
description: "Known alphaX execution failure modes, detection signals, and mitigations."
tags: ["alphax", "failure-modes", "agent"]
---
# Agent Failure Modes

```yaml
purpose: short P0 failure list for runtime carriers
extend_only_when: repeated applied run or fixture exposes concrete failure

modes:
  IC-001:
    mode: intent misclassification
    signal: trigger asks for risk/progress/review/problem framing but chosen loop differs from docs/agent-invocation-contract.md
    mitigation: reclassify, rerun first pass, ask only if target/write boundary still unclear

  SC-001:
    mode: scope drift
    signal: project review or source review edits files without explicit scope switch
    mitigation: stop writes, report boundary conflict, ask for project work or source work approval

  EV-001:
    mode: weak evidence treated as strong
    signal: design doc, memory, chat, or stale .alphaX/ used as proof of implementation/release/acceptance
    mitigation: downgrade claim, add unverified_claims, inspect direct source or validation evidence

  EV-002:
    mode: stale context accepted as current
    signal: .alphaX/, handoff, or memory conflicts with live source but remains state call
    mitigation: live source wins; record conflict and next verification

  FC-001:
    mode: false completion
    signal: done/mergeable/releasable/healthy without implementation, validation, integration, acceptance evidence
    mitigation: use completion fields and narrowest evidence-supported call

  WL-001:
    mode: wrong-layer work
    signal: downstream patch while upstream problem, structured expression, or contract is ambiguous
    mitigation: stop at responsible boundary; return missing L0-L2 decision or contract gap

  OQ-001:
    mode: missing next action
    signal: summary does not change action, validation, or decision state
    mitigation: add one concrete next action or explicit no-op with evidence

  DB-001:
    mode: data boundary leak
    signal: project facts, private paths, process ledgers, pilot evidence, transcripts, or secrets enter tracked source
    mitigation: remove/redact; keep data in target .alphaX/ or conversation

failure_response:
  - identify mode id
  - state triggering evidence
  - apply mitigation or ask smallest missing decision
  - put unsupported claims under unverified_claims
  - record durable mechanism feedback only if sanitized and useful

non_goals: [knowledge base, scheduler policy, behavioral scoring system]
```
