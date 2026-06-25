# Review Feedback Report

Use this packet after a source review or project review run when
the run produced feedback useful for alphaX itself.

This packet is candidate material. It does not approve tracked source edits.

## Header

- date: `<YYYY-MM-DD>`
- actor: `alphaX`
- kind: `review_feedback`
- review_scope: `<project_review|source_review>`
- target_surface: `<project key, repo key, or alphaX source>`
- source_alphaX_version: `<vX.Y.Z or unknown>`
- write_boundary: `mechanism feedback only`

## What Helped

- `<alphaX mechanism, rule, template, or boundary that helped>`

## What Got In The Way

- `<ambiguity, missing field, awkward step, or misleading wording>`

## Unused Mechanisms

| Mechanism | Used? | Defensive Reason | Delete Candidate? |
| --- | --- | --- | --- |
| `<mechanism>` | `<yes|no|partial>` | `<failure mode and trigger scenario>` | `<yes|no>` |

## Candidate Source Iteration

- `<small source change candidate, or none>`

## Evidence Pointers

- `<PR, commit, report path, command summary, or target .alphaX report pointer>`

## Boundary Checks

- target_project_facts_copied: `<no|explain>`
- secrets_or_private_paths: `<none|explain>`
- raw_transcript_or_hidden_cot: `<none|explain>`

## Confidence

`<high|medium|low>`

## Unverified Claims

- `<claim not yet proven by repeated review runs>`
