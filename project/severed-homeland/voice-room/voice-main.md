# 配音部当前入口

owner: voice-room
status: g_p_retake_timed_48k_candidates_written_final_pending_human_listening_qc
last_updated: 2026-06-21

## 第 01 集 G-P 配音命令

source: `director-room/season-01/01/G-P/`

总导演已签署 G-P / P-01 至 P-05 重拍版配音方向。配音部只负责声音锁、台词 cue、候选音频、口型交接和听审 QC；不改导演正文、视频部、音乐部或项目台账。

## 2026-06-21 G-P 成片节奏版候选

- current_package: `voice-room/season-01/01/G-P/g-p-retake-voice-package-20260621.md`
- lipsync_handoff: `voice-room/season-01/01/G-P/g-p-retake-lipsync-handoff-20260621.json`
- audio_gate_qc: `voice-room/.work/asset-versions/G-P/audio-gate-qc-retake-20260621.md`
- timing_manifest: `voice-room/.work/asset-versions/G-P/runs/20260621-gp-retake-timed-48k-manifest.json`
- assets_voice: `director-room/season-01/01/G-P/P-01..P-05/assets/voice/`
- generated_candidates: 8 条成片节奏版 `candidate-48k.wav` 已写入各分镜 `assets/voice/`。
- sample_rate_note: 源 TTS 为 24 kHz mono；本批已裁头尾、按导演时间窗 time-fit，并上采样为 48 kHz mono PCM WAV。文件可进剪辑节奏候选，但不是 final。
- final_gate: 全部仍需人工听审、响度检查、伪影检查和导演确认；未达到成片 final 质量门前，不得改名为无 `candidate` 后缀的 final WAV。

| 分镜 | 配音/口型任务 | 当前裁决 |
|---|---|---|
| P-01 | NAR001 旁白“肃明历1226年冬，北方兽族联盟撞关。”；C024 头领“粮仓锁死！拉弩！退下去也是饿死！” | 已生成 48k 成片节奏候选；旁白无口型，头领粗口型；均需人工听审 |
| P-02 | C016“边墙缺粮，今天一粒不留。藏粮的，全户入册。”；C017“把孩子手按上去。” | 已生成 48k 成片节奏候选；C016/C017 均需口型对齐；C016 压缩率高，优先听审 |
| P-03 | 儿童旧歌“白芷晒，薄荷晾，陈皮翻一翻。”；识别童“他会旧歌。”；C016“带走，教成识别童。” | 已生成 48k 成片节奏候选；旧歌“晒”为旧调触发点；儿童声全部需人工听审 |
| P-04 | C007 白翳“她带着旧驿血牒往北逃。封旧驿，活捉。” | 已生成 48k 成片节奏候选；三段口型；压缩率高，优先听审 |
| P-05 | 无对白、无旁白、无口型；接收音乐/SFX | 已写 `assets/voice/timing-manifest.json` 标注无口型；沈维桑鼻息默认 `omitted_by_design` |

## 声音锁沿用 / 新录判断

| voice_id | 使用范围 | 当前裁决 |
|---|---|---|
| NAR001-VOICELOCK-V001 | P-01 唯一旁白 | 只沿用全局旁白母音色方向；不沿用任何旧句或旧旁白文件 |
| C024-GROUP-VOICELOCK-V001 | P-01 军户头领 | 沿用边墙军户群像声线规则；本句必须按风雪压迫下喊法新录或确认候选 |
| C016-VOICELOCK-V001 | P-02 小吏、P-03 小吏 | 沿用虫吏制度化声音锁；P-02 / P-03 均使用当前导演正式文本 |
| C017-GROUP-VOICELOCK-V001 | P-02 奴兵短令 | 沿用奴兵群像质感；短、硬、半可见口型 |
| C025-GROUP-VOICELOCK-V001 | P-03 儿童旧歌、识别童 | 只沿用平民/儿童层规则；儿童旧歌需人工听审防止恐怖童谣化 |
| C007-VOICELOCK-V001 | P-04 白翳 | 沿用白翳温和、洁净、危险的声音锁；本句必须冷静、轻、准 |
| C002-VOICELOCK-V001 | P-04 晏南枝喘息 | 本轮不生成对白；如导演要身体气口，另列拟音 / 呼吸生产 |
| C001-VOICELOCK-V001 | P-05 可选鼻息 | 默认省略；不产生可读唇形 |

## 当前角色声音卡缺口

- C001、C002、C007、C016、C017、C024、C025、NAR001：已有声音锁方向或 preview，但本轮 48k 节奏候选仍未通过人工听审。
- C021：仅为音乐 / 声效边界参考，不归入本轮人声 final。
- C025：儿童旧歌第三字“晒”必须滑出旧调；现有候选仅可用于剪辑节奏和听审，不可直接当 final。

## 历史候选处理

- 2026-06-21 早前 v0001 解释性旁白、v0002 叙事纠错候选和旧台词方向均已撤回，不再在本入口保留旧台词文本。
- 旧文件只作为失败诊断和工具记录留在 `.work`，不得被视频、剪辑或成片部门抓取为正式对白。
- 当前唯一有效文本以本文件、配音包、口型交接 JSON 和各 `assets/voice/timing-manifest.json` 为准。

## 职业精神内核

- 一角色一声音，一声音一历史。
- 声音服务人物，不炫技、不抢戏。
- 不改台词含义，不替编剧补戏；信息不足时提出 `needs_script_fix` 或 `needs_director_replan`。
- 目录、命名、状态、交接路径和正式资源归口服从项目办公室现场契约。
- 导演认可后的分镜台词音频回到项目办公室指定的导演部分镜目录，通常放入 `director-room/{season-id}/{episode-id}/{shot-group-id}/{shot-id}/assets/voice/`，配音部工作区只保留过程、候选和专业判断。

## 当前专业资料

- 配音技巧库草案：`voice-room/.work/voice-technique-library.md`
- 长期记忆候选：`voice-room/.work/memory-candidates.md`

## 当前边界

本文件只保存配音部工作入口、当前有效文本和交接路径。成片 final 音频必须在人工听审和导演确认后另行晋级。
