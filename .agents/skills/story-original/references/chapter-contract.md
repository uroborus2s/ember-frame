# 小说章节合同

正式小说章节必须先在项目现场契约指定的隐藏工作区有结构卡，再输出干净正文。结构卡服务创作和质检，不展示给普通读者。

## 一、隐藏章节元数据

写入项目现场契约指定的隐藏章节卡位置，例如契约中的 `hidden_chapter_card_file` 或 `hidden_chapter_card_dir`。不得在本合同中硬编码项目路径。

```text
hidden_chapter_card_file
```

每章隐藏卡包含：

```text
chapter_id:
title:
source_episode:
source_refs:
bible_refs:
viewpoint_character:
main_location:
story_function:
status:
literary_intent:
```

## 二、隐藏结构卡

正文前必须先明确：

```text
opening_hook:
character_goal:
external_conflict:
internal_conflict:
scene_pressure:
visible_actions:
information_release:
turn_or_reversal:
ending_hook:
adaptation_notes:
language_texture:
emotional_aftertaste:
bible_dependency:
```

`bible_refs` 和 `bible_dependency` 必须指向项目现场契约指定的 `source_bible_file` 中的前提来源。章节不得自行新增重大世界规则、人物关系、历史事件、关键道具功能或主线因果。

## 三、公开正文格式

公开章节只保留小说阅读需要的内容：

```text
# 第X章 章节名

正文……
```

不要在公开稿里附结构卡、评分、下游种子、作者解释或管理说明。若用户明确要求，也可以在正文后附极短创作说明，但不得喧宾夺主。

公开章节必须由 `chief-novelist-agent` 统一主笔、改写或最终定稿。后台子 agent 可以供料、提出备选段落和质检意见，但不得把多个子 agent 的段落直接拼接为公开章节。

## 四、正文要求

小说正文必须做到：

- 读者愿意读下一章；
- 人物欲望通过行为显露；
- 设定变成身体、道具、选择和关系上的压力；
- 场景有光、声、气味、温度、材质、地面、衣物、呼吸、距离；
- 事件能被改成镜头；
- 对白暴露人物，不替作者背设定；
- 章末留下新的压力、问题、危险、选择或情绪余波；
- 语言有节奏、有质感、有具体性，避免空泛套话；
- 至少有一个让读者记得住的动作、意象、道具或句子。
- 所有故事前提来自项目现场契约指定的 `source_bible_file`。
- 章节文风、叙述距离、人物声音和思想能量保持统一。

## 五、打回模式

出现以下情况，章节必须重写：

- 开头像百科设定；
- 没有人物目标；
- 没有可见行动；
- 只有气氛，没有冲突；
- 只有对白，没有身体行为；
- 地点切换没有因果；
- 人物选择只为剧情方便；
- 结尾没有钩子或余波；
- 语言平庸、抽象、套话严重；
- 新增 Bible 之外的重大故事前提；
- 呈现明显多人拼接感，缺少总小说家统一笔迹；
- 下游部门无法提取场景、动作、声音或情绪材料。

## 六、隐藏下游信号

每章的下游信号写入隐藏结构卡：

```text
编剧段落
导演瞬间
美术要求
配音要求
音乐要求
可见动作
```

这些不是剧本，也不是提示词，只是给下游的故事源头信号。它们不得出现在公开小说正文中，除非用户明确要求查看。
