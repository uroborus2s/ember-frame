# 《断航故土》第01集缺失场景图生成要求

版本：v01  
日期：2026-06-03  
范围：第01集《清明香入村》在残阳坳主场景资产完成后的剩余场景/镜头参考图需求  
状态：待设计提示词与线程任务

## 1. 当前完成状态

残阳坳项目级主场景批次 `project_canyangao_location_v01` 已完成 13 张 canonical PNG：

- 火前、火中、火后三张主场景状态图。
- 村口验血席、罗家药屋外景、罗家药屋内景、药柜暗格、后院旧井。
- 井下暗门、侧巷虫族木车、谷口猎人陷阱、外山坡车辙回望。
- 残阳坳材质陈设板。

这些图片已经覆盖第01集 SC002-SC008 的主要场景需求；第01集还缺少的主要是序幕蒙太奇的三段外部/异地场景，以及两个第01集镜头级组合参考。

## 2. 高优先缺口

### 2.1 北境局部战场

Asset ID：`ref_ep01_sc001_sh002_northern_battle_fragment_v01`  
建议输出路径：`project/severed-homeland/01/assets/reference-frames/sc001_sh002_northern_battle_fragment.png`  
对应镜头：`SC001-SH002`

设计要求：

- 9:16 竖屏低机位贴雪。
- 只表现局部：铁蹄、残旗影、半埋兵器、伤兵手或背影、边墙阴影。
- 北境色彩使用冷白雪、阴影蓝、旧铁、干血暗红少量点色。
- 人族军户只给背影、手和伤兵轮廓，不出现可识别新角色正脸。
- 不做大规模战争全景、英雄冲锋、怪物潮或高魔战场。

### 2.2 金河征粮道

Asset ID：`ref_ep01_sc001_sh003_jinhe_grain_levy_road_v01`  
建议输出路径：`project/severed-homeland/01/assets/reference-frames/sc001_sh003_jinhe_grain_levy_road.png`  
对应镜头：`SC001-SH003`

设计要求：

- 9:16 竖屏近景/中近景。
- 征粮动作靠物件表达：征粮木牌、粮袋车辙、孩子空碗、虫蜡封牌、检查桌边缘。
- 群众只用手、鞋、袖口、碗和背影，不做可识别群演脸。
- 金河征粮道使用土黄粮道、湿木、粮牌暗黄、虫蜡白覆盖，不要欢乐蒸汽朋克。
- 画面不能出现现代标识、现代车辆、可读文字或 UI。

### 2.3 南方密室旧驿图桌

Asset ID：`ref_ep01_sc001_sh004_southern_secret_room_relay_table_v01`  
建议输出路径：`project/severed-homeland/01/assets/reference-frames/sc001_sh004_southern_secret_room_relay_table.png`  
对应镜头：`SC001-SH004`

设计要求：

- 9:16 竖屏近景，道具和手部为主。
- 场景元素：旧驿图桌、药包、红线卷轴、暗火、断裂日月纹、磨损金赤路线痕。
- 只拍手、地图、药包和火星，不出现新角色正脸。
- 昭明旧痕必须残缺、被遮挡或被保存，不做完整复国圣徽。
- 火星用于 match cut 到清明香，不能变成魔法爆光。

## 3. 中优先镜头级补图

### 3.1 药屋门口失言与识句记号

Asset ID：`ref_ep01_sc005_zhaomian_threshold_identification_v01`  
建议输出路径：`project/severed-homeland/01/assets/reference-frames/sc005_zhaomian_threshold_identification.png`  
对应镜头：`SC005`

设计要求：

- 在已完成的 `loc_canyangao_medicine_house_exterior.png` 基础上做镜头组合参考。
- 低机位、儿童脆弱感：门槛、沈照眠小草药袋、药名牌、短矛影子、白册边角。
- 白册边角需要给后期/Prompt Room 留出“旧驿识句”信息位，但图片生成阶段不要生成可读文字。
- 白翳压迫来自回头、白袍冷亮和白册，不做夸张反派重音或高魔效果。

### 3.2 结尾封锁线与井沿反光

Asset ID：`ref_ep01_sc008_final_spear_line_well_glint_v01`  
建议输出路径：`project/severed-homeland/01/assets/reference-frames/sc008_final_spear_line_well_glint.png`  
对应镜头：`SC008`

设计要求：

- 在已完成的 `loc_canyangao_gate_blood_check.png`、`loc_canyangao_old_well_courtyard.png` 和 `loc_canyangao_medicine_house_exterior.png` 基础上做最终镜头组合参考。
- 短矛封锁线必须同时隔断药屋与后院。
- 白翳台阶站位略高于村民，但不拍成胜利者，只拍成流程继续推进。
- 最后井沿月白反光只能是一线冷亮，不能露出井下人、完整玉片或石门线索。

## 4. 不建议生成为独立美术图

- `SC001-SH001` 黑场字幕：属于剪辑/字幕设计，不需要 Art Room 场景图。可由后期使用黑场与冷白字幕完成。
- 白册可读文字特写：当前图像生成阶段应避免生成文字。若镜头要求 `旧污疑似`、`山籍猎户` 等可读内容，建议在 Prompt Room 或后期阶段使用精确文字层处理。

## 5. 下一轮线程建议

建议生成 5 张第01集 reference-frame PNG，分 2 个线程：

1. `episode01-intro-montage-reference-v01`：北境战场、金河征粮道、南方密室三张。
2. `episode01-canyangao-shot-reference-v01`：药屋门口失言、结尾封锁线井沿反光两张。

所有图片使用 `project/severed-homeland/01/assets/reference-frames/` 作为 canonical output directory；中间图进入同级 `history/`，使用 `.v001` 后缀，不创建版本目录。
