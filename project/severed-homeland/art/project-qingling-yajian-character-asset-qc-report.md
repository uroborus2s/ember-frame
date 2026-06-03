# 《断航故土》青翎鸦见角色板 QC 报告

日期：2026-06-03  
批次：`project_qingling_yajian_character_v01`  
资产：`character_qingling_yajian_multi_state_board_v01`

## 1. 输出文件

| 类型 | 路径 | 状态 |
| --- | --- | --- |
| 最终角色板 | `project/severed-homeland/assets/characters/character_qingling_yajian_multi_state_board.png` | PASS |
| 美术方向 | `project/severed-homeland/art/project-qingling-yajian-character-art-direction.md` | PASS |
| 资产清单 | `project/severed-homeland/art/project-qingling-yajian-character-asset-manifest.json` | PASS |
| 角色设计 | `project/severed-homeland/art/project-qingling-yajian-character-designs.json` | PASS |
| 图像提示词 | `project/severed-homeland/prompts/project-qingling-yajian-character-image-prompts.json` | PASS |
| 线程计划 | `project/severed-homeland/art/project-qingling-yajian-character-thread-plan.json` | PASS |
| 线程结果 | `project/severed-homeland/art/project-qingling-yajian-character-thread-results.json` | PASS |
| 资产索引 | `project/severed-homeland/art/project-qingling-yajian-character-asset-index.json` | PASS |

## 2. 图像 QC

| 检查项 | 结果 | 说明 |
| --- | --- | --- |
| 单一角色身份 | PASS | 三个全身状态保持同一鸦族斥候体貌，不像三名不同角色。 |
| 多状态建模 | PASS | 包含北境雪羽斥候常态、攀墙割旗潜入态、寒鸦堡风雪传讯态。 |
| 个人识别锚点 | PASS | 左侧青翎、右眼旧伤、鸦族头面、羽纹臂披、骨钩、绳盘、传讯筒、短刀、遮火罐和誓绳/骨环系统可读。 |
| 服装系统 | PASS | 烟羽黑、骨白、旧铁、兽皮绳、黑石雪尘和冻土灰保持北境雪羽轻兵逻辑；衣物完整可用，没有破布流民化。 |
| 徽章连续性 | PASS | 未出现大型万兽徽章、新青翎徽章、鸦族 crest、盾面标、墙面标或旗帜 logo。青翎只读作个人羽色。 |
| 与通用雪羽斥候区分 | PASS | 个人青翎、旧伤、传讯筒和骨环/誓绳系统使她区别于通用北境攻城兵种板。 |
| 与鹿弥区分 | PASS | 未出现鹿角贵族头饰、白色贵族皮草、骨笛主身份、萨满碗火或青玉挂饰。 |
| 与灰墙军 / 肃明虫族区分 | PASS | 未出现人族守墙军制服、日月旧甲片、虫蜡白制度绑带、黑绿甲壳、清明白册或白翅覆黑日系统。 |
| 文字 / UI | PASS | 图片内部未见可读标签、字幕、UI 或水印。 |
| 低魔风格 | PASS | 画面以写实羽披、骨木皮草、绳索工具和黑石雪线为主，无高魔法阵、巨大翅膀或空军奇观。 |

## 3. 文件 QC

- 新增文件均为 `project-qingling-yajian-character-*` 批次，没有覆盖既有徽章、全局风格板、区域色彩板、鹿弥角色板、北境通用兵种板或其他角色资产。
- 最终图像尺寸为 `793 x 1983`，SHA-256 为 `1f4a3f7beef8c7b58a5c5f6f2ca4f04d9a88ca5406617d9fe982b4230de0dccc`。
- 图像原始生成缓存保留在 `/Users/uroborus/.codex/generated_images/019e8b81-7122-7181-8a07-5de746d822a8/ig_04e220c4c97190c6016a1fa07a7518819386eb3611ea8d3989.png`。
- 项目最终图像已复制到 `project/severed-homeland/assets/characters/character_qingling_yajian_multi_state_board.png`。
- 本轮无 rejected intermediate 需要归档到 `assets/characters/history/`。

## 4. 下游建议

Prompt Room 后续引用 `character_qingling_yajian_multi_state_board_v01` 时，应把它作为青翎鸦见个人建模锁。镜头级提示词应继续强调：

- 左侧青翎是个人羽色，不是徽章；
- 不重新设计北境万兽联盟徽章；
- 保留右眼旧伤、鸦族头面、羽纹臂披、骨爪钩、细绳盘、传讯筒、右臂骨环和暗血誓绳；
- 攀墙镜头以骨钩、绳索、爪足和黑石墙面为主，不做英雄飞行；
- 寒鸦堡/边墙镜头允许加雪尘、烟灰围巾和遮火小罐，但不能贵族萨满化或虫族化。
