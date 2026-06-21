# 配音部工作流

```text
读取项目契约、剧本、角色声音卡、导演要求、口型和剪辑约束
  -> 建立或校验角色声音锁
  -> 建立台词 / 旁白 cue
  -> 选择配音技巧和技术方案
  -> 规划 TTS / 人工录制 / 强制对齐
  -> 音频 QC
  -> 返工或导演确认
  -> 按项目契约交接口型、视频和剪辑
```

每条对白记录：

```text
dialogue_id
episode_id
scene_id
shot_id
speaker_character_id
voice_id
text
emotion
intensity
pace
pause
breath
stress
accent
distance
lipsync_required
target_duration
audio_path
audio_version
qc_status
```

路径、命名、隐藏版本库和正式归口由项目办公室契约决定；本文件只定义配音部专业流程和 cue 信息。
