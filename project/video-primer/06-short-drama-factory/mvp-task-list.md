# Short Drama Factory MVP 任务清单

## 1. MVP 范围

MVP 交付一个 CLI-first 工具，完成从创意到短剧项目包、Wan2.2 提示词、ComfyUI 运行计划、patched workflow、结果记录和粗剪的半自动流程。

MVP 必须完成：

- 项目初始化。
- Brief、剧本、bible、shot-list、prompts、generation-plan 生成。
- Wan2.2 workflow patch 导出。
- ComfyUI 服务健康检查。
- 手工导入输出并评分。
- ffmpeg 粗剪。
- 项目记忆沉淀。

MVP 可以延后：

- Web UI。
- 多用户协作。
- 远程 worker 调度。
- 全自动批量重跑。
- 高级视觉模型评分。
- 多视频生成后端。

## 2. 里程碑

| 里程碑 | 目标 | 退出标准 |
| --- | --- | --- |
| M0 立项 | 文档、架构、模块边界完成 | PRD、架构、模块边界、任务清单可评审 |
| M1 CLI 骨架 | 可初始化项目和读取配置 | `sdf init` 可用，测试通过 |
| M2 创作规划 | 自动生成 brief、剧本、bible、shot-list、prompts | 示例创意可生成完整项目规划 |
| M3 ComfyUI 半自动 | 可导出 patched workflow | 生成的 JSON 可拖入 ComfyUI 检查 |
| M4 评分与粗剪 | 可导入输出、评分、粗剪 | 6 镜头样例可输出 `v01_rough.mp4` |
| M5 Shanforge 纳管 | 文档、任务、memory 同步 | 可用 Shanforge 跟踪工作项和演进 |

## 3. 任务列表

### TASK-001 初始化独立项目仓库

估算：0.5 人天

优先级：P0

内容：

- 创建 `short-drama-factory` 项目。
- 配置 `pyproject.toml`、`uv`、`ruff`、`pytest`。
- 创建基础包结构。

验收：

- `uv run pytest` 可执行。
- `uv run ruff check .` 可执行。
- 包名 `short_drama_factory` 可导入。

### TASK-002 建立 CLI 入口

估算：0.5 人天

优先级：P0

内容：

- 使用 Typer 创建 `sdf` CLI。
- 实现 `sdf --help`、`sdf version`。
- 设计全局参数：`--project`、`--config`、`--yes`。

验收：

- `sdf --help` 展示命令树。
- CLI 错误返回非 0 exit code。

### TASK-003 定义 Domain 数据模型

估算：1 人天

优先级：P0

内容：

- 定义 `ProjectSpec`、`Brief`、`ScriptDocument`、`CharacterBible`、`SceneBible`、`ShotPlan`、`PromptPackage`、`GenerationPlan`、`ScoreReport`。
- 实现 Pydantic 校验。

验收：

- 缺少必填字段时校验失败。
- 典型 6 镜头样例可通过校验。

### TASK-004 实现项目初始化

估算：0.5 人天

优先级：P0

内容：

- 实现 `sdf init <project-id>`。
- 创建标准目录。
- 写入 `project.json`。

验收：

- 重复初始化不覆盖已有文件。
- 初始化后目录结构完整。

### TASK-005 实现文件存储层

估算：1 人天

优先级：P0

内容：

- JSON 读写。
- Markdown 写入。
- JSONL 追加日志。
- 路径安全检查。

验收：

- 所有写入限制在项目目录内。
- JSONL 记录包含 timestamp、stage、status、summary、artifacts。

### TASK-006 实现 LLM Provider 接口

估算：1 人天

优先级：P0

内容：

- 定义 provider 抽象接口。
- 实现至少一个 provider。
- 支持 dry-run/mock provider，用于测试。

验收：

- 无网络时测试可通过 mock provider。
- provider 错误被结构化返回。

### TASK-007 实现 Brief Agent

估算：1 人天

优先级：P0

内容：

- 输入一句创意。
- 输出 brief JSON 和 Markdown。
- 加入人工确认 Gate。

验收：

- 示例“雨夜归家”可生成完整 brief。
- brief 缺目标时长时返回 warning。

### TASK-008 实现 Script Agent

估算：1 人天

优先级：P0

内容：

- 根据 brief 生成 outline、script_v01、script_v02_polished。
- 约束目标时长和角色数量。

验收：

- 剧本包含动作、对白、情绪节奏。
- 润色版不改变 brief 硬约束。

### TASK-009 实现 Continuity Agent

估算：1 人天

优先级：P0

内容：

- 生成 `characters.json`、`scenes.json`、`style.json`。
- 提取固定身份字段、服装字段、场景色彩和连续性字段。

验收：

- 每个主要角色都有固定 prompt 字段。
- 每个核心场景都有光线、色彩、空间关系字段。

### TASK-010 实现 Shot Planner Agent

估算：1.5 人天

优先级：P0

内容：

- 把剧本拆成 6-12 个镜头。
- 为每个镜头选择 T2V/I2V/TI2V/FLF2V。
- 生成 `shot-plan.json` 和 `shot-list.md`。

验收：

- 每个镜头都有目的、动作、时长、工作流类型和失败条件。
- 总时长偏差超过 20% 时返回 warning。

### TASK-011 实现 Prompt Agent

估算：1.5 人天

优先级：P0

内容：

- 为每个镜头生成 prompt block。
- 生成 negative prompt。
- 生成 prompt 版本号和字段来源。

验收：

- 角色镜头复用 character bible。
- 相邻镜头记录连续性字段。

### TASK-012 实现 Asset Planner

估算：0.5 人天

优先级：P0

内容：

- 根据工作流类型生成素材需求。
- 检查 `inputs/` 是否已有素材。

验收：

- I2V 缺参考图时阻断 generation-plan。
- FLF2V 缺首帧或尾帧时阻断 generation-plan。

### TASK-013 实现 Generation Plan

估算：1 人天

优先级：P0

内容：

- 根据 shot-plan 和 prompts 生成 `generation-plan.json`。
- 设置默认 seed、steps、width、height、frames。
- 支持低显存 preset。

验收：

- 每个镜头都有明确 workflow preset 和输出命名。
- 默认不批量生成多个 seed。

### TASK-014 实现 Workflow Patcher

估算：2 人天

优先级：P0

内容：

- 读取 Wan2.2 workflow JSON。
- 定位并替换 prompt、negative prompt、Load Image、seed、尺寸、帧数和输出前缀。
- 输出 patched workflow。

验收：

- 课程 14B I2V 和 FLF2V workflow 至少各有一个样例 patch 成功。
- 节点定位失败时返回具体节点类型和建议。

### TASK-015 实现 ComfyUI 健康检查

估算：0.5 人天

优先级：P0

内容：

- 配置 ComfyUI base URL。
- 检查服务是否可访问。

验收：

- 服务不可用时返回 `service_unavailable`。
- CLI 提示启动 ComfyUI 或检查端口。

### TASK-016 实现 ComfyUI 自动提交 P1

估算：2 人天

优先级：P1

内容：

- 调用 `/prompt`。
- 监听 WebSocket 或查询 history。
- 收集输出路径。

验收：

- 成功生成时写入 `logs/runs.jsonl`。
- 失败时记录错误类别。

### TASK-017 实现输出导入

估算：0.5 人天

优先级：P0

内容：

- 允许用户把 ComfyUI 输出导入对应 shot。
- 记录文件、seed、prompt 版本和来源。

验收：

- `sdf outputs import S01_SH03 path/to/video.mp4` 可写入记录。
- 文件不存在时返回错误。

### TASK-018 实现评分表和手工评分

估算：1 人天

优先级：P0

内容：

- 实现评分维度。
- 支持 CLI 手工输入分数和结论。
- 生成 score-sheet Markdown。

验收：

- 评分写入 `logs/scores.jsonl`。
- A 级、重跑、淘汰三类结论可记录。

### TASK-019 实现自动评分 P1

估算：2 人天

优先级：P1

内容：

- 抽取首中尾帧。
- 调视觉模型或规则评分。
- 输出返工建议。

验收：

- 缺视觉模型时可降级为手工评分。
- 一票否决项可被记录。

### TASK-020 实现粗剪

估算：1 人天

优先级：P0

内容：

- 使用 ffmpeg 按 shot-list 顺序拼接 selects。
- 输出 `outputs/edit/v01_rough.mp4`。
- 写入 edit decision list。

验收：

- 6 个本地测试片段可拼接。
- 缺关键镜头时阻断或标记不完整。

### TASK-021 实现 Memory 更新

估算：0.5 人天

优先级：P0

内容：

- 更新 `memory/current-state.md`。
- 更新 `memory/shot-status.md`。
- 更新 `memory/evolution-notes.md`。

验收：

- 每个阶段结束后 current-state 可反映最新状态。
- 成功 prompt 和失败模式有记录。

### TASK-022 Shanforge 纳管脚本说明

估算：0.5 人天

优先级：P1

内容：

- 编写如何用 Shanforge 纳管该项目的说明。
- 映射 docs、skills、memory 和 workitems。

验收：

- 新开发者能按说明执行 `factory-init` 或历史项目纳管。
- 说明明确 Shanforge 不承载业务代码。

### TASK-023 回归测试和 eval 用例

估算：1.5 人天

优先级：P0

内容：

- 创建 mock provider 测试。
- 创建“雨夜归家”端到端规划用例。
- 创建 workflow patch 单元测试。

验收：

- 无 ComfyUI、无外部 LLM 时核心测试可跑。
- patcher 对样例 workflow 有快照测试。

### TASK-024 用户文档

估算：1 人天

优先级：P0

内容：

- 编写 README。
- 编写 quick start。
- 编写 ComfyUI 配置说明。

验收：

- 新用户能完成从创意到 patched workflow 的流程。
- 文档列出常见错误和排查方式。

## 4. 推荐实施顺序

```text
TASK-001
-> TASK-002
-> TASK-003
-> TASK-004
-> TASK-005
-> TASK-006
-> TASK-007
-> TASK-008
-> TASK-009
-> TASK-010
-> TASK-011
-> TASK-012
-> TASK-013
-> TASK-014
-> TASK-015
-> TASK-017
-> TASK-018
-> TASK-020
-> TASK-021
-> TASK-023
-> TASK-024
```

P1 自动化任务 `TASK-016`、`TASK-019`、`TASK-022` 可在半自动流程稳定后进入。

## 5. MVP 验收场景

输入创意：

```text
雨夜归家：一个疲惫的女性深夜回到公寓，发现门缝里透出陌生暖光，她犹豫后推门进入。
```

验收输出：

```text
brief.md
script/script_v02_polished.md
bible/characters.json
bible/scenes.json
bible/style.json
shots/shot-plan.json
shots/prompts.json
shots/generation-plan.json
workflows/S01_SH01_t2v_v01.json
workflows/S01_SH02_i2v_v01.json
logs/runs.jsonl
logs/scores.jsonl
outputs/edit/v01_rough.mp4
memory/current-state.md
```

通过标准：

- 6-8 个镜头完整。
- 每个镜头都有可执行提示词。
- 至少 I2V 和 FLF2V 各导出一个 patched workflow。
- 可导入手工生成输出并评分。
- 可用本地测试视频拼出粗剪。

## 6. 主要风险和预留缓冲

| 风险 | 建议缓冲 |
| --- | --- |
| Workflow patch 节点定位复杂 | 预留 1 人天做样例兼容和错误报告。 |
| LLM 输出结构不稳定 | 所有 agent 输出必须经 Pydantic 校验和修复回合。 |
| ComfyUI 自动 API 行为差异 | MVP 先保证 patched workflow 手动模式。 |
| 自动评分不可靠 | MVP 保留手工评分，自动评分只做辅助。 |
| 粗剪输入格式不一致 | ffmpeg 前增加 probe 和转码标准化。 |

