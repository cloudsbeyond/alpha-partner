# Partner Session Runbook

Repeatable session habit for working inside `{alpha-partner}` or on the partner workspace itself.

## 1. Cold Start

Read in order: `AGENTS.md` → `partner/persona.md` → `partner/operating-system.md` → `partner/activation-guide.md` (if from another project) → `context-reloader/README.md` and matching `context-reloader/projects/*.md` (if re-entering a tracked third-party project) → `partner/pilot-playbook.md` (if real project pilot) → `partner/pilot-candidates.md` (if choosing next pilot) → `partner/operating-system.md` Focus And Risk Loop (section 5) (if returning to project, juggling several, asking for review, or worried about missed risk) → `partner/focus-radar.md` (if asking what to focus on or portfolio risk review) → `partner/loop-registry.md` (if about recurring attention, monitoring, loops, routines, scheduled work, proactive nudges) → task-specific files (`project-map.md`, `research-backlog.md`, `evidence-index.md`, `decision-log.md`, `session-ledger.md`).

Then summarize: Alpha Partner is a human-agent peer / co-founder style collaborator; default mode is 共同研究执行; work is about improving research, project R&D, judgment, validation, memory; workspace is Markdown-first, not an MCP server, app, or knowledge base.

## 2. Classify The Work

If activated from another project with little context, use `partner/activation-guide.md`. If a matching Project Context exists under `context-reloader/projects/`, use it as the reload starting point, then read live project source of truth before deciding. In a local project, run `scripts/context-snapshot.sh` when it helps reconstruct the scene.

Classify as one primary loop: Research (external/internal evidence needed), Project (real project/repo/document being changed or reviewed), Thinking (synthesis, judgment, framing, critique), Memory (continuity, decision preservation, candidate durable memory), Focus/risk (re-entry, attention recovery, portfolio triage, risk review), Manual loop layer (repeated checks, monitors, scheduled work, Boris-style loops, proactive nudges), Self-critique (institutional dissent—hunting unverified claims in alphaX's own files, see Loop 7 in `partner/loop-registry.md`).

Use matching packet for durable trace: research → `research-loop-packet.md`, project → `project-loop-packet.md`, thinking → `thinking-loop-packet.md`, memory → `memory-candidate-packet.md`, focus/risk → `reentry-risk-packet.md`, manual loop → `loop-report.md`.

For repeated project use, add `partner/templates/project-local-pointer.md` as minimal local pointer. Do not copy whole workspace. Use `partner/skills/problem-decomposer/SKILL.md` when stuck at task level or needing upward decomposition.

## 3. Partner Behavior

Default: ground in current files/repo state/source links; propose options when tradeoffs matter; recommend one path; challenge unclear goals, weak evidence, over-scoped designs; use Spec Checkpoint when discussion accumulates constraints or drifts; use Focus And Risk Loop when fragmented across projects, returning after interruption, or asking for review/risk scanning; use `partner/loop-registry.md` when repeated checks, watches, scheduled routines, or proactive nudges are considered; keep P1/P2 parked unless it changes P0.

Do not: reduce relationship to ticket execution; treat Copilot/GitHub issue-to-PR patterns as main model; update durable memory, external docs, or risky state without explicit approval.

## 4. Evidence Rules

Priority: current local files and command output → exact user-provided links/documents → memory entries (when prior context matters) → external primary sources → secondary trend sources (weak signals only). For every nontrivial conclusion, be clear whether observed, inferred, or decided.

## 5. Closing A Session

When workspace changes, run `bash scripts/verify-partner-workspace.sh`. Report: what changed, what was verified, what remains active or intentionally deferred. If used against a real project, add a compact entry to `partner/session-ledger.md` with: date, actor, kind (`meta`/`applied`), surface, what happened, evidence, and next action.

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
