# NAR001 纪录片旁白

## 0. 卡片元信息

- voice_role_id: NAR001
- display_name: 纪录片旁白
- card_type: narrator_voice_master_card
- current_status: preview_audio_visible_with_character_card_needs_human_listening_qc
- voice_owner: voice-room
- source_reference:
  - `screenwriting/01/screenwriting-main.md`
  - `story-original/bible/source/outline/episode-outline-index.md`
  - `story-original/bible/source/continuity.md`
- preview_audio_path: `director-room/characters/nar001-voice-v001-preview.wav`
- process_version_path: `voice-room/.work/asset-versions/NAR001-VOICELOCK-V001/20260621v0001-preview.wav`
- last_updated: 2026-06-21

## 1. 旁白功能定位

owner: voice-room
status: preview

- 声音功能：用于第一季开场世界背景、制度信息和历史冷感提示，像资料旁白或判词，不替代人物行动。
- 叙述立场：不站在任何角色内心，不替观众煽情，不解释人物动机，只给时代、制度、后果和时间坐标。
- 使用范围：冷开、章节背景、必要的历史/制度信息补足；进入人物现场后应尽量退场。
- 禁止写偏：宣传片腔、热血史诗腔、说书腔、宫廷旁白腔、情绪控诉腔、悬疑吓人腔、像真实播音员的可识别模仿。

## 2. 配音声音母卡

owner: voice-room
status: preview

- voice_id: NAR001-VOICELOCK-V001
- TTS speaker: uncle_fu
- 声线：成熟男性中低声区，干净、平稳、略有纪录片质感，但不做厚重煽情。
- 语速：偏慢，信息段落清楚；慢但不拖，不把短句拉成口号。
- 呼吸：气口少而自然，长句按意义切分，保持“字断气连”的纪录片流动感。
- 情绪层级：默认 0-1 级；只保留客观、冷静、历史距离感，不主动投放悲悯、愤怒或宏大激昂。
- 重音：只给时代、制度词、因果转折和死亡后果；一句只保留一个主重心。
- 距离感：近麦清楚但不贴耳，像站在画面之外陈述事实。
- 低声 / 沉默 / 怒声规则：不使用怒声；压低只用于结尾判词感，不能压成恐吓。
- 直接失败：听起来像广告、宣传片、评书、新闻播报、影视预告、情绪控诉，或像在替角色哭/怒。
- 角色声音试听文件：`director-room/characters/nar001-voice-v001-preview.wav`
- 声音版本 / QC 状态：NAR001-VOICELOCK-V001 / preview / needs_human_listening_qc

## 3. 旁白常用语 / 母音频文本

| 用途 | 文本 | 朗读规则 |
| --- | --- | --- |
| 开场判词 | 北墙五百年，血从未干。 | 短停顿，句尾稳住，不加悲壮。 |
| 制度压迫 | 粮入边墙，名入白册。 | 两个并列信息，重音给“粮”“名”。 |
| 年代坐标 | 肃明历一二二六年，笔下一沾前朝旧字，罪就写成了。 | 年号清楚，后半句压低，不做控诉。 |
| 母样补充句 | 旧名仍会招来死罪，旧路仍有人记得。 | 只作母音色测试句，不等同分镜最终旁白。 |

## 4. Qwen3-TTS 音频生成提示词

- model: `C:/Users/uroborus/Models/Qwen3-TTS-12Hz-0.6B-CustomVoice`
- mode: custom-voice
- language: chinese
- voice: uncle_fu
- sample_text: `北墙五百年，血从未干。粮入边墙，名入白册。肃明历一二二六年，笔下一沾前朝旧字，罪就写成了。旧名仍会招来死罪，旧路仍有人记得。`
- instruct_prompt: `标准中文纪录片旁白，成熟男声，中低声区，平稳、客观、无明显情绪；像历史纪录片资料解说，不像宣传片，不煽情，不压迫，不戏剧化，不模仿任何真实播音员；语速偏慢但不拖，字音清楚，停顿按信息段落，不突出表演感，句尾稳定收住。`
- generation_params:
  - backend: torch
  - device: cpu
  - dtype: float32
  - temperature: 0.55
  - top_k: 30
  - top_p: 0.86
  - repetition_penalty: 1.08
  - max_tokens: 1000
- preview_audio_path: `director-room/characters/nar001-voice-v001-preview.wav`
- process_version_path: `voice-room/.work/asset-versions/NAR001-VOICELOCK-V001/20260621v0001-preview.wav`
- audio_metadata:
  - sample_rate: 24000
  - channels: 1
  - duration_seconds: 21.04
  - format: wav
- qc_status: preview_audio_visible_with_character_card_needs_human_listening_qc

## 5. 旁白 QC

owner: voice-room
status: preview

- 通过目标：可信、可跟随、信息清楚，平但不空，冷但不机械。
- 人工听审重点：是否还有表演感、煽情感、宣传片腔；是否把“肃明历一二二六年”和“白册”读清楚；句尾是否稳定。
- 当前风险：试听版为 24 kHz，低于项目最终 48 kHz 目标；可作母样 preview，不得冒充最终交付音频。
- G-P audio_gate_file_qc_20260621：角色入口 preview 文件存在，实测 24 kHz mono PCM WAV，21.040s；P-01 分镜候选 `voice-room/.work/asset-versions/G-P/P-01-VO-NAR001-001/20260621v0001-candidate.wav` 存在，实测 24 kHz mono，5.280s，可进入人工听审和切头尾候选；未人工听审、未转 48 kHz 前不得标为 `P-01/assets/voice/P-01-VO-NAR001-001.wav` final。
- 下一步：人工听审通过后再标记为 locked；若觉得 `uncle_fu` 太有生活感，可用同一提示词改试更冷的 speaker 版本。

## 6. 冲突与变更记录

- date: 2026-06-21
- department: voice-room
- section: NAR001 narrator voice master card
- change_summary: 建立 `NAR001-VOICELOCK-V001` 纪录片旁白母卡，生成旁白 preview 母音频，并把 Qwen3-TTS 生成提示词、试听文件路径、过程版本路径和 QC 状态写入本卡。
- affects_source_canon: false
- required_return_department: none
- status: preview_audio_visible_with_character_card_needs_human_listening_qc
