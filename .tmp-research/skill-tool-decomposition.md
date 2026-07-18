# Ember Frame：方法进 Skill，能力进 Tool 拆分

目标：复用 OpenMontage 的强项，但不把 76 个 skill 全搬进来。  
原则：方法写进部门 skill，执行能力做成 tool，低频资料只作为参考库。

## 1. 判断规则

```text
读完让 agent 写得更好、判断更准、QC 更专业 = 方法 -> skill
能跑命令、调 API、分析素材、生成文件、登记资产 = 能力 -> tool
只是某个供应商/框架的说明，低频使用 = reference -> 需要时读
```

更具体一点：

```text
导演判断、提示词结构、镜头语言、风格合同、QC 标准 -> skill
视频分析、TTS、STT、FFmpeg、素材入库、视频生成、合成渲染 -> tool
```

## 2. 总控层怎么放

项目办公室不吸收具体创作方法，也不直接调用视频模型。它只管：

```text
部门顺序
输入输出
统一 ID
状态台账
阻塞和返工
正式归口
质量门是否通过
```

不该进项目办公室的内容：

```text
Seedance 提示词怎么写
FLUX 图片提示词怎么写
FFmpeg 怎么裁剪视频
TTS 参数怎么调
```

这些分别属于提示词部、美术部、剪辑部、配音部。

## 3. 功能拆分总表

| 功能 | 方法进哪个 skill | 能力做哪个 tool | 调用部门 |
|---|---|---|---|
| 参考视频分析 | `director-room`：如何观察参考片、拆镜头、判断节奏 | `reference_video_analyzer` | 导演部、剪辑部 |
| 视觉风格统一 | `art-room`、`director-room`、`prompt-room`：视觉风格合同、风格圣经、风格 QC | 可选 `visual_style_extractor` | 美术部、导演部、提示词部 |
| Seedance 镜头提示词 | `prompt-room`：镜头提示词模板、身份锁定、摄影机语言、负面约束 | `seedance_video` 或统一 `video_generator` | 提示词部、视频生成部 |
| FLUX 图片提示词 | `prompt-room`、`art-room`：图片提示词结构、角色/场景一致性、I2I 多参考 | `image_generator` | 美术部、提示词部 |
| 素材冻结和资产台账 | `project-office`：资产必须有 ID、状态和归口；`art-room/edit-room`：素材使用规则 | `asset_resolver` / `asset_manifest` | 全部门 |
| 视频生成 | `video-production-room`：生成策略、分段、首尾帧、失败返工标准 | `video_generator` | 视频生成部 |
| 视频 QC | `video-production-room`、`director-room`：人物、动作、空间、连续性、镜头意图 QC | `video_probe` / `frame_sampler` | 视频生成部、导演部 |
| 配音 | `voice-room`：声音锁、语气、气口、角色声音一致性 | `tts_generator` | 配音部 |
| 转录和字幕 | `voice-room`、`edit-room`：台词对齐、字幕规则、口型交接 | `speech_to_text` / `subtitle_generator` | 配音部、剪辑部 |
| 音乐 | `music-room`：音乐 cue、主题动机、情绪曲线、音乐 QC | `music_generator` / `music_library_resolver` | 音乐部 |
| 音效 | `music-room`、`edit-room`：环境声、动作声、转场声使用规则 | `sfx_generator` / `sfx_resolver` | 音乐部、剪辑部 |
| 剪辑 | `edit-room`：节奏、转场、声画同步、字幕入点 | `ffmpeg_edit` / `timeline_composer` | 剪辑部 |
| 合成渲染 | `edit-room`、`delivery-room`：渲染路线、交付规格、最终检查 | `video_composer` | 剪辑部、交付部 |
| 最终交付 QC | `delivery-room`：时长、清晰度、音频、黑帧、字幕、归档规则 | `delivery_qc` | 成片交付部 |
| 角色动画 | `director-room`、`art-room`、`video-production-room`：rig、pose、表演、连续性 | `svg_character_animator` / `character_animation_qc` | 美术部、视频生成部 |

## 4. 第一批应该真正集成的 10 个能力

### 4.1 `visual-style`

方法进：

```text
art-room
director-room
prompt-room
```

写进去的不是 OpenMontage 原文，而是这些规则：

```text
每个项目必须有视觉风格合同
角色、场景、镜头提示词必须引用风格合同
风格变更必须记录原因
提示词不能临时发明新风格
```

可选 tool：

```text
visual_style_extractor
```

做什么：

```text
从参考图/参考视频/网页中提取颜色、材质、镜头气质、字体、光影关键词
```

### 4.2 `video-understand`

方法进：

```text
director-room
edit-room
```

规则：

```text
参考片不是用来照抄，而是拆内容、节奏、结构、镜头、风格、有效原因
导演部负责判断哪些可借鉴
剪辑部负责判断节奏和转场
```

tool：

```text
reference_video_analyzer
```

输入：

```text
video_path 或 video_url
```

输出：

```text
transcript
scene_list
keyframes
shot_timing
audio_notes
analysis_json
```

### 4.3 `seedance-2-0`

方法进：

```text
prompt-room
video-production-room
```

规则：

```text
视频提示词必须先声明镜头结构
多镜头按时间段写
角色必须有 identity lock
摄影机必须写做什么和不做什么
禁止把字幕/可读文字交给视频模型
复杂镜头优先 standard，不用 fast 碰运气
```

tool：

```text
seedance_video
```

或者先做统一入口：

```text
video_generator
```

输入：

```text
shot_id
prompt
reference_images
duration
aspect_ratio
model_variant
seed
output_path
```

输出：

```text
video_path
metadata
cost
seed
provider
qc_required=true
```

### 4.4 `flux-best-practices`

方法进：

```text
art-room
prompt-room
```

规则：

```text
角色图、场景图、道具图必须分开写
提示词必须保留身份、材质、光影、构图、风格
I2I / 多参考必须写清每张参考图的作用
```

tool：

```text
image_generator
```

### 4.5 `media-use`

方法进：

```text
project-office
art-room
music-room
edit-room
```

规则：

```text
任何进入下游的素材必须冻结成本地文件
任何素材必须有 asset_id
任何素材必须记录来源、用途、状态、归口
失败素材不能进入正式目录
```

tool：

```text
asset_resolver
asset_manifest
```

最小功能：

```text
resolve -> copy/freeze -> probe -> register -> return asset_id
```

### 4.6 `ffmpeg` + `video-edit`

方法进：

```text
edit-room
delivery-room
```

规则：

```text
剪辑操作必须可复现
转码参数必须记录
最终导出必须做时长、分辨率、音频、黑帧检查
```

tool：

```text
ffmpeg_edit
delivery_qc
```

### 4.7 `speech-to-text`

方法进：

```text
voice-room
edit-room
```

规则：

```text
转录用于字幕、口型、声画同步
带时间戳的转录优先
字幕不能只凭剧本文字生成，必须对齐实际音频
```

tool：

```text
speech_to_text
subtitle_generator
```

### 4.8 `doubao-tts`

方法进：

```text
voice-room
```

规则：

```text
中文角色优先使用适合中文语气和停顿的 TTS
每个角色必须有声音锁
每条台词必须记录 voice_id / model / speed / emotion / output_path
```

tool：

```text
tts_generator
```

## 5. 部门内小循环

### 5.1 提示词部小循环

```text
读取导演分镜 + 美术资产 + 项目规格
-> 选择提示词方法：Seedance / FLUX / 其他
-> 写 copy-ready prompt
-> prompt QC
-> 输出提示词包
-> 失败则 needs_prompt_fix
```

方法在 skill：

```text
prompt-room/SKILL.md
prompt-room/references/prompt-technique-library.md
```

能力在 tool：

```text
无必须 tool；提示词部主要产出文档
可选 prompt_linter
```

### 5.2 视频生成部小循环

```text
读取导演分镜 + 参考帧 + 视频提示词
-> 调用 video_generator
-> 保存版本和 metadata
-> 调用 video_qc
-> 通过则 video_qc_passed
-> 不通过则判定返工入口
```

方法在 skill：

```text
video-production-room/SKILL.md
video-production-room/references/ai-video-technique-library.md
```

能力在 tool：

```text
video_generator
video_probe
frame_sampler
```

### 5.3 导演部参考片小循环

```text
输入参考视频
-> 调用 reference_video_analyzer
-> 得到镜头/节奏/关键帧/转录
-> 导演判断可借鉴点
-> 写入导演参考分析
```

方法在 skill：

```text
director-room/SKILL.md
director-room/references/source-learning-index.md
```

能力在 tool：

```text
reference_video_analyzer
```

### 5.4 资产入库小循环

```text
收到图片/视频/音频/音乐
-> resolve/freeze
-> probe
-> register asset_id
-> 写入 asset manifest
-> 返回正式路径
```

方法在 skill：

```text
project-office
art-room
music-room
edit-room
```

能力在 tool：

```text
asset_resolver
asset_manifest
```

### 5.5 剪辑交付小循环

```text
读取通过 QC 的镜头 + 配音 + 音乐 + 字幕
-> 生成 timeline / edit decisions
-> 合成预览
-> QC
-> 修剪或返工
-> 最终导出
```

方法在 skill：

```text
edit-room
delivery-room
```

能力在 tool：

```text
ffmpeg_edit
video_composer
delivery_qc
```

## 6. 建议的 tool 命名和最小接口

先不要做复杂插件系统。最小可用就是 `scripts/tools/` 下的 CLI 或 Python 函数。

```text
scripts/tools/reference_video_analyzer.py
scripts/tools/asset_resolver.py
scripts/tools/video_generator.py
scripts/tools/video_probe.py
scripts/tools/frame_sampler.py
scripts/tools/tts_generator.py
scripts/tools/speech_to_text.py
scripts/tools/subtitle_generator.py
scripts/tools/ffmpeg_edit.py
scripts/tools/delivery_qc.py
```

每个 tool 最小统一输出：

```json
{
  "success": true,
  "tool": "tool_name",
  "input": {},
  "outputs": {},
  "metadata": {},
  "error": null
}
```

## 7. 迁移顺序

### 第一阶段：只做规则，不做大工具

```text
prompt-room 加 Seedance/FLUX 提示词方法
director-room 加参考视频观察方法
project-office 加 asset_id / manifest 规则
edit-room 加 FFmpeg 剪辑和交付 QC 规则
voice-room 加中文 TTS 和 STT 规则
```

### 第二阶段：补最小工具

```text
reference_video_analyzer
asset_resolver
video_probe
ffmpeg_edit
delivery_qc
```

### 第三阶段：接生成 provider

```text
video_generator
image_generator
tts_generator
music_generator
sfx_generator
```

### 第四阶段：再考虑合成引擎

```text
Remotion 或 HyperFrames 二选一先跑通
不要一开始两个都重度接入
```

## 8. 不应该做的事

```text
不要把 OpenMontage 76 个 skill 全复制进来
不要把供应商 API 文档塞进 project-office
不要让工具决定剧情、角色、导演意图
不要让提示词部重写剧情
不要让视频生成部用随机结果改 canon
不要让剪辑部用剪辑掩盖源头问题
```

一句话：

```text
skill 管“怎么判断、怎么写、怎么验收”
tool 管“怎么生成、怎么分析、怎么落文件”
project-office 管“谁交给谁、状态是什么、失败退回哪里”
```

