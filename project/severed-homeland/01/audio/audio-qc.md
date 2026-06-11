# 第01集 Audio QC

## Qwen3-TTS 旁白交付

- 状态：通过 format / timing QC；男播音声线已按精炼旁白重生，待人工听感终审。
- 后端：MLX。
- 模型：`mlx-community/Qwen3-TTS-12Hz-1.7B-CustomVoice-bf16`。
- 声线：`uncle_fu`。
- 语言：`chinese`。
- 选择理由：第一集旁白改为男中低音、胸腔共鸣、雄厚历史感声线；`uncle_fu` 比上一版候选声线更厚、更沉，更接近史书开卷的旁白方向，且 MLX 路线适配 Apple Silicon Mac。
- 生成约束：本轮不使用 `ffmpeg atempo` 或同类后期变速；通过导演精炼旁白文字来控制时长。

## 已生成文件

| Cue | Shot | Final file | Provider file | Duration | Target window | QC |
| --- | --- | --- | --- | ---: | --- | --- |
| d001 | SC001-SH001 | `01/audio/dialogue/d001.wav` | `01/audio/dialogue/provider/qwen3-tts/d001.wav` | 4.080000s | 00:00.0-00:04.1 | ready / listen-check needed |
| d002 | SC001-SH002 | `01/audio/dialogue/d002.wav` | `01/audio/dialogue/provider/qwen3-tts/d002.wav` | 2.000000s | 00:05.2-00:07.2 | ready |
| d006 | SC002-SH004 | `01/audio/dialogue/d006.wav` | `01/audio/dialogue/provider/qwen3-tts/d006.wav` | 7.520000s | 00:27.2-00:34.8 | ready |
| d010 | SC003-SH004 | `01/audio/dialogue/d010.wav` | `01/audio/dialogue/provider/qwen3-tts/d010.wav` | 5.440000s | 00:59.2-01:04.7 | ready |

## 检查结果

- 文件格式：WAVE PCM, mono, 24000 Hz, Int16。
- 时长：四条最终文件均为自然男中低音雄厚历史感语速；通过精炼文字控制时长，不压缩音频。
- 声线一致性：d001 已从 6 个同参数候选中按 d002/d006/d010 声学参考筛选，选用 `provider/qwen3-tts/candidates/d001-c03.wav`。
- 路径：provider 版和最终短文件均已落盘。
- 注意：上一版 d001/d002 听感偏快的原因是 manifest 记录过 `ffmpeg atempo` timing conform，尤其 d002 为贴 1.8s 旧窗口做过明显压缩；本轮已取消该策略。

## 未完成范围

- 本文件只覆盖旁白 cue：`d001`、`d002`、`d006`、`d010`。
- 角色对白、配乐、SFX 尚未生成，`audio-manifest.json` 不标记全量完成。
- 尚未执行人工听感终审，后续需要检查咬字、情绪边界和混音遮挡。
