# P-01 v0210 直接因果台词 QC

## 用户问题

用户指出：`粮仓封了` 仍然没有因果关系，听不懂。

## 编剧 / 导演裁决

反馈成立。`粮仓封了！回弩位！门破了，都得死！` 仍旧把“粮仓状态”放在开头，但没有先告诉观众角色正在做什么，也没有说明粮仓和动作之间的关系。

旧句撤回，新句采用：

```text
别跑！铁栅锁了！粮仓拿不到！回弩位，守门！
```

新版因果：

```text
别跑
  -> 因为铁栅锁了，退路断了
  -> 因为粮仓拿不到，下去没有用
  -> 所以回弩位，守住城门
```

## 配音 / 混音处理

- 原始候选：`voice-room/.work/asset-versions/G-P/P-01-VO-C024-HEAD-001/20260622v0210-short-candidate.wav`
- 正式审片 48k clip：`assets/voice/P-01-VO-C024-HEAD-001-v0210-direct-cause-48k.wav`
- 整混：`assets/edit/P-01-v0210-direct-cause-audio-mix-20260622.wav`
- C024 clip：4.52 秒，48 kHz mono，约 -17.6 dBFS。
- C024 段整混：约 -15.5 dBFS；旁白段约 -24.2 dBFS；声桥约 -46.8 dBFS。
- 处理方式：裁出五个有效短令，压缩模型无意义长空隙，只保留每句之间 0.15 秒气口。

## 输出文件

- 审看视频：`assets/edit/P-01-v0210-direct-cause-director-previs-subtitled-20260622.mp4`
- 无硬字幕版：`assets/edit/P-01-v0210-direct-cause-director-previs-20260622.mp4`
- 声音混合：`assets/edit/P-01-v0210-direct-cause-audio-mix-20260622.wav`
- C024 新台词：`assets/voice/P-01-VO-C024-HEAD-001-v0210-direct-cause-48k.wav`
- 配音 cue manifest：`assets/voice/P-01-v0210-voice-cue-manifest.json`
- 接触表：`assets/edit/P-01-v0210-contact-sheet-20260622.jpg`
- 视频部 manifest：`video-production-room/.work/asset-versions/P-01-video/20260622v0210/render-manifest.json`

## 导演结论

v0210 通过为 `direct_cause_dialogue_and_voice_audibility_previs_review`：台词从“状态说明”改为“制止动作 -> 解释原因 -> 给出新动作”，因果比 v0209 更清楚。

v0210 不通过为最终成片：C024 仍是 TTS 候选，不是人工最终表演；画面仍是低模导演预演，不证明最终角色卡绑定、口型、人物表演和正式美术质量。
