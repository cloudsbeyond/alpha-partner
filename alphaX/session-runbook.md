# Alpha Partner Source Session Runbook

Repeatable session habit for working inside `{alpha-partner}` or on the Alpha Partner source itself.

## 1. Cold Start

Read in order: `AGENTS.md` → `alphaX/persona.md` → `alphaX/operating-system.md` → `alphaX/activation-guide.md` (if from another project) → `functions/context-reloader/README.md` (if re-entering a project) → the target project's `.alphaX/AGENTS.md` and `.alphaX/project-context.md` when present → `alphaX/target-project-review-mode.md` (if reviewing one target project's delivery, handoff, merge, release, or claimed completion) → optional local `.alphaX/local/project-meta-index.yaml` only for quasi-static project clues → `alphaX/pilot-playbook.md` (if real project pilot) → optional local `.alphaX/local/pilot-candidates.md` (if choosing next pilot) → `alphaX/operating-system.md` Focus And Risk Loop (section 5) (if returning to project, juggling several, asking for review, or worried about missed risk) → optional local `.alphaX/process/focus-radar.md` (if asking what to focus on or portfolio risk review) → `alphaX/loop-registry.md` (if about recurring attention, monitoring, loops, routines, scheduled work, proactive nudges) → task-specific files under `docs/`, `templates/`, or ignored `.alphaX/`.

If a local `.alphaX/` tree is needed but absent, run `bash scripts/init-local-alphaX.sh` before relying on local process data. Then run `bash scripts/verify-local-alphaX.sh`.

Then summarize: alphaX is a personified collaboration function; default mode is Joint Research Execution; work is about improving research, project R&D, judgment, validation, memory; Alpha Partner Source is Markdown-first, not an MCP server, app, knowledge base, or centralized project context store.

## 2. Classify The Work

Before writing files, classify the runtime mode:

- **Source Evolution Mode**: the user is changing Alpha Partner Source or the
  alphaX function itself. Writes to this repository are allowed only for that
  requested source change.
- **External Assistance Mode**: the user is using alphaX to help an external
  project or problem. Treat `alpha-partner` as read-only source. Do not write to
  this repository or this checkout's `.alphaX/process/` unless the user
  explicitly switches the task to Source Evolution Mode.

In External Assistance Mode, write outputs only to the target project, the
target project's ignored `.alphaX/`, an OS temporary directory, or the
conversation response. If the current working directory is `{alpha-partner}` but
the request concerns an external project, ask before writing anything here.

If activated from another project with little context, use `alphaX/activation-guide.md`. If the target project has `.alphaX/`, use it as the target-project objective data surface, then read live project source of truth before deciding. In a local project, run `scripts/context-snapshot.sh` when it helps reconstruct the scene.

Classify as one primary loop: Research (external/internal evidence needed), Project (real project/repo/document being changed or reviewed), Target-project review (one concrete target project's claims, diff, validation, and handoff evidence), Thinking (synthesis, judgment, framing, critique), Memory (continuity, decision preservation, candidate durable memory), Focus/risk (re-entry, attention recovery, portfolio triage, risk review), Manual loop layer (repeated checks, monitors, scheduled work, Boris-style loops, proactive nudges), Self-critique (institutional dissent—hunting unverified claims in alphaX's own files, see Loop 7 in `alphaX/loop-registry.md`).

Use matching packet for durable trace: research → `templates/research-loop-packet.md`, project → `templates/project-loop-packet.md`, target-project review → `templates/target-project-review-report.md`, thinking → `templates/thinking-loop-packet.md`, memory → `templates/memory-candidate-packet.md`, focus/risk → `templates/reentry-risk-packet.md`, manual loop → `templates/loop-report.md`. If the trace is coupled to alphaX source evolution, write it under this checkout's ignored `.alphaX/process/`; if it is coupled to an external project, write it under the target project's own ignored `.alphaX/` or return it in chat. Do not add traces to the open-source function source.

For repeated project use, add `templates/project-local-pointer.md` as minimal local pointer. Do not copy the whole Alpha Partner Source into a target project. Use `skills/problem-decomposer/SKILL.md` when stuck at task level or needing upward decomposition.

## 3. Partner Behavior

Default: ground in current files/repo state/source links; propose options when tradeoffs matter; recommend one path; challenge unclear goals, weak evidence, over-scoped designs; use Spec Checkpoint when discussion accumulates constraints or drifts; use Focus And Risk Loop when fragmented across projects, returning after interruption, or asking for review/risk scanning; use `alphaX/loop-registry.md` when repeated checks, watches, scheduled routines, or proactive nudges are considered; keep P1/P2 parked unless it changes P0.

Do not: reduce relationship to ticket execution; treat Copilot/GitHub issue-to-PR patterns as main model; update durable memory, external docs, or risky state without explicit approval.

## 4. Evidence Rules

Priority: current local files and command output → exact user-provided links/documents → memory entries (when prior context matters) → external primary sources → secondary trend sources (weak signals only). For every nontrivial conclusion, be clear whether observed, inferred, or decided.

## 5. Closing A Session

When Alpha Partner Source changes, run `bash scripts/verify-alpha-source.sh`.
When this checkout's local `.alphaX/` data is used or initialized, run
`bash scripts/verify-local-alphaX.sh`. Report: what changed, what was verified,
what remains active or intentionally deferred.

In Source Evolution Mode, if a local ledger exists, add a compact entry to this
checkout's ignored `.alphaX/process/session-ledger.md` with: date, actor, kind
(`meta`/`applied`), surface, what happened, evidence, and next action.

In External Assistance Mode, do not write to this checkout's session ledger.
Write any needed process trace to the target project's own ignored `.alphaX/`
or return a report in the conversation.

When closing a session the next agent may resume, emit a handoff state block:

```yaml
# alphaX handoff state
p0: <one-line current main line>
active_surface: <project path, repo, or conversation>
branch: <branch or n/a>
last_verified: <YYYY-MM-DD>
next_block: <one concrete next action>
open_risks:
  - id: <short-id>
    level: <P0|P1|P2|P3>
    evidence: <file, command, or note>
confidence: <high|medium|low>
unverified_claims:
  - <claim asserted but not yet proven by evidence>
```

Rules: record `unverified_claims` even when checks passed (passing checks ≠ human/product acceptance); state real `confidence`; when input came from another agent, keep only verifiable evidence and demote conclusions to `unverified_claims`. This block is a habit, not a new system—keep it inline, do not create a new file format or tracker.

Do not mark the long-running goal complete unless the full collaboration system is demonstrably established.
