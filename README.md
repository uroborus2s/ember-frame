# Ember Frame

Ember Frame 是一个面向 AI 剧制作的 monorepo。仓库以项目为单位组织故事设定、分镜规划、制作教程、工作流资产和后续自动化脚本，根目录使用 `uv` 统一管理 Python 工具链。

当前仓库重点不是单一 Python 包，而是一个创作与制作资料库。根目录 `pyproject.toml` 负责提供统一的开发环境、代码质量工具和未来脚本入口；具体剧集与教程内容放在 `project/` 下。

## 项目目录

```text
project/
  neon-revenant/
  severed-homeland/
  video-primer/
```

### neon-revenant

霓虹、赛博朋克、被抛弃后归来的复仇者。

这是一个偏视觉风格驱动的 AI 剧项目，核心气质是冷色霓虹、城市废墟、义体秩序、身份背叛和归来复仇。后续可沉淀角色 Bible、世界观 Bible、单集脚本、分镜清单、镜头提示词和视觉资产。

### severed-homeland

断航、灭史、故土被切断的第二个故事。

这个项目围绕文明被篡夺、航权被摧毁、历史被重写之后，幸存者如何重新理解故土展开。当前入口文档是 [背景设定 Bible](project/severed-homeland/背景.md)。

### video-primer

面向初学者的本地 AI 视频制作教程，清晰直接。

教程以本地 ComfyUI + Wan2.2 为主线，从安装、模型准备、首次生成逐步推进到可复现的 AI 视频项目。阅读入口见 [本地 ComfyUI + Wan2.2 AI 视频影视制作教程](project/video-primer/index.md)，完整课程结构见 [课程大纲](project/video-primer/course-outline.md)。

## 根目录工具链

本仓库使用 `uv` 管理 Python 版本、虚拟环境、依赖、锁文件和开发工具执行。

常用命令：

```bash
uv sync
uv run ruff format .
uv run ruff check .
```

说明：

- 根项目通过 `[tool.uv] package = false` 声明为非打包项目，适合作为 monorepo 的工具入口。
- 当前 `project/` 下的内容项目主要是 Markdown、图片和工作流资产，不作为 Python workspace member。
- 如果后续某个子项目加入自己的 `pyproject.toml`，再把对应路径加入根目录 `[tool.uv.workspace] members`。
- Python 自动化脚本建议集中放入 `scripts/` 或具名子项目中，并通过 `uv run` 执行。
- 新增 Python 代码和测试后，再把 `uv run mypy .`、`uv run pytest` 纳入交付前检查。

## 内容协作约定

- 故事项目优先沉淀 `Bible -> 剧集大纲 -> 单集脚本 -> 分镜清单 -> 镜头提示词 -> 资产清单`。
- 教程项目优先保证读者能按步骤复现，未实测内容需要明确标注状态。
- 工作流 JSON、截图、输入图和输出样例应放在对应项目的 `assets/` 下。
- 不把 `.venv/`、缓存目录、临时输出、密钥或本地生成的大体积草稿纳入版本控制。

## 后续扩展

建议逐步补齐：

- `project/neon-revenant/` 的世界观 Bible、角色 Bible 和第一集脚本包。
- `project/severed-homeland/` 的主线大纲、角色关系、分集结构和视觉风格板。
- `project/video-primer/` 的真实生成证据、截图索引、参数记录和出版审校闭环。
- 根目录 `scripts/` 的制作流水线脚本，例如分镜表生成、提示词批处理、素材索引和交付清单校验。
