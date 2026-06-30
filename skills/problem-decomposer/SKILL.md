---
name: "problem-decomposer"
description: "Use when a user asks to decompose a problem, asks what a task is really solving, asks what the real problem is, asks for the essence, or appears stuck optimizing a local task without a clear higher objective, evaluation method, or feedback loop."
---

# 问题拆解器

```yaml
skill: problem-decomposer
purpose: move from assigned task to real problem, redefined problem, higher objective, and evaluation loop
not: script or forced template when context is weak

naming_boundary:
  D0-D3: problem decomposition levels
  L0-L4: requirements-to-code chain
  rule: do not confuse D-level reasoning with L-level delivery ownership

Interaction Language:
  default: user's language
  stable_identifiers: [D0, D1, D2, D3]
  source_file_or_publication: follow target language requirement

when_to_use:
  - user asks to decompose task/problem
  - user asks what task is really solving
  - user asks real problem/objective
  - user asks for first-principles challenge
  - team is stuck in local optimization
  - technical plan lacks business objective or evaluation
  - current task may be means mistaken for end

workflow:
  D0:
    label: Current Task
    asks:
      [current task, local improvements, optimization ceiling, bottleneck type]
    rule: acknowledge value, then state boundary
  D1:
    label: Real Problem
    asks:
      [why do task, real problem behind it, alternate paths, hidden assumption]
    rule: question whether assigned action is the right path
  D2:
    label: Redefined Problem
    asks:
      [
        higher-goal effect,
        wrong framing,
        adjacent/upstream problem,
        new solution path,
      ]
    rule: look for leverage unlocked by redefining the problem
  D3:
    label: Higher Objective And Loop
    asks: [higher objective, metric/proxy/signal, next action, feedback loop]
    rule: reduce abstraction until observable

output_shape:
  D0 Current Task:
    Task: ""
    Possible improvement: ""
    Current bottleneck: ""
    Validation metric: ""
  D1 Real Problem:
    Upward question: ""
    Real problem: ""
    Ignored path: ""
    Breakthrough direction: ""
    Validation metric: ""
  D2 Redefined Problem:
    Upward question: ""
    Redefinition: ""
    New objective or question: ""
    New solution direction: ""
    Validation metric: ""
  D3 Higher Objective And Loop:
    Higher objective: ""
    Evaluation method: ""
    Improvement path: ""
    Positive loop: ""
  Recommended Focus:
    Focus on D?: ""
    Reason: ""
    Next step: ""

focus_rule:
  D0: task has clear low-cost upside and remains tied to objective
  D1: repeated task optimization has shrinking returns
  D2: original problem is likely wrongly framed
  D3: shared objective, evaluation, or feedback loop is missing

mousetrap_reference:
  D0: improve mousetrap
  D1: catch mice
  D2: eliminate mice
  D3: protect grain
  key_move: understand objective -> define evaluation -> improve -> form feedback loop

missing_information:
  rule: best supported decomposition; mark first weak layer; ask smallest missing question
  useful_questions:
    - what business or user outcome does this affect?
    - how is success evaluated?
    - what has already been tried?
    - what constraint makes current task necessary?
    - what failure would make current task irrelevant?

alpha_partner_use:
  use_before:
    [
      locking P0,
      large architecture/product direction,
      Spec Checkpoint when P0 may be wrong level,
    ]
  use_when: project stuck in implementation details
  preserve_in:
    [thinking-loop packet, project-loop packet, local process decision entry]
  durable_memory_update: explicit user approval only
```
