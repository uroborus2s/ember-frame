# 第 0 实操入口：从零创建第一个 ComfyUI + Wan2.2 项目

> 建议时长：60-90 分钟
> 适用平台：macOS / Windows / Linux
> 本章目标：不讲原理，先让你知道如何打开 ComfyUI、下载最小模型、创建项目文件夹、拖入工作流、填输入并点击第一次运行。

## 先看结论：你要做的 10 件事

| 顺序 | 你要做什么 | 成功标志 |
| ---: | --- | --- |
| 1 | 安装或打开 ComfyUI。 | 浏览器能打开 `http://127.0.0.1:8000/`。 |
| 2 | 找到 ComfyUI 基础目录。 | 能看到 `input/`、`output/`、`models/`。 |
| 3 | 在电脑上创建自己的项目文件夹。 | 有 `inputs/`、`outputs/`、`workflows/`、`screenshots/`、`notes/`。 |
| 4 | 先只下载 Wan2.2 5B TI2V 最小模型。 | 3 个模型文件放到正确目录。 |
| 5 | 把课程参考图复制到 ComfyUI 的 `input/`。 | `LoadImage` 节点能选中这张图。 |
| 6 | 把课程 JSON 拖到 ComfyUI 画布。 | 画布出现 Wan2.2 5B TI2V 节点。 |
| 7 | 在模型节点选择文件。 | 模型下拉框不再红框报缺失。 |
| 8 | 填正向提示词、宽高、帧数、seed。 | 参数记录表里能写清每个值。 |
| 9 | 点击右上角“运行”。 | 成功生成视频，或失败但记录了错误原文。 |
| 10 | 把输出、截图、工作流保存到项目文件夹。 | 项目文件夹里能复盘这次实验。 |

## 你要先分清两个目录

初学者最容易混淆这两个目录：

| 目录 | 谁使用 | 作用 |
| --- | --- | --- |
| ComfyUI 基础目录 | 软件使用 | 放模型、输入图、输出结果。 |
| 项目目录 | 你自己管理 | 放某个视频项目的素材、截图、工作流备份和记录。 |

例子：

```text
ComfyUI 基础目录：
<你的 ComfyUI 基础目录>

你的项目目录：
~/AI-Video-Projects/wan22-first-project
```

生成时，ComfyUI 会从自己的 `input/` 读图，从自己的 `models/` 读模型，把结果写到自己的 `output/`。项目目录负责保存副本和记录，方便你以后复盘。

## 第 1 步：确认 ComfyUI 能打开

打开浏览器，输入：

```text
http://127.0.0.1:8000/
```

成功时，你应该看到：

| 位置 | 应该看到 |
| --- | --- |
| 页面中间 | 深色网格画布和节点。 |
| 顶部 | 当前工作流标签，例如 `Unsaved Workflow`。 |
| 右上角 | 蓝色“运行”按钮。 |

如果打不开，不要下载模型，先回到第 2 章处理启动问题。

## 第 2 步：找到 ComfyUI 基础目录

路径示例，请替换为你自己的实际目录：

```text
macOS Desktop: ~/Documents/ComfyUI
Windows Desktop: %USERPROFILE%\Documents\ComfyUI
Linux 手动安装: ~/ComfyUI
```

你需要确认里面至少有这些目录：

```text
ComfyUI/
├── input/
├── output/
└── models/
    ├── diffusion_models/
    ├── text_encoders/
    └── vae/
```

如果 `models/` 下面缺少某个子目录，就手动创建同名目录。目录名要完全一致，特别是 `diffusion_models` 有复数 `s`。

## 第 3 步：创建你的第一个项目文件夹

项目文件夹不是 ComfyUI 自动创建的，需要你自己建。建议位置：

### macOS / Linux

```bash
mkdir -p ~/AI-Video-Projects/wan22-first-project/inputs
mkdir -p ~/AI-Video-Projects/wan22-first-project/outputs
mkdir -p ~/AI-Video-Projects/wan22-first-project/workflows
mkdir -p ~/AI-Video-Projects/wan22-first-project/screenshots
mkdir -p ~/AI-Video-Projects/wan22-first-project/notes
```

### Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\AI-Video-Projects\wan22-first-project\inputs"
New-Item -ItemType Directory -Force "$env:USERPROFILE\AI-Video-Projects\wan22-first-project\outputs"
New-Item -ItemType Directory -Force "$env:USERPROFILE\AI-Video-Projects\wan22-first-project\workflows"
New-Item -ItemType Directory -Force "$env:USERPROFILE\AI-Video-Projects\wan22-first-project\screenshots"
New-Item -ItemType Directory -Force "$env:USERPROFILE\AI-Video-Projects\wan22-first-project\notes"
```

课程也提供了项目模板：[first-wan22-project](../../templates/first-wan22-project/README.md)。你可以照它的目录结构创建自己的项目。

项目目录最后应该像这样：

```text
wan22-first-project/
├── inputs/
├── outputs/
├── workflows/
├── screenshots/
└── notes/
```

## 第 4 步：先下载最小 5B 模型，不要一开始下载全部

官方 ComfyUI Wan2.2 教程说明：5B TI2V 版本用于入门，官方文档也指出 5B 版本适合 8GB 显存配合 ComfyUI 原生 offloading 使用。第一次只下载 5B 所需的 3 个文件。

| 文件类型 | 下载文件 | 放到哪里 |
| --- | --- | --- |
| Diffusion Model | [wan2.2_ti2v_5B_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors) | `ComfyUI/models/diffusion_models/` |
| VAE | [wan2.2_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan2.2_vae.safetensors) | `ComfyUI/models/vae/` |
| Text Encoder | [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) | `ComfyUI/models/text_encoders/` |

下载方式：

1. 点击上面的链接。
2. 等浏览器下载完成。
3. 不要改文件名。
4. 把文件移动到对应目录。
5. 重启 ComfyUI 或刷新模型列表。

正确放置后应是：

```text
ComfyUI/
└── models/
    ├── diffusion_models/
    │   └── wan2.2_ti2v_5B_fp16.safetensors
    ├── text_encoders/
    │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
    └── vae/
        └── wan2.2_vae.safetensors
```

## 模型下载管理工具怎么选

有工具，但不要一开始装一堆。模型下载管理分成 4 类：

| 工具 | 适合谁 | 优点 | 风险或限制 | 本课程建议 |
| --- | --- | --- | --- | --- |
| ComfyUI 自动下载/模型面板 | 完全新手 | 界面化，遇到缺模型时可能直接下载或显示进度。 | 不同安装版本行为不同，网络不稳定时可能卡住。 | 第一优先，能用就先用。 |
| `comfy-cli` | 想用命令管理 ComfyUI 的用户 | 官方 CLI，可以安装、启动、更新，也支持模型下载命令。 | 需要会终端，路径写错会下到错误目录。 | 第二优先，用于可复现教程命令。 |
| Hugging Face `hf` CLI | 经常从 Hugging Face 下载模型的用户 | 能登录、下载、管理缓存，适合私有或受限模型。 | 默认会有缓存和下载目录概念，新手容易不知道文件最终在哪。 | 适合批量下载后手动移动。 |
| `aria2c` | 网络不稳定、需要断点续传的大文件下载 | 支持断点续传和多连接下载。 | 只是下载器，不知道 ComfyUI 模型目录。 | 作为高级备用方案。 |

`ComfyUI Manager` 主要用于安装、更新和管理自定义节点。它对“缺节点”很有用，但不要把它当作所有模型权重的唯一下载入口。模型文件最终是否能用，仍然取决于：文件名是否正确、是否放到正确的 `ComfyUI/models/` 子目录、加载节点是否选中了对应文件。

### ComfyUI 里下载模型的实际流程

在 ComfyUI 里下载模型，通常不是先去“模型库”随便搜，而是先加载一个工作流，让 ComfyUI 知道缺哪个模型。

1. 打开 ComfyUI：`http://127.0.0.1:8000/`。
2. 拖入本章 5B 工作流 JSON：`video_wan2_2_5B_ti2v.json`。
3. 如果右上角或节点上出现“缺少模型/Show missing models/显示缺失模型”一类提示，点开它。
4. 如果界面提供 `Download`、`下载`、`Install` 或类似按钮，就点击下载。
5. 下载时看侧边栏的模型面板、任务面板或下载进度。不同版本显示位置不同。
6. 下载完成后，按 `R` 刷新节点定义，或重启 ComfyUI。
7. 回到 `UNETLoader`、`CLIPLoader`、`VAELoader`，确认下拉框能选到对应文件。

截图里的缺失模型面板可以这样读：

| 面板内容 | 它的意思 | 正确操作 |
| --- | --- | --- |
| `缺失模型 (3)` | 当前工作流缺 3 个文件，不是节点坏了。 | 展开每一组，逐个核对文件名。 |
| `diffusion_models (1)` | 缺 Wan2.2 主模型。 | 下载后放到 `models/diffusion_models/`。 |
| `text_encoders (1)` | 缺 UMT5 文本编码器。 | 下载后放到 `models/text_encoders/`。 |
| `vae (1)` | 缺 VAE。 | 下载后放到 `models/vae/`。 |
| `全部下载` | 尝试按工作流记录的链接批量下载。 | 能看到任务或进度时使用；没有反应时不要反复点击。 |
| `复制链接` | 复制该模型的 Hugging Face 直链。 | 用浏览器、`comfy-cli`、`hf` CLI 或 `aria2c` 手动下载。 |

如果点击 `下载` 或 `全部下载` 后没有任何进度，优先按下面顺序判断：

1. 等 10-20 秒，看右侧任务面板或下载按钮是否出现进度。
2. 点一次 `Refresh`，确认不是界面状态没有刷新。
3. 打开浏览器访问任意一个模型链接。如果浏览器也打不开 Hugging Face，问题就是网络访问，不是 ComfyUI。
4. 如果浏览器能下载，但 ComfyUI 界面下载不动，直接用 `复制链接` 加“浏览器手动下载”，不要继续在界面里试。
5. 如果公司、校园网或国内网络访问 Hugging Face 不稳定，通常需要代理、镜像或断点续传下载器。ComfyUI Desktop 不一定会继承你终端里的代理环境变量，所以“终端能访问”不等于“桌面应用能自动下载”。

是否需要配置代理，按这个标准判断：

| 现象 | 判断 | 建议 |
| --- | --- | --- |
| 浏览器打不开 Hugging Face 或下载速度为 0 | 需要处理网络访问。 | 先开系统代理或网络工具，再刷新下载；仍不稳定就手动下载。 |
| 浏览器能下载，ComfyUI 按钮不动 | 不一定是代理问题，可能是 Desktop 自动下载失败但无提示。 | 用 `复制链接` 手动下载并放入模型目录。 |
| 下载到一半失败 | 大文件网络不稳定。 | 用 `aria2c` 或浏览器断点续传，避免重新下 16GB。 |
| 文件已下载但节点仍红 | 文件放错目录或文件名被改。 | 按 `diffusion_models`、`text_encoders`、`vae` 三个目录重新核对。 |

如果界面没有下载按钮，或者下载一直不动，不要反复点击运行。改用下面“浏览器手动下载”，把文件放到正确目录。

ComfyUI Desktop 官方文档也说明：Desktop 的模型文件夹位置可能和便携版不同，可以通过顶部 logo 或 Help/Open folder 打开模型目录；自动下载通常从 Hugging Face 拉取，网络不通时要复制模型链接手动安装。

### 方式 A：浏览器手动下载

这是最容易理解的方法：

1. 点击本章模型链接。
2. 等浏览器下载完成。
3. 不改文件名。
4. 把文件移动到对应目录。
5. 回到 ComfyUI，按 `R` 刷新，或重启 ComfyUI。

适合第一次学习，因为每一步都能看见文件在哪里。

### 方式 B：用 comfy-cli 下载

官方 `comfy-cli` 文档提供了 `comfy model download` 命令。格式是：

```bash
comfy model download --url "<模型直链>" --relative-path models/diffusion_models
```

5B diffusion model 示例：

```bash
comfy model download --url "https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors" --relative-path models/diffusion_models
```

注意：

1. `relative-path` 要写 ComfyUI 期望的相对目录。
2. VAE 要写 `models/vae`。
3. Text Encoder 要写 `models/text_encoders`。
4. 下载后仍要在 ComfyUI 里确认下拉框能选到文件。

### 方式 C：用 Hugging Face hf CLI 下载到临时目录

`hf` CLI 适合从 Hugging Face 仓库下载文件。为了避免新手把文件下错目录，本课程建议先下载到临时目录，再手动移动。

```bash
hf download Comfy-Org/Wan_2.2_ComfyUI_Repackaged \
  split_files/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors \
  --local-dir ~/Downloads/wan22-models
```

下载完成后，把文件移动到：

```text
ComfyUI/models/diffusion_models/
```

如果模型需要登录或同意协议，先执行：

```bash
hf auth login
```

### 方式 D：用 aria2c 断点续传

`aria2c` 是通用下载器，不懂 ComfyUI。它的任务只是把大文件稳定下载下来。

```bash
aria2c -c -x 8 -s 8 \
  -d "<ComfyUI基础目录>/models/diffusion_models" \
  -o "wan2.2_ti2v_5B_fp16.safetensors" \
  "https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors"
```

参数含义：

| 参数 | 含义 |
| --- | --- |
| `-c` | 继续未完成下载。 |
| `-x 8` | 最多 8 个连接。 |
| `-s 8` | 把下载分成 8 段。 |
| `-d` | 保存目录。 |
| `-o` | 保存文件名。 |

如果你不熟悉终端，不要从 `aria2c` 开始。先用浏览器或 ComfyUI 自动下载。

## 第 5 步：什么时候再下载 14B 模型

第一次不要下载 14B。先用 5B 跑通，再按显存和课程进度下载。

| 任务 | 需要文件 | 放置目录 |
| --- | --- | --- |
| 14B T2V | `wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors`、`wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors` | `models/diffusion_models/` |
| 14B T2V | `wan_2.1_vae.safetensors` | `models/vae/` |
| 14B T2V | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `models/text_encoders/` |
| 14B T2V 4-step LoRA | `wan2.2_t2v_lightx2v_4steps_lora_v1.1_high_noise.safetensors`、`wan2.2_t2v_lightx2v_4steps_lora_v1.1_low_noise.safetensors` | `models/loras/` |
| 14B I2V / FLF2V | `wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors`、`wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors` | `models/diffusion_models/` |
| 14B I2V / FLF2V | `wan_2.1_vae.safetensors`、`umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `models/vae/`、`models/text_encoders/` |
| 14B I2V / FLF2V 4-step LoRA | `wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors`、`wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors` | `models/loras/` |

这张表以仓库内置工作流 JSON 的 `Model Links` 为准。LoRA 不是第一次跑通 5B 必需文件；使用 14B 模板里的 4-step 加速分组时才需要下载。FLF2V 使用 I2V 的 high/low noise 模型位置，因此第一次不要把 FLF2V 作为下载目标。

## 第 6 步：把参考图放到 ComfyUI input

课程入门图在：

```text
docs/assets/inputs/chapter-05/05-input-starter-product.png
```

把它复制到 ComfyUI 的：

```text
ComfyUI/input/
```

同时也复制一份到你的项目目录：

```text
wan22-first-project/inputs/
```

区别：

| 放置位置 | 用途 |
| --- | --- |
| `ComfyUI/input/` | 给 ComfyUI 的 `LoadImage` 节点读取。 |
| `wan22-first-project/inputs/` | 给你自己归档，证明项目用了哪张图。 |

## 第 7 步：拖入课程 JSON

本章使用：

```text
docs/assets/workflows/wan22/video_wan2_2_5B_ti2v.json
```

操作：

1. 打开 ComfyUI 页面。
2. 从文件管理器里拖住这个 JSON。
3. 松手放到 ComfyUI 画布中间。
4. 等节点加载完成。
5. 把这个 JSON 也复制到你的项目目录：

```text
wan22-first-project/workflows/video_wan2_2_5B_ti2v.json
```

如果你用软件内模板入口，也可以搜索 `Wan2.2`。但不同版本界面入口可能变化，所以课程优先使用拖入 JSON。

## 第 8 步：第一次只改这些输入

拖入 JSON 后，只改下面几项：

| 输入项 | 节点 | 第一次怎么填 |
| --- | --- | --- |
| 参考图 | `LoadImage` | 选择 `05-input-starter-product.png`。 |
| 正向提示词 | `CLIP Text Encode (Positive Prompt)` | 填本章给出的产品提示词。 |
| 负向提示词 | `CLIP Text Encode (Negative Prompt)` | 保留默认；如果为空，填基础负向词。 |
| 宽高/帧数 | `Wan22ImageToVideoLatent` | 8GB 用 `512 x 288`、`33` 帧；12GB 用 `640 x 360`、`49` 帧。 |
| seed/steps/cfg | `KSampler` | 把 seed 随机化模式切到固定，记录 seed 数字；steps 12-20；cfg 4-6。 |

正向提示词：

```text
a black futuristic product on a dark desk, slowly rotating, blue rim light, slow camera push-in, cinematic close-up
```

基础负向提示词：

```text
text, watermark, logo, blurry, low quality, distorted shape, extra objects, flickering
```

## 第 9 步：点击运行

点击右上角蓝色“运行”按钮，或使用快捷键：

| 平台 | 快捷键 |
| --- | --- |
| macOS | `Cmd + Enter` |
| Windows / Linux | `Ctrl + Enter` |

运行后只会有两类结果：

| 结果 | 你要做什么 |
| --- | --- |
| 成功生成 | 打开 `ComfyUI/output/`，把最新视频复制到 `wan22-first-project/outputs/`。 |
| 失败报错 | 截图保存到 `wan22-first-project/screenshots/`，把错误原文写入 `notes/run-log.md`。 |

## 第 10 步：填写第一次运行记录

不要临时新建一个简化记录表。复制模板项目后，直接填写 `notes/run-log.md` 里的完整字段。第一次至少要填这些项目：

| 字段 | 为什么必须填 |
| --- | --- |
| 系统 / GPU / 显存 | 判断本次结果能否迁移到其他机器。 |
| ComfyUI、Python、PyTorch、CUDA/MPS 版本 | 排查跨版本差异。 |
| 工作流文件 hash | 确认不是另一个 JSON。 |
| 模型文件与 hash | 确认模型文件完整且一致。 |
| seed 和随机化模式 | 只填 seed 数字不够，必须说明是固定还是随机。 |
| 采样器、scheduler、steps、cfg、fps | 复现采样和导出条件。 |
| 输出媒体元数据 | 记录时长、分辨率、编码和文件大小。 |
| 错误原文、处理动作、复测结论 | 让失败也能复盘。 |

## 如果你现在仍不知道该做什么

按这个最短路径做，不要继续读后面的章节：

1. 打开 `http://127.0.0.1:8000/`。
2. 创建 `wan22-first-project/` 项目文件夹。
3. 下载 5B 的 3 个模型文件并放进对应 `models/` 子目录。
4. 把 `05-input-starter-product.png` 放进 `ComfyUI/input/`。
5. 拖入 `video_wan2_2_5B_ti2v.json`。
6. 选择图片，填提示词，降到低分辨率。
7. 点击“运行”。
8. 成功就复制输出，失败就截图和记录错误。

完成这 8 步后，再回头读第 1-5 章。

## 参考来源

- [ComfyUI 官方 Wan2.2 原生工作流教程](https://docs.comfy.org/tutorials/video/wan/wan2_2)
- [Comfy-Org/Wan_2.2_ComfyUI_Repackaged 模型仓库](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)
- [ComfyUI Wan2.2 示例页](https://comfyanonymous.github.io/ComfyUI_examples/wan22/)
- [ComfyUI 模型目录说明](https://docs.comfy.org/development/core-concepts/models)
- [ComfyUI comfy-cli 文档](https://docs.comfy.org/comfy-cli/getting-started)
- [Hugging Face hf CLI 文档](https://huggingface.co/docs/huggingface_hub/main/en/guides/cli)
- [aria2 官方手册](https://aria2.github.io/manual/en/html/)
