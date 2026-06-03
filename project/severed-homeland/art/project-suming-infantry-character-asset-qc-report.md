# 《断航故土》肃明虫族小兵角色板 QC 报告

日期：2026-06-03  
批次：`project_suming_infantry_character_v01`  
资产：`character_suming_insect_infantry_multi_state_board_v01`

## 1. 输出文件

| 类型 | 路径 | 状态 |
| --- | --- | --- |
| 最终角色板 | `project/severed-homeland/assets/characters/character_suming_insect_infantry_multi_state_board.png` | PASS |
| 美术方向 | `project/severed-homeland/art/project-suming-infantry-character-art-direction.md` | PASS |
| 资产清单 | `project/severed-homeland/art/project-suming-infantry-character-asset-manifest.json` | PASS |
| 角色设计 | `project/severed-homeland/art/project-suming-infantry-character-designs.json` | PASS |
| 图像提示词 | `project/severed-homeland/prompts/project-suming-infantry-character-image-prompts.json` | PASS |
| 线程计划 | `project/severed-homeland/art/project-suming-infantry-character-thread-plan.json` | PASS |
| 线程结果 | `project/severed-homeland/art/project-suming-infantry-character-thread-results.json` | PASS |
| 资产索引 | `project/severed-homeland/art/project-suming-infantry-character-asset-index.json` | PASS |

## 2. 图像 QC

| 检查项 | 结果 | 说明 |
| --- | --- | --- |
| 非人形虫族步兵 | PASS | 主体为低伏虫族体态、复眼、护颚、反关节腿和爪足，不是人类穿甲。 |
| 小兵阶层 | PASS | 体量和姿态低于厉螳，未出现指挥令牌、将领姿态或高阶背甲系统。 |
| 与白翳区分 | PASS | 无高筒官帽、虫蜡白官袍、白册、虫蜡针或近人形上层官员轮廓。 |
| 三状态可读性 | PASS | 封村巡逻、押运 / 粮仓守门、追捕突进三种用途明确。 |
| 服装系统 | PASS | 通过甲壳、旧铁束具、虫蜡白绑带、暗绿绳带和小牌体现基层军务，不是完整布衣制服。 |
| 徽章连续性 | PASS WITH NOTE | 小牌和蜡印只作为锁定“白翅覆黑日”徽章的微型物理引用。后续提示词不得把这些小牌当作新徽章或放大重画。 |
| 文字 / UI | PASS | 图片内部未见可读标签、字幕、UI 或水印。 |
| 低魔风格 | PASS | 画面以写实甲壳、旧铁、虫蜡和黑石材质为主，无高魔法阵或科幻机甲。 |

## 3. 文件 QC

- JSON 文件均为项目级新文件，没有覆盖既有白翳、厉螳、核心角色或徽章文件。
- 图像原始生成缓存保留在 `/Users/uroborus/.codex/generated_images/019e8961-1934-7861-9a01-7eb5697df620/ig_02f92d126e639932016a1f14edbe088197a9fc06c348f8fe46.png`。
- 项目最终图像已复制到 `project/severed-homeland/assets/characters/character_suming_insect_infantry_multi_state_board.png`。
- 当前无 retained intermediate，因此 `history_files` 为空。

## 4. 下游建议

Prompt Room 后续引用 `character_suming_insect_infantry_multi_state_board_v01` 时，应把它作为肃明基层清剿队、粮仓守门、押运与追捕镜头的稳定视觉锁。镜头级提示词应继续强调：

- 只使用既有肃明 / 清明院徽章作为微型物理引用；
- 两到三只小兵即可形成封锁感，避免怪物潮；
- 小兵不能越级成厉螳，也不能变成白翳式上层虫族官员；
- 不把虫蜡白绑带误画成完整人类布衣或制服。

