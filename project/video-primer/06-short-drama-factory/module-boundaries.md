# Short Drama Factory 模块边界

## 1. 边界原则

模块边界按“稳定事实源”和“执行责任”划分：

- Domain 只描述业务对象和规则，不调用 LLM、ComfyUI 或 ffmpeg。
- Application 编排业务流程，不直接解析具体 workflow 节点细节。
- Agents 负责生成结构化内容，不直接写散乱文件。
- Adapters 负责外部系统接入，不做创作决策。
- Storage 负责读写，不理解短剧质量。

## 2. 模块总览

| 模块 | 责任 | 禁止事项 |
| --- | --- | --- |
| `domain` | 定义 Project、Brief、Script、Character、Scene、Shot、Prompt、Score 等模型和校验规则。 | 禁止调用外部 API。 |
| `application` | 编排阶段、调用 agent、调用 adapter、写入项目产物。 | 禁止硬编码具体 LLM 或 ComfyUI 节点 ID。 |
| `agents` | 以结构化输入生成 brief、剧本、bible、分镜、prompt、评分建议。 | 禁止直接操作视频文件和 ComfyUI API。 |
| `adapters.llm` | 封装 LLM provider。 | 禁止决定产品流程和阶段 Gate。 |
| `adapters.comfyui` | 封装 ComfyUI API、workflow patch、输出收集。 | 禁止生成剧本和提示词。 |
| `adapters.media` | 封装 ffmpeg 粗剪、转码、截图。 | 禁止修改 shot-list 和评分结论。 |
| `storage` | 文件系统、JSON、Markdown、JSONL、SQLite 可选持久化。 | 禁止混入业务判断。 |
| `templates` | prompt 模板、项目模板、workflow preset。 | 禁止保存项目实例状态。 |
| `evals` | 用例、rubric、回归验证。 | 禁止作为运行时唯一事实源。 |

## 3. 目录边界

```text
src/short_drama_factory/
  cli/               # 用户入口
  domain/            # 纯模型和规则
  application/       # 用例服务和流程编排
  agents/            # AI 角色实现
  adapters/          # 外部系统适配
  templates/         # 模板和 preset
  evals/             # 评估用例和 rubric
  storage/           # 持久化
```

## 4. Domain 模块

### 4.1 允许

- Pydantic 模型定义。
- 字段校验。
- 状态枚举。
- 业务不变量，例如 shot 必须有 `shot_id`、`duration_sec`、`workflow_type`。

### 4.2 不允许

- 读取本地文件。
- 调用 LLM。
- 调用 ComfyUI。
- 运行 ffmpeg。
- 写日志文件。

### 4.3 主要对象

| 对象 | 说明 |
| --- | --- |
| `ProjectSpec` | 项目基本信息、目标时长、后端配置。 |
| `Brief` | 题材、角色、冲突、风格、限制。 |
| `ScriptDocument` | 大纲、剧本、对白和节奏。 |
| `CharacterBible` | 角色固定字段、参考图需求、情绪弧线。 |
| `SceneBible` | 场景空间、光线、色彩和连续性。 |
| `ShotPlan` | 镜头清单和工作流选择。 |
| `PromptPackage` | 正向、负向、版本和字段来源。 |
| `GenerationPlan` | 工作流、参数、素材和输出命名。 |
| `ScoreReport` | 评分、结论和返工建议。 |

## 5. Application 模块

Application 是主流程协调层。

### 5.1 服务

| 服务 | 责任 |
| --- | --- |
| `ProjectService` | 初始化项目、加载 project.json、阶段状态更新。 |
| `ScriptService` | 调用剧本 agent，保存脚本版本。 |
| `ContinuityService` | 生成和校验 bible。 |
| `ShotService` | 生成 shot-list 和 shot-plan。 |
| `PromptService` | 生成 prompts.json 和 prompt markdown。 |
| `GenerationService` | 生成运行计划、导出 workflow、调用生成后端。 |
| `EvaluationService` | 评分、分类、返工建议。 |
| `EditService` | 生成粗剪。 |
| `MemoryService` | 更新项目 memory 和 Shanforge 摘要。 |

### 5.2 禁止

- 直接拼接 provider-specific prompt。
- 直接访问 ComfyUI HTTP 路径。
- 直接用 `subprocess` 调 ffmpeg。
- 将大段 LLM 输出只保存在内存中。

## 6. Agent 模块

Agent 是可替换的创作单元。每个 agent 必须接受结构化输入并返回结构化输出。

### 6.1 Agent 输出契约

```json
{
  "status": "success",
  "summary": "Generated 8-shot plan",
  "artifacts": ["shots/shot-plan.json"],
  "next_actions": ["generate-prompts"],
  "warnings": []
}
```

### 6.2 Agent 列表

| Agent | 读入 | 写出 |
| --- | --- | --- |
| `ProducerAgent` | 创意、项目配置 | brief |
| `ScriptAgent` | brief | outline、script |
| `ScriptDoctorAgent` | script | 修改建议、润色稿 |
| `ContinuityAgent` | script、brief | character/scene/style bible |
| `ShotPlannerAgent` | script、bible | shot-plan |
| `PromptAgent` | shot-plan、bible | prompts |
| `AssetAgent` | shot-plan | asset-plan |
| `EvaluatorAgent` | outputs、shot-plan、bible | score report |
| `EditorAgent` | selects、shot-list | edit decision list |

### 6.3 Skill 关系

Skill 只提供方法论和模板，不作为执行后端。推荐 skill：

```text
short-drama-scriptwriting
short-drama-continuity
short-drama-shot-planning
wan22-prompt-engineering
comfyui-generation-qc
short-drama-editing
```

## 7. Adapter 模块

### 7.1 LLM Adapter

统一接口：

```python
class LLMProvider:
    def generate(self, task: LLMTask) -> LLMResult: ...
```

不允许业务服务直接调用 OpenAI、Anthropic、Gemini 或本地模型 SDK。

### 7.2 ComfyUI Adapter

统一接口：

```python
class GenerationBackend:
    def check_health(self) -> BackendHealth: ...
    def export_workflow(self, plan: ShotGenerationPlan) -> WorkflowArtifact: ...
    def submit(self, plan: ShotGenerationPlan) -> GenerationJob: ...
    def wait(self, job_id: str) -> GenerationResult: ...
    def collect(self, job_id: str) -> list[OutputArtifact]: ...
```

ComfyUI adapter 可以知道 workflow 节点结构，但不能决定镜头应该用 T2V 还是 I2V。这是 `ShotPlannerAgent` 和 `GenerationService` 的责任。

### 7.3 Media Adapter

统一接口：

```python
class MediaEditor:
    def rough_cut(self, timeline: EditTimeline) -> EditResult: ...
    def extract_frames(self, video: Path, points: list[str]) -> list[Path]: ...
```

## 8. Workflow 与 Gate 边界

| 阶段 | Gate |
| --- | --- |
| brief | 用户确认或 `--auto-approve` |
| script | 用户确认剧本方向 |
| bible | 校验角色、场景、风格字段完整 |
| shot-plan | 校验镜头总时长和必填字段 |
| prompts | 校验 prompt block 完整 |
| generation-plan | 校验素材、工作流和参数 |
| generation | 校验 ComfyUI 服务、模型、节点、显存风险 |
| evaluation | 一票否决项检查 |
| edit | 关键镜头存在检查 |

Gate 不应写在 agent prompt 中，而应写在 application 服务中。

## 9. Shanforge 集成边界

Shanforge 负责工程治理，不直接负责生成短剧素材。

| Shanforge 能做 | Shanforge 不做 |
| --- | --- |
| 初始化和纳管项目 | 直接运行视频扩散模型 |
| 管理 docs、memory、workitems | 替代 ComfyUI |
| 提供 skills 和角色协议 | 保存大体积视频输出 |
| 沉淀演进 baseline | 直接修改业务代码绕过 PR/Gate |

推荐同步点：

```text
short-drama-factory/project memory
-> .factory/memory/current-state.md
-> .factory/memory/evolution-baseline.md
```

## 10. 版本边界

| 文件 | 版本策略 |
| --- | --- |
| 剧本 | `script_v01.md`、`script_v02_polished.md` |
| Prompt | `prompt_v01`、`prompt_v02_fix-motion` |
| Workflow | `S01_SH03_i2v_v01.json` |
| 输出视频 | `S01_SH03_v01_seed102.mp4` |
| 评分 | 追加写入 `scores.jsonl` |
| 记忆 | 阶段结束后更新摘要，不逐条覆盖历史 |

## 11. 跨模块禁止事项

- Agent 不直接写最终文件，必须通过 Application/Storage。
- Prompt 模板不保存项目状态。
- Workflow patcher 不生成创意内容。
- Evaluator 不移动文件，移动建议由 Application 执行。
- CLI 不直接实现业务逻辑，只调用 Application 服务。
- Memory 不作为唯一事实源，项目 JSON 和正式文档仍是权威输入。

