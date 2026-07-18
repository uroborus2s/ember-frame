# 音乐部当前入口

owner: music-room
status: g_p_retake_stem_candidates_generated_pending_human_listening_director_mix
last_updated: 2026-06-21

## 1. 当前任务

第 01 集 G-P/P-01 至 P-05 已由总导演签署。音乐部已完成冷开声音节奏第一版正式回填，P-01 至 P-05 均有 cue；正式 cue、环境声和声音节奏结论已写回对应分镜文档 `## 5. 音乐与声音节奏区`。C021 北境共生兽已补 48 kHz stereo 声效方向 preview，并完成文件级 QC；该小样只用于角色卡闸门听审，不替代分层 stem、避让测试和成片终混。P-01..P-05 仍未发现 `assets/music/` final 音频文件。

## 2. 总导演音乐命令

| 分镜 | 声音/音乐任务 | 入点与退出 |
|---|---|---|
| P-01 | 骨钟、巨兽撞门、绞盘、暴雪、粮门死黄气氛；不铺旋律 | 黑场骨钟入，粮筹划册声出 |
| P-02 | 粮筹划册、灶膛碎、麦粒落泥、黑铁环、虫蜡黏响 | 接骨钟余音，虫蜡剥离出 |
| P-03 | 儿童歌声中断、针破皮、木牌轻响、白墙静默 | 接虫蜡针声，木牌轻响出 |
| P-04 | 雨打瓦、红线崩断、刀尖刮墙、白册合页 | 白册合页切断雨声出 |
| P-05 | 鸡叫、湿松针脚步、兔子碰弓身、铜锣三下 | 鸡叫入，铜锣余音压入 A-01 |

音乐不得把 G-P 做成宏大热血片头；前半以制度机器声为主，旋律克制到近无。

## 3. G-P 声音方向

- 前半不铺满旋律，以骨钟、粮筹、虫蜡针、白册合页、铜锣、雨声和空间静默构成制度机器声。
- P-01 到 P-04 要冷、硬、短，不抢叙事证据。
- P-05 用鸡叫和铜锣把时代机器落回残阳坳。

## 4. 归口规则

过程版本进入 `music-room/.work/`；导演认可后的分镜音乐回到对应分镜目录 `assets/music/`。

## 5. 当前待处理声效

- C021-CREATURE-SFXLOCK-V001：过程版本 `music-room/.work/asset-versions/C021-CREATURE-SFXLOCK-V001/20260621v0001-preview.wav`；角色卡可听小样 `director-room/characters/c021-creature-sfx-v001-preview.wav`；两者实测 48 kHz stereo PCM WAV，8.000s。下一步需人工听审、拆分低频体量 / 骨铃绳环 / 门体受压 / 雪地重步 / 兽息 / 暴雪空间层，并测试不覆盖骨钟、床弩、军户喊声和粮门声桥。
- P-01 final stem 需求：`low_body_pressure`、`bone_bell_rope`、`gate_stone_stress`、`snow_heavy_steps`、`creature_breath_pain`、`blizzard_roomtone`；终混时头领喊声和骨钟优先，C021 不能连续咆哮或奇观化。
- P-02..P-05 final 声音文件均未生成：按各分镜 `## 4.5` checklist 和 `## 5` cue 点补齐环境声 / Foley / SFX，不得用近无音乐掩盖缺失。

## 6. 2026-06-21 G-P 配乐预览

根据用户要求“需要配乐”，音乐部为 G-P director cut preview v0001 生成 48 kHz stereo 音乐 / 声效氛围小样：

- `music-room/.work/asset-versions/G-P-MX-preview/20260621v0001/G-P_cold_open_score_preview_v0001_48k_stereo.wav`

音乐设计：

- 低频冷 drone 承接北墙、白册、虫蜡和残阳坳；
- 骨钟、虫蜡针、雨夜低击、铜锣三下作为制度机器声；
- 音乐在旁白下自动压低，避免遮挡台词；
- 该版本是 preview，不是 final stem。下一步需拆为 `low_drone`、`bone_bell`、`wax_needle`、`rain_roomtone`、`copper_gong` 等 stem 并做导演听审。

## 7. 2026-06-21 G-P 重拍版 stem 候选

音乐部已按 G-P 重拍命令生成 P-01 至 P-05 的 48 kHz stereo PCM WAV 候选 mix 与分层 stem，并写入分镜 `assets/music/` 和本部门隐藏版本库。该批次用于剪辑候选声画装配，状态为 `music_room_qc_passed_pending_human_listening_director_mix`，不是导演终混 master。

正式文档：

- cue sheet: `music-room/G-P-remake-music-sfx-cue-sheet.md`
- stem handoff: `music-room/G-P-remake-stem-handoff.md`
- QC: `music-room/G-P-remake-music-sfx-qc.md`

分镜交接：

- `director-room/season-01/01/G-P/P-01/assets/music/`
- `director-room/season-01/01/G-P/P-02/assets/music/`
- `director-room/season-01/01/G-P/P-03/assets/music/`
- `director-room/season-01/01/G-P/P-04/assets/music/`
- `director-room/season-01/01/G-P/P-05/assets/music/`

特别说明：P-03 的 `child_song_timing_guide_no_voice` 只提供旧歌触发节奏，不含童声，不替代配音部 final；全部 cue 仍需与 final 台词、final 视频和剪辑时间线做人工听审与 ducking。
