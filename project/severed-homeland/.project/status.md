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
- 第 01 集导演总控已建立：`director-room/season-01/01/episode-director-main.md`
- 第 01 集 G-P 分镜组已由总导演签署过旧版导演区，但用户 2026-06-21 复审继续指出 v0002 仍不可读：P-01 像静态设定图，`粮门不开，人先补墙`、`北墙五百年，血从未干` 等台词对普通观众不直接，战争、强行征粮、儿童训化和追捕压力没有被镜头动作打出来。总导演已撤回 v0002 clarity approval，把 v0002 改列为失败诊断样片；编剧和导演已锁定 G-P 新一轮重写方向：P-01 直接交代北方兽族联盟撞关和粮仓锁死，P-02 直接拍强行征粮和全户入册，P-03 直接拍孩子被带去教成识别童，P-04 直接拍旧驿血牒追捕线。正式成片仍需基于新台词、新镜头命令重拍 final 24fps / 4K 视频源、final 配音、final stem、精确 overlay、终混、剪辑和交付规格闸门。

## 当前阶段状态

| 环节 | 状态 | 说明 |
|---|---|---|
| 故事原著 | locked | 保留正式原著和故事 Bible |
| 编剧 | g_p_user_review_rewrite_required | 第 01 集 G-P 冷开台词可听性与画面可见性被用户复审打回；已在 `screenwriting/01/screenwriting-main.md` 标记旧自检不通过并写入直接台词重写方向 |
| 导演 | g_p_director_rewrite_required | G-P v0002 可读性闸门撤回；P-01 至 P-04 已追加用户复审后的新拍摄命令，旧台词候选不得进正式 |
| 美术 | formal_reference_frames_all_approved | G-P/P-01 至 P-05 正式 `P-XX.png` 全部恢复；P-02 C017 按手返工和 P-04 逃跑运动返工均已通过 |
| 配音 | g_p_rewrite_voice_required | v0001 五句 Microsoft Huihui 解释旁白撤回；v0002 旧候选也因台词改写撤回，需按新直接台词重录 / 重生成并听审 |
| 音乐 | score_preview_generated_final_stems_pending | G-P/P-01 至 P-05 已完成制度机器声、静默点和 cue 入出点计划；G-P director cut preview v0001 已有 48 kHz stereo 程序化配乐 / 声效预览；最终音乐 stem、C021 分层与终混仍未完成 |
| 提示词 | video_shoot_prompt_package_ready_for_video_preflight | P-01 至 P-05 已完成 copy-ready 视频拍摄提示词包回填，P-02 已锁定 C017 执行按手、C016 登记、C025 护子失败 |
| 视频生成 | g_p_rewrite_source_retake_required | ComfyUI 已可调用，但现有 P-01 至 P-05 审片源不能继续包装；必须按新导演命令重拍可见动作，尤其 P-01 不得再是静态图 |
| 剪辑 | v0002_failed_diagnostic_waiting_rewrite | G-P director cut preview v0002 改列失败诊断样片，不再作为 clarity proof；下一剪辑必须基于新剧本、新配音和新源镜头 |
| 成片交付 | not_started | 需等待导演终审剪辑版本 |

## 下一步项目办公室动作

1. 编剧部正式启动前，确认第 01-03 集编剧稿是否作为当前正式稿继续使用。
2. 编剧部继续第 04-12 集时，从各集 `.work/from-root-episode-20260620/` 读取旧逐集稿，精修后写成 `screenwriting/{episode-id}/screenwriting-main.md`。
3. 以 G-P/P-01 至 P-05 为首批制作对象，但 v0002 可读性证明已撤回。当前下一轮优先执行 G-P 台词可听性和镜头动作重写后的 final 24fps / 4K 源镜头重拍、final 配音听审 / 切分、儿童试唱、final 音乐 / 声效 stem、精确 overlay 和终混，并保持成片交付阻塞。
4. 下游部门只能补充对应分镜文档的所属区块；导演签署区不得被覆盖。
5. 具体分镜最终图片、视频、配音、音乐和剪辑交接必须回到对应 `director-room/season-01/01/G-P/{shot-id}/` 目录。

