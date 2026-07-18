DO NOT send optional commentary

# Ember Frame Agent Rules

这些规则适用于本仓库内的所有 Codex/agent 工作，优先级高于临时习惯和个人偏好。

## 技能与规则文件读取硬要求

读取 `SKILL.md`、`.agents/skills/**` 下的引用文件、项目规则、长 Markdown、中文文档时，必须遵守以下流程：

1. 必须按 UTF-8 读取。PowerShell 读取文本时使用 `-Encoding UTF8`。
2. 对长文件必须分段读取，不能依赖一次性终端输出。
3. 必须确认已经读到文件末尾。没有确认 EOF 前，视为未完成读取。
4. 如果出现乱码、截断、工具提示输出被省略、或只看到文件前半段，必须立刻重读；在完整读取前禁止继续执行该技能或规则。
5. `SKILL.md` 引用的相对路径文件也按同一标准读取，直到所需规则全部完整读完。

推荐 PowerShell 读取方式：

```powershell
Get-Content -Raw -Encoding UTF8 "C:\path\to\SKILL.md"
```

长文件分段读取方式：

```powershell
$lines = Get-Content -Encoding UTF8 "C:\path\to\SKILL.md"
$lines.Count
$lines[0..199]
$lines[200..399]
$lines[400..599]
```

如果最后一个分段没有覆盖 `$lines.Count - 1`，不得认为文件已读完。任何 agent 在发现读取不完整后，都必须先补读到最后一行，再继续任务。
