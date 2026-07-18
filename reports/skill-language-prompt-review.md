# Skill 语言与 Prompt 说明评审报告

评审日期：2026-07-07

评审对象：`C:\Users\uroborus\project\ember-frame\.agents\skills` 下 12 个 `SKILL.md`，以及各 `SKILL.md` 直接引用、会影响说明理解的 Markdown 工作流、质量闸门、交接契约、技巧库和 agent 任务卡。JSON schema 与 `openai.yaml` 不作为中文说明文本评分对象，仅作为输出约束来源识别。

评分口径：0-10 分，衡量说明文件作为 Codex skill prompt 的可路由性、边界清晰度、输入输出约束、流程可执行性、语言清晰度和冗余控制。分数不是部门能力或创作质量评分。

## 总评分表

| Skill | 分数 | 综合判断 | 首要修复点 |
|---|---:|---|---|
| `voice-room` | 8.3 | 边界、流程、输出、QC 都较完整，语言稳定 | 合并重复边界句，统一“配音/口型/剪辑”交接术语 |
| `prompt-room` | 8.2 | prompt 结构最清楚，输出物可检查 | 统一场景方位体系，补足失败回退与版本记录 |
| `video-production-room` | 8.1 | 技术选择、准入、QC 和 agent 分工较强 | 缩短 SKILL.md，把技巧长表更多移入引用文件 |
| `project-office` | 8.0 | 管理边界明确，可追溯性强 | 精简正文与管理标准重复处，统一状态词 |
| `music-room` | 7.6 | 简洁、可执行，输出物明确 | 补足音乐 cue、参考学习、版权边界的字段定义 |
| `edit-room` | 7.4 | 入口清楚，剪辑职责聚焦 | 修正字幕来源表述冲突，扩展交接和 QC 字段 |
| `screenwriting` | 7.2 | 工作流清楚，剧本输出有方向 | 缩短 description，明确唯一故事源与实际路径的关系 |
| `delivery-room` | 7.1 | 简洁，职责边界无大问题 | 对最终交付而言过薄，需补版本、验收、回退字段 |
| `director-room` | 7.0 | 导演判断体系强，refs 质量高 | 修复语病，压缩强修辞和重复边界，降低入口负担 |
| `imagegenpro` | 6.8 | 图像生成隔离原则清楚 | 移除通用 skill 中的项目专案锁定段，统一语言与输出模板 |
| `story-original` | 6.5 | 创作目标完整，文学标准明确 | 大幅压缩宣言式表达，把理念和技法移入 refs |
| `art-room` | 6.2 | 覆盖面最全，但最臃肿 | 拆分 872 行入口文件，去重输出规格/技巧库/线程流程 |

## 高优先级问题

### 1. 多个 `SKILL.md` 过长，入口 prompt 承担了手册职责

`art-room`、`story-original`、`director-room` 尤其明显。`SKILL.md` 同时写了触发条件、部门哲学、流程、输出规格、技巧库摘要、agent 清单、QC、调度规则和示例，导致模型进入 skill 后需要在大量非即时信息中筛选当前任务相关内容。

建议：`SKILL.md` 只保留“何时使用、先读哪些 refs、最小工作流、输出 envelope、硬性失败条件”。创作理念、长技术菜单、案例锁定、agent 详细任务卡应放入 `references/` 或 `agents/`。

### 2. Frontmatter `description` 普遍过长，影响路由精度

`art-room`、`director-room`、`story-original`、`screenwriting`、`video-production-room`、`voice-room` 的 description 把触发词、边界、输出、限制、部门定位都塞进一段。作为 skill 路由文本，它们更适合 1-2 句。

建议格式：

```text
<部门名>。用于 <核心任务>。用户提到 <3-8 个触发词> 时使用。
```

### 3. 重复内容多，后续容易漂移或冲突

高重复区域包括：

- `art-room/SKILL.md` 与 `asset-output-requirements.md`、`asset-card-prompt-templates.md`、`ai-image-technique-library.md` 重复。
- `director-room/SKILL.md` 与 `department-workflow.md`、`director-diagnostic-layer.md` 重复。
- `story-original/SKILL.md` 与 `source-backfill-workflow.md`、`quality-gate.md` 重复。
- `video-production-room/SKILL.md` 与 `ai-video-technique-library.md`、各 agent 卡重复。

建议：同一规则只保留一个权威位置，`SKILL.md` 用“必须读取 X 并按其中 Y 执行”引用，避免复述。

### 4. 存在少量语义冲突或易误读点

- `director-room/SKILL.md` 开头出现“`# 导演部` 的核心任务...”式断句，标题与正文拼接后语法不完整。
- `edit-room` 的字幕规则存在表述不一致：一处要求字幕来自剧本，另一处要求最终字幕以实际音频转写/对齐为准并回查剧本。
- `prompt-room` 的场景方位说明仍有“正面/背面/左侧/右侧”式列表，而 `art-room`、`imagegenpro` 更强调中心锚点和 NW/N/NE 方位。生产体系应统一。
- `screenwriting` refs 写“唯一输入源是 story-original”，而 `SKILL.md` 又强调路径由项目办公室契约决定。建议改成“唯一故事前提源为项目办公室批准的 story-original 输出；实际路径由项目契约决定”。
- `imagegenpro` 作为通用技能，却包含 `SC001` 级别的项目专案锁定段，容易污染其它项目。

### 5. 短 skill 的流程测试性不足

`delivery-room`、`edit-room`、`music-room` 的 `SKILL.md` 很简洁，这是优点；但它们的 refs 也偏短，对“每一步是否完整、输出是否完全满足要求”的自动测试不够友好。建议为每个部门补一张最小字段清单：必需输入、必需输出、可阻塞状态、QC 失败回退、交接对象。

## 逐 Skill 评审与精简改写建议

### `art-room` - 6.2/10

主要问题：

- 872 行入口文件过长，已经接近部门手册，不适合作为路由后的即时执行 prompt。
- `SKILL.md` 重复展开资产输出、卡片模板、技巧库、线程生成、agent 分工，和引用文件高度重叠。
- Frontmatter description 太长，且有“项目契约 制作目录”的空格/断词问题。
- “必须/不得”规则很多，但优先级不总是清楚；执行者难判断当前任务需要读哪些部分。
- 图片线程调度规则和艺术资产规范放在一起，边界偏宽。

可直接替换的精简 description：

```text
美术制作部。用于在项目契约与导演分镜明确后，规划、制作和 QC 角色、场景、道具、服装、风格圣经、九宫格参考、参考帧和图片资产。用户提到美术资产、角色卡、场景卡、道具卡、风格统一、参考帧或图片资产 QC 时使用。
```

建议替换正文骨架：

```text
# 美术制作部

先确认项目办公室交接包、导演分镜和资产需求是否存在；缺失则返回 blocked_needs_project_contract 或 needs_director_handoff。
根据任务类型只读取必要引用：workflow、artifact-contract、asset-output-requirements、asset-card-prompt-templates、ai-image-technique-library、thread-image-workflow。
输出必须使用项目办公室指定路径和 artifact envelope，不硬编码项目目录。
所有候选图、参考图、角色/场景/道具卡必须经过 asset-qc；未通过 QC 的资产不得晋升为正式资产或交给导演/提示词/视频部门。
```

### `delivery-room` - 7.1/10

主要问题：

- 作为“成片交付部”，说明过薄；最终导出、版本归档、验收回退、QC 失败处置字段不足。
- `handoff-contract.md` 和 `quality-gate.md` 结构清楚但字段较少，难以覆盖多版本交付。
- 触发条件明确，但缺少“不能替剪辑/导演返修素材”的边界句。

可直接替换的精简 description：

```text
成片交付部。用于汇总已通过剪辑和导演终审的成片，执行交付规格、最终导出、成片 QC、版本归档和用户验收。用户提到最终视频、导出、交付、终审、成片 QC 或版本归档时使用。
```

建议补充正文句：

```text
若剪辑预览、导演终审或上游素材未通过，不进入最终导出；只记录阻塞原因并退回对应部门。
交付输出至少包含 delivery-spec、final-export-manifest、final-qc-report、version-archive 和 acceptance-record。
```

### `director-room` - 7.0/10

主要问题：

- 开头语法不完整，标题后接“的核心任务”会造成阅读断裂。
- Frontmatter description 过长，几乎把整个部门职责写成一段。
- “总导演、独断、作品灵魂、手脚、观众视线”等表达重复，气势强但压缩了可执行信息。
- 与 `department-workflow.md`、`director-diagnostic-layer.md` 的边界/QC 内容重复。
- agent 清单完整，但“何时派哪个 agent、何时只由主任务完成”可更短更硬。

可直接替换的精简 description：

```text
导演部。用于把定稿剧本和项目办公室交接包转化为正式导演分镜包，裁决镜头目的、观众视线、空间调度、镜头语言、转场和导演 QC。用户提到导演启动、分镜、镜头看不懂、转场不连贯、导演判断或分镜返修时使用。
```

建议替换开头：

```text
# 导演部

导演部的核心任务是把定稿剧本和允许的上游材料转化为可供美术、提示词、视频、配音、音乐和剪辑执行的导演分镜包。导演部只裁决镜头目的、观众视线、空间调度、连续性、转场和质量判断；不执行图像生成、视频生成、配音、音乐、剪辑或项目台账维护。
```

### `edit-room` - 7.4/10

主要问题：

- 字幕来源规则需统一：剪辑字幕不应只凭剧本文字，但 quality gate 又写“字幕是否来自剧本”，容易误判。
- refs 对 EDL、预览片、音画同步、转场失败回退的字段偏少。
- “剪辑部不修失败视频素材”边界清楚，可继续保留。

可直接替换的精简 description：

```text
剪辑部。用于把通过 QC 的视频镜头、配音、音乐和字幕资料剪成可审看的预览片，并处理节奏、转场、声画同步、字幕和 EDL。用户提到剪辑、节奏、转场、字幕、声画同步、预览片或 EDL 时使用。
```

建议统一字幕规则：

```text
字幕以剧本台词为文本权威，以实际配音转写、cue sheet 和时间轴对齐为时间权威；二者不一致时必须标记差异并回退配音/编剧/导演确认。
```

### `imagegenpro` - 6.8/10

主要问题：

- 通用技能中夹入 `SC001` 专案级锁定段，虽然是示例，但会让其它项目继承不该继承的镜头/空间假设。
- 开头英文 “Center-anchor radial orientation grids” 与中文主体混排，降低入口清晰度。
- 缺少独立引用模板，导致长规则都堆在 `SKILL.md`。
- “主任务/生图子任务”隔离原则很好，但输出字段可更模板化。

可直接替换的精简 description：

```text
通用图片生成与参考帧修正流程。用于生成、重做、统一或局部修正项目图片，重点保证角色身份、场景空间、道具站位、镜头连续性、材质光影和候选图晋升规则。用户提到生图、重做参考帧、角色/场景漂移、局部修正或 candidate 晋升时使用。
```

建议移动：

```text
将 SC001 专案锁定段移入项目案例文件，例如 references/cases/sc001-radial-grid.md；SKILL.md 只保留通用的中心锚点、方位、参考图压缩、子任务隔离和 QC 规则。
```

### `music-room` - 7.6/10

主要问题：

- 结构简洁清楚，但“参考学习”边界和版权/相似度禁区可再明确。
- workflow、quality gate、handoff 都偏短，音乐 cue 的必填字段还可更测试化。
- 路径由项目办公室决定的句式多次出现，可统一为一次硬规则。

可直接替换的精简 description：

```text
音乐制作部。用于根据剧本、导演阐述、剪辑节奏和场景情绪规划或制作配乐、主题动机、环境音乐、音乐 cue、参考学习、音乐 QC 和剪辑交接。用户提到配乐、BGM、主题音乐、情绪曲线、音乐参考或音乐返修时使用。
```

建议补充字段：

```text
music-cue 必填：cue_id、scene_or_shot_id、entry_time、exit_time、emotion_curve、instrumentation、tempo_or_pulse、loop_or_stem_need、reference_boundary、handoff_to_edit。
```

### `project-office` - 8.0/10

主要问题：

- 说明整体清楚，是当前最像“管理 skill”的文件之一。
- `SKILL.md` 与 `project-management-standard.md` 有一定重复；长期维护时容易两处不同步。
- 状态词较多，建议形成统一枚举，避免 blocked/needs_config/needs_handoff 等自由扩散。
- “隐藏过程文件”规则清楚，但可补“哪些可见、哪些隐藏”的简表。

可直接替换的精简 description：

```text
项目办公室。用于管理 AI 剧从原著、编剧、导演、美术、配音、音乐、提示词、视频、剪辑到交付的全流程协作、目录契约、状态台账、交接、返工、阻塞和长期记忆。用户提到项目管理、部门协作、统一 ID、流程台账、交接或返工时使用。
```

建议正文收束：

```text
SKILL.md 只保留项目创建/接管/诊断/交接/返工五类入口；目录标准、状态枚举、共享角色卡和记忆规则以 references 为唯一权威。
```

### `prompt-room` - 8.2/10

主要问题：

- 任务边界清晰，能区分图片提示词、视频提示词、负面提示词、控制条件和 QC。
- `prompt-technique-library.md` 中场景方位体系应与 `art-room`、`imagegenpro` 的中心锚点方位统一。
- 可补充提示词失败后的回退路径：改 prompt、补资产、退导演、退美术、标记工具限制。
- description 略长，但仍可读。

可直接替换的精简 description：

```text
提示词部。用于把编剧、导演、美术、配音、音乐和视频生产要求转成可复制的图片提示词、视频拍摄提示词、负面提示词、资产条件和提示词 QC。用户提到提示词规范化、视频提示词、图片提示词、角色/场景漂移或提示词经验沉淀时使用。
```

建议统一方位句：

```text
场景提示词统一使用 center_anchor_id 加 NW/N/NE/W/C/E/SW/S/SE 方位；正面、背面、左侧、右侧只可作为角色朝向或镜头相对关系，不作为场景布局主坐标。
```

### `screenwriting` - 7.2/10

主要问题：

- description 过长，包含太多输出和触发词。
- refs 结构清楚，但 `workflow.md` 的“唯一输入源是 story-original”容易和项目办公室路径契约冲突。
- `SKILL.md` 对剧本主稿的必填字段可再显式一点，不完全依赖 refs。
- “文学性/精神内核/可拍摄/可配音”方向正确，但评分/QC 字段可更细。

可直接替换的精简 description：

```text
编剧部。用于把项目办公室批准的原著、故事圣经和改编要求转化为结构化文学剧本主稿，包含可拍摄场景、对白语气、声音音乐意图、角色影视化信息和导演交接。用户提到剧本、台词、分集剧本、剧本返修或编剧交接时使用。
```

建议统一输入句：

```text
唯一故事前提源是项目办公室批准的 story-original 输出；实际读取路径、版本和允许材料由 project-office 契约决定。
```

### `story-original` - 6.5/10

主要问题：

- 629 行入口文件偏长，且宣言式语言较多。
- “总小说家、文学魅力、神圣、敬畏、不是梗概机器”等表达重复，能激发创作方向，但会挤压执行步骤。
- 与 source backfill、chapter contract、quality gate 的内容重复。
- 子 agent 使用规则较好，但可以更短：什么时候创建，输入什么，产出什么，主任务如何审稿。
- 输出规格强，但隐藏在较长文本中，测试者需要人工提取。

可直接替换的精简 description：

```text
故事原著部。用于把故事梗、世界观、人物设定、大纲、梗概或不完整剧本创作或回补为完整、有阅读吸引力、可追更、可改编的小说原著和故事圣经。用户提到原著、小说正文、故事源头、补小说、章节规划或故事回补时使用。
```

建议替换正文开头：

```text
# 故事原著部

先判断输入材料是原创起点、改编素材、残缺大纲还是剧本反推；再选择创作、回补、补章节或修订模式。
输出必须能支持后续编剧改编：完整正文、人物关系、世界观规则、章节结构、未解悬念、改编注意事项和 handoff。
文学理念和长技巧库放入 references；SKILL.md 只保留工作流、输出、QC 和阻塞条件。
```

### `video-production-room` - 8.1/10

主要问题：

- 技术判断和 QC 很强，尤其 tool-capability、reference-frame gate、I2V/FLF2V/V2V、lipsync 和 evolution agent 分工清楚。
- `SKILL.md` 265 行仍偏长，和 `ai-video-technique-library.md`、agent 卡有重复。
- “工具能力不足不得降低导演标准”非常好，建议提升为统一失败状态。
- 可补充“何时只规划、何时允许执行生成”的统一入口句，减少执行误判。

可直接替换的精简 description：

```text
视频生成部。用于根据导演分镜、首帧/尾帧、提示词、控制图、配音口型和工具能力规划或执行 I2V、FLF2V、V2V、口型视频、分段生成、镜头素材 QC 和剪辑交接。用户提到视频生成、镜头素材、ComfyUI、Wan、角色/场景漂移、口型视频或视频 QC 时使用。
```

建议补充入口句：

```text
默认只产出生成计划、准入检查和 QC 结论；只有用户或项目契约明确授权且 tool-capability-report 通过时，才执行真实生成。
```

### `voice-room` - 8.3/10

主要问题：

- 结构完整，边界清楚，声音锁、cue sheet、TTS/人工录制、口型交接和 QC 都可执行。
- `SKILL.md` 与 refs 多次重复“不得替视频/剪辑硬救、低于 90 分不得交接”等边界。
- `audio-generation-study.md` 内容有价值，但作为学习材料应和执行硬规则分开，避免把经验建议误读为所有项目必做。
- 可统一“角色声音锁”和“speaker/voice_id”的字段命名。

可直接替换的精简 description：

```text
配音部。用于根据剧本台词、角色声音锁、导演语气要求、口型和剪辑节奏规划或生成角色配音、旁白、声音锁、cue sheet、口型交接和配音 QC。用户提到配音、声音、音色、语气、气口、停顿、TTS、口型或声音锁时使用。
```

建议正文收束：

```text
SKILL.md 保留声音锁、台词 cue、录制/生成、QC、lipsync handoff 五步；TTS 技术经验、工具优缺点和案例学习放入 references，执行时按项目工具能力选择。
```

## 横向改写模板

建议所有部门统一采用以下 `SKILL.md` 最小结构：

```text
---
name: <skill-name>
description: <1-2 句触发说明>
---

# <部门名>

## 使用时机
用户提到 <触发词> 时使用；不处理 <明确排除项>。

## 先读文件
按任务类型读取必要 references；长文件按 UTF-8 分段确认 EOF。

## 最小流程
1. 确认项目办公室契约、上游输入和版本。
2. 判断任务模式：规划 / 执行 / QC / 返修 / 交接。
3. 产出指定 artifact envelope。
4. 运行或记录 QC。
5. 通过则交接；失败则写明归属部门、失败证据和回退路径。

## 输出要求
列出必需文件、必需字段、禁止输出、路径规则。

## 质量闸门
列出直接失败项、分数线、阻塞状态。
```

## 建议统一术语

| 当前问题 | 建议统一 |
|---|---|
| `blocked`、`needs_config`、`needs_upstream_revision`、`blocked_needs_project_contract` 混用 | 建立全项目状态枚举：`ready`、`needs_project_contract`、`needs_upstream_handoff`、`needs_user_decision`、`blocked_tool_unavailable`、`failed_qc` |
| `候选`、`隐藏版本库`、`正式目录` 表述分散 | 统一为 `candidate`、`hidden_version_store`、`approved_artifact`、`handoff_package` |
| 字幕时间权威不统一 | 文本权威=剧本，时间权威=实际音频/cue sheet，对不一致必须标记 |
| 场景方位体系不统一 | 场景布局统一 `center_anchor_id + 九宫格方位`，角色朝向另写 |
| “参考学习”边界不清 | 明确“只学习结构和方法，不复制旋律、画面、文案、水印、UI 或特定作者表达” |

## 总结

这组 skill 的优势是部门体系完整、边界意识强、QC 和交接意识明显，尤其 `voice-room`、`prompt-room`、`video-production-room`、`project-office` 已经接近可稳定执行的 prompt 规范。主要问题不是缺内容，而是入口说明过载、重复复述和少量术语不统一。优先修复顺序建议为：先压缩 `art-room`、`story-original`、`director-room` 三个长入口；再统一字幕/方位/状态词；最后为短部门补最小可测试字段。
