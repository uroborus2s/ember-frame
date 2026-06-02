# 全局参考资产质检记录

项目：《断航故土》

范围：本轮只生成全局参考资产，不生成完整全量资产。

## 当前推荐版本

1. v3徽章锁定图：`assets/style/v03/style_emblem_lock_v03.png`
2. 昭明合徽：`assets/style/v03/symbol_zhaoming_sunmoon_v03.png`
3. 肃明徽章：`assets/style/v03/symbol_suming_whitewing_blackhalo_v03.png`
4. 旗帜/徽记锁定板：`assets/style/v04/style_faction_flags_v04.png`
5. 核心道具板规则参考：`assets/props/v04/prop_core_set_v04.png`
6. 沈维桑：`assets/characters/v03/char_shen_weisang_v03_sheet.png`
7. 晏南枝：`assets/characters/v04/char_yan_nanzhi_v04_sheet.png`
8. 白翳：`assets/characters/v03/char_bai_yi_v03_sheet.png`
9. 沈照眠：`assets/characters/v02/char_shen_zhaomian_v02_sheet.png`
10. 陆青砾：`assets/characters/v02/char_lu_qingli_v02_sheet.png`
11. 薛临墙：`assets/characters/v02/char_xue_linqiang_v02_sheet.png`
12. P1 服装区分联系表：`assets/costumes/v01/p1_costume_role_differentiation_v01.png`

## 可用但需自然融合精修

以下资产已通过确定性 v3 徽章叠加修正，徽章规则准确，但叠加痕迹明显，适合作为视觉规则与布局参考，不宜直接作为最终成片美术：

1. `assets/style/v03/style_zhaoming_relic_v03.png`
2. `assets/props/v03/prop_border_set_v03.png`
3. `assets/props/v04/prop_core_set_v04.png`

## 场景合成废稿

以下资产不应再作为场景图使用。它们的问题不是“融合还不够自然”，而是把确定性徽章当成非场景内大图标贴在画面上，破坏空间逻辑：

1. `assets/locations/v03/loc_suohou_pass_v03_board.png`
2. `assets/locations/v03/loc_moon_oath_relay_v03_board.png`

处理结论：保留为错误记录或徽章漂移修正失败案例；正式场景目标改为 `assets/locations/v04/loc_suohou_pass_v04_board.png` 与 `assets/locations/v04/loc_moon_oath_relay_v04_board.png`。

## 用户反馈修订

1. 昭明日月徽改为“日轮托白月”：月白弧月放入金色日轮内部，融成一枚合徽。
2. 肃明国视觉改为“抽象白翅覆黑日”：黑日增加冷白/暗灰日晕，白翅改为几何、秩序带、折线翼骨式抽象覆盖，不使用写实虫翼。
3. 晏南枝改为流亡皇族公主女性：粗布外衣清冷整洁，旧而不破，保持周秦式贵族礼法气质。
4. 沈维桑强化为17岁少年：剑眉、清亮戒备眼神、瘦硬猎户感。
5. P1 人族角色的贫困不能统一画成破布。服装可以粗布、旧、打补丁、蒙尘和修补，但不能破烂；猎户、村童、墙下混裔、边军必须通过服装职业信息区分。
6. 白翳必须保留虫族监察者特征。`char_bai_yi_v02` 像“戴面具的人族”且虫族特征不足，废弃；新稿以 v01 的几丁质面部、复眼和翼膜方向为基准。

## 版本结论

- `style_faction_flags_v01`：废稿。昭明/肃明辨识度不足。
- `style_faction_flags_v02`：部分可用。昭明日月合徽可参考，肃明白翅仍偏具象。
- `style_faction_flags_v03`：降级。AI 旗帜图可作为材质气氛参考，但不能再作为精确徽章标准。
- `style_faction_flags_v04`：推荐。确定性 SVG/PNG 旗帜锁定图，用于后续所有旗帜、徽记、官署和阵营标识的 v3 标准。
- `char_yan_nanzhi_v01`：废稿。身份方向不稳定。
- `char_yan_nanzhi_v02`：废稿。衣服过于破旧。
- `char_yan_nanzhi_v03`：降级为可用旧稿。v04 更好地处理粗布完整性和内层昭明纹样。
- `char_yan_nanzhi_v04`：推荐。女性流亡皇族身份清楚，粗布完整，旧帝国内层纹样自然。
- `char_shen_weisang_v02`：降级。少年体态可参考，但衣服过破且令牌仍拆分日/月。
- `char_shen_weisang_v03`：推荐。平民猎户职业轮廓清楚，衣物完整可补丁，令牌使用日轮托白月合徽。
- `char_bai_yi_v01`：外形基准旧稿。保留虫族监察者的几丁质面部、复眼和翼膜方向。
- `char_bai_yi_v02`：废稿。像“戴面具的人族”，不再作为白翳推荐形象。
- `char_bai_yi_v03`：推荐。基于 v01 虫族方向自然重生成，保留几丁质面部、复眼、翼膜，并融合 v3 肃明徽章。
- `char_shen_zhaomian_v01`：降级。村童状态服装过于破烂。
- `char_shen_zhaomian_v02`：推荐。村童短襦/围裙/草药袋完整，清明状态保留白袍、虫蜡手环和 v3 肃明标记。
- `char_lu_qingli_v01`：降级。脸和姿态可参考，但服装破碎且过通用。
- `char_lu_qingli_v02`：推荐。灰蓝短袄、功能口袋、黑市木牌、碎陶护符和窄刀形成墙下身份。
- `char_xue_linqiang_v01`：降级。老兵气质可参考，但布条徽章和破损程度需修正。
- `char_xue_linqiang_v02`：推荐。边军旧甲、御寒层、骨哨、长枪和反面旧日月布条可读。
- `prop_core_set_v03`：降级。构图可参考，但多个旧文明印记仍会被误读为旧日轮。
- `prop_core_set_v04`：徽章规则参考。主要昭明旧物已叠加 v3 日月合徽，但仍需自然融合精修。
- `style_zhaoming_relic_v01_failed_emblem_drift`、`loc_moon_oath_relay_v01_failed_emblem_drift`、`prop_core_set_v01_failed_emblem_drift`、`prop_border_set_v01_failed_emblem_drift`、`loc_suohou_pass_v03_failed_zhaoming_emblem_drift`：均移入 `assets/rejected/emblem-drift/`，不得作为推荐资产引用。

## 后续约束

后续 Prompt Room 与 Director Room 不应再引用根目录图片路径。统一使用 `assets/{category}/vXX/` 路径，并优先引用 `asset-index.json` 中的 `current_recommendations`。
