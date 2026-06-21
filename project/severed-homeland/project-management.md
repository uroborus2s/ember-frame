# 《断航故土》项目管理说明

本文件是本项目所有部门共同遵守的现场版项目管理说明。它不是创作文件，也不是流水账；它只说明目录、交接、返工、长期记忆和阅读范围。

项目管理的目的不是把每个岗位变成机器螺丝钉，而是在保证质量和流程的同时，尊重每个岗位的创造力、专业判断和主动性。

## 阅读索引

各部门先看本索引，只读自己需要的小节。

```text
故事原著部：读 1, 2, 3, 7, 8, 9, 11, 12, 14, 15, 18
编剧部：读 1, 2, 3, 5, 6, 8, 9, 14, 15, 16, 18
导演部：读 1, 2, 3, 5, 6, 8, 9, 14, 15, 16, 17
美术部：读 1, 2, 3, 5, 6, 8, 9, 14, 15, 16, 17, 18
配音部：读 1, 2, 3, 5, 6, 8, 9, 14, 15, 16, 17, 18
音乐部：读 1, 2, 3, 5, 6, 8, 9, 15, 16, 17, 18
提示词部：读 1, 2, 3, 5, 6, 8, 9, 15, 16, 17, 18
视频生成部：读 1, 2, 3, 5, 6, 8, 9, 15, 16, 17, 18
剪辑部：读 1, 2, 3, 5, 6, 8, 9, 15, 16, 17, 18
成片交付部：读 1, 2, 3, 5, 6, 8, 9, 15, 16, 18
项目办公室：读全部
```

凡涉及图片、视频、音频、字幕、交付格式或清晰度要求的部门，还必须读取根目录 `project-spec.md`。

## 1. 核心理念

- 化繁为简：只保留真正帮助生产的结构。
- 尊重创作：流程服务创作，不用流程压扁人。
- 一眼可读：正式输出必须让下游马上知道看什么、用什么、下一步做什么。
- 过程隐藏：草稿、日志、评分、返工过程和项目管理台账默认进入隐藏目录。
- 长期沉淀：只有能复用的经验才进入项目长期记忆。

## 2. 明面目录规则

明面目录只放当前正式产物。每个部门默认只有一个当前正式入口文档，必要时可有少量固定索引。

默认结构：

```text
department/
  current-output.md
  .work/
  .history/
```

- `current-output.md`：当前正式产物，给下游直接使用。
- `.work/`：当前过程、草稿、检查、候选经验、临时协作材料。
- `.history/`：旧版本、迁移遗留、废弃结构、已归档过程。

如果从旧结构迁移，统一放入：

```text
.history/from-previous-structure/
```

专业部门可以有自己的隐藏版本库，用来保存候选、废弃、返工前和被替换的资产版本。新资产不在明面目录创建可见 `raw/`、`rejected/`、`approved/`、`history/`、`versions/` 或 `drafts/`。

## 3. 正式输出规则

正式输出从大到小组织，让人一眼看懂。

推荐层级：

```text
剧
  集
    场
      镜头 / 分镜
```

部门正式输出只写本部门应交付的结论，不塞过程表格、内部评分、工具日志或多轮讨论。

## 4. 项目办公室隐藏目录

项目管理过程写入隐藏目录：

```text
.project/
```

核心文件保持少量：

```text
.project/status.md
.project/handoff-index.json
.project/revision-log.jsonl
.project/blockers.md
.project/final-approval-gate.md
```

只有进入相应生产阶段、确实需要追踪时，才建立更细台账：

```text
.project/ledgers/episode-status.json
.project/ledgers/shot-status.json
.project/ledgers/asset-status.json
.project/ledgers/audio-status.json
```

Git 同步规则：

必须同步到 git 的隐藏项目文件：

```text
.project/status.md
.project/blockers.md
.project/final-approval-gate.md
.project/handoff-index.json
.project/revision-log.jsonl
.project/contracts/
.project/ledgers/
```

不提交到 git 的隐藏过程文件：

```text
.project/tmp/
.project/cache/
.project/runs/
.project/logs/
.project/history/
*/.work/
*/.history/
*/.cache/
*/.tmp/
```

判断原则：能让另一个人恢复项目状态、交接关系和质量门的轻量文件要同步；临时素材、旧包、跑批日志、失败版本、缓存和个人本地配置不提交。真正可复用的经验整理进 `project-memory.md`，不是把过程文件塞进 git。

## 5. 交接规则

每次部门交接只记录下游真正需要的信息：

```text
source_department
target_department
handoff_files
status
quality_gate
known_risks
blocked_items
approval_owner
```

交接记录写入：

```text
.project/handoff-index.json
```

部门正式文档中只保留下游需要执行的结论，不重复交接台账。

## 6. 返工规则

返工必须可追溯，但不打扰明面目录。

返工记录写入：

```text
.project/revision-log.jsonl
```

返工至少写清：

```text
issue_id
detected_by_department
affected_episode
affected_scene
affected_shot
affected_asset
failure_type
evidence
root_cause_department
required_fix
blocked_downstream
status
```

只有确认能长期复用的教训，才由项目办公室提炼进 `project-memory.md`。

## 7. 项目长期记忆

项目根目录可有：

```text
project-memory.md
```

它不是流水账，只保存压缩后的长期规则。

各部门只能把候选经验放入：

```text
department/.work/memory-candidates.md
```

项目办公室负责筛选、合并、删除和改写长期记忆。每次整理都要读旧记忆，合并重复，删除过时内容，把含糊描述改写成可执行规则。

## 8. 统一 ID

所有部门共用同一套 ID，不得自行发明另一套命名系统。

```text
episode_id: 01
scene_id: SC004
shot_id: SC004-SH003
character_id: C001
prop_id: P003
location_id: L001
dialogue_id: D011
music_cue_id: MX004
asset_id: E01_R017
render_id: SC004-SH003-V001
edit_id: E01_EDIT_V001
delivery_id: E01_FINAL_V001
```

确需新增 ID，必须写入项目办公室索引。

## 9. 不得越权

- 任何部门只能修改自己拥有的共享文件区块，不得覆盖其他部门已锁定区块。
- 角色总卡正式归口为导演部根入口 `director-room/characters/`，采用“一角色一文件、分区块协作”：原著部写源头 Canon，编剧部写影视化角色卡，美术部写视觉角色卡，配音部写声音角色卡，视频生成部写视频执行角色卡。
- 下游发现上游角色信息不足时，必须通过变更记录或返工入口提出，不能直接改源头 Canon。
- 美术部不能改剧情。
- 配音部不能改台词含义。
- 音乐部不能改变场景情绪功能。
- 提示词部不能重设人物身份和场景空间。
- 视频生成部不能用随机生成结果改 canon。
- 剪辑部不能用剪辑掩盖剧情缺口。
- 导演部可以要求返工，但必须给证据、责任部门和通过标准。

## 10. 项目办公室维护规则

项目办公室负责维护本文件。修改本文件必须服务于生产清晰度，不得为了管理而增加无复用价值的文档。

各部门不需要读取项目办公室 skill，也不需要读取模板文件；执行项目任务时，只读本文件索引和自己需要的小节。

任何部门正式启动前，项目办公室必须先补齐该部门的输入准入、输出与目录契约。未补齐时，该部门状态为 `blocked_needs_project_contract`，不得从部门 skill 中临时拼路径。

## 11. 故事原著部输入准入

故事原著部读取项目素材时，必须先按本小节判断素材等级。所有素材都要先进入 `story-original/bible/` 的整理流程；只有进入 `story-original/bible/story-bible.md` 的内容，才能成为小说正文前提。

A 类：项目级故事前提源，优先用于建立原著部 Bible。

```text
project.json
story-original/bible/source/world.md
story-original/bible/source/geography.md
story-original/bible/source/factions.md
story-original/bible/source/timeline.md
story-original/bible/source/characters.md
story-original/bible/source/scenes.md
story-original/bible/source/continuity.md
story-original/bible/source/visual-style.md
story-original/bible/source/outline/series-outline.md
story-original/bible/source/outline/episode-outline-index.md
story-original/bible/source/synopsis/story-synopsis.md
project-memory.md
```

B 类：逐集故事回补参考，只能用于补齐 Bible 中的事件、人物和连续性缺口。

```text
screenwriting/{episode-id}/.work/from-root-episode-20260620/brief/episode-brief.md
screenwriting/{episode-id}/.work/from-root-episode-20260620/script/episode-outline.md
screenwriting/{episode-id}/.work/from-root-episode-20260620/script/final-script.md
screenwriting/{episode-id}/.work/from-root-episode-20260620/reports/continuity-report.md
screenwriting/{episode-id}/.work/from-root-episode-20260620/reports/script-score.md
```

C 类：只作辅助参考，不能直接决定故事 canon。当前清理后的项目根目录不保留这些生产目录；如需追溯，只能由项目办公室从旧归档包或隐藏历史中指定。

```text
{episode-id}/storyboard/storyboard-plan.md
{episode-id}/shots/shot-list.json
{episode-id}/shots/scene-breakdown.json
{episode-id}/director/director-brief.md
{episode-id}/director/camera-plan.md
{episode-id}/continuity/visual-continuity-bible.json
art/
assets/
```

D 类：默认排除，不能进入原著 Bible，除非用户明确要求并确认其故事意义。

```text
prompts/
production/
renders/
audio/
post/
qc/
reviews/
ComfyUI / Wan / I2V 参数
失败图片、失败视频、失败提示词、旧剪辑结果
```

建立 Bible 前必须写素材来源登记：

```text
story-original/bible/source-ledger.md
```

来源登记至少包含：

```text
source_path
source_tier: A|B|C|D
used_for_bible: true|false
bible_section
imported_facts
conflicts
decision
```

## 12. 故事原著部输出与目录契约

故事原著部只向下游交付当前正式原著和必要的故事前提，不把过程、质检、评分、草稿、任务记录放在明面目录。

正式工作目录：

```text
story-original/
```

正式输出：

```text
story-original/novel.md
story-original/chapters/
story-original/bible/story-bible.md
story-original/bible/source-ledger.md
```

目录含义：

```text
story-original/novel.md                  当前完整小说原著
story-original/chapters/                 长篇章节正文；若使用章节制，novel.md 作为总入口
story-original/bible/story-bible.md      原著部唯一故事前提
story-original/bible/source-ledger.md    素材来源登记
story-original/bible/source/             已拷贝的来源材料
story-original/.work/                    隐藏后台材料、任务、质检、交接、经验
story-original/.history/                 旧版、废弃结构、迁移遗留
```

隐藏工作材料放入：

```text
story-original/.work/outline.md
story-original/.work/character-inner-drives.md
story-original/.work/suspense-map.md
story-original/.work/chapter-index.md
story-original/.work/adaptation-handoff.md
story-original/.work/qc/story-doctor-report.md
story-original/.work/qc/season-story-score.md
story-original/.work/tmp/
story-original/.work/memory-candidates.md
story-original/.work/memory/evolution-notes.md
```

硬规则：

- 公开小说正文只能写入 `story-original/novel.md` 或 `story-original/chapters/`。
- 正文前提只能来自 `story-original/bible/story-bible.md`。
- 角色总卡不是小说正文；正式归口为 `director-room/characters/`，原著部只写源头 Canon，编剧、美术、配音和视频生成部只能写各自区块。
- 过程材料不得散落到剧本、导演、提示词、视频或制作目录。
- `story-original/.work/` 里的内容是后台材料，不是对外正文。
- 旧结构迁移材料统一放入 `story-original/.history/from-previous-structure/`。

## 13. 后续部门契约补齐规则

编剧、导演、美术、配音、音乐、提示词、视频、剪辑和交付部门启动前，项目办公室必须补齐对应部门契约。

每个部门契约至少包含：

```text
部门当前正式文档
允许读取的输入
禁止读取的输入
正式输出
隐藏输出
历史归档
交接文件
完成条件
返工入口
```

契约可以写在本文件的新小节，也可以写入 `.project/contracts/{department}.md`，但本文件阅读索引必须指向它。

未补齐契约的部门不得正式生产。这样可以避免每个 skill 自己定义一套目录，项目现场始终只有一个管理口径。

## 14. 跨部门角色总卡合同

角色总卡采用“一角色一文件、分区块协作”。它是角色 canon、影视化表演、美术视觉、配音声音和视频执行锁点的共享承载文件，但每个部门只能修改自己拥有的区块。

角色总卡正式归口放在导演部根目录下，作为全项目对外最简单、最稳定的角色入口。这样做不是把角色 canon 变成导演部私产，而是让导演部作为作品总控入口统一看见人物状态，项目办公室负责区块契约，专业部门按区块维护同一份文件。

推荐目录：

```text
director-room/characters/
  character-index.md
  CHAR-001-name.md
  c001m.png
  c001-voice-v001-preview.wav
  CHAR-002-name.md
  c002m.png
  c002-voice-v001-preview.wav
```

角色母图与角色图提示词必须就近归口到同一角色入口：正式角色母图图片放在 `director-room/characters/`，与对应角色总卡同目录；图片提示词写入该角色卡 `Section 3 美术视觉角色卡`。美术部 `.work/` 可保留机器可读副本、候选图、失败尝试和版本追溯，但不得作为下游查找角色母资产或角色图提示词的第一入口。

角色声音母样与音频生成提示词也必须就近归口到同一角色入口：可供下游一眼试听和识别的角色级母音色 preview 音频放在 `director-room/characters/`，与对应角色总卡同目录；音频生成提示词、声音锁、试听文件路径和 QC 状态写入该角色卡 `Section 4 配音声音角色卡`。配音部 `.work/asset-versions/` 保留过程版本、候选、废弃版本和 manifest，不得作为下游查找角色声音母样的第一入口。未通过人工听审和质量门的角色声音母样必须标记 `preview` 或 `needs_fix`，不得冒充分镜最终配音。

角色母卡标准模板使用 `PROJECT-CHAR-MODEL-SHEET-V2`。该模板不是单纯“三视图”，而是可复用 production model sheet：上排至少五个全身转面视图（正面、三分之四正面、严格侧面、三分之四背面、背面），中排至少六个同脸表情头像 / 半身头像，下排包含主色板、关键材质裁切和角色道具格。模板可有无文字的分栏线、色块和道具小格，但不得出现标签文字、箭头、UI、水印或说明文字。

角色母卡 QC 的第一条是同脸一致性：大特写、全身正面、侧面可见脸和表情组必须像同一个人，同一骨相、眼距、鼻梁、嘴形、脸型、发际线和年龄感；如果看起来像亲属、替身或同风格另一个人，必须标记 `needs_fix`，不得交给提示词部或视频生成部。

区块所有权：

```text
Section 1 源头 Canon              owner: story-original
Section 2 编剧影视化角色卡        owner: screenwriting
Section 3 美术视觉角色卡          owner: art-room
Section 4 配音声音角色卡          owner: voice-room
Section 5 视频执行角色卡          owner: video-production-room
Section 6 冲突与变更记录          owner: project-office 协调，各部门追加记录
```

文件模板：

```text
# CHAR-001 角色名

## 0. 卡片元信息
- character_id:
- display_name:
- current_status:
- source_owner: story-original
- screenwriting_owner: screenwriting
- art_owner: art-room
- voice_owner: voice-room
- video_owner: video-production-room
- last_updated:

## 1. 源头 Canon
owner: story-original
status: draft | locked | needs_fix

- 身份：
- 年龄 / 时代位置：
- 出身：
- 关键过往：
- 核心伤口：
- 欲望：
- 恐惧：
- 行为底线：
- 人物弧光：
- 不可改动事实：
- 原著关键段落来源：

## 2. 编剧影视化角色卡
owner: screenwriting
source: Section 1 源头 Canon
status: draft | locked | needs_fix

- 戏剧功能：
- 剧中人物目标：
- 台词风格：
- 口头禅 / 常用句式：
- 音色、气口、停顿：
- 情绪遮掩方式：
- 常见动作：
- 镜头里必须看见的状态：
- 每集状态变化：
- 禁止写偏：

## 3. 美术视觉角色卡
owner: art-room
source: Section 1 源头 Canon + Section 2 编剧影视化角色卡
status: draft | locked | needs_fix

- 年龄感：
- 五官气质：
- 体态：
- body_metrics:
  - height:
  - build:
  - body_ratio:
  - silhouette:
  - scale_refs:
- 发型：
- 服装体系：
- 色彩体系：
- 材质：
- 标志物：
- 伤痕 / 污渍 / 磨损：
- 表情基调：
- 多表情组：
- 色板 / 道具格：
- 角色母图文件：
- 角色母图提示词：
- 角色 master card 要求：
- episode state card 要求：

## 4. 配音声音角色卡
owner: voice-room
source: Section 1 源头 Canon + Section 2 编剧影视化角色卡
status: draft | locked | needs_fix

- 声线：
- 语速：
- 呼吸：
- 情绪层级：
- 爆发方式：
- 低声 / 沉默 / 哭腔 / 怒声规则：
- 角色声音试听文件：
- 音频生成提示词：
- 声音版本 / QC 状态：

## 5. 视频执行角色卡
owner: video-production-room
source: Section 1 源头 Canon + Section 2 编剧影视化角色卡 + Section 3 美术视觉角色卡 + Section 4 配音声音角色卡
status: draft | locked | needs_fix

- 动作连续性禁区：
- 易漂移风险：
- 口型 / 面部表演注意：
- 服装、发型、道具不可漂移项：
- 群像或模板角色的视频生成约束：

## 6. 冲突与变更记录
- date:
- department:
- section:
- change_summary:
- affects_source_canon: true | false
- required_return_department:
- status:
```

修改规则：

- 原著部只改 Section 1。
- 编剧部只改 Section 2。
- 美术部只改 Section 3。
- 配音部只改 Section 4。
- 视频生成部只改 Section 5。
- Section 1 被锁定后，任何下游不得直接修改，只能提出 `needs_story_source_fix`。
- 美术部可以读取 Section 1 和 Section 2，但主要依据 Section 2 做影视视觉落地，并用 Section 1 校验不能画偏。
- 视频生成部可以读取 Section 1-4，但只把执行中的角色漂移风险、口型风险和动作连续性锁点写入 Section 5，不得用生成结果反改 canon。

## 15. 全链路输入输出最小契约

本项目按“故事 → 编剧 → 导演 → 美术/配音/音乐/提示词 → 视频生成 → 剪辑 → 成片交付”推进。每个部门只交付当前阶段必须让下游使用的正式成果，过程材料进入本部门隐藏目录或 `.project/`。

| 部门 | 允许输入 | 当前正式输出 | 交给谁 | 完成条件 |
|---|---|---|---|---|
| 故事原著部 | `project.json`、`story-original/bible/source/`、`project-memory.md`、用户明确指定材料 | `story-original/novel.md`、`story-original/bible/story-bible.md`；角色总卡的 `Section 1 源头 Canon` 写入 `director-room/characters/` | 编剧部、导演部 | 原著正文、故事 Bible、角色源头 Canon 和来源登记可互相印证 |
| 编剧部 | 原著正式输出、角色总卡、项目长期记忆、`screenwriting/` 内已保留的逐集脚本材料 | `screenwriting/season-screenwriting-main.md`、`screenwriting/{episode-id}/screenwriting-main.md` | 导演部、配音部、音乐部 | 剧、集、场/分镜层级清晰；人物目标、台词、动作、情绪连续 |
| 导演部 | 编剧正式输出、`director-room/characters/` 角色总卡、必要故事 Bible | `director-room/characters/` 角色总卡入口；`director-room/{season-id}/{episode-id}/{shot-group-id}/{shot-id}/` 分镜目录，其中 `{shot-id}.md` 是唯一共享文档，`{shot-id}.png` 和 `{shot-id}.mp4` 是导演认可后的分镜图与分镜视频 | 美术部、提示词部、视频生成部、剪辑部 | 全片角色入口清晰；每个分镜有明确人物状态、动作入口、动作出口、镜头意图和质量通过标准；总导演签署后作为该分镜唯一共享入口 |
| 美术部 | 导演分镜要求、角色总卡、场景/道具 canon | 角色母图图片放回 `director-room/characters/` 并在对应角色卡 `Section 3` 写入角色图提示词；美术方案和过程版本进入本部门隐藏区；导演认可后的分镜图片回到对应分镜目录 | 提示词部、视频生成部、导演部 | 角色身份、脸部骨相、服装、空间、道具和画风不互相打架；角色母资产入口与角色卡一致；角色母卡符合 `PROJECT-CHAR-MODEL-SHEET-V2`，包含转面、表情、色板和道具格；最终分镜资产已回到导演部对应分镜目录 |
| 配音部 | 编剧台词、导演语气要求、角色声音卡 | 角色级声音锁、试听母音频和音频生成提示词写回 `director-room/characters/` 对应角色卡入口；声音方案和过程版本进入本部门隐藏区；导演认可后的分镜配音回到对应分镜目录 | 视频生成部、剪辑部、导演部 | 每个主角色有可追踪声音锁、试听母音频、音频生成提示词和 QC 状态；每句台词有角色、情绪、语速、气口和可用音频；最终分镜音频已回到导演部对应分镜目录 |
| 音乐部 | 剧本情绪线、导演节奏、剪辑需求 | 音乐方案和过程版本进入本部门隐藏区；导演认可后的分镜音乐回到对应分镜目录 | 剪辑部、交付部、导演部 | cue 点、情绪功能、进入退出位置清楚；最终分镜音乐已回到导演部对应分镜目录 |
| 提示词部 | 导演要求、美术资产、配音口型需求、视频工具限制 | 提示词结论写回 `{shot-id}.md` 对应区块；候选和测试进入本部门隐藏区 | 视频生成部、导演部 | 提示词不改剧情、不改身份、不重设空间，只把上游要求转成可执行提示 |
| 视频生成部 | 导演分镜、参考帧、提示词、配音/口型要求 | 视频过程版本进入本部门隐藏区；导演认可后的分镜视频回到对应分镜目录，文件名为 `{shot-id}.mp4` | 剪辑部、导演部 | 镜头人物不断线，动作不无故停顿，画面与导演要求一致；最终分镜视频已回到导演部对应分镜目录 |
| 剪辑部 | 通过 QC 的视频、配音、音乐、字幕和导演节奏 | 剪辑过程版本进入本部门隐藏区；导演认可后的分镜剪辑交接回到对应分镜目录 | 导演部、交付部 | 声画同步，节奏顺，人物位置、情绪和动作接得上 |
| 成片交付部 | 导演通过的剪辑预览、交付规格、字幕音频 | `delivery-room/delivery-main.md`、最终成片与交付记录 | 用户、项目归档 | 导演终审通过，技术 QC 通过，版本归档清楚 |

未启动部门不提前生成大量空目录。某部门开始工作前，项目办公室只创建该部门必要的当前正式文档、`.work/`、`.history/` 和本阶段所需的交接记录。

## 16. 项目循环控制与导演衔接

项目办公室的职责是让创作不断线，而不是替代任何部门创作。它只负责把关状态、交接、返工路径和版本边界。

统一状态：

```text
not_started
ready
in_progress
needs_fix
blocked
locked
delivered
```

阶段冻结顺序：

```text
故事锁定 → 编剧锁定 → 导演分镜锁定 → 美术/配音/音乐/提示词就绪 → 视频镜头通过 → 剪辑通过 → 成片交付
```

导演连续性闸门：

- 编剧交给导演前，必须能看出每个主要人物在本集的目标、情绪变化、进入状态和离开状态。
- 导演锁定分镜前，必须写清人物在每个分镜的动作入口、动作出口、视线、站位、关键道具和情绪落点。
- 美术、提示词、视频生成不能改变人物身份、服装体系、空间关系和关键道具位置。
- 视频镜头不能接受“人物突然中断、停顿、消失、情绪跳变、动作不接上”的结果；此类问题必须退回到最小责任部门。
- 剪辑不能用剪切掩盖剧情缺口。剪辑发现人物位置、情绪或动作接不上时，应退回导演或视频生成部，而不是自行改 canon。

共享分镜文档优先：

- 导演分镜锁定后，项目办公室为该分镜建立 `director-room/{season-id}/{episode-id}/{shot-group-id}/{shot-id}/` 分镜目录；后续部门围绕其中同一个 `{shot-id}.md` 补充自己负责的区块。
- 图片需求、图片提示词、角色参考、场景参考、视频生成要求、配音口型要求、音乐 cue、剪辑衔接和 QC 回传，都写入该分镜文档的对应部门区块。
- 各部门可以在自己的 `.work/` 中保留草稿、失败尝试、候选提示词、测试参数和废弃版本，但明面正式结论必须回到同一个分镜目录：文字结论回到 `{shot-id}.md`，导演认可后的分镜图片、视频、音频和剪辑交接文件都放在该分镜目录内。
- 被总导演签署的导演区块不得被下游改写；下游只能追加自己拥有的区块或提出返工。

返工只退回到最小必要上游：

```text
故事事实错 → 故事原著部
戏剧动机或台词错 → 编剧部
镜头调度或人物动作不清 → 导演部
形象、空间、道具错 → 美术部
声音、语气、气口错 → 配音部
提示词误读上游 → 提示词部
画面生成失败 → 视频生成部
声画节奏不接 → 剪辑部
交付格式或终审问题 → 成片交付部
```

导演只需要看三类项目办公室信息：

```text
.project/status.md
.project/blockers.md
.project/final-approval-gate.md
```

## 17. 导演部分镜目录契约

导演部正式启动时，项目办公室只创建必要目录，不提前铺满空文件夹。导演部根目录同时承载全项目最简角色入口 `characters/`，以及按“季 -> 集 -> 分镜组 -> 分镜”规划的分镜目录。`characters/` 可由项目办公室在导演分镜阶段前提前创建，作为全片角色总卡正式归口；这不代表导演分镜已经启动。一个分镜就是一个完整目录，目录内放该分镜唯一说明文档、分镜图片、分镜视频和导演认可后的必要资产。

推荐目录：

```text
director-room/
  characters/
    character-index.md
    CHAR-001-name.md
  {season-id}/
    season-director-main.md
    {episode-id}/
      episode-director-main.md
      {shot-group-id}/
        group-main.md
        {shot-id}/
          {shot-id}.md
          {shot-id}.png
          {shot-id}.mp4
          assets/
            voice/
            music/
            edit/
  .work/
    agents/
      director-agent/
      scene-breakdown-agent/
      visual-continuity-agent/
      shot-planner-agent/
      scene-coordinate-agent/
      cinematographer-agent/
      storyboard-agent/
      handoff-package-agent/
      director-qc-agent/
      user-feedback-triage-agent/
    tmp/
  .history/
```

目录含义：

```text
director-room/characters/                                                   全片唯一对外角色总卡入口
director-room/characters/character-index.md                                角色总卡索引
director-room/characters/CHAR-001-name.md                                  单个角色共享总卡
director-room/characters/c###m.png                                         对应角色母图；正式图片与提示词随角色卡归口
director-room/characters/c###-voice-v###-preview.wav                       对应角色声音母样试听；正式路径、提示词和 QC 状态随角色卡 Section 4 归口
director-room/{season-id}/season-director-main.md                         季级导演入口
director-room/{season-id}/{episode-id}/episode-director-main.md           集级导演入口
director-room/{season-id}/{episode-id}/{shot-group-id}/group-main.md      分镜组入口
director-room/{season-id}/{episode-id}/{shot-group-id}/{shot-id}/         单个分镜完整目录
director-room/{season-id}/{episode-id}/{shot-group-id}/{shot-id}/{shot-id}.md   单个分镜唯一共享文档
director-room/{season-id}/{episode-id}/{shot-group-id}/{shot-id}/{shot-id}.png  导演认可后的分镜图片
director-room/{season-id}/{episode-id}/{shot-group-id}/{shot-id}/{shot-id}.mp4  导演认可后的分镜视频
director-room/{season-id}/{episode-id}/{shot-group-id}/{shot-id}/assets/        该分镜导演认可后的配音、音乐、剪辑交接等必要资产
director-room/.work/agents/{agent-name}/                                      员工/agent 草稿、过程、评分、返工和废弃文件
director-room/.work/tmp/                                                      临时拼装材料
director-room/.history/                                                       旧版、废弃结构、迁移遗留
```

`{shot-id}.md` 采用区块所有权，不采用多个部门互相覆盖。这个文档同时承载分镜说明、美术要求、图片提示词、视频提示词、角色卡限制、场景站位、运镜走向和各部门回填结论。推荐结构：

```text
# {shot-id} 分镜文档

## 0. 镜头元信息
owner: project-office

## 1. 导演签署区
owner: director-room
status: draft | locked | needs_fix

### 分镜说明
### 角色卡限制
### 场景站位
### 运镜走向

## 2. 美术资产区
owner: art-room
status: not_started | in_progress | locked | needs_fix

## 3. 图片提示词区
owner: prompt-room
status: not_started | in_progress | locked | needs_fix

## 4. 配音与口型区
owner: voice-room
status: not_started | in_progress | locked | needs_fix

## 5. 音乐与声音节奏区
owner: music-room
status: not_started | in_progress | locked | needs_fix

## 6. 视频生成区
owner: video-production-room
status: not_started | in_progress | locked | needs_fix

## 7. 剪辑衔接区
owner: edit-room
status: not_started | in_progress | locked | needs_fix

## 8. 导演回看与返工记录
owner: director-room + project-office
```

硬规则：

- 一个分镜/镜头只有一个正式分镜目录，目录内只有一个正式共享文档 `{shot-id}.md`。
- 导演部员工/agent 不在明面目录各自输出正式文件；员工过程全部进入 `director-room/.work/agents/{agent-name}/`。
- 总导演认同并锁定后，`## 1. 导演签署区` 才能成为下游正式输入。
- 下游部门只能修改自己拥有的区块，不能改导演区块、角色 canon 或其他部门锁定区块。
- 提示词部不拥有创作意图，只拥有模型表达规范；图片提示词和视频提示词必须回到对应分镜文档的提示词区。
- 工具日志、失败图、失败视频、候选提示词、测试参数和废弃版本进入各部门隐藏 `.work/`，不得塞进 `{shot-id}.md` 或分镜正式资产位置。
- 只有总导演认可、或按项目办公室质量门标记为可交付的最终文件，才能进入该分镜目录。
- 具体分镜的最终图片必须命名为 `{shot-id}.png`；最终视频必须命名为 `{shot-id}.mp4`；配音、音乐、剪辑交接等必要资产放入该分镜目录下的 `assets/`。
- 具体分镜最终视频文件名必须使用分镜名 / 分镜 ID，不使用 `approved_v3.mp4`、`final_final.mp4` 或工具随机名。
- 若某区块发现上游不清楚，状态标为 `needs_fix`，通过项目办公室返工入口退回最小责任部门。

其他台账只在需要追溯时读取，不进入导演日常判断视野。

## 18. 全部门资产版本库与最终归口契约

所有专业部门的过程区只保存制作过程、候选和废弃版本；凡服务具体分镜的最终认可结果，必须回到导演部对应分镜目录。正在制作的每一个资产，都必须在本部门隐藏工作区建立独立版本库；试错、废弃、未选中、返工前和被替换版本不进入明面目录。

推荐目录：

```text
art-room/
  art-main.md
  shared-assets/
    asset-index.json
    props/
    overlays/
    style/
  .work/
    asset-versions/
      {asset-id}/
        20260620v0001.png
        20260620v0002.png
        manifest.jsonl
  .history/

video-production-room/
  video-main.md
  .work/
    asset-versions/
      {shot-id}/
        20260620v0001.mp4
        20260620v0002.mp4
        manifest.jsonl
  .history/

director-room/{season-id}/{episode-id}/{shot-group-id}/{shot-id}/
  {shot-id}.md                         分镜说明、导演要求和各部门共享区块
  {shot-id}.png                        导演认可后的该分镜最终图片
  {shot-id}.mp4                        导演认可后的该分镜最终视频
  assets/
    voice/                             导演认可后的该分镜配音
    music/                             导演认可后的该分镜音乐
    edit/                              导演认可后的该分镜剪辑交接文件
```

命名规则：

```text
{department}/.work/asset-versions/{asset-id-or-shot-id}/YYYYMMDDvNNNN.ext
```

示例：

```text
art-room/.work/asset-versions/c001-portrait/20260620v0001.png
video-production-room/.work/asset-versions/SC001-SH010/20260620v0002.mp4
voice-room/.work/asset-versions/SC001-SH010-D011/20260620v0001.wav
```

公共可复用视觉母资产正式归口：

```text
art-room/shared-assets/
```

适用范围包括阵营徽章、旗帜、纹样、印章、封条、石刻符号、常驻道具母版、公共服饰纹样和全剧风格母资产。它们由美术部维护正式图片和 QC，项目办公室维护归口契约，下游部门通过正式路径引用。

角色母资产仍按角色总卡合同归口到 `director-room/characters/`。具体分镜最终图片、视频、配音、音乐和剪辑交接仍回到对应分镜目录。公共资产不因被某个分镜使用而复制进该分镜目录；只有该分镜独有损坏、遮挡、角度或局部重绘结果，才作为分镜资产回到对应分镜目录。

角色声音母样属于角色总卡入口的一部分，正式可见试听文件随角色卡放入 `director-room/characters/`；配音部隐藏版本库继续保存同一声音锁的过程版本、候选版本、失败版本和 manifest。分镜级最终台词音频不放入角色目录，仍按对应分镜目录 `assets/voice/` 归口。

公共视觉资产契约：

```text
.project/contracts/shared-visual-assets.md
```

硬规则：

- 一个正在制作的资产、音频、音乐 cue、视频镜头或剪辑段，对应一个隐藏版本库文件夹。
- `{asset-id}` 使用项目统一资产 ID 或镜头共享文件中的资产 ID，不临时乱命名。
- 文件名使用 `YYYYMMDDvNNNN.ext`；同一资产内按生成顺序递增，不复用编号。
- 所有被废弃、未选中、返工前、被替换的图片、音频、音乐、视频或剪辑版本都进入该资产自己的隐藏版本库。
- 部门目录不得创建明面 `raw/`、`rejected/`、`approved/` 目录作为正式生产结构；这些状态写入隐藏版本库 manifest。
- 具体分镜的最终认可图片只进入对应分镜目录并命名为 `{shot-id}.png`；最终认可视频只进入对应分镜目录并命名为 `{shot-id}.mp4`；最终认可配音、音乐和剪辑交接进入该分镜目录下的 `assets/`。
- `{shot-id}.md` 只引用最终路径和必要的版本库路径，不塞候选图、候选音频、候选视频或工具日志。
- `manifest.jsonl` 只写最小追溯信息：版本文件、来源提示词或线程、状态、废弃原因、是否值得沉淀为经验。
- 只有可复用的经验才进入 `project-memory.md`；普通试错过程只留在隐藏版本库。

## 19. 项目总文档与最终成果规格

每个项目根目录必须维护一份项目总文档：

```text
project-spec.md
```

`project-spec.md` 只记录全项目稳定规格，不记录过程讨论。它至少说明：

```text
项目类型与目标平台
画幅比例
最终图片规格
视频交付规格
音频交付规格
字幕与文字要求
清晰度、码率、格式和色彩要求
预览版与最终版区别
未确认项和决策人
```

各部门只要产物会影响最终画面、声音或交付质量，都必须按 `project-spec.md` 执行。若工具能力达不到规格，不能静默降级，必须写入 `.project/blockers.md` 或交接风险。

