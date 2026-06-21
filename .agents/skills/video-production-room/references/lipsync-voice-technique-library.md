# 配音与口型视频技巧库

本文件服务视频生成部处理“配音驱动的视频镜头”和“口型镜头”。配音部拥有声音锁、台词、情绪、气口和口型时间权威；视频生成部只负责把这些音频事实正确映射到可见嘴部、面部表演、身体微动和剪辑素材中。

## 使用原则

```text
音频权威来自配音部，不来自视频模型猜测。
说话人身份必须来自角色锁，不允许镜头中临时换 speaker。
口型镜头优先短段，按停顿和气口切分。
嘴部同步只是最低要求，表情、眼神、头部和身体节奏也要符合台词情绪。
口型失败不能交给剪辑硬救；必须重跑、换工具或退回配音时间表。
```

## 必读输入

```text
<project-office-designated voice-lock path>
<project-office-designated dialogue-cue-sheet path>
<project-office-designated lipsync-handoff path>
<project-office-designated voice-qc path>
<project-office-designated dialogue-audio asset path>
```

每条对白至少需要：

```text
dialogue_id
shot_id
speaker_character_id
voice_id
text
emotion
pace
pause
breath
lipsync_required
audio_path
start_time
end_time
```

## 技巧菜单

### LIP-SYNC-01 音频时间权威

用途：
保证口型以配音部的 cue sheet 为准。

规则：

```text
使用 dialogue_id 绑定音频和镜头；
使用 start_time / end_time 限定口型段；
使用 pause / breath 标记闭口、吸气、停顿；
使用 emotion / pace 控制嘴型幅度和头部节奏；
不让视频模型自由改台词或生成字幕。
```

QC：
口型起止早于或晚于音频超过项目容许范围时失败；非说话人误动嘴失败。

### LIP-SHOT-01 说话镜头构图准入

用途：
确保口型工具有足够清晰的嘴部区域。

准入：

```text
嘴部可见且无遮挡；
脸部角度不过度侧背；
嘴唇、下颌、牙齿区域没有严重阴影或糊脸；
角色身份、发型、服装和光线已通过美术 QC；
镜头不在快速旋转、强遮挡或极端运动中完成精确口型。
```

不适合精确口型的镜头：

```text
背影说话、极远景、强雨雪烟尘遮脸、快速打斗中说完整台词、
强逆光剪影看不到嘴、头部大幅转动导致口型不可读。
```

这些镜头应改为画外音、反应镜头、侧脸弱口型或剪辑遮挡策略，但必须经导演和配音/剪辑契约允许。

### LIP-SEG-01 按气口和停顿分段

用途：
避免一整句长台词导致嘴型累积漂移。

规则：

```text
按自然停顿、逗号、情绪转折、吸气和剪辑点切段；
每段保留少量头尾静止或闭口帧；
段间不能改变脸型、身份、光线和服装；
强情绪台词可以在重音前后拆段。
```

QC：
停顿时嘴仍乱动、闭口帧不足或气口节奏不自然，必须重跑。

### LIP-EXPR-01 表情与口型分层

用途：
防止只有嘴在动，眼神、眉、头部和身体没有表演。

分层：

```text
mouth:
  音素、开合、唇形、下颌。

face:
  眉、眼、鼻翼、脸颊、紧张/松弛。

head:
  点头、停顿、微转、回避、靠近。

body:
  呼吸、肩颈、手部、重心微移。
```

规则：
表情必须服从配音情绪和导演镜头目的。悲伤不应笑口型，压低声音不应大幅夸张张嘴。

### LIP-TOOL-01 工具选择

按镜头需求选择口型工具：

```text
Wav2Lip 类:
  适合已有视频的嘴部同步修正；优先检查嘴部清晰度和脸部稳定。

MuseTalk 类:
  适合较高质量、较快的音频驱动嘴部区域生成；适合虚拟人和可控素材。

SadTalker 类:
  适合单图 talking head 或头像式说明，不适合复杂全身电影镜头直接替代。

LivePortrait 类:
  适合肖像表情、头部和驱动视频迁移；需要谨慎处理身份保持和口型精度。

Wan-S2V / audio-driven cinematic video 类:
  适合从静态图和音频生成半身/全身说话表演，但必须经过角色、空间和剪辑 QC。
```

工具不可用或许可不适合时，标记 blocked，不得伪造工具能力。

### LIP-CUT-01 剪辑友好口型

用途：
让剪辑部可以自然接入对白。

要求：

```text
口型段前至少有短暂闭口或呼吸准备；
句尾有闭口或表情落点；
重音处可见表情或头部微动；
反应镜头和说话镜头之间有可剪余量；
handoff 写清推荐入点、出点和已知风险。
```

QC：
台词第一帧已经张嘴、句尾被截断、重音点无表情或无法接反应镜头，不能通过 QC。

## 直接失败

```text
speaker_character_id 与画面人物不一致
voice_id 与角色声音锁不一致
音频被改词、漏词或私自重排
没有气口和停顿
口型明显不同步
非说话人误动嘴
嘴部熔化、牙齿闪烁、下颌抽搐
表情与台词情绪冲突
口型文件不可追踪
```

## 交接给剪辑部

口型镜头在 `render-manifest.json` 中必须写：

```text
dialogue_id
speaker_character_id
voice_id
audio_ref
lipsync_required
lipsync_status
mouth_visibility
recommended_in
recommended_out
known_lipsync_risks
```

`handoff-to-edit.md` 必须说明哪些镜头是精确口型、哪些是弱口型/画外音/反应镜头策略，以及不能剪断的台词重音点。

## 学习来源边界

本库吸收 Wav2Lip、MuseTalk、SadTalker、LivePortrait、Wan-S2V 等公开项目的方法分类。具体项目执行时，以配音部的声音锁和口型交接为最高权威。
