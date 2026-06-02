# 全局参考资产质检记录

项目：《断航故土》

范围：本轮只生成全局参考资产，不生成完整全量资产。

## 当前推荐版本

1. v3徽章锁定图：`assets/style/v03/style_emblem_lock_v03.png`
2. 昭明合徽：`assets/style/v03/symbol_zhaoming_sunmoon_v03.png`
3. 肃明徽章：`assets/style/v03/symbol_suming_whitewing_blackhalo_v03.png`
4. 旗帜/徽记锁定板：`assets/style/v04/style_faction_flags_v04.png`
5. 核心道具板规则参考：`assets/props/v04/prop_core_set_v04.png`
6. 晏南枝：`assets/characters/v03/char_yan_nanzhi_v03_sheet.png`
7. 白翳外形基准：`assets/characters/v01/char_bai_yi_v01_sheet.png`
8. 白翳徽章规则参考：`assets/characters/v03/char_bai_yi_v03_sheet.png`
9. 沈维桑：`assets/characters/v02/char_shen_weisang_v02_sheet.png`

## 可用但需自然融合精修

以下资产已通过确定性 v3 徽章叠加修正，徽章规则准确，但叠加痕迹明显，适合作为视觉规则与布局参考，不宜直接作为最终成片美术：

1. `assets/style/v03/style_zhaoming_relic_v03.png`
2. `assets/locations/v03/loc_suohou_pass_v03_board.png`
3. `assets/locations/v03/loc_moon_oath_relay_v03_board.png`
4. `assets/props/v03/prop_border_set_v03.png`
5. `assets/characters/v03/char_bai_yi_v03_sheet.png`
6. `assets/props/v04/prop_core_set_v04.png`

## 用户反馈修订

1. 昭明日月徽改为“日轮托白月”：月白弧月放入金色日轮内部，融成一枚合徽。
2. 肃明国视觉改为“抽象白翅覆黑日”：黑日增加冷白/暗灰日晕，白翅改为几何、秩序带、折线翼骨式抽象覆盖，不使用写实虫翼。
3. 晏南枝改为流亡皇族公主女性：粗布外衣清冷整洁，旧而不破，保持周秦式贵族礼法气质。
4. 沈维桑强化为17岁少年：剑眉、清亮戒备眼神、瘦硬猎户感。

## 版本结论

- `style_faction_flags_v01`：废稿。昭明/肃明辨识度不足。
- `style_faction_flags_v02`：部分可用。昭明日月合徽可参考，肃明白翅仍偏具象。
- `style_faction_flags_v03`：降级。AI 旗帜图可作为材质气氛参考，但不能再作为精确徽章标准。
- `style_faction_flags_v04`：推荐。确定性 SVG/PNG 旗帜锁定图，用于后续所有旗帜、徽记、官署和阵营标识的 v3 标准。
- `char_yan_nanzhi_v01`：废稿。身份方向不稳定。
- `char_yan_nanzhi_v02`：废稿。衣服过于破旧。
- `char_yan_nanzhi_v03`：推荐。用于后续角色、服装和分镜参考。
- `char_shen_weisang_v02`：推荐用于人物体态和少年感。若日月驿令需要特写，应另生成道具板或角色 v03 来修正令牌合徽。
- `char_bai_yi_v01`：外形基准。保留虫族监察者的几丁质面部、复眼和翼膜方向。
- `char_bai_yi_v02`：废稿。像“戴面具的人族”，不再作为白翳推荐形象。
- `char_bai_yi_v03`：徽章规则参考。基于 v01 叠加确定性 v3 肃明徽章，但贴合痕迹明显，仍需自然融合重生成。
- `prop_core_set_v03`：降级。构图可参考，但多个旧文明印记仍会被误读为旧日轮。
- `prop_core_set_v04`：徽章规则参考。主要昭明旧物已叠加 v3 日月合徽，但仍需自然融合精修。
- `style_zhaoming_relic_v01_failed_emblem_drift`、`loc_moon_oath_relay_v01_failed_emblem_drift`、`prop_core_set_v01_failed_emblem_drift`、`prop_border_set_v01_failed_emblem_drift`、`loc_suohou_pass_v03_failed_zhaoming_emblem_drift`：均移入 `assets/rejected/emblem-drift/`，不得作为推荐资产引用。

## 后续约束

后续 Prompt Room 与 Director Room 不应再引用根目录图片路径。统一使用 `assets/{category}/vXX/` 路径，并优先引用 `asset-index.json` 中的 `current_recommendations`。
