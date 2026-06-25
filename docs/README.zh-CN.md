# alpha-partner 中文说明

`alpha-partner` 是 `alphaX` 的本地 source/meta base。`alphaX` 是一个带有人格化协作风格的项目协作函数，不是常驻运行实体本身。

英文公开源码是 canonical source；本文件是中文使用入口。正式合约、运行边界和 SOP 以根目录 `AGENTS.md` 为准。

## 它是什么

alphaX 是一个可复用的协作函数，用来辅助 AI 产品和软件工程工作。它可以被交付成 Skill、MCP surface、subagent 或 supervisor-agent action；这个仓库是 Markdown-first source。

它关注：

- 降低项目重新进入成本；
- 识别并复查项目风险；
- 在 handoff、合入、freeze 或发布前做项目复查；
- 维护项目 lifecycle hygiene 和本地 `.alphaX/` 压缩信号；
- 复查 alphaX source 的 contract drift 和机制漂移；
- 用 checkpoint 方式评估 re-entry、update、evidence、action 四类记忆质量；
- 通过 `agent-runtime-services` 的 memory family 能力做可选存储和召回；
- 形成有来源支撑的判断；
- 维护 contract-first 的工程链路；
- 保持实现、验证和证据可追踪；
- 定期做外部校准；
- 沉淀紧凑的决策和证据记录。

## 四类 scope

每次 alphaX 运行，在写文件前必须先判定 scope：

- **`source work`**：修改 Alpha Partner Source 或 alphaX function 本身。
- **`source review`**：复查 Alpha Partner Source、alphaX 机制或本 checkout ignored `.alphaX/process/` 治理数据；默认 report-first，不改 tracked source。
- **`project work`**：辅助某个具体项目、文档、产品问题、研究任务或工程问题；`alpha-partner` 是只读 source。
- **`project review`**：在 handoff、合入、release、freeze 或声称完成前，对一个具体项目做 report-first 证据复查。

Scope guard 是每个 scope 对应的写入边界。`project work` 和 `project review` 只能写到被辅助项目、该项目 ignored `.alphaX/`、系统临时目录，或直接在对话里报告。`source review` 可在有用且允许时写入本 checkout ignored `.alphaX/process/` 的 source-facing note；tracked source 修改必须切到 `source work`。

## 快速开始

新会话先读：

```text
AGENTS.md
alphaX/session-runbook.md
```

本地初始化和验证：

```bash
bash scripts/init-local-alphaX.sh
bash scripts/verify-local-alphaX.sh
bash scripts/verify-alpha-source.sh
```

可以把私有字面量加入 `.alphaX/local/private-patterns.txt`；如果这些内容出现在 GitHub-tracked tree，source verifier 会失败。

## Memory Family Helper

`scripts/alphaX-memory-family-rpc.mjs` 是本 source 当前交付的
`agent-runtime-services` 常驻 memory family JSON-RPC helper。plugin skill 后续可以复用
这个脚本，但本轮不刷新已安装 plugin。why/how 合约见
`docs/checkpoint-memory-evaluation-prd.md`。

```bash
node scripts/alphaX-memory-family-rpc.mjs describe
node scripts/alphaX-memory-family-rpc.mjs memory.event.append event.json
node scripts/alphaX-memory-family-rpc.mjs memory.claim.upsert claim.json
node scripts/alphaX-memory-family-rpc.mjs memory.relation.upsert relation.json
node scripts/alphaX-memory-family-rpc.mjs memory.context.retrieve retrieve.json
```

默认 endpoint 是常驻本地服务 `http://127.0.0.1:8765/rpc`；可用
`RUNTIME_SERVICES_RPC_URL` 指向其他兼容常驻 endpoint。临时启动服务只用于隔离验证，
不是 alphaX 的正常运行路径。

## 常用触发

中文触发是语义触发，不依赖英文源码里的字面示例。

```text
alphaX 介入一下
帮我恢复一下这个项目现场
review 一下我现在几个项目的风险
合入前审一下这个项目声称的功能是否真的实现
这件事真正要解决的问题是什么？
```

默认交互语言跟随用户：用户用中文，alphaX 应使用中文反馈；`D0-D3`、`P0/P1/P2`、`confidence`、`unverified_claims` 这类稳定结构字段保持不翻译。

## 目录结构

- `alphaX/`：共享行为、运行循环、激活、会话、pilot，以及 `source work`、`source review`、`project work`、`project review` 四类 scope 的独有文件夹。
- `assets/`：可共享视觉资产，包括 alphaX 插件 icon。
- `templates/`：研究、项目、思考、记忆和项目本地映射模板。
- `skills/`：本地 reasoning skill。
- `docs/`：研究、证据、资产边界、本地 `.alphaX/` schema 和中文入口。
- `scripts/`：源码验证、本地 `.alphaX/` 初始化、上下文快照工具，以及
  `agent-runtime-services` memory family JSON-RPC helper。

## Source Review

`alphaX/source-review/README.md` 定义了可复用的 alphaX source review 机制，用来检查 alphaX 自身的 contract drift、证据质量、过期状态、false completion 和弱假设。

Source review 只产出 `meta`，不得触达外部项目。真正运行这个机制时，使用 `alphaX/source-review/bootstrap.md` 作为 cold-start 程序。

## Project Review

`alphaX/project-review/README.md` 定义了单个项目内的 project review。它用于在 handoff、合入、发布、freeze 或声称完成前，复查项目声明、代码改动、验证证据、source drift 和项目本地 `.alphaX/` objective data，并输出 implementation、validation、integration 和 completion-call 状态。

这个 scope 默认 report-first；如果需要落本地证据，只能写入被复查项目 ignored `.alphaX/`。如果本次 review 对 alphaX 机制本身有学习价值，可以另写一份脱敏机制反馈到本 checkout ignored `.alphaX/process/review-feedback/`，但不能复制项目事实。

当项目进入 PR/合入、handoff、freeze、发布、公开阶段，或项目本地 `.alphaX/`
显得过期/噪声过高时，使用 `templates/project-review/lifecycle-hygiene.md`
复查远端状态、公开元数据、提交形态、license 姿态、tracked source 是否干净、`.alphaX/`
是否仍被 ignored，以及项目本地 `.alphaX/` 是否需要在保留未冻结证据的前提下压缩成当前状态和证据指针。

## 数据边界

`.alphaX/` 是 ignored 的本地数据面，不进入 GitHub-tracked tree。

- 项目的 `.alphaX/`：该项目的客观状态、迭代事件、证据指针和本地报告。
- 本 checkout 的 `.alphaX/local/`：本机路径、准静态项目线索和本地配置。
- 本 checkout 的 `.alphaX/process/`：只放 alphaX 自身治理、source work 和 source review 的过程数据。

开源仓库只承载可复用的函数资产：合约、SOP、模板、验证规则和通用 reasoning loop。数据资产分类见 `docs/asset-boundary.yaml`。

## 发布前检查

```bash
bash scripts/verify-alpha-source.sh
bash scripts/verify-local-alphaX.sh
git diff --check
git ls-files '.alphaX/*'
```

如果 `.alphaX/` 被 Git 跟踪，说明本地数据边界被破坏，需要先修正。

公开发布基线应来自已清理的公开源码树。旧本地历史和被忽略的 `.alphaX/`
数据不得进入公开历史。

## License

MIT。见根目录 `LICENSE`。
