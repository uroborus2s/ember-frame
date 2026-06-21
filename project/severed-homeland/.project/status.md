# 《断航故土》项目办公室状态

last_updated: 2026-06-21

## 当前整理结论

- 项目根目录已切换为现场版 `project-management.md` 统一管理口径。
- 项目根目录已建立 `project-spec.md`，用于维护图片、视频、音频、字幕和最终交付规格。
- 已保留：项目长期记忆、原著正式成果、故事基础来源、角色总卡、现有编剧成果、逐集编剧相关材料。
- 已迁出：旧导演、美术、提示词、视频、音频、剪辑、渲染、质检和过程性生产材料。
- 根目录 `memory/` 已迁入隐藏历史：`.project/history/from-previous-root/memory-20260620/`。
- 根目录 `bible/`、`outline/`、`synopsis/` 已归入 `story-original/`。
- 根目录 `01`-`12` 已归入 `screenwriting/`。
- 角色总卡已归口到导演部根入口 `director-room/characters/`；角色母图图片和角色图提示词随对应角色卡归口，不再拆到独立正式资产目录。
- 旧内容包位置：`C:\Users\uroborus\Downloads\severed-homeland-legacy-before-project-office-cleanup-20260620-180445.tar.gz`

## 当前可用正式入口

- 项目规范：`project-management.md`
- 项目总文档 / 成果规格：`project-spec.md`
- 项目长期记忆：`project-memory.md`
- 项目配置：`project.json`
- 原著：`story-original/novel.md`
- 原著前提：`story-original/bible/story-bible.md`
- 故事基础来源：`story-original/bible/source/`
- 角色总卡与角色母图：`director-room/characters/`
- 编剧总稿：`screenwriting/season-screenwriting-main.md`
- 已有分集编剧稿：`screenwriting/01/screenwriting-main.md`、`screenwriting/02/screenwriting-main.md`、`screenwriting/03/screenwriting-main.md`
- 第 04-12 集待精修编剧来源：`screenwriting/{04-12}/.work/from-root-episode-20260620/`

## 当前阶段状态

| 环节 | 状态 | 说明 |
|---|---|---|
| 故事原著 | locked | 保留正式原著和故事 Bible |
| 编剧 | in_progress | 已保留第 01-03 集编剧主稿和季总稿；第 04-12 集旧逐集稿已归入编剧部 `.work/`，等待精修成正式主稿 |
| 导演 | not_started | 需等待编剧正式交接 |
| 美术 | in_progress | C001/C002 角色母图已回写角色卡入口；其他资产后续按新契约重建 |
| 配音 | not_started | 需等待编剧台词和导演语气要求 |
| 音乐 | not_started | 需等待剧本情绪线和导演节奏 |
| 提示词 | not_started | 需等待导演分镜和美术正式资产 |
| 视频生成 | not_started | 需等待提示词、参考帧和配音口型要求 |
| 剪辑 | not_started | 需等待通过 QC 的视频、配音、音乐 |
| 成片交付 | not_started | 需等待导演终审剪辑版本 |

## 下一步项目办公室动作

1. 编剧部正式启动前，确认第 01-03 集编剧稿是否作为当前正式稿继续使用。
2. 编剧部继续第 04-12 集时，从各集 `.work/from-root-episode-20260620/` 读取旧逐集稿，精修后写成 `screenwriting/{episode-id}/screenwriting-main.md`。
3. 导演部启动前，补齐导演部正式输出路径和分镜连续性检查清单。
4. 导演部启动时采用“一个镜头一个共享正式文件”，员工/agent 过程写入隐藏工作区，下游部门按区块补充同一镜头文件。
5. 所有下游部门启动前，只创建必要目录和当前正式文档。

