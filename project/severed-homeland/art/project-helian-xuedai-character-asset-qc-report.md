# 《断航故土》赫连雪岱角色资产 QC

Date: 2026-06-03

Scope: 赫连雪岱高级熊族护卫多状态角色板。

## Final Asset

| Asset ID | File | Status |
|---|---|---|
| `character_helian_xuedai_multi_state_board_v05` | `project/severed-homeland/assets/characters/character_helian_xuedai_multi_state_board.png` | pass |

## History

| File | Status | Notes |
|---|---|---|
| `project/severed-homeland/assets/characters/history/character_helian_xuedai_multi_state_board.v001.png` | retained rejected version | 鹿族近卫旧稿，因与霜蹄鹿族/鹿弥辨识度过近而归档。 |
| `project/severed-homeland/assets/characters/history/character_helian_xuedai_multi_state_board.v002.png` | retained rejected version | 熊脸兽首旧稿，因不符合“高级护卫仍是人脸、偏圆脸、熊耳和面纹”的修正而归档。 |
| `project/severed-homeland/assets/characters/history/character_helian_xuedai_multi_state_board.v003.png` | retained rejected version | 人脸熊族护卫稿，但熊耳仍偏头饰/毛团，脸部压迫感不足，眼神杀气不够，已归档。 |
| `project/severed-homeland/assets/characters/history/character_helian_xuedai_multi_state_board.v004.png` | retained rejected version | 真实熊耳方向有所改善，但醒目圆绒耳仍有毛绒玩具感，会削弱高级女武士压迫性，已归档。 |

## QC Checks

| Check | Result | Notes |
|---|---|---|
| Character identity | pass | 角色读作白熊族部落高级女护卫、高级女武士和礼仪执行者，不是鹿弥换装、霜蹄鹿族、低等部落民或萨满。 |
| Face direction | pass | 脸仍是人脸为主，但通过重眉骨、厚颧骨、宽下颌、厚直鼻梁、冷黑鼻面和紧闭嘴角形成压迫性兽人脸型。 |
| Bear-clan read without ears | pass | 最终图不再依赖醒目圆绒熊耳；熊族特征由鬓颊/后颈白熊绒毛、熊爪形面纹、厚颈肩、熊掌式大手、短黑爪、掌垫/爪茧和盾斧爪痕共同建立。 |
| Warrior gaze | pass | 眼型狭长、上压，深褐眼带冰蓝冷光，近景有冷静杀意，符合高级女武士护卫的威慑感。 |
| Rank distinction | pass | 服装完整、干净、贵重而克制，装备有高级护卫秩序感，不是低等粗糙部落民。 |
| Scale and silhouette | pass | 三状态均比人族护卫更宽更重，并保留大手、厚实肩背、重装护卫站姿，能和鹿弥纤长鹿族萨满轮廓形成同框差异。 |
| Three-state continuity | pass | 高级近卫礼装、雪线护送战备装、族中礼仪执行装共享同一压迫性人脸、白熊鬓颊绒毛、熊爪形面纹、白熊皮披、银黑胸甲和护卫装备。 |
| Costume system | pass | 白熊皮厚披、银黑骨铁胸甲、冰灰厚织内层、深褐护腹、青铜护腕、青玉扣和暗红誓约绳符合新版角色 Bible。 |
| Guard equipment | pass | 骨铁大盾、长柄护卫斧、盾面刮痕、熊爪刻痕、宽重冰钉靴和护卫挂件可读。 |
| Northern color system | pass | 白熊皮、银黑骨铁、黑铁、青铜、深褐皮革、冰灰为主体，青玉绿和暗红誓约绳为点色，不与鹿族冰蓝轻贵族体系混淆。 |
| Wanshou badge rule | pass | 未重画北境万兽联盟徽章，也未生成熊族个人家徽、胸章、肩章、旗帜或现代 logo；符号停留在熊爪刻痕、骨木、绳结、玉扣、青铜和器物层面。 |
| Low-magic boundary | pass | 无攻击法术、大法阵或高魔光效；角色资产以人脸熊族特征、体量、服装、盾斧装备和礼仪挡路姿态建模。 |
| Text/watermark | pass | 未见可读文字、标签、UI 或水印。 |
| History hygiene | pass | canonical 输出路径只存放 v05 最终图，v001、v002、v003 和 v004 均保留在 `history/` 并使用版本后缀。 |

## Handoff Notes

Prompt Room 应使用 `character_helian_xuedai_multi_state_board_v05` 作为第 09 集远景护卫、鹿弥护送队伍和后续北境线白熊族高级重装近卫的主角色参考。单镜头中必须保留人脸为主但有压迫性的重眉骨、厚颧骨、宽下颌、厚直鼻梁、熊爪形面纹、鬓颊/后颈白熊绒毛、狭长杀气眼神、厚实肩背、白熊皮厚披、银黑骨铁胸甲、骨铁大盾、长柄护卫斧、青铜护腕、深褐护腹、熊掌式大手短黑爪、青玉扣、暗红誓约绳和冰钉靴；不得把醒目圆绒熊耳作为身份锚点。如需使用北境阵营符号，只能引用既有万兽系统的骨木绳结、熊爪刻痕和誓约绳语言，不得生成新的熊族徽章或个人 crest。
