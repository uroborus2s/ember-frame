# 音频生成与对齐技术参考

本文件用于选择技术方案，不绑定单一工具。执行时还要遵守项目授权、隐私、算力和交付规格。

## 目录

- 技术选择原则
- 音色生成
- 稳定 TTS
- SSML 与可控朗读
- 强制对齐与口型
- 参考音频采集
- 参考来源

## 技术选择原则

- 角色一致性优先于单句惊艳。
- 授权清晰优先于相似度。
- 可复现优先于偶然好听。
- 口型可对齐优先于过度表演。
- 工具输出不能改写台词含义。

## 音色生成

可学习项目：GPT-SoVITS、F5-TTS、CosyVoice、OpenVoice、XTTS-v2。

适用：

- 建立角色候选母音色。
- 少量参考样本下快速试声。
- 小样阶段多版本比选。

风险：

- 跨句稳定性不足。
- 情绪强时音色漂移。
- 参考音频授权不清。

规则：

- 先做角色级小样，不直接批量生产分镜台词。
- 通过母音色 A/B 对照后，再进入正式台词流程。
- 禁止以可识别真实人物声音作为未经授权的目标。

## 稳定 TTS

可学习项目：Piper 等轻量、本地、可复现方案。

适用：

- 临时预演。
- 旁白或低风险说明性台词。
- 需要快速批量验证节奏。

风险：

- 情绪表达弱。
- 角色辨识度不足。

## SSML 与可控朗读

可学习资料：Google Cloud Text-to-Speech SSML、Alexa SSML。

适用：

- 旁白、说明、节奏稳定的台词。
- 需要控制语速、停顿、音高或重音。

规则：

- SSML 是控制工具，不是表演判断。
- 标签不能替代人物关系、潜台词和情绪层级分析。

## 强制对齐与口型

可学习工具：Montreal Forced Aligner、WhisperX、aeneas。

适用：

- 可见说话人需要口型对齐。
- 需要词级或音素级时间。
- 剪辑需要准确起止时间。

风险：

- 台词过快导致口型失真。
- 强行压缩牺牲表演和清晰度。

处理：

- 若目标时长与自然语速冲突，优先退导演部调整镜头节奏，或退编剧部调整台词长度。

## 参考音频采集

可学习资料：NVIDIA Riva TTS dataset recording guide 等公开录制指南。

要求：

- 干净、低噪、低混响。
- 文本准确，不吞字。
- 覆盖中性、低声、急促、压抑、爆发等角色常用状态。
- 同一角色参考样本保持设备、空间和距离感一致。

## 参考来源

- GPT-SoVITS: https://github.com/RVC-Boss/GPT-SoVITS
- F5-TTS: https://github.com/swivid/F5-TTS
- CosyVoice: https://github.com/FunAudioLLM/CosyVoice
- OpenVoice: https://github.com/myshell-ai/OpenVoice
- Coqui XTTS-v2: https://huggingface.co/coqui/XTTS-v2
- Piper: https://github.com/OHF-Voice/piper1-gpl
- WhisperX: https://github.com/m-bain/whisperX
- Montreal Forced Aligner: https://montreal-forced-aligner.readthedocs.io/en/stable/
- aeneas: https://github.com/readbeyond/aeneas
- Google Cloud Text-to-Speech SSML: https://cloud.google.com/text-to-speech/docs/ssml
- Alexa SSML: https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html
- NVIDIA Riva TTS dataset recording guide: https://docs.nvidia.com/deeplearning/riva/user-guide/docs/tutorials/tts-dataset-recording-at-home.html
