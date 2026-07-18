# 视频生成部学习来源索引

最后核验日期：2026-06-22

本索引用来记录视频生成部吸收过的优秀开源项目、官方工作流和网络教程。它不是工具排行榜，也不是固定推荐清单；AI 视频工具变化很快，执行项目前必须重新确认可用工具、许可证、硬件和当前质量。

## 开源视频生成项目

### Wan2.2 / Wan2.1

来源：

- `https://github.com/Wan-Video/Wan2.2`
- `https://github.com/Wan-Video/Wan2.1/`

吸收方法：

- I2V、T2V、FLF2V 是视频部必须区分的生成模式。
- 720P、24fps、首尾帧和 consumer GPU 可运行性属于工具能力报告字段，不应写死在项目提示词里。
- FLF2V 适合锁定动作终点和接剪点。

落地规则：

- 通过 QC 的首帧和尾帧优先于长文本提示。
- 复杂镜头先拆 3-5 秒，不把一整段动作交给模型自由发挥。

### ComfyUI Wan Video Examples

来源：

- `https://docs.comfy.org/tutorials/video/wan/wan-video`
- `https://docs.comfy.org/tutorials/video/wan/wan-flf`
- `https://comfyanonymous.github.io/ComfyUI_examples/wan/`

吸收方法：

- 用官方示例确认模型文件、工作流类型、首尾帧和 I2V/FLF2V 输入要求。
- FLF2V 需要明确 start image 和 end image，适合锁定视频边界和中间过渡。
- workflow 是工具执行证据，不是导演意图来源。

落地规则：

- video-production-room 记录 workflow / model refs，但不发明节点和模型名称。
- 只把符合本项目质量门的输出晋升到项目办公室指定的正式归口；过程版本留在隐藏版本库。

### HunyuanVideo / HunyuanVideo-I2V

来源：

- `https://github.com/Tencent-Hunyuan/HunyuanVideo`
- `https://github.com/Tencent-Hunyuan/HunyuanVideo-I2V`
- `https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5`
- `https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/assets/HunyuanVideo_1_5_Prompt_Handbook_EN.md`

吸收方法：

- 区分 T2V、I2V、轻量化版本和硬件门槛。
- 用工具能力报告记录模型适用边界，而不是对所有镜头默认使用同一模型。

落地规则：

- T2V 可用于预演或概念测试；正式镜头优先使用通过 QC 的首帧和控制证据。

### CogVideoX

来源：

- `https://github.com/zai-org/CogVideo`
- `https://huggingface.co/zai-org/CogVideoX-5b`

吸收方法：

- 开源视频模型可用于文本/图像到视频和 fine-tuning 研究。
- 后处理增强可以改善 fps/resolution，但不能改变源视频 QC 结论。

落地规则：

- 如果源视频动作、身份、空间失败，不用增强工具硬救。

### LTX-Video

来源：

- `https://github.com/Lightricks/LTX-Video`

吸收方法：

- 高效视频模型适合纳入工具能力候选，但必须实测当前版本能力。

落地规则：

- 只在工具能力报告确认后进入生成计划。

### Mochi

来源：

- `https://github.com/genmoai/mochi`

吸收方法：

- 开源大模型可用于视频生成测试和横向比较。

落地规则：

- 不因社区热度直接替换项目已通过的稳定流程。

## 口型和音频驱动视频项目

### Wav2Lip

来源：

- `https://github.com/Rudrabha/Wav2Lip`

吸收方法：

- 音频到口型同步是独立能力，应和普通 I2V 分开 QC。

落地规则：

- 只处理配音部提供的音频时间权威；不改台词。

### MuseTalk

来源：

- `https://github.com/TMElyralab/MuseTalk`
- `https://huggingface.co/TMElyralab/MuseTalk`

吸收方法：

- 实时/高质量 lip-sync 工具适合说话人镜头候选。

落地规则：

- 先检查嘴部可见度和角色身份稳定，再执行。

### SadTalker

来源：

- `https://github.com/OpenTalker/SadTalker`
- `https://sadtalker.github.io/`

吸收方法：

- 单图 talking head 可作为头像式或补充口型方案，不应替代复杂电影镜头。

落地规则：

- 适合局部肖像，不适合直接承担多人空间调度。

### LivePortrait

来源：

- `https://github.com/KlingAIResearch/LivePortrait`
- `https://liveportrait.github.io/`

吸收方法：

- 肖像动画和驱动控制可用于表情/头部运动候选。

落地规则：

- 需要重点 QC 身份保持、头部稳定和口型精度。

### Wan-S2V

来源：

- `https://humanaigc.github.io/wan-s2v-webpage/`

吸收方法：

- 音频驱动影视化视频生成可以处理对话、唱歌和表演，但仍需角色、场景、口型和剪辑 QC。

落地规则：

- 适合纳入口型和半身/全身说话镜头候选，不能绕过配音部时间权威。

## 网络教程与官方提示指南

### Runway 官方 Gen-4 Video Prompting Guide / Academy

来源：

- `https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide`
- `https://academy.runwayml.com/`
- `https://academy.runwayml.com/guides/prompting-guide`

吸收方法：

- 视频提示需要明确主体、动作、镜头运动、风格、环境和约束。
- 镜头运动词应服务画面目的，不是装饰。
- I2V 中输入图定义构图、主体、光线和风格，提示词重点描述运动、镜头和时间推进。

落地规则：

- 视频提示词必须回到导演镜头目的和美术连续性，不写空泛“电影感”。

### 用户提供的短视频分秒提示词截图复盘

来源：

- 用户提供的短视频截图：航拍路线标注、分秒运镜提示词、近景微表情提示词示例。

吸收方法：

- 把“0s-2s / 2s-5s / 5s-7s”提示词拆成可执行的 `time_slices`，每段必须有起点、终点、镜头节拍、动作节拍和接剪依据。
- 宏大运镜不能只靠文字，应把红线路线、箭头、参考图转成 motion map / camera path / 首尾帧控制；标注本身不得进入最终画面。
- 微表情提示词只适合近景短段和低运动强度，需要身份锁、表情边界和短时长 QC。

落地规则：

- 见 `references/ai-video-technique-library.md` 中 `VID-TIMELINE-PROMPT-01 分秒时间轴提示词`。
- 不复制创作者原始文案、平台 UI、账号标识、红线箭头或截图字幕；只沉淀可复用结构和质量门。

### SwarmUI / 社区 I2V 经验

来源：

- `https://github.com/mcmonkeyprojects/SwarmUI/discussions/716`

吸收方法：

- 先生成一张足够好的图，再用 I2V 让它动，通常比纯 T2V 更可控。

落地规则：

- 正式镜头优先使用通过 QC 的首帧 I2V，而不是纯文本赌稳定性。

## 吸收边界

- 公开资料只作为方法来源，不能覆盖项目导演签署、角色 canon、美术资产、配音时间权威和剪辑要求。
- 不复制教程文案、付费工作流、平台 UI、截图水印和创作者标签。
- 不把某个模型的一次成功参数写成通用硬规则。
- 新工具进入正式生产前，必须先通过 `tool-capability-agent` 记录能力、限制、许可证、硬件和测试结果。
