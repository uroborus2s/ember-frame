# 原著回补工作流

当项目已经有 Bible、大纲、梗概、剧本或其他故事前提材料，但缺少完整小说原著时，使用本流程。它适用于任何故事项目，不绑定特定作品。

## 一、目标

原著回补不是把现有剧本改写成散文，也不是复制大纲。它要补齐剧本和下游制作缺失的故事源头，同时把小说本身写得好看。

必须补齐：

- 事件因果；
- 人物内心；
- 场景转场；
- 情绪推进；
- 身体行动；
- 道具意义；
- 悬念释放；
- 章节追读；
- 文学语言、气质、节奏和独特细节。

## 二、启动方式

先读取项目现场契约，再按契约读取用户已有材料，然后进行轻量交互。只追问会影响主线、人物命运、风格边界和篇幅目标的问题。

如果素材不足，先给用户一个“创作确认”：

```text
已锁定内容
原著部将主动补全的内容
需要用户确认的风险点
预计输出形态
```

用户确认后再进入正文生产。

## 三、项目现场契约与读取顺序

先读取项目根目录的 `project-management.md`，只读阅读索引中分配给故事原著部的小节。若项目现场文档不存在，或没有写清故事原著部输入准入、输出与目录契约、交接文件路径和返工入口，必须标记：

```text
blocked_needs_project_contract
```

不得在本流程中临时硬编码项目路径。所有输入、正式输出、隐藏输出、历史归档、交接文件和返工记录位置，以项目现场契约为准。

按项目现场文档读取输入准入清单：

```text
A 类：项目级故事前提源，优先用于建立原著部 Bible。
B 类：逐集 / 分篇故事回补参考，只能用于补齐 Bible 中的事件、人物和连续性缺口。
C 类：辅助参考，不能直接决定故事 canon。
D 类：默认排除，不能进入原著 Bible，除非用户明确要求并确认其故事意义。
```

剧本、导演、美术、提示词、视频、剪辑等下游材料只能帮助判断“已经生产过什么”和“哪里缺故事源头”，不能替代小说原著，也不能绕过原著部 Bible 直接成为正文 canon。

读取顺序：

```text
1. project-management.md 阅读索引与故事原著部契约
2. A 类输入
3. B 类输入
4. 必要时读取 C 类输入
5. 排除 D 类输入
```

所有外部素材必须先进入项目现场契约指定的原著部 Bible 整理流程。正文创作只能以契约指定的 `source_bible_file` 为前提。外部旧 bible、旧大纲、旧梗概、旧剧本和连续性报告不能被正文作者直接当作 canon 使用；它们必须先由 `bible-curator-agent` 归纳、去冲突、补全并写入原著部 Bible。

建立 Bible 前必须按项目现场契约指定的 `source_ledger_file` 登记素材来源。

登记字段：

```text
source_path
source_tier: A|B|C|D
used_for_bible: true|false
bible_section
imported_facts
conflicts
decision
```

## 四、原著部 Bible

交互式启动或素材读取完成后，先输出到项目现场契约指定的 `source_bible_file`。

必须写清：

- 故事核心承诺；
- 题材、风格和读者感受；
- 世界规则；
- 时代、地理和社会背景；
- 主角与关键人物；
- 人物关系和主要冲突；
- 核心事件因果；
- 主线、支线和终局方向；
- 关键场景、组织、道具；
- 必须保留内容；
- 禁止内容；
- 未确认问题。

Bible 是正文创作的唯一前提。如果创作中需要新增重大事实，先更新 `source_bible_file`；会改变用户已确认方向时，先向用户确认。

## 五、隐藏工作顺序

项目模式下，原著部只在项目现场契约指定的位置沉淀自己的成果。契约至少要给出：

```text
source_bible_file
source_ledger_file
public_novel_file
chapter_output_dir
hidden_work_dir
history_dir
adaptation_handoff_file
handoff_index_file
revision_log_file
```

旧结构、剧本目录、分镜目录、提示词目录、视频制作目录和剪辑目录都不能作为原著部活动输出区。需要追溯旧材料时，应先按项目现场契约登记、归档或迁移；未进入 `source_bible_file` 的内容不能直接进入正文。

后台材料默认写入契约指定的 `hidden_work_dir`。

### 1. 隐藏故事总纲

写清：

- 故事核心承诺；
- 主角路线；
- 对抗压力；
- 章节或集数对应关系；
- 关键反转；
- 终局兑现；
- 主题句；
- 作品气质和语言方向。

### 2. 隐藏人物内驱

每个主要人物写：

```text
外在目标
内在需求
恐惧
创伤
习惯动作
说话质地
压力下行为
禁止行为
阶段变化
文学表现关键词
```

### 3. 隐藏悬念地图

追踪：

```text
提出的问题
提出章节
误导线索
部分答案
兑现章节
对应篇章或集数
情绪后果
```

### 4. 隐藏章节索引

每章记录：

```text
chapter_id
title
source_episode
story_function
opening_hook
character_goal
external_conflict
internal_conflict
scene_anchor
turn_or_reversal
ending_hook
adaptation_value
literary_intent
```

### 5. 小说正文

对外写入项目现场契约指定的 `public_novel_file`。长篇可按契约拆入 `chapter_output_dir`。

正文文件只保留小说内容，不暴露后台结构卡、评分表、返工记录和管理说明。

正文创作采用总小说家主笔制。后台材料可以拆分，公开正文必须由总小说家统一文学判断、统一改写和最终定稿。`draft-assistant-agent` 只在长篇、卡稿或需要备选写法时生成草稿或备选段落，不得未经总小说家统一直接成为公开正文。

正文阶段只能使用：

```text
source_bible_file
hidden_outline_file
hidden_character_inner_drives_file
hidden_suspense_map_file
hidden_chapter_index_file
hidden_scene_notes_file
```

其中隐藏工作材料也必须由 Bible 推导，不得新增 Bible 之外的故事前提。

推荐正文流程：

```text
后台材料完成
  -> chief-novelist-agent 写章节文学判断
  -> 按需调用 draft-assistant-agent 生成草稿或备选段落
  -> chief-novelist-agent 统一重写公开正文
  -> story-doctor-agent 质检
  -> chief-novelist-agent 最终裁决
```

### 6. 质检和返工

每章写完后立即在隐藏目录评分。不通过就返工，不得积压到最后才总审。

隐藏评分不得只检查结构、格式和素材覆盖。必须按 `references/quality-gate.md` 同时写入模拟目标读者试读评分。内置 QC 优先使用子 agent 模拟试读；当前环境无法创建子 agent 时，才可降级为内部读者模拟。必须包括：

```text
reader_response_score
reader_response_source
reader_dropoff_risk
reader_confusion_points
reader_emotional_hits
reader_next_chapter_desire
reader_plain_language_verdict
```

子 agent 试读只能标注为 `simulated_reader_agent_feedback`，不能冒充真实人类反馈。真实读者反馈只有在用户通过交互或外部试读 / 评论 / 平台材料明确提供时，才作为附加输入纳入，不属于原著部隐藏 QC 自动生成项。如果读者感受分低于打回线，即使章节结构完整、素材回补齐全，也必须返工。

质检报告写入项目现场契约指定的隐藏质检位置。

### 7. 编剧交接

如果故事要进入编剧部，写入项目现场契约指定的 `adaptation_handoff_file`，并由项目办公室在 `handoff_index_file` 中登记交接状态、交接文件、质量门结果、已知风险和阻塞项。

这个文件服务下游部门，不作为对外小说稿的一部分。

## 六、回补原则

- 不覆盖外部项目材料，除非用户明确要求写回 canon；原著部自己的 Bible 写入项目现场契约指定的 `source_bible_file`。
- 不把失败图片、视频、提示词、剪辑结果写入原著。
- 不用剧本已有问题解释剧本问题；应暴露故事源头缺口。
- 不重新发明主线，除非 canon 自相矛盾且用户确认。
- 不绕过 `source_bible_file` 直接写正文。
- 不把多名子 agent 的段落直接拼接为公开正文。
- 不用后台拆分替代总小说家主笔。
- 优先写具体事件，不写抽象世界观。
- 流程正确但小说不好看，仍然视为未完成。

## 七、完成定义

原著回补完成必须满足：

- 项目现场契约存在，并写清原著部输入准入、输出目录、隐藏目录、交接路径和返工入口；
- `source_bible_file` 存在；
- `source_ledger_file` 存在；
- 对外小说正文存在；
- 公开正文经过总小说家统一主笔或改写；
- 所有计划章节存在；
- 每章质检通过；
- 隐藏全稿评分存在，且包含模拟目标读者试读评分和来源标注；
- `story_doctor_report_file` 存在；
- 如需进入编剧部，`adaptation_handoff_file` 存在，且项目办公室 `handoff_index_file` 已登记；
- 编剧部不需要再猜“为什么发生”。
