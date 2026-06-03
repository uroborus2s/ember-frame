# 《断航故土》鹿弥角色资产 QC

Date: 2026-06-03

Scope: 鹿弥多状态角色板。

## Final Asset

| Asset ID | File | Status |
|---|---|---|
| `character_lu_mi_multi_state_board_v01` | `project/severed-homeland/assets/characters/character_lu_mi_multi_state_board.png` | pass |

## QC Checks

| Check | Result | Notes |
|---|---|---|
| Character identity | pass | 角色读作约 20 岁的美丽霜蹄鹿族贵族年轻萨满，不是儿童、贫寒萨满或普通人类。 |
| Beastfolk anatomy | pass with note | 鹿耳、短角/骨金角饰清楚可读。后续 Prompt Room 仍应强调鹿耳和短角属于半兽人本体特征，不是普通头饰。 |
| Three-state continuity | pass | 北境贵族雪装、寻灾源行装、霜蹄祭仪装共享同一面部、耳角、冰蓝服装、皮草与道具体系。 |
| Costume system | pass | 珍稀白色皮草、冰蓝厚织内层、骨白长袍、银线、青玉扣、极光绿珠串和骨金饰符合角色 Bible。 |
| Fixed props | pass | 骨笛、雪地药草袋、青玉/珠串和小型冰蓝火器皿均可读。 |
| Northern color system | pass | 雪白、冰蓝、骨白、银灰、青玉绿为角色核心，枯草黄、兽皮暗棕和暗血绳作为北境局部，不与边墙灰或清明白混淆。 |
| Wanshou badge rule | pass | 未重画北境万兽联盟徽章，也未生成鹿弥个人家徽、胸章、旗帜或现代 logo；符号停留在角枝纹、骨木、绳结、珠饰和器物层面。 |
| Low-magic boundary | pass | 冰蓝火为小范围萨满/生存火，没有攻击法术、大法阵或高魔光效。 |
| Text/watermark | pass | 未见可读文字、标签、UI 或水印。 |
| History hygiene | pass | 本轮未保留拒绝版本，canonical 输出路径只存放最终图。 |

## Handoff Notes

Prompt Room 应使用 `character_lu_mi_multi_state_board_v01` 作为第 09 集及后续北境线鹿弥的主角色参考。单镜头中必须保留鹿耳/短角、贵族皮草、冰蓝内层、骨笛、药草袋、青玉扣和小范围冰蓝火；如需使用北境阵营符号，只能引用既有万兽系统的骨木绳结和角枝纹语言，不得生成新的鹿族徽章或个人 crest。
