# P2 次级角色美术资源 QC

项目：《断航故土》

范围：本次只处理用户指定的 P2 次级角色资源包：

1. `char_luo_qinghe_v01`：罗青禾
2. `char_meng_guicang_v01`：孟归藏
3. `char_lu_mi_v01`：鹿弥
4. `char_li_tang_v01`：厉螳
5. `char_gu_huaizhang_v01`：顾怀章

## 当前状态

状态：`completed`

已完成规划、可审计提示词与图片资产：

1. `art/p2-secondary-character-designs.json`
2. `prompts/p2-character-image-prompts.json`
3. `art/p2-thread-plan.json`
4. `art/p2-thread-results.json`
5. `art/p2-asset-index.json`

已调度 Codex 后台图像线程：

1. `p2-secondary-character-sheets`：`019e87d6-062f-73e0-805e-7ef6277eaf1b`
2. `p2-secondary-lineup-board`：`019e87d6-0bca-7f63-9b29-c97d97725a6c`

## 已生成图片

1. `assets/characters/v01/char_luo_qinghe_v01_sheet.png`
2. `assets/characters/v01/char_meng_guicang_v01_sheet.png`
3. `assets/characters/v01/char_lu_mi_v01_sheet.png`
4. `assets/characters/v01/char_li_tang_v01_sheet.png`
5. `assets/characters/v01/char_gu_huaizhang_v01_sheet.png`
6. `assets/characters/v01/p2_secondary_character_lineup_v01.png`

## 连续性检查

通过：

1. 每个资源都有稳定 `asset_id`、`prompt_id` 和目标路径。
2. 提示词均追溯到 `bible/characters.md` 与 `bible/character-visual-locks.json`。
3. 昭明/肃明徽记引用继续使用 v3 锁定资产。
4. 顾怀章在登记表中仍是 priority 3；本批仅按用户明确列表纳入 P2 次级角色包，不修改角色圣经优先级。

图片复查结论：

1. 罗青禾单人 sheet 已按用户反馈重生成为 37 岁温婉坚韧的美妇人，保留草药篮、青布头巾、药柜暗号和驿令交接，不再读成老年女性；P2 总板也已同步重生，避免沿用旧版老年化形象。
2. 孟归藏有明确火损眉眼、烧黑书箱、骨片夹页和护页姿态，不是干净书生。
3. 鹿弥呈现北境雪地旅者、骨笛、短鹿角饰和雪地药草袋，未变成完整鹿人。
4. 厉螳有黑绿甲壳肩甲、铁闸令牌和甲军府军官轮廓，和白翳的清明院白色官僚感区分明确。
5. 顾怀章呈现南方旧礼学者、红线卷轴、残旧礼袍和训令压力感，不像常驻前线战斗角色。

## Prompt Room 交接建议

Prompt Room 可直接引用 `art/p2-asset-index.json` 中的路径，并在分镜提示词里优先使用这些 v01 角色 sheet 作为次级角色身份锁。
