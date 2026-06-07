---
name: problem-decomposer
description: Use when a user asks to decompose a problem, asks what a task is really solving, says to "向上追问", "拆解一下", "本质是什么", or appears stuck optimizing a local task without a clear higher objective, evaluation method, or feedback loop.
---

# Problem Decomposer

Use this skill to move a conversation from "complete the assigned task" toward "understand the real problem, redefine it if needed, and align on a higher objective with evaluation."

This is a reasoning skill, not a script. Do not force a template when context is weak. If a layer lacks evidence, say what is missing instead of inventing an answer.

## Naming Boundary

This skill uses **D0-D3 decomposition levels**.

Do not confuse them with the user's requirements-to-code **L0-L4** chain:

- Requirements-to-code L0-L4 is about problem definition, structured expression, contract, engineering organization, and generated evidence.
- Problem decomposition D0-D3 is about moving from current task to real problem, redefined problem, and higher objective.

## When To Use

Use this skill when:

- the user asks to decompose a task or problem;
- the user asks what the task is really solving;
- the user asks to challenge direction from first principles;
- a team is stuck in local optimization;
- a technical plan has no clear business objective or evaluation method;
- the current task may be a means mistaken for an end.

## Workflow

### D0: Current Task

Clarify what is currently being done or requested.

Answer:

- What is the current task?
- What local improvements are naturally available?
- What is the upper bound of optimizing only this layer?
- Is the bottleneck technical, resource-related, process-related, or problem-definition-related?

Do not dismiss D0. Acknowledge its value, then state its boundary.

### D1: Real Problem

Ask why the task exists.

Answer:

- Why do this task?
- What real problem is behind it?
- If this task path were not available, what other paths might solve the same problem?
- What did the D0 framing hide?

D0 improves the assigned action. D1 asks whether the assigned action is the right way to solve the problem.

### D2: Redefined Problem

Ask whether the real problem is still too narrow or wrongly framed.

Answer:

- If D1 is solved, does the higher goal actually improve?
- Is the problem itself defined incorrectly?
- What adjacent or upstream problem would open more leverage?
- What solution paths appear only after redefining the problem?

D2 is where "improve the mousetrap" can become "do not require catching the mouse."

### D3: Higher Objective And Loop

Align on the higher objective and make it evaluable.

Answer:

- What higher objective should be protected or improved?
- What metric, proxy metric, or observable signal proves progress?
- What next action can improve that metric?
- What feedback loop keeps the work from drifting back to local optimization?

If the higher objective is too abstract, reduce it until it can be observed.

## Output Shape

Use this compact structure by default:

```text
问题拆解地图

D0 当前任务：
- 任务：
- 可做改进：
- 当前瓶颈：
- 验证指标：

D1 真正问题：
- 追问：
- 真正问题：
- 被忽略路径：
- 突破方向：
- 验证指标：

D2 重新定义：
- 追问：
- 重新定义：
- 新目标或新问题：
- 新解决方向：
- 验证指标：

D3 更高目标与闭环：
- 更高目标：
- 评估方法：
- 改进路径：
- 正循环：

建议聚焦：
- 当前建议聚焦在 D?：
- 原因：
- 下一步：
```

## Focus Rule

Recommend the focus layer using this logic:

- Focus D0 when the current task still has clear low-cost upside and remains directly tied to the objective.
- Focus D1 when the team has optimized the task repeatedly but returns are shrinking.
- Focus D2 when the original problem appears wrongly framed or a different problem definition unlocks much higher leverage.
- Focus D3 when the team lacks a shared objective, evaluation method, or feedback loop.

## Mousetrap Reference

Use this story as the reference pattern:

- D0: Improve the mousetrap.
- D1: The real problem is catching mice.
- D2: Catching mice may be unnecessary; eliminating mice may be enough.
- D3: Eliminating mice is still not the highest goal; the real objective may be protecting grain.

The key move is:

```text
understand the objective -> define evaluation -> improve -> form a feedback loop
```

## Information Gaps

When information is missing:

1. Give the best decomposition supported by current context.
2. Mark the first weak layer clearly.
3. Ask only the smallest missing question needed to continue.
4. Do not fill the map with invented business goals or metrics.

Useful missing-context questions:

- What business or user outcome does this task affect?
- How is success currently evaluated?
- What has already been tried?
- What constraint makes the current task look necessary?
- What failure would make the current task irrelevant?

## Partner Workspace Use

Inside the Alpha Partner workspace, use this skill as a thinking-loop accelerator:

- before locking a P0 main line;
- when a project is stuck in implementation details;
- before committing a large architecture or product direction;
- during Spec Checkpoint if the current P0 may be at the wrong level.

If the result should be preserved, write it into a thinking-loop packet, project-loop packet, or decision-log entry. Do not update durable memory without explicit user approval.
