# 第01集 MiniMax / Qwen3-TTS 音频工作流

## 制作边界

- 本工作流覆盖第01集中文对白、旁白、配乐提示词和最终音频挑选。
- 对白和旁白并行生成两版：MiniMax TTS 版与 Qwen3-TTS 版。
- 配乐 cue 同步提供生成提示词；当前把 MiniMax 音乐路线作为主生成路线，Qwen3-TTS 只用于对白、旁白、童谣或需要人声口播的声音层。
- 不创建占位 wav。只有实际导出音频后，才把 `01/audio/audio-manifest.json` 的状态改为完成。

## 双路线命名

| 类型 | MiniMax 路线 | Qwen3-TTS 路线 | 最终选用 |
| --- | --- | --- | --- |
| 对白/旁白 | `01/audio/dialogue/provider/minimax/d001.wav` | `01/audio/dialogue/provider/qwen3-tts/d001.wav` | `01/audio/dialogue/d001.wav` |
| 配乐 | `01/audio/music/provider/minimax/mx001.wav` | 不生成纯配乐，只做必要人声层参考 | `01/audio/music/mx001.wav` |
| 音效 | `01/audio/sfx/provider/sfx/sfx001.wav` | 不适用 | `01/audio/sfx/sfx001.wav` |

## 生成顺序

1. 按 `01/audio/provider-prompts.json` 逐条生成 MiniMax TTS 与 Qwen3-TTS 对白。
2. 每句对白保留两版 provider 文件，不直接覆盖最终 `audio/dialogue/d*.wav`。
3. 对同一句做 A/B QC，优先检查咬字、角色区分、情绪边界、句尾收束、是否与配乐床冲突。
4. 选中版本复制或重新导出为最终短文件名，例如 `d004.wav`。
5. 按同一提示词包生成 MiniMax 配乐 cue，输出到 provider 目录，混音通过后再落到 `01/audio/music/mx*.wav`。
6. 图片锁定后按实际时长更新 `01/post/subtitle-script.md` 时间码。

## 对白 QC 规则

- 角色必须一听可分：旁白冷，官吏干，白翳净，沈家贴近，晏南枝清冷，顾怀章低重。
- 禁止现代综艺感、动漫腔、广播主持腔、夸张反派笑、哭喊式情绪。
- 童声只允许自然短促，不卖萌，不成人化。
- 官吏与白翳不靠吼制造压迫，压迫来自平直、洁净、确定性。
- 句尾不能拖成唱腔，除非提示词明确要求旧歌或童谣质感。
- 旁白不得为了贴短镜头使用 `ffmpeg atempo` 或同类后期加速；如果自然男播音时长超过旧镜头窗口，优先调整 picture lock、字幕窗口或音效铺底。
- 第01集 Qwen3-TTS 旁白锁定 `voice=uncle_fu`、`language=chinese`、`temperature=0.45`、`top_k=25`、`top_p=0.8`、`repetition_penalty=1.05` 与 `provider-prompts.json` 的男中低音雄厚历史感提示词；d001、d002、d006、d010 必须使用同一语调与自然语速标准。

## 配乐 QC 规则

- 音乐必须让中文对白居中清楚，配乐只承压，不抢叙事信息。
- 禁止满编史诗、英雄铜管、现代鼓组、甜美旋律和过度恐怖尖叫。
- 每个场景保留具体声源：骨钟、白册纸声、虫蜡、粮车、雨、药柜、弓弦。
- 结尾必须保留空拍，不用情绪宣泄式收束。

## 交付检查

- `01/audio/provider-prompts.json` 是逐句提示词真源。
- `01/audio/dialogue-plan.json` 是对白文本、镜头、时间窗和最终导出编号真源。
- `01/audio/voice-bible.md` 是角色声线真源。
- `01/post/sound-plan.md` 是配乐、音效、混音关系真源。
