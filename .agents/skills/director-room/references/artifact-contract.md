# 导演部门 Artifact 契约

每个员工子任务返回一个结构化 envelope。员工产物默认是候选执行稿，可能进入导演部当前正式包根目录中的包索引、分镜文件内容草案，或项目办公室指定隐藏工作区中的后台材料。总导演代理负责检查、评分、返工、签署和单包装配。

员工不得自行写共享文件。员工不得把自己的内容草案发布成独立明面正式文件，也不得宣布自己的工作已经完成。明面正式包按“季 -> 集 -> 分镜组 -> 分镜文件”组织，每个分镜一个完整文件；不得按运镜、动作、人物、场景、光影、声音、转场、连续性或 QC 拆分文件。

## Envelope

```json
{
  "status": "success",
  "summary": "一句话说明本员工提交了哪个候选执行稿。",
  "director_order_ref": "本轮总导演命令或签署要求的简短引用",
  "artifacts": [
    {
      "path_role": "director_package.season.<season_id>.episode.<episode_id>.group.<storyboard_group_id>.storyboard.<storyboard_id>",
      "kind": "markdown",
      "content": "# <storyboard-id>\n..."
    }
  ],
  "next_actions": ["cinematographer-agent"],
  "warnings": [],
  "handoff": {
    "main_output_role": "director_package",
    "section": "分镜文件",
    "assumptions": [],
    "quality_notes": [],
    "needs_director_signature": true,
    "blocked_questions": []
  }
}
```

## 状态值

- `success`：候选执行稿可进入总导演评审，但不代表完成。
- `warning`：内容草案可评审，但存在风险；总导演代理必须保留风险并纳入评分。
- `blocked`：缺少导演启动包、必需输入、配置或事实，员工无法继续。

## Artifact 规则

- `path_role` 是逻辑位置，不是文件路径。实际写入路径由项目办公室导演启动包决定。
- 正式输出只允许装配成一个导演部当前正式包根目录。
- `path_role` 应优先指向包索引或具体分镜文件，例如 `director_package.season.<season_id>.episode.<episode_id>.group.<storyboard_group_id>.storyboard.<storyboard_id>`。
- Markdown 用于包索引、分镜文件、交接摘要、导演 QC 和最终对下游说明。
- JSON/YAML 只作为隐藏工作区或契约指定附录使用，不得默认散落在明面目录。
- 员工输出不得包含绝对路径；总导演代理根据项目办公室启动包使用实际路径。
- artifact 内容必须完整到可以进入总导演审判，并在签署后被装配进导演部正式包。
- 写入具体分镜的 artifact 必须能并入单个 `<storyboard-id>.md`，不能只是一份独立的“运镜文件”“人物文件”“场景文件”或“光影文件”。
- 不得重写源剧本、角色设定、场景设定、连续性报告或评分报告。
- 不得输出最终提示词、ComfyUI 工作流、模型配置、渲染登记、音频清单、剪辑决定表或交付文件。
- 若产物涉及后续生产需求，只记录导演要求和验收标准，不把占位路径伪装为 ready 资产。

## 必需交接字段

- `main_output_role`：固定为 `director_package`，除非项目办公室启动包另有命名。
- `section`：本员工负责的包索引、分镜文件部分或隐藏工作材料名称。
- `assumptions`：本员工做出的具体假设。
- `quality_notes`：本员工发现的风险、取舍或优势。
- `needs_director_signature`：固定为 `true`，表示员工提交稿必须经过总导演签署才算完成。
- `blocked_questions`：仅在 `status` 为 `blocked` 时填写；缺少固定必需输入时不要提问，直接报错。

## 评审 Envelope

总导演代理对每个员工内容草案生成评审记录。评审记录写入项目办公室指定隐藏工作区或项目办公室返工索引，不进入明面正式包。

```json
{
  "agent": "shot-planner-agent",
  "section": "分镜组与分镜文件",
  "attempt": 2,
  "status": "needs_revision",
  "score": 91,
  "threshold": 90,
  "director_signature": "rejected",
  "checks": [
    {"name": "director_order", "status": "needs_revision"},
    {"name": "source_refs", "status": "passed"},
    {"name": "director_intent", "status": "passed"}
  ],
  "revision_request": ["分镜顺序虽然完整，但没有体现总导演要求的观众误判路径。"],
  "reviewer_notes": ["评分达线不等于签署，退回同一员工重做。"]
}
```

评分未达标时，`status` 为 `needs_revision`，`revision_request` 必须足够具体，便于同一员工返工。评分达标但 `director_signature` 为 `rejected` 时，同样必须返工；只有 `director_signature` 为 `approved` 时，员工产物才算完成。
