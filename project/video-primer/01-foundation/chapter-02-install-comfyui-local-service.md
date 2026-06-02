# 第 2 章：安装 ComfyUI 与启动本地服务

> 建议时长：60-90 分钟
> 适用平台：macOS / Windows / Linux
> 本章目标：让零基础学习者完成 ComfyUI 启动，并知道每一个目录、地址、日志和截图代表什么。

## 本章你会做成什么

完成本章后，你应该能得到下面 5 个结果：

| 结果 | 成功标准 |
| --- | --- |
| ComfyUI 页面能打开 | 浏览器访问 `http://127.0.0.1:8000/`，能看到 ComfyUI 节点画布。 |
| 你知道基础目录在哪里 | 能找到 `input/`、`output/`、`models/`、`custom_nodes/`、`user/`。 |
| 你知道模型以后放哪里 | 能打开 `models/`，并看到 `diffusion_models/`、`text_encoders/`、`vae/` 等目录。 |
| 你能检查服务状态 | 能打开 `http://127.0.0.1:8000/system_stats`，看到系统、Python、PyTorch、设备信息。 |
| 你能读启动日志 | 能在日志里找到启动命令、端口和 `Python server is ready`。 |

本章在我的机器上已经完成实测：

| 项目 | 本机实测值 |
| --- | --- |
| ComfyUI 应用 | `/Applications/ComfyUI.app` |
| ComfyUI 基础目录 | `<你的 ComfyUI 基础目录>` |
| 用户目录 | `<你的 ComfyUI 基础目录>/user` |
| 输入目录 | `<你的 ComfyUI 基础目录>/input` |
| 输出目录 | `<你的 ComfyUI 基础目录>/output` |
| 服务地址 | `http://127.0.0.1:8000/` |
| ComfyUI 版本 | `0.22.3` |
| Desktop 版本 | `0.9.4` |
| Python 版本 | `3.12.12` |
| PyTorch 版本 | `2.10.0` |
| 当前设备 | `mps` |

## 第 0 步：先看最终成功画面

这是本机 ComfyUI 已经启动后的真实页面。你第一次打开时，页面里可能有不同节点，也可能是空白画布；关键是顶部能看到工作流标签、右上角能看到“运行”按钮，中间是节点画布。

![ComfyUI 浏览器首页](../assets/screenshots/chapter-02/02-01-comfyui-browser-home.png)

这张图里有一个红色错误提示“缺少 1 个所需模型”。这是正常教学素材：它说明 ComfyUI 服务已经启动，前端能打开，只是当前工作流引用的模型文件还没放好。模型文件会在第 4 章和第 5 章处理。

本章判断“启动成功”的标准不是模型能生成，而是：

1. 页面能打开。
2. 画布能显示。
3. 服务接口能返回系统状态。
4. 能找到本地目录和日志。

## 第 1 步：选择安装方式

ComfyUI 官方文档把本地安装分成 Desktop、Portable、Manual 等方式。当前课程建议初学者这样选：

| 平台 | 推荐方式 | 适合谁 |
| --- | --- | --- |
| macOS Apple Silicon | ComfyUI Desktop | 零基础、想先跑通界面的用户。 |
| Windows + NVIDIA GPU | ComfyUI Desktop 或 Windows Portable | 零基础优先 Desktop；想跟最新版或离线管理时用 Portable。 |
| Linux | Manual Installation | 熟悉终端、自部署、远程服务器用户。 |

官方系统需求说明：ComfyUI 支持 Windows、Linux 和 macOS，Desktop 当前适合 Windows 与 macOS Apple Silicon；Linux 走手动安装路径。参考：[ComfyUI System Requirements](https://docs.comfy.org/installation/system_requirements/)。

## 第 2 步：macOS Desktop 安装与启动

本节是本机实测路径，适合 Apple Silicon Mac。

### 2.1 打开应用

操作：

1. 打开 Finder。
2. 进入 `应用程序`。
3. 找到 `ComfyUI.app`。
4. 双击打开。

你应该看到：

- ComfyUI Desktop 启动。
- 应用会自动准备 Python 环境。
- 第一次启动可能会花几分钟安装依赖。
- 启动完成后，浏览器或应用窗口会显示 ComfyUI 页面。

本机应用路径：

```text
/Applications/ComfyUI.app
```

### 2.2 确认服务地址

ComfyUI Desktop 会在本机启动一个网页服务。本机实测地址：

```text
http://127.0.0.1:8000/
```

操作：

1. 打开 Chrome、Edge 或 Safari。
2. 在地址栏输入 `http://127.0.0.1:8000/`。
3. 按回车。

成功后你会看到 ComfyUI 画布，类似本章第 0 步截图。

如果打不开：

| 现象 | 处理 |
| --- | --- |
| 浏览器提示无法连接 | ComfyUI 可能还没启动完成，等 30-60 秒再刷新。 |
| 仍然无法连接 | 打开日志，找是否出现 `Python server is ready`。 |
| 端口被占用 | 第 7 步看端口排查。 |

## 第 3 步：Windows Desktop 安装与启动

本节给 Windows 用户照做。由于本机是 macOS，本节截图会在后续 Windows 实测时补充；但步骤和成功标准是一样的。

### 3.1 安装前检查

你需要先确认三件事：

| 检查项 | 怎么看 |
| --- | --- |
| Windows 版本 | `设置 -> 系统 -> 关于` |
| NVIDIA GPU | `任务管理器 -> 性能 -> GPU` |
| 显卡驱动 | 打开 PowerShell，输入 `nvidia-smi` |

PowerShell 输入：

```powershell
nvidia-smi
```

成功时你会看到显卡型号、驱动版本、显存占用。
如果提示找不到命令，先安装或更新 NVIDIA 驱动。

### 3.2 启动 ComfyUI Desktop

操作：

1. 从 ComfyUI 官方下载页安装 Desktop。
2. 安装完成后，从开始菜单打开 ComfyUI。
3. 等待依赖初始化。
4. 打开浏览器访问 `http://127.0.0.1:8000/`。

成功标准：

- 页面能打开。
- 右上角能看到运行按钮。
- 如果页面里出现模型缺失错误，不影响本章通过。

### 3.3 Windows 本章要截图什么

| 截图 | 内容 |
| --- | --- |
| Windows 系统信息 | 证明系统版本。 |
| 任务管理器 GPU 页 | 证明显卡和显存。 |
| `nvidia-smi` | 证明驱动可用。 |
| ComfyUI 首页 | 证明服务启动。 |
| ComfyUI 目录 | 证明能找到 `models`、`input`、`output`。 |

## 第 4 步：Linux 手动安装与启动

Linux 没有本章实测截图，但要掌握标准路径。官方手动安装流程包含：创建独立 Python 环境、克隆 ComfyUI、安装依赖、启动服务。参考：[ComfyUI Manual Installation](https://docs.comfy.org/installation/manual_install)。

### 4.1 创建环境

官方文档强调独立环境可以避免污染系统 Python。你可以用 Conda：

```bash
conda create -n comfyenv python=3.12
conda activate comfyenv
```

### 4.2 克隆代码

```bash
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
```

### 4.3 安装依赖

NVIDIA CUDA 用户参考官方 PyTorch 命令。当前官方文档示例为 CUDA 13.0：

```bash
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130
pip install -r requirements.txt
```

### 4.4 启动服务

```bash
python main.py --listen 127.0.0.1 --port 8000
```

成功后，终端里应该能看到类似服务启动的信息。然后打开：

```text
http://127.0.0.1:8000/
```

如果是远程服务器，先不要直接开放公网端口。优先用 SSH 隧道：

```bash
ssh -L 8000:127.0.0.1:8000 user@server-ip
```

然后在本机浏览器打开 `http://127.0.0.1:8000/`。

## 第 5 步：确认 ComfyUI 服务真的可用

打开系统状态接口：

```text
http://127.0.0.1:8000/system_stats
```

本机截图如下：

![ComfyUI system_stats](../assets/screenshots/chapter-02/02-02-comfyui-system-stats.png)

你不需要读懂所有 JSON。零基础只看 5 个字段：

| 字段 | 本机实测 | 你要理解什么 |
| --- | --- | --- |
| `os` | `darwin` | 当前系统，macOS 会显示 darwin。 |
| `comfyui_version` | `0.22.3` | ComfyUI 后端版本。 |
| `python_version` | `3.12.12` | ComfyUI 当前使用的 Python。 |
| `pytorch_version` | `2.10.0` | 深度学习运行库版本。 |
| `devices.name` | `mps` | 当前使用的计算设备。Mac Apple Silicon 常见为 `mps`。 |

如果这个页面打不开，但 ComfyUI 首页能打开，刷新再试。
如果首页和这个接口都打不开，说明服务没有真正启动。

## 第 6 步：找到基础目录

本机 ComfyUI Desktop 的基础目录是：

```text
<你的 ComfyUI 基础目录>
```

截图如下：

![ComfyUI 基础目录](../assets/screenshots/chapter-02/02-03-comfyui-base-folder.png)

你会看到这些目录：

| 目录 | 以后做什么用 |
| --- | --- |
| `.venv/` | ComfyUI 的 Python 虚拟环境。新手不要手动改它。 |
| `custom_nodes/` | 后续安装扩展节点的位置。第 22 章再讲。 |
| `input/` | 放输入图片、参考图、首尾帧等。 |
| `models/` | 放模型文件。第 4 章会详细讲。 |
| `output/` | 生成的视频和图片会出现在这里。 |
| `temp/` | 临时文件。一般不用手动管理。 |
| `user/` | 用户配置、工作流、数据库等。 |

### 6.1 你的操作

macOS：

1. 打开 Finder。
2. 按 `Shift + Command + G`。
3. 输入：

```text
<你的 ComfyUI 基础目录>
```

4. 回车。

Windows：

1. 打开资源管理器。
2. 找到 ComfyUI 安装或用户数据目录。
3. 找到包含 `models`、`input`、`output` 的目录。

Linux：

1. 进入你 `git clone` 的目录。
2. 默认是：

```bash
cd ~/ComfyUI
```

3. 确认目录：

```bash
ls
```

成功标准：你能找到 `models`、`input`、`output`。

## 第 7 步：找到模型目录

打开 `models/`：

![ComfyUI models 目录](../assets/screenshots/chapter-02/02-04-comfyui-models-folder.png)

本章不下载模型，但你必须知道后续模型放哪里：

| 目录 | 第几章会用 | 用途 |
| --- | --- | --- |
| `diffusion_models/` | 第 4-6 章 | Wan2.2 的主模型文件放这里。 |
| `text_encoders/` | 第 4-6 章 | 文本编码器放这里。 |
| `vae/` | 第 4-6 章 | VAE 文件放这里。 |
| `loras/` | 第 22 章 | LoRA 风格或角色增强文件。 |
| `checkpoints/` | 基础图像模型 | 传统 checkpoint 文件。 |
| `clip_vision/` | 图像理解相关工作流 | 某些图像条件节点会用。 |

新手最容易犯的错误是：把所有 `.safetensors` 都扔到 `models/checkpoints/`。
Wan2.2 官方工作流需要的文件不一定放在 `checkpoints/`，第 4 章会逐个列出来。

## 第 8 步：读启动日志

本机日志路径：

```text
~/Library/Logs/ComfyUI/main.log
```

日志截图：

![ComfyUI 启动日志](../assets/screenshots/chapter-02/02-05-comfyui-main-log.png)

本机日志里有几行非常重要：

```text
Successfully created virtual environment at <你的 ComfyUI 基础目录>/.venv
Server start
Running command: <你的 ComfyUI 基础目录>/.venv/bin/python ...
--listen 127.0.0.1 --port 8000
Python server is ready
```

逐行解释：

| 日志内容 | 意思 |
| --- | --- |
| `Successfully created virtual environment` | Python 环境已经创建。 |
| `Server start` | ComfyUI 准备启动服务。 |
| `Running command` | 真正启动后端的命令。 |
| `--listen 127.0.0.1 --port 8000` | 服务只监听本机，端口是 8000。 |
| `Python server is ready` | 后端已经准备好，可以打开页面。 |

如果你看到错误，不要先重装。先判断属于哪类：

| 错误位置 | 常见原因 | 处理 |
| --- | --- | --- |
| 创建虚拟环境失败 | 权限、磁盘、Python 环境问题。 | 检查磁盘空间和目录权限。 |
| 安装依赖失败 | 网络、镜像、依赖版本问题。 | 换网络或按官方手动安装命令排查。 |
| 端口启动失败 | 8000 被占用。 | 换端口或关闭占用进程。 |
| 页面打开但节点报错 | 模型文件缺失或工作流引用了不存在的模型。 | 第 4 章处理模型目录。 |

## 知识点 1：本地服务与浏览器界面

### 例子 A：成功启动的情况

输入：

```text
http://127.0.0.1:8000/
```

操作：

1. 打开浏览器。
2. 在地址栏输入上面的地址。
3. 按回车。

输出：

- 页面标题是 ComfyUI。
- 能看到节点画布。
- 右上角有“运行”按钮。
- 如果当前工作流缺模型，会出现红色错误框，但页面本身是成功打开的。

答案：这是“服务已启动，模型未准备好”的状态。本章通过，第 4 章再解决模型。

### 例子 B：服务没有启动的情况

输入同样的地址：

```text
http://127.0.0.1:8000/
```

输出：

- 浏览器提示无法连接。
- `system_stats` 也打不开。

操作流程：

1. 回到 ComfyUI 应用或终端。
2. 看日志中有没有 `Python server is ready`。
3. 如果没有，继续看错误在依赖、权限还是端口。
4. 如果端口被占用，在 macOS/Linux 输入：

```bash
lsof -nP -iTCP:8000 -sTCP:LISTEN
```

5. Windows PowerShell 输入：

```powershell
netstat -ano | findstr :8000
```

答案：这是“服务未启动或端口不可访问”的状态，先修服务，不要下载模型。

## 知识点 2：Python 环境与依赖

### 例子 A：Desktop 自动创建环境

本机日志显示：

```text
Successfully created virtual environment at <你的 ComfyUI 基础目录>/.venv
```

操作流程：

1. 打开 ComfyUI Desktop。
2. 第一次启动时等待它自动创建 `.venv`。
3. 不要手动删除 `.venv`。
4. 如果依赖安装失败，先截日志，不要重复乱点。

答案：Desktop 已经帮你管理 Python 环境，新手不要自己把依赖装到系统 Python。

### 例子 B：Linux 手动创建环境

输入：

```bash
conda create -n comfyenv python=3.12
conda activate comfyenv
python --version
```

输出应该类似：

```text
Python 3.12.x
```

操作流程：

1. 先创建环境。
2. 激活环境。
3. 再安装 PyTorch 和 ComfyUI 依赖。
4. 每次启动前确认你已经激活 `comfyenv`。

答案：手动安装的关键是“先进入正确 Python 环境，再安装依赖，再启动”。

## 知识点 3：启动日志阅读

### 例子 A：正常日志

你要找这些内容：

```text
Server start
--listen 127.0.0.1 --port 8000
Python server is ready
```

操作流程：

1. 打开日志。
2. 搜索 `Server start`。
3. 搜索 `--port`。
4. 搜索 `Python server is ready`。

答案：三项都存在，说明服务启动链路完整。

### 例子 B：异常日志

你可能看到：

```text
Address already in use
ModuleNotFoundError
No module named ...
Permission denied
```

操作流程：

| 错误 | 怎么办 |
| --- | --- |
| `Address already in use` | 端口被占用，换端口或关闭占用进程。 |
| `ModuleNotFoundError` | 依赖没有装进当前环境，重新确认虚拟环境。 |
| `Permission denied` | 目录权限不够，换用户目录或修权限。 |
| 页面红框缺模型 | 不属于安装失败，第 4 章放模型。 |

答案：日志不是给程序员专用的。新手只要能定位“端口、依赖、权限、模型缺失”四类就够了。

## 跟做实操：从零完成本章

### 操作 1：打开 ComfyUI

macOS：

1. 打开 Finder。
2. 进入 `应用程序`。
3. 双击 `ComfyUI.app`。
4. 等待 30-120 秒。

Windows：

1. 打开开始菜单。
2. 搜索 `ComfyUI`。
3. 点击启动。
4. 等待依赖初始化。

Linux：

```bash
cd ~/ComfyUI
conda activate comfyenv
python main.py --listen 127.0.0.1 --port 8000
```

### 操作 2：打开浏览器页面

输入：

```text
http://127.0.0.1:8000/
```

你应该看到 ComfyUI 画布。
保存截图到：

```text
docs/assets/screenshots/chapter-02/02-01-comfyui-browser-home.png
```

### 操作 3：打开系统状态页面

输入：

```text
http://127.0.0.1:8000/system_stats
```

你应该看到 JSON 文本。
保存截图到：

```text
docs/assets/screenshots/chapter-02/02-02-comfyui-system-stats.png
```

### 操作 4：找到基础目录

macOS 本机路径：

```text
<你的 ComfyUI 基础目录>
```

你要确认有这些目录：

```text
custom_nodes/
input/
models/
output/
temp/
user/
```

### 操作 5：找到模型目录

进入：

```text
<你的 ComfyUI 基础目录>/models
```

你要确认至少知道这三个目录后续会用：

```text
diffusion_models/
text_encoders/
vae/
```

### 操作 6：打开日志

macOS 本机路径：

```text
~/Library/Logs/ComfyUI/main.log
```

你要找：

```text
Python server is ready
```

找到它，本章实操通过。

## 本章截图清单

| 截图编号 | 文件 | 是否已实测 |
| --- | --- | --- |
| 02-01 | `02-01-comfyui-browser-home.png` | 已完成，本机 ComfyUI 首页。 |
| 02-02 | `02-02-comfyui-system-stats.png` | 已完成，本机服务状态。 |
| 02-03 | `02-03-comfyui-base-folder.png` | 已完成，本机基础目录。 |
| 02-04 | `02-04-comfyui-models-folder.png` | 已完成，本机模型目录。 |
| 02-05 | `02-05-comfyui-main-log.png` | 已完成，本机启动日志。 |

## 本章验收清单

完成下面 8 项，才能进入第 3 章：

- [ ] 能打开 `http://127.0.0.1:8000/`。
- [ ] 能打开 `http://127.0.0.1:8000/system_stats`。
- [ ] 能说出自己的 ComfyUI 基础目录。
- [ ] 能找到 `models/`。
- [ ] 能找到 `input/` 和 `output/`。
- [ ] 能找到日志文件或终端启动输出。
- [ ] 能解释“页面红框缺模型”和“服务无法连接”的区别。
- [ ] 已保存本章至少 5 张截图。

## 常见错误与排查

| 错误 | 新手常见误解 | 正确处理 |
| --- | --- | --- |
| 首页能打开但红框报错 | 以为安装失败。 | 这是工作流缺模型，不是服务失败。 |
| `127.0.0.1:8000` 打不开 | 以为要下载模型。 | 先看服务和日志，模型与端口无关。 |
| 找不到 `models` | 不知道基础目录在哪里。 | 先用 Desktop 配置或日志找到 `base-directory`。 |
| 把模型放到桌面 | 后续节点找不到模型。 | 模型必须放进 ComfyUI 能扫描的目录。 |
| 删除 `.venv` | 以为能清理空间。 | 会破坏 Python 环境，除非你明确知道如何重装。 |

## 课后练习

1. 写下你的 ComfyUI 地址。
2. 写下你的基础目录路径。
3. 写下你的模型目录路径。
4. 截图 `system_stats` 页面，并圈出系统、Python、PyTorch、设备。
5. 打开日志，复制包含 `--listen`、`--port`、`Python server is ready` 的三行。

## 下一章衔接

第 3 章会进入 ComfyUI 界面与节点图基础。你已经能打开页面，下一章要学会识别：节点、端口、连线、队列、运行按钮、缩放导航、错误提示和保存工作流。

