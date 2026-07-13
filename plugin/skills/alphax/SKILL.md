---
name: alphax
description: Use when the user invokes @alphaX, alphaX, Alpha Partner, or asks for source work, source review, project work, project review, context reload, spec checkpointing, or focus/risk review.
---

# alphaX

alphaX is the thin Codex entrypoint for Alpha Partner Source. The plugin is a
carrier, not the Source authority, runtime, or project store.

## Source Identity Gate

Before substantive work:

1. Infer exactly one scope: `source-work`, `source-review`, `project-work`, or
   `project-review`. Ambiguous external-project requests default to
   `project-work`; completion/merge/release judgment defaults to
   `project-review`.
   Risk, progress, re-entry, or focus requests without an explicit completion,
   merge, release, handoff, or claimed-implementation review are
   `project-work`; they must not issue a completion or merge-readiness call.
   Problem-decomposition requests stay `project-work` when they inspect a live
   project; observing incomplete implementation or failed validation does not
   upgrade them to `project-review`. A request to design or evaluate a manual
   loop is also `project-work` by default, even when alphaX is named as the loop
   subject. Use a source scope only when the user explicitly asks to review or
   change Alpha Partner Source.
   Exact alphaX self-critique or source-drift triggers are `source-review`
   unless the user explicitly names target-project drift. Once selected, do not
   switch between source review and project review in one answer.
2. Derive `ALPHAX_PLUGIN_ROOT` from this installed skill path: it is the parent
   of `skills/` in the absolute path ending in `skills/alphax/SKILL.md`. Do not
   guess a machine-specific path.
3. Run the package-local resolver:

```bash
python3 "$ALPHAX_PLUGIN_ROOT/bin/alphax_plugin.py" \
  resolve-invocation \
  --plugin-root "$ALPHAX_PLUGIN_ROOT" \
  --scope <scope>
```

For `source-work` or `source-review`, check `ALPHAX_SOURCE_ROOT` first. When it
is set, pass that exact path as `--live-source-root`; never substitute the
target-project cwd. Otherwise use the current workspace only when it is the
`alpha-partner` checkout. If neither is available, report the source scope as
blocked instead of silently switching scopes. Project scopes must not require a
live checkout; they use the immutable accepted Source snapshot embedded in the
plugin.

When `ALPHAX_SOURCE_ROOT` is set, use two distinct shell arguments rather than
embedding the flag and path in one expansion:

```bash
python3 "$ALPHAX_PLUGIN_ROOT/bin/alphax_plugin.py" \
  resolve-invocation \
  --plugin-root "$ALPHAX_PLUGIN_ROOT" \
  --scope <source-work-or-source-review> \
  --live-source-root "$ALPHAX_SOURCE_ROOT"
```

4. Use only `resolved_root` from that result for the required Source reads.
5. Record this compact identity in the first progress update and final handoff:

```yaml
alphaX_source_identity:
  scope: <scope>
  package_version: <plugin version>
  package_source_commit: <carrier Source commit>
  package_source_branch: <carrier Source branch>
  package_source_authority: accepted|candidate
  source_commit: <resolved commit>
  source_branch_or_ref: <source_branch or source_ref>
  source_authority: accepted|candidate
  source_dirty: <true|false; required for source scopes>
  source_fingerprint: <fingerprint; required for source scopes>
```

`project-work` and `project-review` must resolve the embedded accepted Source
and reject a snapshot whose content hash differs from package provenance.
`source-work` and `source-review` may use an explicit working tree, but must
label it `candidate` unless it exactly matches the accepted ref and is clean.

## Required Startup

Read from `resolved_root`:

- always: `AGENTS.md`, `docs/agent-invocation-contract.md`, and
  `alphaX/session-runbook.md`;
- **Bounded project implementation fast path:** when the user supplies a
  concrete external target, an L3/L4 implementation request, and an executable
  validation signal, read `alphaX/project-work/agent-workflow.md`, target
  instructions, live source, and tests. If no re-entry, focus/risk, spec,
  research, memory, or manual-loop trigger is present, do not read activation,
  re-entry, operating-system, or loop-registry documents;
- read `alphaX/persona.md` only when behavior or tone requires it;
- read `alphaX/activation-guide.md` only for explicit engage/activation or when
  the target cannot be reconstructed from the first live-project pass;
- read `alphaX/project-work/context-reloader.md` only for project progress,
  re-entry, stale-context, or target `.alphaX/` reconstruction;
- read `alphaX/operating-system.md` only for focus/risk, research, memory,
  manual-loop, intake-rule, or non-default evidence-rubric work. The ordinary
  project delivery loop is carried by its project workflow;
- project work outside the bounded fast path:
  `alphaX/project-work/agent-workflow.md`;
- project review: `alphaX/project-review/agent-workflow.md`;
- source review: `alphaX/source-review/agent-workflow.md`;
- explicit loops, routines, nudges, and source self-critique:
  `alphaX/loop-registry.md`;
- source work: relevant `alphaX/`, `docs/`, `templates/`, `skills/`, and
  `scripts/` files.

After selecting the scope and loop, check the smallest matching Source skill.
The final response for a nontrivial run must name the selected loop and report
`skill_trigger_check` as either `checked: <source skill path>` or
`not_applicable: <reason>`; reading this plugin entry alone is not that check.

If a required file is absent, report its resolved path and continue only when a
safe non-source fallback exists.

Do not ask the user to restate full context before inspecting live project
source, Git, project-local `.alphaX/`, exact links, and relevant Source.

## Scope Guard

- `source-work`: tracked Alpha Partner Source or canonical plugin packaging may
  change after owner acceptance.
- `source-review`: report first; no tracked Source edit without scope switch.
- `project-work`: Alpha Partner Source is read-only; write only to the target
  project, its allowed ignored `.alphaX/`, temp storage, or the conversation.
- `project-review`: evidence review only; do not fix without scope switch.

Live project source wins over `.alphaX/`, memory, handoff, and summaries.
External publication, risky operations, durable memory updates, secrets, and
destructive commands require explicit approval.

## Spec Checkpoint

For PRD, solution, requirement, architecture, or product-spec alignment, run
the Source-defined Spec Checkpoint before refreshing external documents. Keep
P0 narrow, move future-useful content to P1/P2 or pending decisions, and do not
invent a new framework.

## Output Habits

- Mirror the user's language.
- Separate observed evidence, inference, missing evidence, confidence, and
  unverified claims.
- Prefer responsible-boundary fixes over one-case patches.
- Preserve alphaX as a personified collaboration function, not an always-on
  entity or control plane.
- Include one concrete next action and the Source identity for nontrivial runs.

## Conditional Contract Projection

Project only the fields required by the selected Source contract:

- Manual nudge: report candidate nudge, urgency, cooldown, and the approval
  boundary. Active-session advice is allowed; external push, scheduling, or
  cross-app observation still needs explicit approval.
- Evidence-boundary override: preserve the primary request's selected scope and
  loop; the override changes the read or evidence plan, not the routing. Name
  the exact `overridden_default` and `override_reason`, then explicitly preserve
  `observed_evidence`, `inference`, `missing_evidence`, `confidence`,
  `unverified_claims`, and `next_action`. Do not hide an override as normal
  execution. In `project-work`, report the evidence-supported `hold` or
  `rework` state without declaring the project complete/incomplete or
  merge-ready/not-merge-ready; those judgments require `project-review`.
- Problem decomposition: preserve `project-work`, explicitly name the first
  weak D0-D3 layer, and mark an unsupported higher objective as missing
  evidence instead of inventing D3.
- Alternative-path comparison: when Define and comparison criteria are strong
  enough to compare paths but evidence is too weak for an irreversible choice,
  recommend the smallest reversible pilot as the provisional path and explain
  why each alternative is deferred. If Define itself is unsupported, stop
  there rather than fabricate candidate paths.
- Insight or patch candidate: read `skills/insight-catcher/SKILL.md` and
  `alphaX/source-work/intelligence-ceiling-half-life.md`; name the
  `aligned_vision_signal`, definite `source_value` and changed judgment call,
  `landing_layer`, `smallest_source_surface`, replay support, and owner gate.
  If the input does not identify a concrete aligned signal or changed judgment
  call, hold it as missing evidence rather than inventing either value.
- Project execution with missing delivery evidence: read
  `alphaX/project-work/agent-workflow.md`; report current state, target artifact
  or decision, next action, advance/hold/rework, gate, validation method and
  evidence, feedback route, responsible-boundary rework items, changed or
  requested artifact, open residue, memory-candidate quality, and an explicit
  execute-or-reframe call. Missing values are reasons to hold or reframe, not
  reasons to omit the fields.
