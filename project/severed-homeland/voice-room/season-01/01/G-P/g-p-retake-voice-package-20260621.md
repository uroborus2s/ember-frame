# G-P 重拍版配音包

owner: voice-room
status: timed_48k_edit_candidates_written_final_pending_human_listening_qc
last_updated: 2026-06-21

## 1. 执行结论

- 本包只覆盖第 01 集 G-P / P-01 至 P-05 重拍版配音 cue、声音锁判断、口型对齐交接和候选音频 QC。
- 已把 8 条重拍台词制作成导演时间窗内的成片节奏版候选，并写入各分镜 `assets/voice/`。
- 本机可用 TTS 源只产出 24 kHz mono；本批 `candidate-48k.wav` 为裁头尾、time-fit、上采样后的 48 kHz mono PCM WAV。可进剪辑节奏候选，不是 final。
- P-02 C016 已从 10.480s 压入 0.30-3.60s；P-04 C007 已从 9.040s 压入 2.50-5.35s。二者压缩率高，必须优先人工听审伪影和可懂度。
- P-05 无正式对白、无旁白、无口型需求；已写无口型 manifest，接收音乐 / SFX，不生成多余人声。

## 2. 声音锁沿用 / 新录判断

| voice_id | 使用范围 | 可沿用内容 | 必须新录 / 确认 | 当前裁决 |
|---|---|---|---|---|
| NAR001-VOICELOCK-V001 | P-01 唯一旁白 | 可沿用全局纪录片旁白母音色方向 | 当前正式句需听审，确认冷、低、短，不宣传片化 | 沿用声音锁方向，不沿用旧音频 |
| C024-GROUP-VOICELOCK-V001 | P-01 军户头领 | 可沿用边墙军户群像声线规则 | 必须确认风雪压迫下喊法，不英雄化 | 新录 / 候选听审 |
| C016-VOICELOCK-V001 | P-02 小吏、P-03 小吏 | 可沿用虫吏制度化声音锁 | 必须确认流程宣判、不拖腔、快而清楚 | 新录 / 候选听审 |
| C017-GROUP-VOICELOCK-V001 | P-02 奴兵短令 | 可沿用奴兵群像质感 | 必须短、硬、半可见口型，与 C016 区分 | 新录 / 候选听审 |
| C025-GROUP-VOICELOCK-V001 | P-03 儿童旧歌、识别童 | 可沿用普通平民 / 儿童层规则 | 儿童旧歌需确认“晒”旧调触发点，不怪物化 | 新录 / 候选听审 |
| C007-VOICELOCK-V001 | P-04 白翳 | 可沿用白翳温和、洁净、危险的声音锁 | 必须确认干净、温和、冷，像系统已经合上 | 新录 / 候选听审 |
| C002-VOICELOCK-V001 | P-04 晏南枝喘息 | 可沿用晏南枝端正克制的身体气口规则 | 本轮不生成对白；身体气口另归拟音 / 呼吸清单 | 待后续 |
| C001-VOICELOCK-V001 | P-05 可选鼻息 | 可沿用沈维桑克制少年气口规则 | 默认不录；若导演要气口，另录极轻鼻息 | `omitted_by_design` |

## 3. Cue / Timing / QC 表

| audio_id | shot | 文本 | voice_id | 目标窗 | 48k candidate | 时长 | fit | 口型 | QC 分 | 剪辑状态 | final 状态 |
|---|---|---|---|---|---|---:|---:|---|---:|---|---|
| P-01-VO-NAR001-001 | P-01 | 肃明历1226年冬，北方兽族联盟撞关。 | NAR001-VOICELOCK-V001 | 0.40-3.20 | `director-room/season-01/01/G-P/P-01/assets/voice/P-01-VO-NAR001-001-candidate-48k.wav` | 2.800s | 2.173x | 无可见说话人 | 86 | 可进剪辑候选 | 需人工听审 |
| P-01-VO-C024-HEAD-001 | P-01 | 粮仓锁死！拉弩！退下去也是饿死！ | C024-GROUP-VOICELOCK-V001 | 2.95-5.25 | `director-room/season-01/01/G-P/P-01/assets/voice/P-01-VO-C024-HEAD-001-candidate-48k.wav` | 2.300s | 1.693x | 半可见 / 粗口型 | 82 | 可进剪辑候选 | 需人工听审 |
| P-02-VO-C016-CLERK-001 | P-02 | 边墙缺粮，今天一粒不留。藏粮的，全户入册。 | C016-VOICELOCK-V001 | 0.30-3.60 | `director-room/season-01/01/G-P/P-02/assets/voice/P-02-VO-C016-CLERK-001-candidate-48k.wav` | 3.300s | 2.621x | 可见三段口型 | 78 | 可进剪辑候选 | 需人工听审，优先 |
| P-02-VO-C017-ENFORCER-001 | P-02 | 把孩子手按上去。 | C017-GROUP-VOICELOCK-V001 | 3.75-4.85 | `director-room/season-01/01/G-P/P-02/assets/voice/P-02-VO-C017-ENFORCER-001-candidate-48k.wav` | 1.100s | 1.127x | 半可见短口型 | 86 | 可进剪辑候选 | 需人工听审 |
| P-03-VO-C025-CHILD-001 | P-03 | 白芷晒，薄荷晾，陈皮翻一翻。 | C025-GROUP-VOICELOCK-V001-child | 0.20-1.65 | `director-room/season-01/01/G-P/P-03/assets/voice/P-03-VO-C025-CHILD-001-candidate-48k.wav` | 1.450s | 2.662x | 儿童旧歌口型 | 72 | 可进剪辑候选 | 需人工听审，优先 |
| P-03-VO-C025-IDCHILD-001 | P-03 | 他会旧歌。 | C025-GROUP-VOICELOCK-V001-recognition-child | 1.80-2.45 | `director-room/season-01/01/G-P/P-03/assets/voice/P-03-VO-C025-IDCHILD-001-candidate-48k.wav` | 0.650s | 1.833x | 可见短句 | 84 | 可进剪辑候选 | 需人工听审 |
| P-03-VO-C016-CLERK-001 | P-03 | 带走，教成识别童。 | C016-VOICELOCK-V001 | 3.75-5.10 | `director-room/season-01/01/G-P/P-03/assets/voice/P-03-VO-C016-CLERK-001-candidate-48k.wav` | 1.350s | 2.017x | 半可见 / 粗口型 | 82 | 可进剪辑候选 | 需人工听审 |
| P-04-VO-C007-BAIYI-001 | P-04 | 她带着旧驿血牒往北逃。封旧驿，活捉。 | C007-VOICELOCK-V001 | 2.50-5.35 | `director-room/season-01/01/G-P/P-04/assets/voice/P-04-VO-C007-BAIYI-001-candidate-48k.wav` | 2.850s | 2.530x | 白翳三段口型 | 76 | 可进剪辑候选 | 需人工听审，优先 |

## 4. 口型目标时间

| audio_id | 计划时间窗 | 词 / 意群切分 |
|---|---|---|
| P-01-VO-NAR001-001 | 0.40-3.20s | 无口型；冷、低、短 |
| P-01-VO-C024-HEAD-001 | 2.95-5.25s | 粮仓锁死 2.95-3.55；拉弩 3.66-4.00；退下去也是饿死 4.08-5.25 |
| P-02-VO-C016-CLERK-001 | 0.30-3.60s | 边墙缺粮 0.30-0.95；今天一粒不留 0.98-1.78；藏粮的，全户入册 2.16-3.60 |
| P-02-VO-C017-ENFORCER-001 | 3.75-4.85s | 把孩子手按上去，落按掌动作 |
| P-03-VO-C025-CHILD-001 | 0.20-1.65s | 白芷 0.20-0.48；晒 0.48-0.62 轻滑旧调；薄荷晾 0.65-1.02；陈皮翻一翻 1.05-1.65 |
| P-03-VO-C025-IDCHILD-001 | 1.80-2.45s | 他会旧歌，短、清楚、仍像孩子 |
| P-03-VO-C016-CLERK-001 | 3.75-5.10s | 带走 3.75-4.10；教成识别童 4.16-5.10 |
| P-04-VO-C007-BAIYI-001 | 2.50-5.35s | 她带着旧驿血牒 2.50-3.55；往北逃 3.64-4.16；封旧驿，活捉 4.30-5.35 |
| P-05 | 全镜 | 无对白、无口型；音乐 / SFX 接收鸡叫、脚步、兔子碰弓身、铜锣三下 |

## 5. Assets/Voice 交接目录

| shot | assets/voice 内容 | 说明 |
|---|---|---|
| P-01 | `P-01-VO-NAR001-001-candidate-48k.wav`; `P-01-VO-C024-HEAD-001-candidate-48k.wav`; `timing-manifest.json` | 旁白 + 头领喊声，可试贴 |
| P-02 | `P-02-VO-C016-CLERK-001-candidate-48k.wav`; `P-02-VO-C017-ENFORCER-001-candidate-48k.wav`; `timing-manifest.json` | C016 / C017 两段口型，可试贴 |
| P-03 | `P-03-VO-C025-CHILD-001-candidate-48k.wav`; `P-03-VO-C025-IDCHILD-001-candidate-48k.wav`; `P-03-VO-C016-CLERK-001-candidate-48k.wav`; `timing-manifest.json` | 儿童旧歌、识别童、小吏，可试贴 |
| P-04 | `P-04-VO-C007-BAIYI-001-candidate-48k.wav`; `timing-manifest.json` | 白翳三段口型，可试贴 |
| P-05 | `timing-manifest.json` | 无对白、无口型；无 WAV |

## 6. 仍需生产 / 听审的问题

- `needs_human_listening_qc`: 所有 8 条 48k 候选均为 24k TTS 源上采样 + time-fit，必须人工听审工具伪影、气口、情绪和可懂度。
- `priority_listening`: P-02 C016、P-03 儿童旧歌、P-04 C007 压缩率最高，优先听审。
- `needs_final_promotion`: 通过听审后才能生成或命名为无 `candidate` 后缀的 final WAV。
- `needs_sfx_handoff`: P-05 只接收音乐 / SFX，不需要配音部补对白。
