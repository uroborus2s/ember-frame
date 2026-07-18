# OpenMontage `.agents/skills` 分析报告

来源目录：`C:\Users\uroborus\project\OpenMontage\.agents\skills`

分析范围：

- 直接一级 skill：76 个 `SKILL.md`
- 额外代码脚本：42 个左右，主要集中在 HyperFrames、media-use、music-to-video、video-understand、website-to-video、remotion-to-hyperframes
- 未逐个分析二进制资产、音效、图片纹理和模板静态资源；这些属于执行资产，不是 skill 的决策逻辑

结论先说：

OpenMontage 的 `.agents/skills` 不是“项目总控流程”，而是 Layer 3 能力知识库。它们告诉 agent：某个工具、供应商、动画库、视频工作流应该怎么用。真正的总控流程在 `AGENT_GUIDE.md`、`pipeline_defs/*.yaml` 和 `skills/pipelines/**`。`.agents/skills` 更像专业工具手册、提示词技法库、渲染/音频/视频/动画的技术作业指导书。

对 Ember Frame 来说，不建议 76 个全量搬运。应该优先复用影视生产相关、分镜生成相关、视频生成提示词相关、音频和合成相关的 skill。纯 Web/UI/Three.js/GSAP 文档类 skill 可以作为资料库，不应该进入主流程。

## 一、整体分类

### 1. 视频制作核心类，优先复用

这些直接关系到 Ember Frame 的“从分镜到镜头资产再到剪辑成片”：

- `ai-video-gen`
- `seedance-2-0`
- `ltx2`
- `video-understand`
- `video-edit`
- `ffmpeg`
- `media-use`
- `visual-style`
- `motion-graphics`
- `hyperframes`
- `hyperframes-core`
- `hyperframes-creative`
- `hyperframes-animation`
- `hyperframes-media`
- `hyperframes-cli`
- `remotion`
- `remotion-best-practices`
- `website-to-video`
- `music-to-video`

### 2. 图像、视频、音频供应商类，按工具接入情况复用

这些是 provider / API 具体用法：

- `bfl-api`
- `flux-best-practices`
- `grok-media`
- `doubao-tts`
- `elevenlabs`
- `music`
- `sound-effects`
- `speech-to-text`
- `text-to-speech`
- `setup-api-key`
- `acestep`
- `heygen`
- `avatar-video`
- `create-video`
- `faceswap`
- `video-translate`
- `agents`

### 3. 角色动画和动画语言类，适合补强导演部、美术部、视频生成部

- `character-rigging`
- `pose-library-design`
- `svg-character-animation`
- `canvas-procedural-animation`
- `character-animation-qa`
- `framer-motion`
- `lottie-bodymovin`
- `gsap-core`
- `gsap-timeline`
- `gsap-plugins`
- `gsap-react`
- `gsap-frameworks`
- `gsap-scrolltrigger`
- `gsap-performance`
- `gsap-utils`

### 4. 可视化 / 3D / UI 类，按项目需要放入资料库

- `threejs-fundamentals`
- `threejs-animation`
- `threejs-geometry`
- `threejs-interaction`
- `threejs-lighting`
- `threejs-loaders`
- `threejs-materials`
- `threejs-postprocessing`
- `threejs-shaders`
- `threejs-textures`
- `d3-viz`
- `manim-composer`
- `manimce-best-practices`
- `manimgl-best-practices`
- `tailwind-design-system`
- `vercel-react-best-practices`
- `vercel-composition-patterns`
- `web-design-guidelines`
- `beautiful-mermaid`

### 5. 迁移辅助类，只有特定场景才需要

- `video-download`
- `video-toolkit`
- `playwright-recording`
- `synthetic-screen-recording`
- `remotion-to-hyperframes`

## 二、逐 skill 分析

| Skill | 作用 | OpenMontage 中的角色 | Ember Frame 复用建议 |
|---|---|---|---|
| `acestep` | ACE-Step 1.5 音乐生成、歌曲、翻唱、stem 分离 | 音乐生成和音频素材生产的 provider 技法 | 可给 `music-room`，作为本地/开源音乐生成方案；需要 ACE-Step 环境时再接 |
| `agents` | ElevenLabs 语音 AI agent、实时语音助手 | 交互式语音代理能力，不是普通视频制作主链 | 暂不进入主流程；以后做互动角色或实时客服式角色时再用 |
| `ai-video-gen` | 多 gateway 视频生成 API，文生视频/图生视频/异步轮询 | 视频生成 provider 总说明 | 强烈建议给 `video-production-room` 和 `prompt-room`，作为视频生成通用调用和提示词规范 |
| `avatar-video` | HeyGen avatar 视频生成 | 虚拟人口播/数字人 | 可给 `voice-room` + `video-production-room`，但只在数字人口播项目启用 |
| `beautiful-mermaid` | Mermaid 图表渲染为 SVG/PNG | 图解视频、技术解释视频的图表资产生产 | 可低优先级复用到 `art-room` 或 explainer 类项目 |
| `bfl-api` | BFL/FLUX API 调用、异步、限流、webhook | 图片生成 provider 技法 | 可给 `art-room` 和 `prompt-room`，尤其是角色/场景参考图 |
| `canvas-procedural-animation` | p5.js/canvas 程序化角色效果、粒子、天气、走路循环 | 本地程序动画补充能力 | 可作为 `video-production-room` 的轻量动画方案，不进主流程 |
| `character-animation-qa` | 角色动画 QC：schema、Playwright、帧采样、ffprobe | 本地角色动画质量门 | 很适合 Ember，放入 `director-room` / `video-production-room` 的角色动画质检规则 |
| `character-rigging` | 2D 角色 rig：部件、pivot、层级、约束、视图 | 可复用角色动画资产结构 | 很适合 Ember 的角色总卡/美术部，尤其长期剧集角色一致性 |
| `create-video` | HeyGen create video API | HeyGen 视频创建主流程 | 只在 HeyGen 数字人/模板视频项目中复用 |
| `d3-viz` | D3 自定义数据可视化 | 图表、网络、地图、复杂 SVG 可视化 | 对剧情视频价值低；技术解释类项目再用 |
| `doubao-tts` | 豆包/火山引擎 TTS，中文、多语言、字级时间戳 | 中文配音 provider | 强烈建议给 `voice-room`，中文项目比 ElevenLabs 更贴近 |
| `elevenlabs` | ElevenLabs TTS、音效、音乐、克隆、Remotion 同步 | 英文/多语言音频生产主 provider | 可给 `voice-room` 和 `music-room`，但中文主项目不必默认优先 |
| `faceswap` | HeyGen 换脸 API | 头像/人脸替换 | 谨慎使用；不应进入剧情主流程，除非项目明确需要 |
| `ffmpeg` | 视频音频处理、转码、裁剪、压缩、抽音频 | 所有视频后处理基础工具 | 必须复用；给 `video-production-room`、`edit-room`、`delivery-room` |
| `flux-best-practices` | FLUX 图片生成提示词、模型选择、I2I、多参考、文字 | 图片提示词技法库 | 强烈建议给 `art-room` 和 `prompt-room` |
| `framer-motion` | 用 Disney 12 动画原则指导 React 动画 | motion design 语言 | 可给 `director-room` 和 `edit-room`，抽取原则，不必照搬 React 代码 |
| `grok-media` | Grok 图片/视频生成 API、提示词、异步 | xAI 图像/视频 provider | 只有接 Grok 时复用；方法可参考，非核心 |
| `gsap-core` | GSAP 基础 tween、ease、stagger、matchMedia | 网页/HyperFrames 动画基础 | 可给 HyperFrames/合成路线；剧情 AIGC 主流程不必全量引入 |
| `gsap-frameworks` | Vue/Svelte 等框架里的 GSAP 生命周期和清理 | 前端动画工程规则 | 低优先级 |
| `gsap-performance` | GSAP 性能：transform、opacity、batch、60fps | 动画性能质量门 | 可抽取为合成 QC 规则 |
| `gsap-plugins` | ScrollTo、Flip、Draggable、SplitText、DrawSVG 等插件 | 高级动态图形和文字动画 | 可给 `edit-room` / motion graphics，不进主流程 |
| `gsap-react` | React 中使用 GSAP：useGSAP、refs、cleanup | React 动画工程规则 | 如果 Ember 用 React 合成，可复用；否则低优先级 |
| `gsap-scrolltrigger` | 滚动驱动动画 | 网站演示/网页动效 | 对视频主流程价值低 |
| `gsap-timeline` | 动画时间线编排 | 镜头内运动节奏编排 | 可抽象给 `director-room` / `edit-room`，用于“动作按 beat 编排”的语言 |
| `gsap-utils` | clamp、mapRange、random、snap 等动画工具函数 | 动效工程辅助 | 低优先级 |
| `heygen` | HeyGen API 总入口，已标 deprecated | 旧版 HeyGen 路由 | 不建议直接搬；只保留到数字人专题资料 |
| `hyperframes` | HyperFrames 总路由入口，按意图选择工作流 | HTML/CSS/GSAP 视频合成体系入口 | 可作为 Ember 合成体系参考，但不应替代导演/剪辑总控 |
| `hyperframes-animation` | HyperFrames 动画规则、蓝图、转场、runtime adapter | 动态图形动画技法库 | 高价值；可给 `edit-room` / `video-production-room`，尤其短视频包装 |
| `hyperframes-cli` | HyperFrames CLI dev loop、lint、validate、render、doctor | 渲染和验证执行流程 | 如果采用 HyperFrames，必须迁移；否则不用 |
| `hyperframes-core` | HyperFrames composition 合同：data 属性、clip、timeline、验证 | 合成文件结构规范 | 如果 Ember 要 HTML 合成视频，非常值得复用 |
| `hyperframes-creative` | HyperFrames 非动画创意：调色、字体、节奏、旁白、品牌 | 合成阶段的创意方向 | 可抽取到 `edit-room` 和 `art-room`，不要直接当总控 |
| `hyperframes-media` | TTS/BGM/SFX/transcription/captions 的共享音频引擎 | 合成音频资产统一入口 | 很有参考价值；可给 `voice-room`、`music-room`、`edit-room` |
| `hyperframes-registry` | 安装和接线 HyperFrames blocks/components | 组件库/模板复用 | 对 Ember 不建议优先；会带来模板化和同质化风险 |
| `lottie-bodymovin` | Lottie 动画原则和 After Effects 导出 | 动画资产交换 | 中等价值；如果用 AE/Lottie 才需要 |
| `ltx2` | LTX-2.3 视频生成，T2V/I2V、分辨率、帧数、提示词 | 本地/模型视频生成 provider | 可给 `video-production-room`；适合做本地/开源视频生成备选 |
| `manim-composer` | 数学/技术解释视频的分镜和 scenes.md 流程 | Manim 视频编排 | 只在科普/数学解释类项目复用 |
| `manimce-best-practices` | Manim Community 规则、模板、CLI | 数学动画执行规范 | 条件复用 |
| `manimgl-best-practices` | ManimGL 规则、模板、交互开发 | 数学动画执行规范 | 条件复用 |
| `media-use` | 媒体素材解析器：BGM/SFX/image/icon -> 本地冻结文件 + ledger | 资产检索、缓存、冻结、登记 | 很值得借鉴；可变成 Ember 的素材资产入口和素材台账机制 |
| `motion-graphics` | HyperFrames motion graphics 完整工作流：初始化、计划、取素材、设计、构建、渲染、验证 | 动态图形短片生产流水线 | 高价值，但应拆开吸收进 `edit-room` / `prompt-room`，不要整体覆盖剧情流程 |
| `music` | ElevenLabs Music API | 音乐生成 provider | 可给 `music-room`，但中文/版权项目需要替代方案 |
| `music-to-video` | 音乐驱动、beat-synced HyperFrames 视频工作流 | 音乐可视化/歌词/节奏短片 | 高价值，但只用于音乐驱动视频；不是剧情主流程 |
| `playwright-recording` | Playwright 录制网页交互视频 | App demo / UI walkthrough | 可用于工具演示视频；剧情项目低优先级 |
| `pose-library-design` | 2D 角色 pose、动作循环、表情状态设计 | 角色动画动作库 | 很适合 Ember 的角色表演库 |
| `remotion` | Toolkit-specific Remotion 转场、组件、项目约定 | React 视频合成扩展 | 若 Ember 采用 Remotion，可复用；否则只借鉴时间线/转场思想 |
| `remotion-best-practices` | Remotion captions、FFmpeg、音频可视化、SFX 等规则 | Remotion 基础最佳实践 | 若使用 Remotion 合成，必须复用 |
| `remotion-to-hyperframes` | 把 Remotion composition 迁移为 HyperFrames | 迁移工具，不是创作流程 | 只在已有 Remotion 代码迁移时使用 |
| `seedance-2-0` | Seedance 2.0 视频生成提示词、镜头语言、多镜头、口型、音频 | OpenMontage premium video default | 极高价值；应进 `prompt-room` 和 `video-production-room`，尤其镜头提示词 |
| `setup-api-key` | ElevenLabs API key 检查和配置引导 | 环境配置 helper | 只保留思路，不要进创作流程 |
| `sound-effects` | ElevenLabs 音效生成 | 音效资产生产 | 可给 `music-room` / `edit-room`，用于环境声、撞击、UI 声 |
| `speech-to-text` | ElevenLabs Scribe 转录、时间戳、说话人、实时流 | 字幕、口型、素材理解 | 高价值；给 `voice-room`、`edit-room`、`video-understand` 类流程 |
| `svg-character-animation` | SVG 角色 rig 动画，GSAP/CSS/Remotion/HyperFrames | 本地角色动画实现 | 高价值；给 `video-production-room` 的角色动画分支 |
| `synthetic-screen-recording` | Remotion TerminalScene 合成终端录屏 | 合成式屏幕演示 | 对剧情项目低；对教程/软件演示高 |
| `tailwind-design-system` | Tailwind v4 设计系统、tokens、组件模式 | Web UI 设计工程 | 对视频主链低；可用于 Ember 后台工具界面 |
| `text-to-speech` | HeyGen Starfish TTS | HeyGen TTS provider | 条件复用；中文主项目优先 Doubao/其他中文 TTS |
| `threejs-animation` | Three.js keyframe、骨骼、morph、混合动画 | 3D 动画 | 条件复用；只有 3D 场景/虚拟制片时需要 |
| `threejs-fundamentals` | Three.js scene/camera/renderer/Object3D | 3D 基础 | 条件复用 |
| `threejs-geometry` | Three.js geometry、BufferGeometry、instancing | 3D 几何建模 | 条件复用 |
| `threejs-interaction` | Three.js raycasting、controls、输入 | 交互 3D | 对成片制作低，交互应用才需要 |
| `threejs-lighting` | Three.js light、shadow、IBL | 3D 灯光 | 条件复用 |
| `threejs-loaders` | GLTF/texture/HDR/loading manager | 3D 资产加载 | 条件复用 |
| `threejs-materials` | PBR、basic、phong、shader materials | 3D 材质 | 条件复用 |
| `threejs-postprocessing` | bloom、DOF、SSAO、film grain、glitch | 3D 后期效果 | 可借鉴到视觉风格，但不是主链 |
| `threejs-shaders` | GLSL、ShaderMaterial、uniforms、noise、gradient | 自定义视觉效果 | 高门槛，按需 |
| `threejs-textures` | texture、UV、environment、filtering | 3D 纹理 | 条件复用 |
| `vercel-composition-patterns` | React component composition patterns | 前端组件工程 | 只用于 Ember 管理后台/工具 UI |
| `vercel-react-best-practices` | React/Next 性能、水瀑、bundle、server/client 数据 | 前端性能规则 | 只用于 Ember 前端 UI |
| `video-download` | yt-dlp 下载视频、字幕、音频、metadata | 参考素材/源素材获取 | 可给素材采集流程；注意版权和用户授权 |
| `video-edit` | FFmpeg trim、concat、resize、speed、extract audio | 剪辑基础操作 | 必须复用到 `edit-room` |
| `video-toolkit` | claude-code-video-toolkit 一体化视频制作 | 旧式一体化工具链 | 不建议整体集成；容易和 Ember 分部门流程冲突 |
| `video-translate` | HeyGen 视频翻译、lip-sync、多语言 | 本地化配音/翻译 | 可给 `voice-room` / `delivery-room` 的本地化分支 |
| `video-understand` | 场景检测、转录、关键帧提取、Whisper | 参考视频分析、素材理解 | 强烈建议复用；可补强导演部“观察镜头”的能力 |
| `visual-style` | 创建/提取/应用视觉风格，含 gallery、templates、connectors | 视觉风格合同 | 极高价值；应进入 `art-room`、`director-room`、`prompt-room` |
| `web-design-guidelines` | UI/UX/accessibility 代码审查 | Web 界面审查 | 只用于 Ember 工具 UI |
| `website-to-video` | 网站截图、品牌提取、脚本、VO、HyperFrames 视频 | 网站转宣传短片 | 对剧情项目低；对产品/官网宣传片高 |

## 三、真正带代码的 skill

这些不是单纯文档，里面有脚本，可以直接研究代码结构。

### `media-use`

脚本：

- `scripts/resolve.mjs`
- `scripts/eval.mjs`
- `scripts/lib/cache.mjs`
- `scripts/lib/freeze.mjs`
- `scripts/lib/manifest.mjs`
- `scripts/lib/probe.mjs`
- `scripts/lib/providers.mjs`
- `scripts/lib/bgm-provider.mjs`
- `scripts/lib/sfx-provider.mjs`
- `scripts/lib/image-provider.mjs`
- `scripts/lib/brand-provider.mjs`

价值：

- 把“我要一个 BGM / SFX / image / icon”变成统一 resolve 流程。
- 先查项目缓存，再查全局缓存，再查 provider，再冻结成项目本地文件，再写 manifest。
- 这套思想非常适合 Ember Frame 的“素材归档 + 资产台账”。

建议：

- 不要照搬 provider 代码。
- 先复用机制：resolve -> freeze -> manifest -> asset_id。

### `video-understand`

脚本：

- `scripts/understand_video.py`

价值：

- 参考视频分析、场景检测、关键帧提取、转录。
- 能补上 Ember Frame 现在很需要的“观察镜头”能力。

建议：

- 归入 `director-room` 的参考片分析。
- 也归入 `edit-room` 的源素材审查。

### `music-to-video`

脚本：

- `scripts/analyze-beatgrid.py`
- `scripts/validate-plan.mjs`
- `scripts/assemble-index.mjs`
- `scripts/stage-assets.mjs`
- `scripts/lib/storyboard.mjs`

价值：

- 它的强点不是音乐 API，而是“音乐先分析一次，然后所有画面按 beat grid 编排”。
- 对 MV、歌词视频、节奏宣传片很有价值。

建议：

- 不进剧情主流程。
- 可作为 `music-room` + `edit-room` 的专题分支。

### `hyperframes-media`

脚本：

- `scripts/audio.mjs`
- `scripts/heygen-tts.mjs`
- `scripts/lib/tts.mjs`
- `scripts/lib/bgm.mjs`
- `scripts/lib/sfx.mjs`
- `scripts/lib/heygen.mjs`

价值：

- 把 TTS、BGM、SFX、字幕、转录统一成一个音频生产入口。
- 对 Ember 的 `voice-room`、`music-room`、`edit-room` 很有参考价值。

建议：

- 先学“统一音频入口 + provider fallback + 本地文件输出”。
- 不要直接依赖 HeyGen。

### `website-to-video`

脚本：

- `scripts/w2h-verify.mjs`

价值：

- 网站截图、品牌提取、脚本、VO、合成、验证的完整流程。

建议：

- 只对产品宣传片有用。
- 不进入 AI 剧主流程。

### `remotion-to-hyperframes`

脚本：

- `scripts/lint_source.py`
- `scripts/frame_strip.sh`
- `scripts/render_diff.sh`
- 测试 fixtures

价值：

- 迁移工具链，不是创作工具链。
- 能看出 OpenMontage 对“迁移质量”的要求：lint、baseline render、目标 render、SSIM diff、记录 gaps。

建议：

- 只借鉴“迁移验证方法”。

### `beautiful-mermaid`

脚本：

- `scripts/render.ts`
- `scripts/create-html.ts`

价值：

- 技术说明视频里图表渲染有用。

建议：

- 低优先级。

## 四、最值得 Ember Frame 借鉴的能力

### A. 立刻值得吸收

1. `visual-style`
   - 把风格从“口头感觉”变成可交接文档。
   - 应进入美术部、导演部、提示词部。

2. `seedance-2-0`
   - 视频提示词里最有价值的部分。
   - 尤其是 opener、camera behavior、多镜头、realism enforcement、format priority。

3. `video-understand`
   - 让 agent 能观察参考片、拆场景、抽关键帧。
   - 这是“像导演一样看镜头”的基础能力。

4. `media-use`
   - 素材检索、冻结、缓存、manifest 机制。
   - 可改造成 Ember 的资产入口。

5. `ffmpeg` + `video-edit`
   - 剪辑、转码、抽音频、压缩、concat 的基础。
   - 应成为剪辑部和交付部基础工具知识。

6. `speech-to-text`
   - 口型、字幕、参考片分析、素材转录都需要。

7. `character-rigging` + `pose-library-design` + `svg-character-animation` + `character-animation-qa`
   - 对长期剧集角色一致性很重要。

### B. 第二批吸收

1. `hyperframes-core` / `hyperframes-animation` / `hyperframes-creative` / `hyperframes-cli`
   - 如果 Ember 要做 HTML/CSS/GSAP 合成视频，就吸收。
   - 如果主路线是 AIGC 镜头 + 剪辑，则先不急。

2. `remotion` / `remotion-best-practices`
   - 如果 Ember 采用 Remotion，就吸收。
   - 不要同时重度引入 Remotion 和 HyperFrames，先选一个合成主线。

3. `music-to-video`
   - 适合 MV、歌词视频、节奏宣传片。

4. `doubao-tts`
   - 中文配音优先级高。

5. `flux-best-practices` / `bfl-api`
   - 美术图片生产很实用。

### C. 暂时不要进入主流程

- `video-toolkit`：一体化工具链，容易和 Ember 的分部门流程冲突。
- `agents`：实时语音 agent，不是视频制作主链。
- `faceswap`：风险高，且不是主流程能力。
- `video-translate`：只做本地化时需要。
- `threejs-*`：除非明确走 3D 虚拟制片。
- `tailwind-*` / `vercel-*` / `web-design-guidelines`：适合工具 UI，不适合 AI 剧生产主链。

## 五、建议集成到 Ember Frame 的方式

不要把 OpenMontage 的 `.agents/skills` 原样复制到 Ember。更合适的方式是：

```text
+ project-office
   只吸收：能力登记、状态台账、阻塞/返工规则

+ director-room
   吸收：video-understand、visual-style、framer-motion 动画原则、角色连续性 QC

+ art-room
   吸收：visual-style、flux-best-practices、bfl-api、character-rigging

+ prompt-room
   吸收：seedance-2-0、ai-video-gen、ltx2、flux-best-practices、grok-media

+ voice-room
   吸收：doubao-tts、elevenlabs、speech-to-text、text-to-speech

+ music-room
   吸收：music、sound-effects、acestep、hyperframes-media 的音频组织方式

+ video-production-room
   吸收：ai-video-gen、seedance-2-0、ltx2、svg-character-animation、character-animation-qa

+ edit-room
   吸收：ffmpeg、video-edit、hyperframes-core/remotion-best-practices、music-to-video 的节奏结构

+ delivery-room
   吸收：ffmpeg、video-edit、video-understand 的最终检查方法
```

## 六、最重要的架构启发

OpenMontage 的这些 skill 最大价值不是“工具清单”，而是三件事：

1. 把供应商经验沉淀成 Layer 3 技能。
   - 例如 Seedance 怎么写镜头提示词。
   - FLUX 怎么写图像提示词。
   - ElevenLabs 怎么控制停顿、音色、音效。

2. 把生成结果落成可追踪资产。
   - media-use 的 freeze / manifest 思想值得学。
   - Ember Frame 不应该让图片、视频、音频散落在临时目录。

3. 把创作工具放进专业工位。
   - 视频生成 skill 不直接决定剧情。
   - 音乐 skill 不改变场景情绪功能。
   - 合成 skill 不替代导演判断。

这和 Ember Frame 的方向一致：总控固定大流程，小任务内部循环，专业部门只做自己该做的事。

## 七、最小迁移方案

第一阶段只迁移 10 个能力，不要贪多：

1. `visual-style`
2. `video-understand`
3. `seedance-2-0`
4. `ai-video-gen`
5. `flux-best-practices`
6. `media-use`
7. `ffmpeg`
8. `video-edit`
9. `speech-to-text`
10. `doubao-tts`

这 10 个已经能显著增强：

- 风格统一
- 参考片分析
- 视频提示词质量
- 素材台账
- 剪辑/交付基础能力
- 中文配音与字幕能力

第二阶段再考虑：

- `character-rigging`
- `pose-library-design`
- `svg-character-animation`
- `character-animation-qa`
- `hyperframes-*` 或 `remotion-*`
- `music-to-video`

第三阶段才考虑：

- Three.js
- D3
- Manim
- Tailwind/Vercel
- HeyGen 数字人全家桶

