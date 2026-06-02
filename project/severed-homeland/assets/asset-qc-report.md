# 全局参考资产质检记录

项目：《断航故土》

范围：本轮只生成全局参考资产，不生成完整全量资产。

## 当前推荐版本

1. 旗帜/徽记：`assets/style/v03/style_faction_flags_v03.png`
2. 晏南枝：`assets/characters/v03/char_yan_nanzhi_v03_sheet.png`
3. 沈维桑：`assets/characters/v02/char_shen_weisang_v02_sheet.png`

## 用户反馈修订

1. 昭明日月徽改为“日轮托白月”：月白弧月放入金色日轮内部，融成一枚合徽。
2. 肃明国视觉改为“抽象白翅覆黑日”：黑日增加冷白/暗灰日晕，白翅改为几何、秩序带、折线翼骨式抽象覆盖，不使用写实虫翼。
3. 晏南枝改为流亡皇族公主女性：粗布外衣清冷整洁，旧而不破，保持周秦式贵族礼法气质。
4. 沈维桑强化为17岁少年：剑眉、清亮戒备眼神、瘦硬猎户感。

## 版本结论

- `style_faction_flags_v01`：废稿。昭明/肃明辨识度不足。
- `style_faction_flags_v02`：部分可用。昭明日月合徽可参考，肃明白翅仍偏具象。
- `style_faction_flags_v03`：推荐。用于后续所有旗帜、徽记、官署和阵营标识。
- `char_yan_nanzhi_v01`：废稿。身份方向不稳定。
- `char_yan_nanzhi_v02`：废稿。衣服过于破旧。
- `char_yan_nanzhi_v03`：推荐。用于后续角色、服装和分镜参考。
- `char_shen_weisang_v02`：推荐用于人物体态和少年感。若日月驿令需要特写，应另生成道具板或角色 v03 来修正令牌合徽。

## 后续约束

后续 Prompt Room 与 Director Room 不应再引用根目录图片路径。统一使用 `assets/{category}/vXX/` 路径，并优先引用 `asset-index.json` 中的 `current_recommendations`。
