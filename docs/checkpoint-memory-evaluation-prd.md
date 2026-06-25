# Checkpoint Memory Evaluation PRD

This PRD defines the source contract for checkpoint memory evaluation and
optional storage/recall through the `agent-runtime-services` memory family.

## Product Objective

alphaX should improve long-running project continuity by proving that remembered
state is current, evidence-backed, and action-guiding at concrete checkpoints.
The P0 capability is:

```text
checkpoint -> evidence-bounded state call -> memory quality evaluation -> next action
```

When executable storage/recall is useful, alphaX uses the resident
`agent-runtime-services` service as the open-source runtime substrate:

```text
append-only event -> extracted claim -> relationship context -> retrieval bundle
```

The substrate preserves source-backed memory objects. alphaX still owns
interpretation, user-facing judgment, approvals, and action choice.

## Why This Exists

Long-running agent work fails when the agent:

- re-enters a project from a stale summary;
- keeps an old decision after the user changed direction;
- cites memory without knowing the evidence boundary;
- produces a background recap that does not change the next action.

DynamicMem makes the same issue visible at benchmark level: memory quality must
be tested across checkpoints, and failures often come from retrieval or delivered
evidence rather than final wording alone. For alphaX, the practical answer is
not to start with a bigger memory backend. The answer is to evaluate memory at
project/source lifecycle checkpoints and require evidence, update handling, and
next-action usefulness.

`agent-runtime-services` is useful here because it is a resident infrastructure
plane that already exposes the shape alphaX needs without turning the substrate
into a decision system: events are replayable, claims keep evidence and
freshness/status, relations preserve support or supersession context, and
retrieval returns a bundle rather than a final business decision.

## DynamicMem Reference And Borrowed Ideas

DynamicMem is the research anchor for the evaluation shape, not a product spec to
copy wholesale. The useful borrowings are:

- evaluate memory across checkpoints, because a final answer can hide stale or
  missing intermediate state;
- test both remembering stable facts and updating changed facts;
- separate memory retrieval or delivered evidence failures from final answer
  wording failures;
- make each checkpoint ask what the current real state is and what action should
  follow.

alphaX adapts those ideas to project and source work:

- DynamicMem's quarterly checkpoints become project/source lifecycle checkpoints
  such as re-entry, handoff, freeze, release, project review, and source work.
- User-profile facts become project claims, source decisions, risks, boundaries,
  evidence pointers, and next actions.
- "Has the agent remembered the user correctly?" becomes four dimensions:
  `re-entry memory`, `update memory`, `evidence memory`, and `action memory`.
- Retrieval evidence must be checkpoint-bounded: later evidence can update a
  claim, but it must not be retroactively presented as known at an earlier
  checkpoint.

What alphaX does not borrow:

- DynamicMem's personal-assistant application taxonomy;
- its exact dataset construction or scoring pipeline;
- a requirement to build a new long-term memory backend before evaluating
  memory behavior.

## P0 Capability Scope

P0 introduces one evaluation loop and one source-level helper script.

### Checkpoint Memory Evaluation

Evaluate four dimensions:

- `re-entry memory`: can alphaX recover current P0, boundary, risks, and next
  action?
- `update memory`: can alphaX downgrade or replace superseded direction,
  terminology, and conclusions?
- `evidence memory`: can alphaX trace judgments to files, commands, URLs,
  artifacts, or explicit user decisions?
- `action memory`: can alphaX turn current state into the next useful action?

Each dimension must produce `pass`, `partial`, or `fail` with evidence and a
gap. Unsupported claims stay in `unverified_claims`.

Rubric:

| Dimension | Pass | Partial | Fail |
| --- | --- | --- | --- |
| `re-entry memory` | Current P0, boundary, main risks, and next action are recovered from checkpoint-allowed evidence. | Some current state is recovered, but a key boundary, risk, or next action still needs confirmation. | The output mostly repeats background, misses the current state, or relies on stale/non-checkpoint evidence. |
| `update memory` | Superseded direction, terminology, claims, or conclusions are explicitly downgraded, replaced, or linked through `supersedes` / stale status. | Newer direction is noticed, but old wording or claims remain mixed into the current state. | Old direction or frozen terminology is still treated as active after newer evidence or user decision. |
| `evidence memory` | Each material judgment points to files, commands, URLs, user decisions, or memory events/claims within the evidence cutoff. | Evidence exists for some claims, but important judgments are weakly sourced or need follow-up. | Material judgments rely on memory-only assertion, missing source pointers, or evidence from after the checkpoint without disclosure. |
| `action memory` | The evaluation produces a concrete next action, verification step, blocked decision, or explicit no-op with evidence. | It suggests a plausible move but leaves owner, evidence, or validation unclear. | It only summarizes history and does not change action, validation, or decision state. |

Cross-cutting rule: a `pass` cannot be assigned when the evidence column is
empty. A `fail` or `partial` must name the gap and either park it, assign a next
verification step, or record it under `unverified_claims`.

### Memory Family Helper

`scripts/alphaX-memory-family-rpc.mjs` is the source-level adapter for the
resident `agent-runtime-services` JSON-RPC endpoint. It supports:

- `memory.event.append`, `memory.event.get`, `memory.event.list`;
- `memory.claim.upsert`, `memory.claim.get`, `memory.claim.query`;
- `memory.relation.upsert`, `memory.relation.query`;
- `memory.context.retrieve`;
- inspection calls: `version`, `capabilities.describe`, `resources.status`.

Default resident endpoint config:

```json
{
  "agentRuntimeServices": {
    "baseUrl": "http://127.0.0.1:8765/"
  }
}
```

The default config path is `.alphaX/local/agent-runtime-services.json`. The
helper normalizes `baseUrl` to `/rpc`. Override the config file path with
`ALPHAX_MEMORY_CONFIG`, or override the resolved endpoint directly with
`RUNTIME_SERVICES_RPC_URL`. Starting a scratch service is only an isolated
validation fallback, not the normal alphaX path.

## How It Works

1. Choose the surface and checkpoint.
2. Define the evidence cutoff.
3. Inspect live source and local `.alphaX/` state.
4. Call the resident `agent-runtime-services` memory family through:

```bash
node scripts/alphaX-memory-family-rpc.mjs describe
node scripts/alphaX-memory-family-rpc.mjs memory.event.append event.json
node scripts/alphaX-memory-family-rpc.mjs memory.claim.upsert claim.json
node scripts/alphaX-memory-family-rpc.mjs memory.relation.upsert relation.json
node scripts/alphaX-memory-family-rpc.mjs memory.context.retrieve retrieve.json
```

5. Evaluate the four dimensions in `templates/checkpoint-memory-evaluation.md`.
6. Use the result to choose the next action, update source, or park P1/P2 work.

## Contract With agent-runtime-services

alphaX depends on the public memory family shape, not on internal files:

- every memory operation uses explicit `namespace`;
- retrieval uses explicit `tableName`;
- references are scoped by the operation namespace;
- claims carry `evidence`, `confidence`, `status`, `freshness`, and optional
  `supersedes`;
- retrieval returns candidates, claims, events, relations, and policy metadata
  as a bundle;
- the bundle is evidence for alphaX, not a final decision.

## Non-Goals

P0 does not add:

- a persistent alphaX runtime entity;
- global durable memory writes;
- per-checkpoint startup or ownership of the runtime services process;
- source connectors for chat, wiki, calendar, mail, CRM, or issue trackers;
- automatic approvals, task routing, or external actions;
- a new vector database contract in Alpha Partner Source;
- plugin package refresh.

## Acceptance Signals

The capability is accepted when:

- `AGENTS.md` names checkpoint memory evaluation;
- `alphaX/operating-system.md` defines the loop and ARS-backed storage/recall
  boundary;
- `templates/checkpoint-memory-evaluation.md` can record evaluation and memory
  family calls;
- `scripts/alphaX-memory-family-rpc.mjs` can describe/call allowed memory family
  methods against a compatible resident JSON-RPC endpoint;
- source verification requires the template and helper script;
- a local `.alphaX/process/` report can evaluate source iterations when local
  process data is used.

## Deferred Decisions

- Whether plugin skill packaging should bundle or reference the helper script.
- Whether a future source release should add higher-level wrappers for common
  checkpoint events and claims.
- Which namespaces/table names become conventional for concrete project pilots.
- Whether repeated applied evidence justifies a dedicated always-on runtime.
