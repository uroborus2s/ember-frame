# 第01集 Audio QC

## Qwen3-TTS 旁白交付

- 状态：通过 timing / format QC，待人工听感终审。
- 后端：MLX。
- 模型：`mlx-community/Qwen3-TTS-12Hz-1.7B-CustomVoice-bf16`。
- 声线：`Serena`。
- 语言：`chinese`。
- 选择理由：第一集旁白需要冷静历史感和风格控制，1.7B CustomVoice 比 0.6B 更适合做正式旁白；MLX 路线适配 Apple Silicon Mac。

## 已生成文件

| Cue | Shot | Final file | Provider file | Duration | Target window | QC |
| --- | --- | --- | --- | ---: | --- | --- |
| d001 | SC001-SH001 | `01/audio/dialogue/d001.wav` | `01/audio/dialogue/provider/qwen3-tts/d001.wav` | 3.486542s | 00:00.0-00:03.5 | ready |
| d002 | SC001-SH002 | `01/audio/dialogue/d002.wav` | `01/audio/dialogue/provider/qwen3-tts/d002.wav` | 1.788792s | 00:03.5-00:05.3 | ready |
| d006 | SC002-SH004 | `01/audio/dialogue/d006.wav` | `01/audio/dialogue/provider/qwen3-tts/d006.wav` | 7.989250s | 00:27.2-00:35.2 | ready |
| d010 | SC003-SH004 | `01/audio/dialogue/d010.wav` | `01/audio/dialogue/provider/qwen3-tts/d010.wav` | 9.006083s | 00:59.2-01:08.2 | ready |

## 检查结果

- 文件格式：WAVE PCM, mono, 24000 Hz, Int16。
- 时长：四条最终文件均贴近 `dialogue-plan.json` 的规划窗口。
- 路径：provider 版和最终短文件均已落盘。
- 注意：`d002` 的目标窗口很短，后期时间压缩较明显；如果画面剪辑允许，建议 picture lock 时给这句保留 2.2s 到 2.6s，会更自然。

## 未完成范围

- 本文件只覆盖旁白 cue：`d001`、`d002`、`d006`、`d010`。
- 角色对白、配乐、SFX 尚未生成，`audio-manifest.json` 不标记全量完成。
- 尚未执行人工听感终审，后续需要检查咬字、情绪边界和混音遮挡。
