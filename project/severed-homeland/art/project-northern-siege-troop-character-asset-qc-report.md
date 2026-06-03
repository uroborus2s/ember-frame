# 《断航故土》北境攻城兵种通用角色板 QC 报告

日期：2026-06-03  
批次：`project_northern_siege_troop_character_v02`  
资产：`character_northern_siege_troop_multi_state_board_v02`

## 1. 输出文件

| 类型 | 路径 | 状态 |
| --- | --- | --- |
| 最终角色板 | `project/severed-homeland/assets/characters/character_northern_siege_troop_multi_state_board.png` | PASS |
| 历史归档 | `project/severed-homeland/assets/characters/history/character_northern_siege_troop_multi_state_board.v001.png` | ARCHIVED |
| 历史归档 | `project/severed-homeland/assets/characters/history/character_northern_siege_troop_multi_state_board.v002.png` | ARCHIVED |
| 美术方向 | `project/severed-homeland/art/project-northern-siege-troop-character-art-direction.md` | PASS |
| 资产清单 | `project/severed-homeland/art/project-northern-siege-troop-character-asset-manifest.json` | PASS |
| 角色设计 | `project/severed-homeland/art/project-northern-siege-troop-character-designs.json` | PASS |
| 图像提示词 | `project/severed-homeland/prompts/project-northern-siege-troop-character-image-prompts.json` | PASS |
| 线程计划 | `project/severed-homeland/art/project-northern-siege-troop-character-thread-plan.json` | PASS |
| 线程结果 | `project/severed-homeland/art/project-northern-siege-troop-character-thread-results.json` | PASS |
| 资产索引 | `project/severed-homeland/art/project-northern-siege-troop-character-asset-index.json` | PASS |

## 2. 图像 QC

| 检查项 | 结果 | 说明 |
| --- | --- | --- |
| 八个模板完整性 | PASS | 黑牙破门、铁角盾墙、白鬃雪狼骑、雪獾掘地、灰皮拖城巨魔、雪羽攀墙、霜蹄梦笛祭兵、赤鬃督战骑兵均已进入最终图。 |
| 物种体型差异 | PASS | 重步兵、牛族盾兵、狼骑、雪獾工兵、巨魔、鸟族攀墙、鹿族祭兵与狮裔贵族在体型、脸部和姿态上可区分。 |
| 兵种职能 | PASS | 破门斧/槌、骨铁盾、狼骑弓刀、黑石楔/骨铲、粗链拖钩、爪钩绳索、骨笛药草袋、战旗长刀均可读。 |
| 徽章连续性 | PASS | 最终图未出现大型墙面、盾面、旗帜或胸章式新徽章；只保留骨木、绳结和工具材质语言。 |
| 与鹿弥区分 | PASS WITH NOTE | 霜蹄祭兵保留萨满/鹿族气质，但其他攻城兵未套用鹿弥贵族造型。 |
| 与灰墙军 / 肃明虫族区分 | PASS | 未出现人族守墙军制服、旧日月甲片、虫蜡白制度绑带、黑绿甲壳或清明白翅覆黑日系统。 |
| 文字 / UI | PASS | 图片内部未见可读标签、字幕、UI 或水印。 |
| 低魔风格 | PASS | 画面以写实骨木皮草、黑石雪线和低量冰蓝火为主，无高魔法阵或科幻甲胄。 |

## 3. 迭代记录

- `v001` 已移入 `assets/characters/history/`，原因是第一版存在过大的墙面符号和盾面纹样，可能被误读为重新设计北境万兽徽章。
- `v002` 已移入 `assets/characters/history/`，原因是该版只包含 4 个模板，未覆盖用户确认的 8 个北境攻城兵种。
- 最终版重新生成，补齐 8 个模板，并继续去除大型标志，只保留小型骨木、绳结、工具和材质语言。

## 4. 文件 QC

- 图像原始生成缓存保留在 `/Users/uroborus/.codex/generated_images/019e8b56-3c88-7102-ac61-d9d3aba920ac/ig_07ee11ed0cfdbe52016a1f9d849798819588f6285be4cec21b.png`。
- 项目最终图像已复制到 `project/severed-homeland/assets/characters/character_northern_siege_troop_multi_state_board.png`。
- 当前 canonical 路径只保留 8 模板确认版。

## 5. 下游建议

Prompt Room 后续引用 `character_northern_siege_troop_multi_state_board_v02` 时，应把它作为北境攻城线的 8 模板角色建模锁。镜头级提示词应继续强调：

- 不重新设计北境万兽联盟徽章；
- 每个兵种必须保留各自物种比例、身高体量和职能装备；
- 小队镜头使用少量可识别兵种即可，不做兽潮；
- 冰蓝火只作为低量生存火或工具光，不做攻击法术；
- 若出现万兽体系，只用小型骨木誓结、绳结、工具刻片或盾背挂件，不放大成新徽章。
