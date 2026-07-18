# 项目管理规范模板

本文件是项目办公室用于创建项目现场文档的模板，不要求各部门 skill 直接引用。创建或初始化项目时，项目办公室必须在项目根目录生成 `project-management.md`，各部门只读取该项目现场文档中索引指定的小节。

项目现场文档必须先放索引，避免部门读取庞大文档。

## 阅读索引模板

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

项目管理的目的不是把岗位变成机器螺丝钉，而是在保证质量和流程的同时，尊重每个岗位的专业判断、创造力和主动性。

共同原则：

- 化繁为简：只保留真正帮助生产的结构。
- 尊重创作：流程服务创作，不用流程压扁人。
- 一眼可读：正式输出必须让下游马上知道看什么、用什么、下一步做什么。
- 过程隐藏：草稿、日志、评分、返工过程和项目管理台账默认进入隐藏目录。
- 长期沉淀：只有能复用的经验才进入项目长期记忆。

## 2. 明面目录规则

明面目录只放当前正式产物。每个部门默认只有一个当前正式入口文档，必要时可有少量固定索引。

默认部门结构：

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

正式输出必须从大到小组织，让人一眼看懂。

推荐层级：

```text
剧
  集
    场
      镜头 / 分镜
```

部门正式输出只写本部门应交付的结论，不塞过程表格、内部评分、工具日志或多轮讨论。

当前正式文档由项目现场版填写，例如：

```text
department/current-output.md
```

具体文件名可按项目既有约定调整，但同一部门必须保持“当前正式入口唯一、旧过程隐藏”的原则。

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

判断原则：能让另一个人恢复项目状态、交接关系和质量门的轻量文件要同步；临时素材、旧包、跑批日志、失败版本、缓存和个人本地配置不提交。真正可复用的经验整理进 `project-memory.md`。

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

只有确认能长期复用的教训，才由项目记忆整理员提炼进 `project-memory.md`。

## 7. 项目长期记忆

项目根目录可有：

```text
project-memory.md
```

它不是流水账，只保存压缩后的长期规则。整理规则见：

```text
project-management.md 的长期记忆小节；详细整理动作由项目办公室执行
```

各部门只能把候选经验放入：

```text
department/.work/memory-candidates.md
```

项目办公室下的 `project-memory-curator` 负责筛选、合并、删除和改写长期记忆。

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

项目办公室负责维护本模板，并在每个项目根目录生成项目现场版 `project-management.md`。

部门 skill 不直接引用本模板。部门执行项目任务时，只读项目根目录 `project-management.md` 的索引和自己需要的小节。

修改本模板必须由用户明确要求。

任何部门正式启动前，项目办公室必须先补齐该部门的输入准入、输出与目录契约。未补齐时，该部门状态为 `blocked_needs_project_contract`，不得从部门 skill 中临时拼路径。

## 11. 部门输入准入模板

具体项目中，某个部门可读取哪些项目文件、哪些能进入 canon、哪些只能辅助参考、哪些默认排除，应写在项目根目录 `project-management.md`，不硬编码在部门 skill 里。

示例：故事原著部输入准入。

```text
A 类：项目级故事前提源，优先用于建立原著部 Bible。
B 类：逐集故事回补参考，只能用于补齐 Bible 中的事件、人物和连续性缺口。
C 类：只作辅助参考，不能直接决定故事 canon。
D 类：默认排除，不能进入原著 Bible，除非用户明确要求并确认其故事意义。
```

项目办公室创建现场文档时，应按具体项目补齐对应路径清单，并在阅读索引里只让相关部门读取该小节。

## 12. 部门输出与目录契约模板

具体项目中，某个部门的正式输出、隐藏输出、目录含义、交接文件路径和历史归档位置，应写在项目根目录 `project-management.md` 或 `.project/` 下的交接契约中，不硬编码在部门 skill 里。

部门 skill 只说明专业职责和质量判断；项目现场文档说明：

```text
正式工作目录
正式输出文件
隐藏工作材料
历史归档位置
交接文件路径
禁止散落的位置
完成条件
```

项目办公室创建现场文档时，应按具体项目补齐对应输出与目录契约，并在阅读索引里只让相关部门读取该小节。

## 13. 后续部门契约补齐规则模板

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

契约可以写在项目根目录 `project-management.md` 的新小节，也可以写入项目隐藏管理目录下的部门契约文件，但 `project-management.md` 的阅读索引必须指向它。

未补齐契约的部门不得正式生产。

## 14. 跨部门角色总卡合同模板

角色总卡是跨部门共享文件，但不是无边界共写。项目办公室必须在项目现场文档中指定角色总卡目录和区块所有权。默认正式归口放在导演部根入口 `director-room/characters/`，让导演和下游只读一个清晰入口；原著、编剧、美术、配音和视频生成仍按区块维护自己的专业内容。

推荐目录：

```text
director-room/characters/
  character-index.md
  CHAR-001-name.md
  CHAR-002-name.md
```

一角色一份总卡。各部门只允许修改自己拥有的区块：

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

角色总卡修改规则：

- 原著部只改 Section 1。
- 编剧部只改 Section 2。
- 美术部只改 Section 3。
- 配音部只改 Section 4。
- 视频生成部只改 Section 5。
- Section 1 被锁定后，任何下游不得直接修改，只能提出 `needs_story_source_fix`。
- 美术部可以读取 Section 1 和 Section 2，但主要依据 Section 2 做影视视觉落地，并用 Section 1 校验不能画偏。
- 视频生成部可以读取 Section 1-4，但只把执行中的角色漂移风险、口型风险和动作连续性锁点写入 Section 5，不得用生成结果反改 canon。

## 15. 全链路输入输出最小契约模板

项目现场文档必须有一张轻量全链路表，说明每个部门允许读什么、正式交付什么、交给谁、完成条件是什么。表格只写结论，不放过程。

推荐链路：

```text
故事 → 编剧 → 导演 → 美术/配音/音乐/提示词 → 视频生成 → 剪辑 → 成片交付
```

每行至少包含：

```text
部门
允许输入
当前正式输出
下游交接对象
完成条件
```

未启动部门不提前生成大量空目录。某部门开始工作前，项目办公室只创建该部门必要的当前正式文档、`.work/`、`.history/` 和本阶段所需的交接记录。

## 16. 项目循环控制与导演衔接模板

项目办公室必须帮助导演看见质量状态和断点，但不替代任何部门创作。

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

导演连续性闸门至少检查：

```text
人物进入状态
人物离开状态
动作是否接上
情绪是否跳变
站位和视线是否连贯
服装、道具、空间是否一致
台词、气口和口型是否匹配
```

返工只退回到最小必要上游，并写入 `.project/revision-log.jsonl`。导演日常只看：

```text
.project/status.md
.project/blockers.md
.project/final-approval-gate.md
```

## 17. 导演部分镜目录契约模板

导演部启动时，项目办公室必须定义导演部根入口和“季 -> 集 -> 分镜组 -> 分镜”的目录规则。原则是：`director-room/characters/` 是全片唯一对外角色总卡入口，且可由项目办公室在导演分镜阶段前提前创建；这不等于导演分镜已经启动。员工/agent 过程隐藏；每个分镜一个完整目录；导演签署后的 `{shot-id}.md` 成为下游共同补充的唯一正式文档，导演认可后的分镜图片、分镜视频和必要资产回到同一分镜目录。

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
    agents/{agent-name}/
    tmp/
  .history/
```

共享分镜文档推荐区块：

```text
0. 镜头元信息                 owner: project-office
1. 导演签署区                 owner: director-room
2. 美术资产区                 owner: art-room
3. 图片提示词区               owner: prompt-room
4. 配音与口型区               owner: voice-room
5. 音乐与声音节奏区           owner: music-room
6. 视频生成区                 owner: video-production-room
7. 剪辑衔接区                 owner: edit-room
8. 导演回看与返工记录         owner: director-room + project-office
```

规则：

- 一个分镜/镜头只有一个正式分镜目录，目录内只有一个正式共享文档 `{shot-id}.md`。
- 导演部员工/agent 草稿、评分、返工和废弃文件进入 `director-room/.work/agents/{agent-name}/`。
- 总导演锁定导演区块后，下游部门只能追加或修改自己拥有的区块。
- 分镜说明、美术、图片提示词、视频提示词、角色卡限制、场景站位、运镜走向、配音口型、音乐 cue、剪辑衔接和 QC 回传都回到同一个 `{shot-id}.md`。
- 失败尝试、工具日志、测试参数和废弃候选进入各部门隐藏 `.work/`，不得污染 `{shot-id}.md` 或分镜正式资产位置。
- 只有总导演认可、或按项目办公室质量门标记为可交付的最终文件，才能进入该分镜目录。
- 具体分镜的最终图片必须命名为 `{shot-id}.png`；最终视频必须命名为 `{shot-id}.mp4`；配音、音乐、剪辑交接等必要资产放入该分镜目录下的 `assets/`。
- 具体分镜的最终视频文件名必须使用分镜名 / 分镜 ID，不使用 `approved_v3.mp4`、`final_final.mp4` 或工具随机名。

## 18. 全部门资产版本库与最终归口契约模板

项目办公室必须定义各专业部门的隐藏版本库和导演分镜目录回收规则。原则是：专业部门隐藏工作区保存试错、废弃和替换版本；凡服务具体分镜的最终认可结果，回到导演部对应分镜目录。

推荐目录：

```text
art-room/
  art-main.md
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

规则：

- 一个正在制作的资产、音频、音乐 cue、视频镜头或剪辑段，对应一个隐藏版本库文件夹。
- `{asset-id}` 使用项目统一资产 ID 或镜头共享文件中的资产 ID。
- 文件名使用 `YYYYMMDDvNNNN.ext`；同一资产内按生成顺序递增，不复用编号。
- 所有被废弃、未选中、返工前、被替换的图片、音频、音乐、视频或剪辑版本都进入该资产自己的隐藏版本库。
- 部门目录不得创建明面 `raw/`、`rejected/`、`approved/` 目录作为正式生产结构；这些状态写入隐藏版本库 manifest。
- 具体分镜的最终认可图片只进入对应分镜目录并命名为 `{shot-id}.png`；最终认可视频只进入对应分镜目录并命名为 `{shot-id}.mp4`；最终认可配音、音乐和剪辑交接进入该分镜目录下的 `assets/`。
- `{shot-id}.md` 只引用最终路径和必要的版本库路径，不塞候选图、候选音频、候选视频或工具日志。
- `manifest.jsonl` 只写最小追溯信息：版本文件、来源提示词或线程、状态、废弃原因、是否值得沉淀为经验。
- 只有可复用的经验才进入 `project-memory.md`；普通试错过程只留在隐藏版本库。

## 19. 项目总文档与最终成果规格模板

每个项目根目录必须维护：

```text
project-spec.md
```

`project-spec.md` 是项目总文档，记录全项目稳定规格，不记录过程讨论。它至少说明：

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

