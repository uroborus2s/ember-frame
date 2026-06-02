# P1 核心角色精修计划

项目：《断航故土》

范围：项目级 P1 核心角色，不包含分集专属参考帧或镜头覆盖图。

## 本轮目标

1. 将 P1 核心角色从 `usable` 推进到 `recommended` 或 `recommended_refined`。
2. 把 v3 昭明/肃明徽章自然融合进角色道具、内层纹样、旧甲磨损压痕和官署标识。
3. 修正“人族贫民服装都像破布”的问题。角色可以穿粗布、旧衣、补丁、蒙尘、焦痕和修补线，但不能统一做成破烂乞逃者。
4. 用服装剪影区分职业与社会位置：猎户、流亡皇族、清明监察者、村童、墙下混裔、边军老军户。

## 服装差异锁

| 角色 | 服饰职业信息 | 禁止方向 |
|---|---|---|
| 沈维桑 | 平民猎户。灰褐短打、皮护腕、弓箭、短刀、陷阱绳、路线小包、肩肘补强。 | 不要王者铠甲；不要通用破布流民；不要大面积撕裂下摆。 |
| 晏南枝 | 流亡皇族公主。流亡态为紫色/冷灰色清冷整洁外袍，旧帝国标识和月白玉片隐蔽收纳；身份态另备旧帝国鲜艳华丽明式汉服参考，红线束发。 | 流亡态不要外露旧帝国标识；不要衣衫褴褛；不要乞逃者；不要把流亡态画成完整宫廷礼服或皇冠。 |
| 白翳 | 虫族清明院监察者。沿用 `char_bai_yi_v01` 的官帽官服方向：高筒清明官帽、无尘白色官袍、骨白硬领、垂带、几丁质面部、复眼、薄翼披肩、虫蜡针、白册、v3 肃明小徽。 | 不要 `char_bai_yi_v02` 的“人戴面具”方向；不要摘掉官帽；不要黑甲武将；不要丢失虫族特征；不要写实昆虫翅膀标本。 |
| 沈照眠 | 平民孩童/清明识别者。村童短襦、围裙或药屋帮工小袋、烧焦发绳；清明状态为白色童袍和虫蜡手环。 | 不要成人破布缩小版；不要把清明状态画成反派华服。 |
| 陆青砾 | 墙下混裔少女。灰蓝短袄、隐藏口袋、黑市木牌、碎陶护符、窄刀、绳结。 | 不要猎户装；不要通用贫民破布；混裔特征不能奇观化。 |
| 薛临墙 | 边军老军户。祖传旧铠甲、厚衬袄、灰墙军布层、骨哨、长枪、雪线绑腿；日月合徽只能是旧甲片上的严重磨损压痕。 | 不要整洁帝国军官；不要纯破布；不要把日月标识画成腰间布条、旗条或清晰外露徽章。 |

## 新推荐输出路径

| 角色/板 | 输出路径 | 状态目标 |
|---|---|---|
| 沈维桑 v03 | `assets/characters/v03/char_shen_weisang_v03_sheet.png` | recommended_refined |
| 晏南枝 v04 | `assets/characters/v04/char_yan_nanzhi_v04_sheet.png` | recommended_refined |
| 白翳 v03 | `assets/characters/v03/char_bai_yi_v03_sheet.png` | symbol_locked_composite_reference |
| 白翳 v04 | `assets/characters/v04/char_bai_yi_v04_sheet.png` | recommended_refined |
| 沈照眠 v02 | `assets/characters/v02/char_shen_zhaomian_v02_sheet.png` | recommended_refined |
| 陆青砾 v02 | `assets/characters/v02/char_lu_qingli_v02_sheet.png` | recommended_refined |
| 薛临墙 v02 | `assets/characters/v02/char_xue_linqiang_v02_sheet.png` | recommended_refined |
| P1 服装区分总板 | `assets/costumes/v01/p1_costume_role_differentiation_v01.png` | recommended |

## QC 标准

- 角色年龄、性别、体态和固定道具必须符合 `bible/character-visual-locks.json`。
- 昭明徽章只使用“日轮托白月”合徽：月白弧月在磨损金日轮内部。
- 肃明徽章只使用“白翅覆黑日”：抽象白翅覆盖带冷白/暗灰日晕的黑日，月纹被抹去。
- 白翳自然精修新稿必须以 `assets/characters/v01/char_bai_yi_v01_sheet.png` 的官帽官服虫族监察者设计为基础：高筒官帽、垂带、白色官袍、薄翼披肩、面甲、复眼、白册和虫蜡针都要保留；以 `assets/characters/v03/char_bai_yi_v03_sheet.png` 只作为 v3 肃明徽章位置/规则参考；`char_bai_yi_v02` 废弃，不作为形象参考。
- 服装可以有补丁、修补线、尘土和局部焦痕，但不能破成流苏或乞讨式碎布。
- 六名 P1 角色并排看时，职业和社会位置必须通过服装一眼区分。
