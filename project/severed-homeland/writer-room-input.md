# Writer Room 输入提示词

## 任务

使用 `writer-room` 重写 `severed-homeland` 第一季全剧。

本项目采用重制模式：保留设定，废弃旧剧本、旧分镜、旧资产、旧资产提示词、旧视频提示词和旧 ComfyUI 参数。

本轮只执行 `series mode`，也就是全剧基础模式。不要开始任何单集剧本、分镜、资产或视频提示词工作。全剧基础模式完成并审核通过后，才允许进入后续单集开发。

## 项目根

```text
project/severed-homeland/
```

## 固定读取输入

只读取下列正式输入：

```text
project.json
背景.md
bible/world.md
bible/geography.md
bible/factions.md
bible/timeline.md
bible/characters.md
bible/scenes.md
bible/continuity.md
bible/visual-style.md
writer-room-input.md
```

`背景.md` 是最完整的设定源。`bible/characters.md` 和 `bible/scenes.md` 是已经整理过的角色与场景设定源。其余 bible 文件如果内容较短或只有占位说明，应由 writer-room 在 series mode 中根据 `背景.md` 重编。

## 禁止读取为 Canon

不要把下面目录中的内容当成剧情 canon：

```text
legacy/
art/
assets/
prompts/
01/
02/
03/
04/
05/
06/
07/
08/
09/
10/
11/
12/
```

这些目录中的旧内容已经归档或留作空生产骨架。旧内容只能作为人工回看资料，不能直接继承到新剧本。

## 重写目标

1. 保留六域大陆、昭明帝国、肃明国、清明籍、断航、旧驿、日月故土宣言、护送旅程、北境压力和故土重释这些核心设定。
2. 重写第一季全剧结构，目标为 12 集，每集 3 分 30 秒到 5 分钟。
3. 第一季应以短剧节奏推进：前 5 秒有钩子，30 秒内建立危机，中段持续升级，结尾保留反转或悬念。
4. 每集主要角色控制在 3 到 5 人，主要场景控制在 2 到 4 个，便于后续 AI 视频生产。
5. 剧本要为后续超写实、电影级质感、极致逼真的视频制作服务，动作必须可拍、可生成、避免僵硬和抽象内心戏。
6. 纪年体系必须使用承接式纪年：旧时代用旧历，新王朝用新历；旧王朝灭国于旧历5249年，该年就是新历元年。第一季开端固定为新历1226年或新王朝历1226年，不再使用“帝国历1226年”。
7. 全剧风格固定为低魔东方史诗护送剧，叠加制度悬疑、政治阴谋和大陆战争阴影。不得把本剧定成诙谐幽默主类型，也不得让大陆争霸取代第一季护送主线。

## 输出要求

本轮只执行 `series mode`，产出以下全剧基础文件：

```text
bible/world.md
bible/geography.md
bible/factions.md
bible/timeline.md
bible/characters.md
bible/scenes.md
bible/continuity.md
bible/visual-style.md
outline/series-outline.md
outline/episode-outline-index.md
synopsis/story-synopsis.md
memory/current-state.md
```

本轮不要创建或填写以下 episode mode 文件：

```text
01/brief/episode-brief.md
01/script/episode-outline.md
01/script/script-v01.md
01/script/final-script.md
01/reports/critique-v01.md
01/reports/continuity-report.md
01/reports/script-score.md
01/memory/current-state.md
01/memory/failure-patterns.json
01/memory/evolution-notes.md
```

这些单集文件必须等全剧基础审核通过后再开始。

## 全剧基础审核 Gate

`series mode` 完成后先停止，等待人工审核。审核至少确认：

- 世界观、地理、势力、时间线互相不冲突。
- 第一季全剧大纲足以支撑 12 集，每集 3 分 30 秒到 5 分钟。
- 分集大纲索引的每集冲突、钩子、结尾悬念和角色推进清楚。
- 角色 bible、场景 bible 和视觉基调能支持后续超写实、电影级视频制作。
- 没有继承旧剧本、旧分镜、旧资产提示词或旧 ComfyUI 参数。

审核通过前，不启动 episode mode、director-room、art-room、ComfyUI 或后期流程。

## 全剧基础通过后的清理规则

新的全剧基础审核通过后，删除当前仅用于重制输入、且不属于正式 writer-room 规范输出的临时设定文档和提示文件。

待删除文件包括：

```text
背景.md
writer-room-input.md
```

删除前必须确认其中有效信息已经完整吸收到以下规范文件：

```text
bible/world.md
bible/geography.md
bible/factions.md
bible/timeline.md
bible/characters.md
bible/scenes.md
bible/continuity.md
bible/visual-style.md
outline/series-outline.md
outline/episode-outline-index.md
synopsis/story-synopsis.md
```

`legacy/` 仍作为旧生产归档，不作为 writer-room、director-room 或 art-room 的正式输入。

## 质量约束

- 不复用旧集剧本结构。
- 不复用旧分镜和旧提示词。
- 不提前生成角色卡、物品卡、场景卡或视频提示词。
- 不把失败资产、废弃镜头、旧 ComfyUI 参数写入剧情事实。
- 所有重大设定变更必须写回对应 bible 文件。
- 全剧基础审核通过后，才能开始第 01 集 episode mode。
- 每集 final-script 通过后，才能交给 director-room 做资产前导演分镜包。
