---
type: "Template"
title: "Insight Catcher Ledger"
description: "Trace template for turning creative inputs into disposition-tracked alphaX mechanism candidates before source changes."
tags: ["alphax", "source-work", "template", "insight-catcher", "creative-inputs", "mechanism-candidates"]
---
# Insight Catcher Ledger

```yaml
generated_frontmatter:
  type: Source Work Trace
  title: Insight Catcher Ledger
  date: "<YYYY-MM-DD>"
  actor: alphaX
  kind: insight_catcher
  scope: source work

input_batch:
  source_summary: "<external content, idea, research signal, note, talk, or creative input summary; not copied content>"
  evidence_boundary: "<what was actually read or supplied>"
  private_or_local_data_excluded: true

disposition_status_values: [covered, partial, absent, parked-with-reason]

candidate_mechanisms:
  - mechanism: "<durable mechanism candidate name>"
    source_value: "<high|medium|low>"
    disposition_status: "<covered|partial|absent|parked-with-reason>"
    status_reason: "<why this status is honest>"
    existing_source_evidence: []
    gap_if_partial_or_absent: []
    do_not_convert_boundary: []
    replay_cases: []
    source_decision: "<no-change|patch-candidate|park|owner-review>"
    tracked_patch_candidate: "<yes|no>"
    evidence_before_source:
      disposition_status: "<covered|partial|absent|parked-with-reason>"
      replay_support: []
      owner_gate_needed: "<yes|no>"

judgment_trace:
  no_silent_loss_check: "<pass|fail>"
  no_narrowing_as_complete_check: "<pass|fail>"
  evidence_before_source_check: "<pass|fail>"
  trace_is_asset_check: "<pass|fail>"
  parking_honesty_check: "<pass|fail>"
  data_boundary_check: "<pass|fail>"
  omissions_or_corrections: []

exit_gates:
  hard_stop_owner_gate:
    triggered: "<yes|no>"
    reason: "<tracked source|external publication|risk operation|none>"
    action: "<owner review|continue>"
  convergence_stop:
    triggered: "<yes|no>"
    consecutive_rounds_without_new_evidence_or_state_change: 0
    action: "<owner review|continue>"
  diminishing_return_stop:
    triggered: "<yes|no>"
    state_transition: "<absent-to-partial|partial-to-covered|none>"
    action: "<stop as no_state_transition|continue>"

completion_boundary:
  proves: []
  does_not_prove: []
  next_action: "<one action>"
```
