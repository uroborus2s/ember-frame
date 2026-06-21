# 编剧部改编依据与项目办公室交接合同

故事原著部对外主交付是小说原著正文。编剧部需要的改编依据写入项目现场契约指定的隐藏交接文件，例如 `adaptation_handoff_file`。不得在本合同中硬编码项目路径。

```text
adaptation_handoff_file
```

该文件服务下游协作，不作为公开小说稿的一部分。若进入编剧部，项目办公室还必须在项目现场契约指定的 `handoff_index_file` 中登记交接记录。

## 一、必需结构

```text
# 编剧改编交接

## 原著状态
- source_complete:
- approved_for_screenwriting:
- story_doctor_report:
- public_novel_file:
- source_bible_file:
- source_ledger_file:
- chief_novelist_approved: true|false
- bible_as_single_source_of_truth: true|false

## 分集 / 篇章映射
episode_id_or_part
source_chapters
required_events
required_emotional_turns
ending_hook

## 人物锁
character_id
must_preserve
voice_seed
habitual_behavior
pressure_behavior
forbidden_behavior
literary_signature

## 场景与道具锁
scene_or_prop_id
story_function
must_preserve
allowed_compression
forbidden_change

## 对白种子
episode_id_or_part
character_id
source_line_or_phrase
subtext
usage_note

## 压缩建议
source_chapter
can_compress
can_merge_with
must_not_cut

## 未关闭风险
risk
affected_episode_or_part
recommended_screenwriting_action
```

## 二、交接规则

- 编剧部可以压缩小说，但不能抹掉关键情绪转折。
- 编剧部可以重排场次，但不能改变已锁定因果。
- 编剧部可以改写台词，但必须保留人物声音种子、潜台词和文学签名。
- 如果剧本需要改变已锁定事件，必须通过项目办公室返工入口退回故事原著部做 story repair，并由项目办公室在 `revision_log_file` 记录 `needs_story_source_fix`。
- 下游制作的失败结果不能反向污染原著。
- 公开给用户的完整稿以小说正文为主，不附本交接合同，除非用户明确要求查看。
- 编剧部的故事前提以项目现场契约指定的 `source_bible_file` 为准；小说正文、隐藏交接和后续剧本都不得绕过 Bible 新增关键 canon。
- 编剧部只能以总小说家确认后的公开小说正文为原著源头；隐藏草稿、备选段落和子 agent 供料不能被当作正式原著。

## 三、项目办公室交接索引

交接索引由项目办公室维护。原著部不得把项目管理台账塞进公开小说正文；只需确保交接所需字段可被登记：

```text
source_department: story-original
target_department: screenwriting
handoff_files: adaptation_handoff_file, public_novel_file, source_bible_file
status: approved | needs_review | blocked
quality_gate: passed | failed
known_risks:
blocked_items:
approval_owner:
```
