# 重制归档报告

## 结论

`severed-homeland` 已进入重制模式。

保留为 writer-room 正式输入：

```text
project.json
writer-room-input.md
背景.md
bible/world.md
bible/geography.md
bible/factions.md
bible/timeline.md
bible/characters.md
bible/scenes.md
bible/continuity.md
bible/visual-style.md
```

已归档，不作为正式输入：

```text
legacy/pre-remake-2026-06-04/
```

归档内容包括旧剧本、旧分镜、旧导演文件、旧资产图、旧资产提示词、旧视频提示词、旧 ComfyUI 参数、旧渲染结果和旧后期材料。

## Writer Room 使用规则

后续使用 `writer-room` 重写全剧时，第一步只执行 `series mode`，也就是全剧基础模式。

本阶段只读取根目录正式输入和 `writer-room-input.md`。不要读取 `legacy/` 作为剧情 canon。

本阶段只产出：

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

全剧基础审核通过前，不启动第 01 集 episode mode，不启动 director-room，不启动 art-room，不生成资产或视频提示词。

新的单集时长规则为：

```text
每集 3 分 30 秒到 5 分钟。
```

## 全剧基础通过后的清理

新的全剧基础审核通过后，删除当前仅用于重制输入、且不属于正式 writer-room 规范输出的临时设定文档和提示文件：

```text
背景.md
writer-room-input.md
```

删除前必须确认其中有效信息已经完整吸收到：

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

## 下一步

运行 `writer-room` 的 series mode，重编全剧基础层、第一季全剧大纲、分集大纲索引和全剧梗概。完成后先进行人工审核，审核通过后再决定是否清理临时设定文档并进入第 01 集开发。
