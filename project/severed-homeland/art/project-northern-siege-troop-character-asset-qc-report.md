# 《断航故土》北境攻城兵种通用角色板 QC 报告

日期：2026-06-03  
批次：`project_northern_siege_troop_character_v01`  
资产：`character_northern_siege_troop_multi_state_board_v01`

## 1. 输出文件

| 类型 | 路径 | 状态 |
| --- | --- | --- |
| 最终角色板 | `project/severed-homeland/assets/characters/character_northern_siege_troop_multi_state_board.png` | PASS |
| 历史归档 | `project/severed-homeland/assets/characters/history/character_northern_siege_troop_multi_state_board.v001.png` | ARCHIVED |
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
| 四个可识别建模 | PASS | 黑牙破门、铁角盾墙、雪獾掘地、雪羽攀墙四个模型体型、脸部、工具和服装逻辑均有差异。 |
| 服装系统 | PASS | 骨片、旧木、兽皮、厚毛、绳结、暗血誓绳、旧铁和黑石雪尘形成统一北境攻城装备语言。 |
| 兵种职能 | PASS | 破门斧/槌、骨铁盾、黑石楔/骨铲/呼吸囊、爪钩/绳索/羽纹臂披均可读。 |
| 徽章连续性 | PASS | 最终图未出现大型墙面、盾面、旗帜或胸章式新徽章；只保留骨木、绳结和工具材质语言。 |
| 与鹿弥区分 | PASS | 没有贵族萨满皮草、骨笛主身份、青玉扣或精致贵族轮廓。 |
| 与灰墙军 / 肃明虫族区分 | PASS | 未出现人族守墙军制服、旧日月甲片、虫蜡白制度绑带、黑绿甲壳或清明白翅覆黑日系统。 |
| 文字 / UI | PASS | 图片内部未见可读标签、字幕、UI 或水印。 |
| 低魔风格 | PASS | 画面以写实骨木皮草、黑石雪线和低量冰蓝火为主，无高魔法阵或科幻甲胄。 |

## 3. 迭代记录

- `v001` 已移入 `assets/characters/history/`，原因是第一版存在过大的墙面符号和盾面纹样，可能被误读为重新设计北境万兽徽章。
- 最终版重新生成，背景和盾面去除大型标志，只保留小型骨木、绳结、工具和材质语言。
- 当前无 retained intermediate 留在 canonical 路径外；最终路径只保留确认版。

## 4. 文件 QC

- 新增文件均为 `project-northern-siege-troop-character-*` 批次，没有覆盖既有徽章、全局风格板、色彩板、鹿弥角色板或其他角色资产。
- 图像原始生成缓存保留在 `/Users/uroborus/.codex/generated_images/019e8b56-3c88-7102-ac61-d9d3aba920ac/ig_07ee11ed0cfdbe52016a1f96496ba481959c0103791778e4e8.png`。
- 项目最终图像已复制到 `project/severed-homeland/assets/characters/character_northern_siege_troop_multi_state_board.png`。

## 5. 下游建议

Prompt Room 后续引用 `character_northern_siege_troop_multi_state_board_v01` 时，应把它作为北境攻城线的通用角色建模锁。镜头级提示词应继续强调：

- 不重新设计北境万兽联盟徽章；
- 每个兵种必须保留各自物种比例和职能装备；
- 小队镜头使用少量可识别兵种即可，不做怪物潮；
- 冰蓝火只作为低量生存火或工具光，不做攻击法术；
- 若出现万兽体系，只用小型骨木誓结、绳结、工具刻片或盾背挂件，不放大成新徽章。
