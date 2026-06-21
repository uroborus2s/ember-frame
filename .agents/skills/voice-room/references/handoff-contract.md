# 配音交接合同

交接文件路径由项目办公室契约决定。配音部只保证交接内容完整，不在本文件写死项目路径。

交给口型 / 视频部门必须包含：

```text
dialogue_id
episode_id
scene_id
shot_id
speaker_character_id
voice_id
text
audio_path
audio_version
start_time
end_time
lipsync_required
word_or_phoneme_timing
qc_status
```

交给剪辑部门必须包含：

```text
dialogue_id
shot_id
speaker_character_id
audio_path
start_time
end_time
emotion
pause
breath
known_risks
qc_status
```

必须写清：

- 角色和声音锁；
- 对白 ID 和分镜 ID；
- 音频路径和版本；
- 起止时间；
- 是否需要口型；
- 情绪、气口、停顿和重音；
- 已知风险和返工状态。

不得交接：

- `not_started`、`needs_fix`、`blocked` 状态音频；
- 未通过 90 分质量门的音频；
- 未按项目契约归档版本信息的音频；
- 未经导演认可却进入正式归口的分镜音频。
