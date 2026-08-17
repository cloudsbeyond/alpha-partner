---
type: "Template"
title: "Review Feedback Report"
description: "Template for sanitized source-review or project-review mechanism feedback."
tags: ["alphax", "template", "source-review"]
---
# Review Feedback Report

```yaml
generated_frontmatter:
  type: Review Feedback Report
  title: Review Feedback Report
  date: "<YYYY-MM-DD>"
  actor: alphaX
  kind: review_feedback
  review_scope: "<project_review|source_review>"
  target_surface: "<project key|repo key|alphaX source>"
  source_alphaX_version: "<source contract|unknown>"
  write_boundary: mechanism feedback only

rule: candidate material; does not approve tracked source edits

what_helped:
  - "<mechanism, rule, template, or boundary>"
what_got_in_the_way:
  - "<ambiguity, missing field, awkward step, misleading wording>"
unused_mechanisms:
  - mechanism: "<name>"
    used: "<yes|no|partial>"
    defensive_reason: "<failure mode and trigger scenario>"
    delete_candidate: "<yes|no>"
candidate_source_iteration: "<small source change or none>"
evidence_pointers: []

source_self_critique:
  required_when: review_scope is source_review and a material mechanism risk is reported
  material_claims:
    - claim: "<specific mechanism claim>"
      cheapest_confirm_or_falsify_test: "<smallest test that can change this claim>"
      if_confirmed: "<keep|narrow|park|escalate call>"
      if_falsified: "<keep|narrow|park|escalate call>"

boundary_checks:
  target_project_facts_copied: "<no|explain>"
  secrets_or_private_paths: "<none|explain>"
  raw_transcript_or_hidden_cot: "<none|explain>"

confidence: "<high|medium|low>"
unverified_claims: []
```
