# 跨部门角色总卡合同

角色总卡采用“一角色一文件、分区块协作”。它是角色 canon、影视化表演、美术视觉、配音声音和视频执行锁点的共享承载文件，但每个部门只能修改自己拥有的区块。

角色总卡正式归口放在导演部根入口，作为全片对外最简单、最稳定的角色输入。导演部负责把角色状态纳入作品总控视野；项目办公室负责区块契约；原著、编剧、美术、配音和视频生成部按各自专业区块维护同一份文件。

推荐目录：

```text
director-room/characters/
  character-index.md
  CHAR-001-name.md
  CHAR-002-name.md
```

## 区块所有权

```text
Section 1 源头 Canon              owner: story-original
Section 2 编剧影视化角色卡        owner: screenwriting
Section 3 美术视觉角色卡          owner: art-room
Section 4 配音声音角色卡          owner: voice-room
Section 5 视频执行角色卡          owner: video-production-room
Section 6 冲突与变更记录          owner: project-office 协调，各部门追加记录
```

下游部门发现上游区块不足时，不得直接覆盖上游内容；必须在 Section 6 记录缺口，并通过项目办公室返工入口退回对应部门。

## 文件模板

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
