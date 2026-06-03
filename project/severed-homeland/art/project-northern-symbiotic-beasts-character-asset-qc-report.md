# 《断航故土》北境共生兽通用角色板 QC 报告

版本：v01  
日期：2026-06-03  
批次：`project_northern_symbiotic_beasts_character_v01`

## 1. 本轮范围

本轮创建项目级“北境共生兽通用多状态角色板”的规划、设计、提示词、线程计划、结果占位、资产索引与 QC 文件。目标是补齐八类北境共生兽的可复用建模：破门猛犸、岩背犀、冰湖甲龟、披甲牦牛群、地热冰蟒、裂风飞龙、冻原雷蜥和霜狼群。

## 2. 文件产出

| 类型 | 路径 | 状态 |
| --- | --- | --- |
| 美术方向 | `project/severed-homeland/art/project-northern-symbiotic-beasts-character-art-direction.md` | PASS |
| 资产清单 | `project/severed-homeland/art/project-northern-symbiotic-beasts-character-asset-manifest.json` | PASS |
| 角色设计 | `project/severed-homeland/art/project-northern-symbiotic-beasts-character-designs.json` | PASS |
| 图片提示词 | `project/severed-homeland/prompts/project-northern-symbiotic-beasts-character-image-prompts.json` | PASS |
| 线程计划 | `project/severed-homeland/art/project-northern-symbiotic-beasts-character-thread-plan.json` | PASS |
| 线程结果 | `project/severed-homeland/art/project-northern-symbiotic-beasts-character-thread-results.json` | PASS |
| 资产索引 | `project/severed-homeland/art/project-northern-symbiotic-beasts-character-asset-index.json` | PASS |

## 3. 设计覆盖检查

| 检查项 | 结果 | 说明 |
| --- | --- | --- |
| 八类兽种覆盖 | PASS | 破门猛犸、岩背犀、冰湖甲龟、披甲牦牛群、地热冰蟒、裂风飞龙、冻原雷蜥、霜狼群均有独立建模规则。 |
| 共生关系 | PASS | 每个兽种都要求出现驭兽者、吹哨者、萨满、盾兵、牵引者或对应骑手，并明确骨笛、血盐、旧伤、牵引或拒令互动。 |
| 徽章规则 | PASS | 明确不重新设计北境万兽联盟徽章，只允许小型骨木誓结、旧木刻片、血盐袋吊牌等物理引用。 |
| 全局风格与色彩 | PASS | 继续使用低魔东方史诗、北境非纯雪原、边墙到北境色彩、骨木皮草材质与黑石雪尘。 |
| 低魔边界 | PASS | 地热冰蟒只做局部热雾和城基震动；冻原雷蜥只做短促电弧；裂风飞龙不做巨龙或大空军。 |
| 服装/束具系统 | PASS | 兽皮绳、旧木、旧铁、暗血誓绳、骨笛绳、血盐袋、旧伤包扎和拖运束具形成统一北境共生兽系统。 |
| 图片文字禁令 | PASS | 提示词明确禁止文字、标签、UI、水印、中文和英文字母。 |

## 4. 图像生成状态

当前未创建后台 Codex 图像线程。原因：可用 `create_thread` 工具要求用户明确请求新线程或独立线程。本轮改用当前线程的内置 `image_gen` 生成 canonical 图像，并复制到项目资产目录。

canonical 输出路径：

`project/severed-homeland/assets/characters/character_northern_symbiotic_beasts_multi_state_board.png`

原始生成文件保留在：

`/Users/uroborus/.codex/generated_images/019e8b80-0a13-77a1-8c8b-8baaa9ed4b86/ig_0ac2d6c6dc639863016a1fa007585081958c1a1488bcaa5251.png`

文件校验：PNG，864 x 1821，RGB。视觉检查通过：画面覆盖八类共生兽及右侧细节面板，未见可读文字、UI、水印或放大的新阵营徽章。裂风飞龙未巨龙化，地热冰蟒保持局部化，冻原雷蜥电弧保持短促局部。

## 5. 风险与重试要求

如果后续生成图片，重点检查：

1. 是否把八类共生兽画成同一种怪物换角或换颜色。
2. 是否把裂风飞龙画成巨龙，或把飞龙数量画成大规模空军。
3. 是否把地热冰蟒画满屏，丢失“局部鳞片、热雾、城基震动”的约束。
4. 是否把冻原雷蜥画成科幻电兽或霓虹电浆。
5. 是否出现大徽章、新动物 crest、盾面 logo、鞍具 logo 或 sticker overlay。
6. 是否缺少驭兽者互动，导致共生兽被误读为无脑怪物或普通坐骑。

## 6. Prompt Room 交接

Prompt Room 后续引用 `character_northern_symbiotic_beasts_multi_state_board_v01` 时，应把它作为北境攻城线与鸣骨岭共生兽镜头的项目级建模锁。镜头级提示词可按兽种拆分，但必须保留体量、束具、骨笛/血盐/旧伤互动、低魔边界和“不重新设计徽章”的硬规则。
