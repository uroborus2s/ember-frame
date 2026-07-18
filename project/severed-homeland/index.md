# 《断航故土》制作总入口

owner: project-office
status: active
last_updated: 2026-07-18

本文件给人和 AI 提供同一个项目入口。先在这里判断“现在该读什么、做什么、交给谁”，再进入部门文档；不要从聊天记录、旧版本目录或工具输出里猜当前真相。

## 1. 首次进入项目只读这些

| 目的 | 唯一入口 |
|---|---|
| 项目创意、集数、受众和已确认请求 | `project.json` |
| 画面、视频、音频、字幕和交付规格 | `project-spec.md` |
| 目录、权限、交接、返工和版本规则 | `project-management.md` |
| 当前进度 | `.project/status.md` |
| 当前阻塞 | `.project/blockers.md` |
| 可复用的长期经验 | `project-memory.md` |
| 部门之间交了什么 | `.project/handoff-index.json` |
| 为什么返工 | `.project/revision-log.jsonl` |

进入具体工作后，再读本部门正式入口和被交接的上游正式文件。未被交接、未锁定或只存在于 `.work/` 的材料，不是正式输入。

## 2. 输入文档结构

项目输入分成四类，不再混在一个“资料”目录里：

```text
project/severed-homeland/
  project.json                          创意委托与项目卡；回答“做什么、给谁看”
  project-spec.md                       成果规格；回答“最终交付成什么样”
  story-original/bible/source/          已登记的故事来源副本
  story-original/bible/source-ledger.md 来源、等级、采用与冲突记录
  project-memory.md                     已验证的长期经验，不是剧情来源
```

输入处理顺序：

```text
人提交创意/资料
  -> 项目办公室登记来源与用途
  -> 原著部判断 A/B/C/D 级
  -> 采用内容写入 story-bible.md
  -> 锁定后才允许进入小说
  -> 下游只读上游锁定产物
```

硬规则：

- `project.json` 记录稳定的创意委托，不记录每轮讨论。
- `project-spec.md` 记录稳定的技术与交付规格，不记录工具试验。
- 原始故事资料先进入 `story-original/bible/source/`，并在 `source-ledger.md` 登记；没有登记的资料不能直接成为 canon。
- `project-memory.md` 只能指导方法，不能覆盖故事 Bible、剧本、导演签署或交付规格。
- 聊天中的新决定必须落到对应正式文档、交接或返工记录；只留在聊天里等于没有交接。
- 遇到冲突不采用“最后写入者优先”：故事事实退回原著部，戏剧表达退回编剧部，镜头执行退回导演部，技术规格退回项目办公室和交付部。

## 3. 项目记忆不是一个大文件夹

项目记忆分五层，各自只回答一种问题：

| 层 | 回答的问题 | 保存位置 | 是否给下游当正式输入 |
|---|---|---|---|
| 创意与规格 | 我们要做什么、交付什么 | `project.json`、`project-spec.md` | 是 |
| 作品 Canon | 故事、人物、剧本、分镜当前是什么 | Bible、小说、剧本、角色总卡、`{shot-id}.md` | 锁定后是 |
| 当前工作状态 | 现在做到哪里、卡在哪里 | `.project/status.md`、`blockers.md`、`handoff-index.json` | 只用于协调 |
| 长期经验 | 哪些规律以后还会反复用 | `project-memory.md` | 作为方法约束 |
| 过程与历史 | 曾经试过什么、为什么没用 | 各部门 `.work/`、`.history/` | 否 |

长期记忆只在部门交接、单集完成、重大返工和整季复盘时整理。各部门把候选经验写到 `department/.work/memory-candidates.md`；项目办公室读取旧记忆后合并、删旧、改写，不做每日追加。

## 4. 中间版本怎么处理

每个文字、图片、音频、视频或剪辑对象都使用同一个稳定 ID，并走同一条版本流：

```text
working -> candidate -> qc_passed -> promoted
                   \-> rejected
promoted -> superseded（被新正式版替代时）
```

隐藏版本库：

```text
{department}/.work/asset-versions/{asset-id-or-shot-id}/
  YYYYMMDDvNNNN.ext
  manifest.jsonl
```

`manifest.jsonl` 每个版本至少记录：

```text
version_file
created_at
created_by: human | ai | tool
source_inputs
prompt_or_instruction_ref
tool_and_key_parameters
status: working | candidate | qc_passed | promoted | rejected | superseded
qc_evidence
rejection_or_replacement_reason
formal_path
```

正式路径不带过程版本号：

- 部门文字结论进入该部门唯一正式入口。
- 角色母资产进入 `director-room/characters/`。
- 公共视觉母资产进入 `art-room/shared-assets/`。
- 单分镜最终图、视频、配音、音乐和剪辑交接进入该分镜目录。
- 正式分镜图片与视频固定命名为 `{shot-id}.png`、`{shot-id}.mp4`。

版本处理规则：

- AI 和人都在隐藏版本库试错；候选文件不得放到明面目录冒充正式产物。
- 晋升正式版时保留原候选版本，把稳定正式路径更新为当前认可结果，并在分镜文档和交接索引记录证据。
- `rejected`、`superseded` 不在活动制作期删除；单集交付后可转入 `.history/` 或外部冷存储，版本清单仍保留。
- 大体积过程媒体和工具日志不进 Git；可恢复当前状态的正式文档、`.project/` 协调文件和状态台账进入 Git。
- `.work/manifest.jsonl` 保存完整本地追溯；跨设备需要恢复的当前晋升状态同步到 `.project/ledgers/`、正式分镜文档和交接索引。
- 不使用 `final-final-v3`、`approved2` 等文件名表达状态；状态写入 manifest，正式路径保持稳定。

## 5. 人和 AI 的职责边界

| 责任 | 人 | AI |
|---|---|---|
| 创意目标 | 决定受众、主题、审美、禁区和成功标准 | 整理成项目卡，指出矛盾和缺项 |
| Canon | 批准重大世界观、人物和主线变化 | 提案、查冲突、保持前后连续 |
| 专业制作 | 选择方向，提供表演与审美判断 | 生成草稿和候选、批处理、技术检查、整理交接 |
| 质量门 | 对高成本返工、导演终审和最终交付负责 | 提供证据、评分、风险和明确建议 |
| 项目记忆 | 确认重要经验是否值得长期保留 | 从过程记录中压缩、合并、删除噪音 |

AI 只有在被明确授权为该关口 `approval_owner` 时才能把阶段标记为 `locked`；最终用户验收、重大 Canon 变更、版权/授权、预算和平台规格不能由 AI 静默决定。

每轮人机协作遵循六步：

1. 人说明目标、限制和本轮成功标准；若信息已在正式文档中，只需引用路径。
2. AI 读取本入口、当前状态、部门契约和明确交接的上游文件。
3. AI 在 `.work/` 制作候选并完成最小自检，不直接覆盖他人锁定区块。
4. AI 把“候选、证据、风险、建议”交给当前审批人；人只需要判断关键选择，不必审阅全部工具日志。
5. 通过后，AI 晋升到稳定正式路径，更新交接、状态和必要台账；未通过则记录最小返工入口。
6. 只有可复用教训进入记忆候选；普通试错留在版本库。

## 6. 从创意到成片的完整流程

| 阶段 | 正式输入 | 方法与工具 | AI 主要工作 | 人的关口 | 正式输出 / 下游 |
|---|---|---|---|---|---|
| 0. 创意立项 | 用户创意、参考资料、平台与资源限制 | 项目办公室、结构化访谈、冲突检查 | 整理项目卡、假设、风险和待决项 | 确认题材、受众、基调、禁区、集数和验收标准 | `project.json`、`project-spec.md` -> 原著部 |
| 1. 故事 Bible | 已登记来源、项目卡 | `story-original`、来源分级、时间线/人物/地理一致性检查 | 建立世界、人物、事件、禁令和来源追溯 | 批准重大 Canon 与故事方向 | `story-bible.md`、`source-ledger.md` -> 小说 |
| 2. 小说原著 | 锁定 Bible | `story-original`、章节规划、故事医生 | 写完整可读故事，补人物欲望、因果和情绪弧 | 判断故事是否成立、是否值得继续 | `novel.md`、`chapters/` -> 编剧部 |
| 3. 文学剧本 | 原著、角色源头 Canon、项目规格 | `screenwriting`、逐集结构、台词朗读、可拍性检查 | 改编场次、动作、对白、声音意图和集尾钩子 | 锁定集级故事、台词含义和表演方向 | 季总稿、分集 `screenwriting-main.md` -> 导演/配音/音乐 |
| 4. 导演与分镜脚本 | 锁定剧本、角色总卡、必要 Bible | `director-room`、空间拆解、调度、镜头语言、观众盲测 | 为每镜写人物入口/出口、站位、视线、运镜、声音和通过标准 | 总导演签署导演区块 | `{shot-id}.md` -> 美术/配音/音乐/提示词 |
| 5. 画面与美术 | 导演签署、角色/场景/道具 Canon | `art-room`、`imagegen`/ComfyUI、参考图一致性 QC | 制作角色母卡、场景/道具母资产、分镜参考帧候选 | 选择风格与身份一致的正式画面 | 角色母资产、公共资产、`{shot-id}.png` -> 提示词/视频 |
| 6. 配音 | 锁定台词、导演语气、角色声音卡 | `voice-room`、人工录制或 `scripts/qwen3_tts.py`、听审 | 生成声音候选、切分台词、标记气口和口型时间 | 听审身份、情绪、可懂度与表演 | 角色声音锁、`assets/voice/` -> 视频/剪辑 |
| 7. 音乐与声效 | 剧本情绪线、导演节奏、剪辑时长需求 | `music-room`、DAW/生成音乐、cue sheet、响度检查 | 设计主题动机、cue、stem、环境声和静默点 | 判断音乐是否服务叙事而非抢戏 | `assets/music/`、音乐区块 -> 剪辑 |
| 8. 提示词封装 | 导演签署、美术正式资产、声音/口型要求、工具限制 | `prompt-room`、图片/视频提示词与负面约束 | 把已锁定创作意图翻译为可执行模型条件 | 只审是否误读上游，不重新创作 Canon | `{shot-id}.md` 提示词区 -> 视频生成 |
| 9. 视频生成 | 分镜文档、参考帧、提示词、配音/口型 | `video-production-room`、Wan I2V/FLF2V/ComfyUI、帧抽样和运动 QC | 批量生成候选，检查身份、动作、空间、时长和口型 | 导演按镜头意图选片或退回最小上游 | `{shot-id}.mp4` -> 剪辑 |
| 10. 剪辑、字幕、混音 | 通过 QC 的镜头、配音、音乐、字幕文本 | `edit-room`、NLE/FFmpeg、声画同步、连续性审片 | 组装、节奏、转场、字幕、混音和预览 QC | 导演审片；剧情缺口不允许靠剪辑掩盖 | 剪辑预览、EDL/交接 -> 交付部 |
| 11. 成片交付 | 导演通过的剪辑、最终规格 | `delivery-room`、`video_probe.py`、`delivery_qc.py` | 导出、技术 QC、命名、校验、归档清单 | 用户最终验收 | 最终成片、交付记录、归档 |
| 12. 复盘与记忆 | 交接、返工、阻塞和验收证据 | 项目办公室、记忆整理 | 合并经验、删除过时规则、关闭台账 | 确认重大经验与下一集策略 | 更新 `project-memory.md`，进入下一集 |

分镜锁定后，美术、配音、音乐和提示词可以并行；视频生成必须等待它实际依赖的资产达到 `locked/ready`。剪辑可以用明确标记的 preview 做节奏预演，但不得把 preview 当最终素材。

## 7. 质量门与返工

```text
创意确认
  -> 故事 Canon 锁定
  -> 小说通过
  -> 剧本锁定
  -> 导演分镜锁定
  -> 美术/声音/音乐/提示词就绪
  -> 视频镜头 QC 通过
  -> 剪辑通过
  -> 技术 QC 通过
  -> 用户最终验收
```

任何失败只退回最小责任源头：故事事实回原著，动机/台词回编剧，调度回导演，形象/空间回美术，声音回配音，情绪音乐回音乐，模型误读回提示词，生成瑕疵回视频，声画节奏回剪辑，格式问题回交付。

返工必须写入 `.project/revision-log.jsonl`，说明证据、责任部门、影响范围、所需修复和被阻塞下游；关闭后再恢复交接。

## 8. 当前项目执行约束

- 目前正在生产的 G-P 过程文档仍被正式入口引用，本轮不做路径搬迁；新产生的候选、QC、诊断、返工单和工具记录立即按 `.work/asset-versions/` 规则保存。
- 等 G-P 当前返工关口关闭后，再把现有明面过程文档连同引用路径一次性迁入隐藏版本库，避免半迁移导致断链。
- 当前真相以 `.project/status.md`、`.project/blockers.md` 和 `.project/final-approval-gate.md` 为准；旧预览、失败诊断样片和未通过导演终审的媒体不得晋升。

## 9. 本仓库可直接复用的制作工具

| 用途 | 工具 |
|---|---|
| 冻结外部/本地参考资产并建清单 | `scripts/tools/asset_resolver.py` |
| 探测视频尺寸、帧率、时长和音轨 | `scripts/tools/video_probe.py` |
| 抽帧审查 | `scripts/tools/frame_sampler.py` |
| 分析参考视频 | `scripts/tools/reference_video_analyzer.py` |
| 裁切、拼接、抽取音频 | `scripts/tools/ffmpeg_edit.py` |
| 基础交付 QC | `scripts/tools/delivery_qc.py` |
| Qwen3-TTS 配音 | `scripts/qwen3_tts.py` |

工具只负责生成证据和执行重复工作；Canon、导演判断、表演判断和最终验收仍由对应审批人负责。
