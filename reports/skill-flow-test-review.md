# Skill 流程测试评审报告

报告日期：2026-07-07

测试负责人：skill 流程测试负责人

## 范围与方法

本次测试覆盖 `C:\Users\uroborus\project\ember-frame\.agents\skills` 下 12 个 skill：

`project-office`、`story-original`、`screenwriting`、`director-room`、`art-room`、`prompt-room`、`imagegenpro`、`voice-room`、`music-room`、`video-production-room`、`edit-room`、`delivery-room`。

测试方式为静态流程走查，不调用外部生图、视频、TTS、剪辑、导出工具，不创建大量资产。所有 `SKILL.md` 及直接引用且影响流程执行的 `agents/`、`references/`、`schemas/` 文件均按 UTF-8 分段读取，并确认覆盖到文件末尾后再判断。

评分基准：

- 9-10：流程闭环强，输入、输出、QC、交接清楚，少量外部执行需实测。
- 7-8.9：静态流程基本闭环，有明确质量门，但存在路径、schema、模板或实测依赖。
- 5-6.9：可执行主链存在，但产物格式、验收、返工或交接不够具体。
- 0-4.9：关键步骤缺失或无法可靠执行。

## 总评分表

| Skill | 分数 | 静态流程结论 | 主要风险 |
|---|---:|---|---|
| project-office | 8.5 | 总控流程完整，可作为其他部门路径和交接权威 | 需要更强的可机读部门路径表和模板校验 |
| story-original | 8.0 | 原著创作、Bible、章节、读者模拟、交接链完整 | 读者模拟和长篇质量仍需人工或真实样本验证 |
| screenwriting | 7.5 | 从原著到文学剧本、角色卡更新、导演交接基本闭环 | 主剧本和角色卡更新缺少机器 schema |
| director-room | 8.8 | 导演启动包、分镜目录、诊断/QC/交接最完整 | 强依赖 project-office 启动包，真实分镜生产需实测 |
| art-room | 8.0 | 美术资产规划、规格、提示词、线程计划、QC 很完整 | `asset-prep-plan` schema 与 SKILL 要求不一致；生图需实测 |
| prompt-room | 7.0 | 提示词生产、QC、共享分镜回写链条清楚 | 缺少提示词包 schema；九宫格语义与美术/导演不一致 |
| imagegenpro | 6.5 | 隔离生图原则清楚，适合候选图生成 | 缺少稳定产物 envelope、路径写入和晋升记录模板 |
| voice-room | 7.2 | 声音锁、cue、QC、口型交接链条可走通 | TTS/录音/强制对齐需实测；缺少可机读输出模板 |
| music-room | 6.8 | 音乐规划、cue、QC、交接主链存在 | 参考文件较短，音频产物、版本和验收字段偏弱 |
| video-production-room | 7.8 | 准入、工具能力、分段生成、QC、剪辑交接完整 | 外部视频/口型工具能力必须实测 |
| edit-room | 6.3 | 剪辑主链存在，能从素材走到预览和交付 | EDL、字幕、预览 QC、返工状态缺少具体模板 |
| delivery-room | 6.0 | 最终交付主链存在 | 导出规格、最终 QC、发布清单、用户验收模板过短 |

## 全局阻塞项

1. 多数部门的正式路径、隐藏版本库、状态台账、归口规则都委托 `project-office`。若项目未先生成合格的 `project-management.md`、`.project/` 契约和 `project-spec.md`，后续 skill 应直接阻塞。
2. 生图、视频生成、口型、TTS、录音、音乐生成、剪辑导出都不能通过静态走查证明可执行，只能判断流程契约完整性，实际工具能力标为“需实测”。
3. `art-room` 的 `asset-prep-plan.schema.json` 与 `SKILL.md`/提示模板要求冲突：SKILL 要求每个 `output_format` 明确 `output_spec_id`、`annotation_policy`、`control_role`，但 schema 必填项未覆盖这些字段。
4. `prompt-room` 的九宫格提示技巧与 `art-room`/导演侧的中心锚点径向九宫格语义不一致，容易让同一“九宫格”在不同部门表示不同产物。
5. `delivery-room`、`edit-room`、`music-room`、`prompt-room` 的参考文件偏短，流程能看懂，但缺少可机器验收的产物模板、状态枚举和返工闭环字段。

## 逐 Skill 流程测试结果

### project-office

评分：8.5/10

步骤链：项目触发与根目录识别 -> 读取或创建 `project-management.md`、`project-spec.md`、`.project/` -> 建立部门目录、隐藏过程目录、交接索引、状态台账、返工记录 -> 分发部门任务 -> 汇总交接与用户确认。

最小模拟输入：

- 项目名称、内容类型、目标产物。
- 一个故事源或部门启动需求。
- 交付规格的最小约束，例如集数、分辨率、语言、成片格式。

产物验收：

- `project-management.md` 含部门状态、路径、当前任务、返工状态。
- `project-spec.md` 含交付规格、命名和质量门。
- `.project/` 下存在隐藏过程、历史、索引或版本管理约定。
- 其他部门能从项目办公室文件找到读取入口、写入位置和交接对象。

缺失/阻塞/冲突：

- 流程说明完整，但部门路径表仍偏文档化，缺少统一可机读 manifest。
- 多部门状态字段如果只靠自然语言维护，后续自动检查容易失真。

最小修复建议：

- 增加 `department-paths.json` 或同等 manifest，列出每个部门的输入、输出、隐藏版本库、交接文件。
- 增加项目初始化 dry-run 检查表，作为所有下游 skill 的前置验收。

### story-original

评分：8.0/10

步骤链：故事梗或背景输入 -> 项目契约读取 -> 故事 Bible/源材料台账 -> 章节规划 -> 原著正文 -> 隐藏章节卡/QC -> 读者模拟反馈 -> 回修 -> 编剧交接。

最小模拟输入：

- 一个故事梗、一组主要角色和目标风格。
- 项目办公室指定的故事目录、隐藏工作目录和交接路径。

产物验收：

- Bible 是世界观、角色、主题和长线伏笔的单一事实源。
- 章节正文可阅读、可追更、可改编。
- 隐藏 QC 报告记录章节质量、读者反应、返工项。
- 交接给编剧部时，包含原著正文、故事圣经、章节摘要和改编注意事项。

缺失/阻塞/冲突：

- 静态链路闭环，但真实“读者模拟”只能验证规则，不能证明读者反应准确。
- 长篇产出质量依赖人工审阅或真实样章测试。

最小修复建议：

- 增加一个最小故事夹具，用 1 个项目、1 章、1 次读者模拟验证所有输出字段。
- 给读者模拟结果增加固定评分字段，方便下游编剧引用。

### screenwriting

评分：7.5/10

步骤链：读取原著交接和故事圣经 -> 改编为结构化文学剧本主稿 -> 更新角色总卡编剧区 -> 剧本 QC -> 返工或锁稿 -> 导演交接。

最小模拟输入：

- 原著正文或章节摘要。
- 故事圣经、角色总卡、项目契约。
- 目标集数和单集时长。

产物验收：

- 只有一份结构化文学剧本主稿，含场景、动作、对白、声音/音乐意图。
- 角色总卡 Section 2 写入编剧影视化角色信息。
- QC 能检查可拍摄性、台词、戏剧性、人物动机和导演交接完整性。
- 导演交接含剧本、角色、声音、场景、转场和风险提示。

缺失/阻塞/冲突：

- 主稿是 Markdown 文档，字段较清楚，但缺少可机读 schema。
- 角色总卡更新区和其他部门共享区需要更明确的冲突处理规则。

最小修复建议：

- 增加 `script-main.md` 模板和角色卡 Section 2 字段清单。
- 增加“剧本锁稿后允许改动字段/禁止改动字段”表。

### director-room

评分：8.8/10

步骤链：接收 project-office 导演启动包 -> 校验定稿剧本和允许上游材料 -> 创建正式导演包根目录 -> 按季/集/分镜组/分镜建目录 -> 导演阐述、场景拆解、镜头规划、空间调度、摄影、转场 -> 分镜医生/转场医生/观众盲测 QC -> 导演 QC -> 下游交接。

最小模拟输入：

- project-office 生成的导演启动包。
- 定稿剧本、角色卡、允许读取的美术/声音/剪辑约束。
- 一个 episode 和一个 storyboard/shot。

产物验收：

- 每个分镜只有一个 `{shot-id}.md` 主文档。
- 分镜目录可容纳 `{shot-id}.png`、`{shot-id}.mp4` 和必要资产引用。
- 分镜文档含导演意图、观众视线、镜头语言、空间调度、光影、声音、转场、QC。
- 诊断员工输出 artifact envelope，父级负责写入和裁决。

缺失/阻塞/冲突：

- 若 project-office 启动包缺失或不完整，director-room 按规则必须 blocked。
- 真实分镜图、视频和观众盲测效果需要实测或人工审阅。

最小修复建议：

- 增加最小导演启动包模板。
- 增加 `{shot-id}.md` 可机读字段或 frontmatter，便于下游自动读取。

### art-room

评分：8.0/10

步骤链：读取项目办公室和导演输出 -> 资产规划 -> 美术总监方向 -> 资产拆解 -> 角色/场景/道具/服装设计 -> 风格连续性 -> 图片提示词 -> 方位/九宫格/母资产 -> 线程计划 -> 候选资产生成记录 -> 资产 QC -> 交接导演、提示词、视频。

最小模拟输入：

- 项目契约、导演签署分镜、角色/场景/道具需求。
- 一个角色、一个场景、一个道具、一个分镜首帧需求。

产物验收：

- 资产卡含 identity lock、尺寸、材质、状态、禁改项。
- 每个输出格式明确 `output_spec_id`、`annotation_policy`、`control_role`。
- 线程计划写明批次、最终路径、隐藏版本库、晋升规则。
- 资产 QC 检查画面规格、身份、空间、道具、版本追溯和下游可用性。

缺失/阻塞/冲突：

- `C:\Users\uroborus\project\ember-frame\.agents\skills\art-room\schemas\asset-prep-plan.schema.json` 的 `output_format` 必填字段未包含 SKILL 要求的 `output_spec_id`、`annotation_policy`、`control_role`。
- 生图、线程调度和资产晋升必须实测。
- 若下游需要的精确路径未由 project-office 契约落地，线程计划无法可靠写最终归口。

最小修复建议：

- 修正 `asset-prep-plan.schema.json`，让 schema 与 SKILL/模板一致。
- 增加一个最小资产 dry-run：1 角色、1 场景九宫格、1 首帧，产出空文件占位和 QC 清单即可。

### prompt-room

评分：7.0/10

步骤链：读取项目契约、导演、美术、配音、视频要求 -> 生成图片/视频/拍摄/负面提示词 -> 分离制作元数据与模型可见提示词 -> Prompt QC -> 返工 -> 写入共享分镜提示词区和交接。

最小模拟输入：

- 一个导演签署镜头。
- 通过 QC 的角色、场景、首帧或控制图。
- 视频生成部目标模式，例如 I2V 或 FLF2V。

产物验收：

- 提示词包区分 `production_metadata`、`model_visible_prompt`、`control_ref`、`negative_prompt`、`copy_ready`。
- 禁止把项目路径、蓝线、箭头、UI、标注当成模型应渲染内容。
- QC 能发现身份、场景、动作、运镜、口型和负面约束缺失。
- 交接能被 video-production-room 直接引用。

缺失/阻塞/冲突：

- 缺少正式 prompt package schema。
- `PT-SCENE-02` 的九宫格表达偏“功能视角集合”，而 art-room/资产规格要求的是中心锚点径向九宫格，语义不一致。

最小修复建议：

- 增加 `prompt-package.schema.json` 或 Markdown 模板。
- 将九宫格术语拆成 `location_orientation_grid_9` 和 `scene_function_board_9`，避免同名冲突。

### imagegenpro

评分：6.5/10

步骤链：主任务读取项目上下文和 QC 标准 -> 压缩短提示词和参考图 -> 隔离生图任务 -> 候选图返回 -> 主任务 QC -> 失败返工或晋升正式 reference-frame。

最小模拟输入：

- 一条短提示词。
- 1-3 张压缩参考图或明确文字约束。
- 晋升目标，例如角色参考、场景母图或首帧。

产物验收：

- 生图子任务不读取项目文件、不继承长上下文、不写文件。
- 每次只处理一个图像目标。
- 候选图先进入候选状态，正式晋升需主任务 QC 和明确批准。
- QC 覆盖身份、空间、道具、光影、镜头连续性。

缺失/阻塞/冲突：

- 缺少与 project-office 对齐的 artifact envelope。
- 没有稳定规定候选图返回格式、路径记录、晋升记录和失败记录。
- 实际 OpenAI image generation、ComfyUI 或其他生图工具需实测。

最小修复建议：

- 增加 `image-candidate-envelope` 模板，字段包括目标、输入、输出、QC、晋升状态。
- 增加“候选到正式 reference-frame”的最小记录清单。

### voice-room

评分：7.2/10

步骤链：读取项目契约、剧本、角色声音卡、导演要求、口型/剪辑约束 -> 建立或校验声音锁 -> 建立对白/旁白 cue -> 选择 TTS/人工录制/强制对齐方案 -> 音频 QC -> 返工或导演确认 -> 交接口型、视频、剪辑。

最小模拟输入：

- 一个角色声音设定。
- 两条对白，含情绪、停顿、目标时长、是否需要口型。
- project-office 指定音频归档和交接路径。

产物验收：

- 每条对白有 `dialogue_id`、`speaker_character_id`、`voice_id`、文本、情绪、气口、停顿、起止时间、音频路径、QC 状态。
- 声音锁跨镜头稳定。
- 低于 90 分不得交接口型、视频或剪辑。
- 交接给口型/视频时含词级或音素级时间依据。

缺失/阻塞/冲突：

- TTS、人工录制、强制对齐和音频 QC 需实测。
- 输出字段清单明确，但缺少 JSON schema 或固定 cue sheet 模板。

最小修复建议：

- 增加 `dialogue-cue-sheet.json` 和 `voice-lock.json` 模板。
- 增加 1 句台词的 dry-run，占位音频路径即可验证交接字段。

### music-room

评分：6.8/10

步骤链：读取项目契约、剧本、导演阐述、剪辑节奏 -> 音乐风格和主题动机规划 -> cue sheet -> 参考学习 -> 音乐 QC -> 返工 -> 剪辑/交付交接。

最小模拟输入：

- 一个场景情绪目标。
- 一个导演节奏说明。
- 一个剪辑时长或 cue 点。

产物验收：

- 音乐 brief 说明主题、情绪曲线、节奏、禁用风格。
- cue sheet 写明 cue_id、起止、功能、情绪、参考、版本、QC。
- QC 能判断是否贴合剧情、是否抢对白、是否可剪。
- 交接含音频路径、版本、使用范围和已知风险。

缺失/阻塞/冲突：

- 参考文件较短，缺少稳定 cue schema。
- 真实音乐生成、录制、混音和版权/授权验证需实测。

最小修复建议：

- 增加 `music-cue-sheet.json` 模板。
- 增加“对白优先、音乐不抢戏、可剪辑余量”的固定 QC 字段。

### video-production-room

评分：7.8/10

步骤链：读取导演签署分镜和共享镜头交接 -> 工具能力检查 -> 首帧/尾帧/控制证据准入 -> 技术选择和 `technique_profile` -> 分段生成计划 -> I2V/FLF2V/V2V/lipsync 执行或计划 -> 视频 QC -> 返工、重跑、退回上游或 blocked -> 剪辑交接 -> 失败经验沉淀。

最小模拟输入：

- 一个导演签署镜头。
- 通过 QC 的首帧，必要时尾帧。
- prompt-room 提供的视频提示词和负面提示词。
- voice-room 提供的 lipsync handoff。
- 一个工具能力报告。

产物验收：

- 工具能力报告记录工具名、版本、模式、分辨率、fps、时长、控制输入、限制和测试状态。
- render manifest 记录 `shot_id`、输入、工具、fps、duration、resolution、segment、QC 状态和已知风险。
- shot QC 按导演符合度、角色、场景、动作、镜头、画质、口型、可剪辑性评分。
- 只有通过 QC 且符合项目质量门的素材才能交给剪辑。

缺失/阻塞/冲突：

- 外部视频模型、口型工具、硬件和许可证都必须实测。
- 若工具不可用，只能产出计划并 blocked，不能证明生成流程完成。

最小修复建议：

- 增加 `tool-capability-report.json`、`render-manifest.json`、`shot-qc-report.json` 最小 schema。
- 增加 1 镜头静态 dry-run，使用占位视频路径验证 manifest 和 QC。

### edit-room

评分：6.3/10

步骤链：读取通过 QC 的视频、配音、音乐、字幕和导演节奏 -> EDL -> 粗剪 -> 声画同步 -> 字幕 -> 剪辑 QC -> 返工或成片预览 -> delivery-room 交接。

最小模拟输入：

- 两个通过 QC 的镜头视频路径。
- 一条配音 cue 和一条音乐 cue。
- 导演节奏和转场要求。

产物验收：

- EDL 说明镜头顺序、入点、出点、转场、音频引用。
- 声画同步和字幕状态可检查。
- 剪辑 QC 能发现节奏、转场、声画、字幕和不可剪素材问题。
- 交接给 delivery-room 时含预览片、EDL、字幕、音频引用和 known risks。

缺失/阻塞/冲突：

- 缺少 EDL schema、字幕格式约束、预览片命名和返工状态模板。
- 真实剪辑、转码、字幕渲染和声画同步需实测。

最小修复建议：

- 增加 `edit-decision-list.json` 或 `edl.md` 模板。
- 增加剪辑 QC 表和“退回视频/配音/音乐/导演”的状态枚举。

### delivery-room

评分：6.0/10

步骤链：读取导演终审通过的剪辑预览和 QC -> 确认交付规格 -> 最终导出 -> 成片 QC -> 版本归档 -> 用户验收。

最小模拟输入：

- 一个成片预览路径。
- 剪辑 QC 和导演批准记录。
- 交付规格，例如分辨率、帧率、编码、字幕、命名。

产物验收：

- delivery spec 明确格式、编码、音频、字幕、命名和输出路径。
- final QC 检查画面、声音、字幕、时长、文件完整性和版本。
- release manifest 记录最终文件、校验、来源、批准人、已知风险。
- 用户验收状态进入项目办公室历史。

缺失/阻塞/冲突：

- 参考文件过短，缺少导出规格模板、最终 QC 表、发布 manifest schema。
- 真实导出、播放检查、校验和归档需实测。

最小修复建议：

- 增加 `delivery-spec.md`、`final-qc.md`、`release-manifest.json` 模板。
- 增加“导演终审通过才能导出最终版”的硬字段。

## 缺失步骤汇总

| 问题 | 影响 skill | 影响 |
|---|---|---|
| 缺少统一最小项目夹具 | 全部 | 无法对全流程做静态 dry-run |
| 下游路径过度依赖自然语言项目契约 | 多数 | 自动化检查难以确认产物位置 |
| 部分部门缺少 JSON/schema 模板 | prompt、voice、music、edit、delivery | 产物能写出来，但不易机器验收 |
| 外部工具能力未实测 | imagegenpro、art、voice、music、video、edit、delivery | 只能判断流程，不可证明真实执行 |
| 九宫格术语冲突 | prompt、art、director、video | 同一术语可能生成不同控制资产 |
| art-room schema 与流程要求不一致 | art | 自动校验会放过关键字段或误判 |

## 需实测清单

- OpenAI image generation、ComfyUI 或其他生图工具的单图候选、重做、局部修正和晋升流程。
- 视频工具的 I2V、FLF2V、V2V、lipsync、分段和 manifest 写入流程。
- TTS、人工录制、强制对齐、词级/音素级时间生成。
- 音乐生成、混音、与对白共存检查。
- 剪辑软件或脚本的 EDL、字幕、声画同步、预览导出。
- 最终导出编码、播放 QC、校验、归档和用户验收。

## 最小修复建议

1. 增加一个 `tests/fixtures/minimal-production-project/` 级别的空项目夹具，只放占位路径和 1 个 episode、1 个 shot、1 个角色、1 个场景、1 条对白，用于所有 skill dry-run。
2. 由 `project-office` 生成统一 `department-paths.json`，让每个部门明确输入、输出、隐藏版本库、正式归口和交接文件。
3. 为 prompt、voice、music、edit、delivery 增加最小 schema 或 Markdown 模板，字段不求多，但必须可验收。
4. 立即修正 `art-room` 的 `asset-prep-plan.schema.json`，补齐 `output_spec_id`、`annotation_policy`、`control_role`。
5. 统一“九宫格”术语，把中心锚点径向九宫格设为下游视频控制资产的唯一标准名称，其他九图板另起名。
6. 给所有外部生成/导出部门增加“未实测时只能计划，不得宣布完成”的统一状态字段。

## 最终结论

12 个 skill 均能建立静态流程链，没有发现完全无法理解或无法进入的 skill。最完整的是 `director-room`、`project-office`、`art-room`、`story-original` 和 `video-production-room`。主要短板不是主流程缺失，而是部分部门缺少可机读模板、路径 manifest、跨部门术语统一和真实工具实测记录。
