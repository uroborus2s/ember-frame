# 原著部 Bible 来源登记

status: locked_from_bible_only
project: severed-homeland
created_for: story-original
rule: 本轮原著 Bible 只使用由旧根目录 `bible/*.md` 迁入的来源文件。旧根目录 `bible/` 已封存到 `story-original/.history/from-root-foundation/bible-duplicate-20260620/`，活动来源文件统一位于 `story-original/bible/source/`。旧剧本、旧分镜、旧资产、旧提示词、旧视频、旧参数、旧剪辑和旧 story-original 产物均未作为原著前提。

## 已拷贝来源

| source_path | copied_to | source_tier | used_for_bible | bible_section | conflicts | decision |
| --- | --- | --- | --- | --- | --- | --- |
| `story-original/.history/from-root-foundation/bible-duplicate-20260620/world.md` | `story-original/bible/source/world.md` | A | true | 核心命题、主题、时代、法术、战争、第一季故事规则、Canon 禁令 | 无 | 作为最高层世界观前提采用 |
| `story-original/.history/from-root-foundation/bible-duplicate-20260620/continuity.md` | `story-original/bible/source/continuity.md` | A | true | 当前 canon 状态、正式事实源、全剧基础事实、第一季路线、全剧分季、禁止事项 | 无 | 作为连续性与禁令前提采用 |
| `story-original/.history/from-root-foundation/bible-duplicate-20260620/factions.md` | `story-original/bible/source/factions.md` | A | true | 种族势力、阵营裂缝、肃明统治、北境诸族、南部、东海、西部 | 无 | 作为势力与社会冲突前提采用 |
| `story-original/.history/from-root-foundation/bible-duplicate-20260620/geography.md` | `story-original/bible/source/geography.md` | A | true | 六域大陆、金河、白曜城、第一季行动路线、地理连续性 | 无 | 作为地理与路线前提采用 |
| `story-original/.history/from-root-foundation/bible-duplicate-20260620/timeline.md` | `story-original/bible/source/timeline.md` | A | true | 昭明历、肃明历、历史事件、第一季当季推进 | 无 | 作为历史纪年和因果前提采用 |
| `story-original/.history/from-root-foundation/bible-duplicate-20260620/characters.md` | `story-original/bible/source/characters.md` | A | true | 角色身份、目标、动机、弧线、关系、行为边界、角色禁令 | 无 | 作为人物前提采用 |
| `story-original/.history/from-root-foundation/bible-duplicate-20260620/scenes.md` | `story-original/bible/source/scenes.md` | A | true | 第一季场景路线、空间逻辑、场景锚点、复用规则、高风险场景 | 无 | 作为场景与空间戏剧前提采用 |
| `story-original/.history/from-root-foundation/bible-duplicate-20260620/visual-style.md` | `story-original/bible/source/visual-style.md` | A | true | 叙事风格、低魔动作边界、人族视觉、虫族统治、北境战争 | 无 | 作为文字描写的视觉与动作边界采用 |

## 已迁入但未纳入本轮 Bible 锁定的来源

| current_path | source_tier | used_for_bible | decision |
| --- | --- | --- | --- |
| `story-original/bible/source/outline/series-outline.md` | A | false | 保留作后续追溯和可能的 Bible 重整参考，不直接作为当前小说正文前提 |
| `story-original/bible/source/outline/episode-outline-index.md` | A | false | 保留作后续追溯和可能的 Bible 重整参考，不直接作为当前小说正文前提 |
| `story-original/bible/source/synopsis/story-synopsis.md` | A | false | 保留作后续追溯和可能的 Bible 重整参考，不直接作为当前小说正文前提 |

## 未纳入来源

本轮按用户要求未读取、未拷贝、未采用以下来源：

- `memory/`
- `screenwriting/{episode-id}/.work/from-root-episode-20260620/`
- `story-original/` 旧文件
- `screenwriting/`
- `director/`
- `storyboard/`
- `art/`
- `assets/`
- `prompts/`
- `production/`
- `renders/`
- `audio/`
- `post/`
- `qc/`
- `reviews/`

## 旧结构封存

为避免旧项目结果影响新流程，原 `story-original/` 下旧目录与旧文档已整体封存到：

```text
story-original/.history/from-previous-structure/2026-06-20/
```

该目录仅作追溯备份，不属于活动前提、活动正文、活动质检或活动交接内容。后续创作不得从该目录补设定、补剧情或补人物动机。

## 前提锁定结论

只有 `story-original/bible/story-bible.md` 中写明的内容可作为原著正文前提。`story-original/bible/source/*.md` 是来源拷贝，供追溯使用；未经整理进入 `story-bible.md` 的内容不得直接写入小说正文。
