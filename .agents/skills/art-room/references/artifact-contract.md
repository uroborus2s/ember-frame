# 美术部产物契约

每个负责规划的子 agent 都返回一个结构化信封。父级 Codex 协调者检查信封后，再把文件写入磁盘。

## 信封结构

```json
{
  "status": "success",
  "summary": "一句话说明结果。",
  "artifacts": [
    {
      "path": "<project-office-designated asset-manifest path>",
      "kind": "json",
      "content": "{ \"assets\": [] }"
    }
  ],
  "next_actions": ["character-design-agent"],
  "warnings": [],
  "handoff": {
    "main_output": "<project-office-designated asset-manifest path>",
    "assumptions": [],
    "quality_notes": [],
    "blocked_questions": []
  }
}
```

## 状态值

- `success`：输出已准备好，可交给下一个 agent。
- `warning`：输出可用，但包含父级需要保留的风险。
- `blocked`：该 agent 缺少父级或用户输入，无法继续。

## 产物规则

- 只使用项目相对路径。
- 美术方向、QC 报告和人工审查笔记使用 Markdown。
- 资产清单、设计规格、提示词计划、线程计划、线程结果和资产索引使用 JSON。
- 子 agent 输出中不要包含绝对路径；由父级协调者负责解析。
- 规划子 agent 不生成图片文件。图片生成是父级协调的 Codex 后台线程步骤。
- 不要把临时 `*-audit*`、`*-review*`、`*-score*`、`*-rewrite*`、`*-after-fix*`、重试、草稿或运行专属中间文件放进明面美术目录；这些材料只能进入项目办公室指定的隐藏工作、审计或版本位置。
- 非正式产物进入固定子目录：`<project-office-designated hidden report path>` 放 QC 与审批摘要，`<project-office-designated hidden audit path>` 放一致性、可读性、改写和修复后审计，`<project-office-designated hidden review path>` 放单资产提示词审查笔记，`<project-office-designated hidden run path>` 放工作线程草稿、重试和被替换的线程计划/结果。

## 必需交接字段

- `main_output`：一个项目相对路径。
- `assumptions`：该角色做出的具体假设。
- `quality_notes`：该角色发现的风险、取舍或优势。
- `blocked_questions`：仅当 `status` 为 `blocked` 时填写问题。
