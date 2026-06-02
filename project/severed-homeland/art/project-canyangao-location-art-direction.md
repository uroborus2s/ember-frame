# 《断航故土》残阳坳场景美术方向

版本：v01  
日期：2026-06-03  
范围：项目级主场景资产，覆盖第01集、第02集和第03集远景回望  
状态：提示词与任务计划创建中

## 1. 场景定位

残阳坳是第一季开端的主要故土场景，不是贫民窟、废墟或单纯火场。它在火前是被压榨但仍有生活秩序的农猎村，在清明复查后被肃明制度覆盖，在第02集夜火中被毁，在第03集之前只剩可识别的旧井、药屋焦梁、车辙和北坡黑石缝方向。

主场景必须同时承担三件事：

1. 建立沈维桑的生活能力来源：猎户、药屋、旧井、水缸、山坡、谷口陷阱。
2. 显示肃明/清明院的制度暴力进入生活空间：白册、虫蜡封门牌、清明香、虫族短矛和暗绿甲壳局部。
3. 为旧驿线索保留低魔证据：药柜暗格、残缺日月纹、月白一线、北坡黑石缝和半枚驿令的方向感。

## 2. 依据文件

- `project/severed-homeland/bible/scenes.md#残阳坳`
- `project/severed-homeland/art/project-style-board-low-magic-eastern-epic.md`
- `project/severed-homeland/art/project-regional-color-system.md#残阳坳`
- `project/severed-homeland/art/project-faction-symbol-system.md`
- `project/severed-homeland/art/project-base-material-boards.md`
- `project/severed-homeland/01/director/camera-plan.md`
- `project/severed-homeland/01/shots/scene-breakdown.json`
- `project/severed-homeland/02/shots/scene-breakdown.json`
- `project/severed-homeland/02/continuity/visual-continuity-bible.json`

## 3. 空间锁定

残阳坳的核心空间关系：

```text
村道 / 村民聚集区 / 村口验血席
   |
药屋台阶与门口 -- 短矛封锁线 -- 后院入口
   |                              |
罗家药屋内 / 药柜 / 暗格            水缸
                                  |
                                旧井

侧门 / 侧巷 / 水沟口 / 虫族木车
   |
谷口窄道 / 猎人滚木陷阱 / 兽道窄缝
   |
外山坡 / 车辙旁 / 北坡黑石缝方向
```

所有图像都应维护这个方向逻辑：药屋、旧井、水缸和后院必须是同一院落关系；侧巷和木车指向北侧山道；谷口兽道通向外坡；外坡回望能看见火场、旧井和药屋焦梁。

## 4. 色彩与材质

残阳坳本地底色：

- 夯土褐 `#6E563E`：土墙、村道、门槛、井边泥土。
- 晚麦金 `#B08A3C`：残阳边缘、麦束、晒谷和火前空气。
- 草药青 `#4F6B4A`：罗家药屋、草药篮、沈家生活锚点。
- 旧木褐 `#3A2B21`：药柜、弓架、门框、水桶、滚木。
- 炊烟灰：火前生活烟、夜火遮挡、火后灰烬。

权力覆盖：

- 虫蜡白 `#D8D0BC`：封门牌、虫蜡封条、白册边缘、识别环。
- 黑绿甲 `#1E2A22`：螳刃追兵局部甲壳、门口剪影、短矛握持。
- 清明冷白：清明香贴地细线，不能变成攻击法术。

旧记忆和危机点色：

- 月白一线 `#C8D7D8`：井口、水面、油纸边缘、半枚驿令断面短反光。
- 金赤暗格：药柜暗格、残缺日月方向痕、灵翼残纹短闪。
- 火场暗红 `#7F2D22`：第02集火场、焦梁、衣角和灰烬边缘。

## 5. 徽章与符号引用规则

不得重新设计阵营徽章。所有场景中的肃明/清明、昭明旧帝国痕迹必须引用现有稳定 PNG 的形体语言：

- 肃明/清明院：`project/severed-homeland/assets/style/faction-emblems/emblem_suming_qingming_state.png`
- 昭明旧帝国：`project/severed-homeland/assets/style/faction-emblems/emblem_zhaoming_empire.png`
- 北境万兽联盟本场景不应出现，除非作为全局风格参考，不进入画面主体。

场景图中允许出现的符号形态：

- 清明白翅覆黑日只能作为虫蜡封牌、白册章、短矛烙牌或远处封条痕迹。
- 昭明日月只能作为药柜暗格、旧驿方向痕、井沿湿苔间的残缺旧印或半枚驿令断纹。
- 不得出现完整、干净、英雄化的昭明大徽，也不得把肃明徽章画成普通黑日、虫形 logo 或柔软天使翼。

## 6. 构图规则

- 默认 9:16 竖屏生产参考图。
- 手机首屏必须可读：空间方向、道具锚点和权力关系不能依赖横向细节。
- 远景只用于主场景总览、火后回望和谷口方向；大部分子场景用中近景、近景、道具特写和门框遮挡。
- 不做大规模屠村全景，不做怪物潮。火灾通过饭碗、门闩、窗纸、木梁、灰、手脚、烟和声音感表现。
- 村民衣物和环境旧而完整，有职业信息，避免破布流民化。

## 7. 场景图清单

本批次建议生成 13 张图，其中 12 张为必需场景图，1 张为可选但推荐的材质陈设板。

| Asset ID | 图像定位 | 用途 |
| --- | --- | --- |
| `loc_canyangao_master_dusk_v01` | 火前主场景总览 | 锁定村道、药屋、旧井、谷口、山坡方向 |
| `loc_canyangao_master_fire_v01` | 夜火主场景总览 | 锁定火中状态与仍可识别的旧井药屋 |
| `loc_canyangao_master_aftermath_v01` | 火后回望总览 | 锁定火后旧井、药屋焦梁、北坡方向 |
| `loc_canyangao_gate_blood_check_v01` | 村口验血席 | 第01集村口清明复查 |
| `loc_canyangao_medicine_house_exterior_v01` | 罗家药屋外景 | 药屋门口、台阶、弓架、封门牌 |
| `loc_canyangao_medicine_house_interior_v01` | 罗家药屋内景 | 药柜压迫、草药篮、水罐、白翳进入后的空间 |
| `loc_canyangao_hidden_relay_compartment_v01` | 药柜暗格与旧驿痕 | 第01集旧驿线索首次清楚露出 |
| `loc_canyangao_old_well_courtyard_v01` | 后院旧井水缸 | 井口、水缸、药屋门口视线关系 |
| `loc_canyangao_well_escape_door_v01` | 井下暗门/药屋后门 | 第02集晏南枝钻出暗门与遮痕路线 |
| `loc_canyangao_side_lane_wooden_cart_v01` | 侧巷虫族木车 | 沈照眠被带走、车辙北向 |
| `loc_canyangao_valley_trap_v01` | 谷口猎人陷阱 | 滚木绳扣、兽道窄缝、追兵局部 |
| `loc_canyangao_outer_slope_rut_v01` | 外山坡车辙旁 | 回望火场、烧焦发绳、北坡黑石缝 |
| `loc_canyangao_material_dressing_board_v01` | 材质陈设板 | 统一土墙、药柜、井沿、虫蜡、灰烬和草药陈设 |

## 8. 禁忌

- 不要高饱和金色田园、仙侠村落、云海神光。
- 不要全屏黑灰火场吞掉空间关系。
- 不要现代村庄、现代医疗器械、现代木车、现代 UI。
- 不要可读文字、标签、水印、字幕或说明牌。
- 不要把虫族小兵画成人类盔甲兵；只露暗绿甲壳、窄复眼、护颚、刃肢、短矛等局部即可。
- 不要把残阳坳画成无职业信息的乞丐营地。

## 9. 下游交接

`project-canyangao-location-image-prompts.json` 负责工具中立图片提示词。`project-canyangao-location-thread-plan.json` 负责 Codex 背景线程任务拆分。Prompt Room 后续可把本批次 asset ID 作为场景底图和 reference frame 的稳定来源。
