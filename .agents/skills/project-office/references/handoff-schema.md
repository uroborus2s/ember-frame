# 交接索引结构

交接索引放在隐藏目录，避免根目录变成项目管理文件堆：

```text
.project/handoff-index.json
```

建议结构：

```json
{
  "project_id": "severed-homeland",
  "updated_at": "YYYY-MM-DD",
  "handoffs": [
    {
      "handoff_id": "H001",
      "source_department": "story-original",
      "target_department": "screenwriting",
      "episode_id": "01",
      "files": [],
      "status": "locked",
      "quality_gate": "passed",
      "risks": [],
      "blocked_items": []
    }
  ]
}
```

返工记录放在：

```text
.project/revision-log.jsonl
```

每行建议结构：

```json
{
  "issue_id": "REV-0001",
  "detected_by_department": "director-room",
  "root_cause_department": "screenwriting",
  "failure_type": "needs_script_fix",
  "affected_episode": "01",
  "affected_scene": "SC004",
  "affected_shot": "SC004-SH003",
  "evidence": "转场缺少因果，观众不知道沈维桑为何回头",
  "required_fix": "补清人物目标和动作触发",
  "status": "needs_fix"
}
```

交接和返工记录只负责追溯，不直接进入部门正式文档。部门正式文档只保留当前下游需要执行的结论。

