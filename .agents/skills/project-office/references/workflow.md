# 项目办公室工作流

## 一、初始化

1. 读取项目根。
2. 读取 `references/project-management-standard.md` 作为模板。
3. 在项目根目录创建或更新 `project-management.md`。
4. 在项目根目录创建或更新 `project-spec.md`，记录图片、视频、音频、字幕和最终交付规格。
5. 确认 `project-management.md` 前部有部门阅读索引，说明每个部门只需读取哪些小节。
6. 扫描现有部门目录。
7. 确认每个部门是否有一个当前正式输出文档。
8. 确认每个部门是否使用 `.work/` 和 `.history/` 隐藏过程目录。
9. 建立或检查隐藏项目目录 `.project/`。
10. 建立轻量部门交接索引。
11. 仅在需要时建立 episode / shot / asset / audio 状态台账。
12. 检查根目录是否只保留当前生产入口、`project-management.md`、`project-spec.md` 和长期复用记忆。

## 二、每轮 / 每个关口检查

项目办公室不做无意义的每日填表。默认在部门交接、单集完成、重大返工、成片交付前进行检查。

检查：

- 哪些部门完成；
- 哪些部门等待上游；
- 哪些素材被拒绝；
- 哪些文件被误放；
- 哪些下游引用了失败素材；
- 哪些返工没有关闭。
- 根目录是否出现过程噪音；
- `project-management.md` 的索引是否仍然准确、简洁；
- `project-spec.md` 的最终成果规格是否仍然准确、没有被过程讨论污染；
- `project-memory.md` 是否需要整理、合并或删减。

## 三、交接检查

每次部门交接必须有：

```text
source_department
target_department
handoff_files
status
quality_gate
known_risks
blocked_items
approval_owner
```

交接记录写入 `.project/handoff-index.json`。部门正式文档里只保留下游需要看的结论，不堆过程表格。

## 四、阻塞处理

阻塞项必须分类：

```text
story
screenwriting
director
art
voice
music
prompt
video
edit
delivery
config
tooling
```

项目办公室只分流，不替部门解决专业问题。

## 五、项目记忆整理

触发时机：

- 每完成一次部门交接，检查是否有候选经验；
- 每完成一集，做一次轻总结；
- 每次重大返工后，必须检查是否产生长期经验；
- 每季完成后，做一次完整复盘。

整理原则：

- 不把 `project-memory.md` 当日志追加；
- 每次整理都要读旧记忆，合并重复，删除过时，改写含糊条目；
- 只保留能指导未来生产的结论；
- 来源过程文件留在 `.work/`、`.history/` 或 `.project/`，根目录只放压缩后的长期规则。

