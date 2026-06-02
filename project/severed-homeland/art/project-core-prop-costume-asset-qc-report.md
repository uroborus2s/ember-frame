# 《断航故土》核心道具与服装资产 QC 报告

批次：`project_core_prop_costume_v01`  
日期：2026-06-02  
状态：规划 QC 通过，后台图片生成已启动，图片 QC 等待回填结果

## 1. 已检查

- 项目根目录：`project/severed-homeland`
- 设计说明：`art/project-core-prop-costume-art-direction.md`
- 资产 manifest：`art/project-core-prop-costume-asset-manifest.json`
- 结构化设计：`art/project-core-prop-costume-designs.json`
- 图片提示词：`prompts/project-core-prop-costume-image-prompts.json`
- 线程计划：`art/project-core-prop-costume-thread-plan.json`
- 资产索引：`art/project-core-prop-costume-asset-index.json`

## 2. 连续性结论

规划层通过。当前设计沿用现有总风格、区域色彩、基础材质和阵营徽章，并明确禁止重新设计徽章。道具粒度与用户要求一致：

| 用户要求 | 本轮资产 |
| --- | --- |
| 半枚日月驿令单独道具图 | `prop_half_sunmoon_relay_token_v01` |
| 月白玉片可与血牒合成晏南枝随身物板 | `prop_yan_nanzhi_carry_board_v01` |
| 清明白册单独道具图 | `prop_qingming_white_register_v01` |
| 虫蜡针可与白册、清明香合成清明院工具板 | `prop_qingming_court_tool_board_v01` |
| 残缺大陆驿道图 | `prop_fragmented_continent_relay_map_v01` |
| 月下盟书残页 | 包含于 `prop_yan_nanzhi_carry_board_v01` |
| 骨哨/骨笛对照图 | `prop_bone_whistle_flute_comparison_v01` |
| 粮牌/黑市木牌/碎陶护符墙下道具组图 | `prop_wallfoot_trade_tokens_v01` |
| 烧焦发绳、小草药袋 | `prop_shen_zhaomian_child_relics_v01` |
| 主角服装每个主角一张多状态角色板 | 6 张核心人物服装板 |
| 阵营通用服装系统板 | `costume_faction_system_board_v01` |
| 群众/阶层服装板 | `costume_crowd_class_system_board_v01` |

## 3. 待图片生成后检查

1. PNG 是否写入计划中的精确路径。
2. 图片是否无可读文字、无标签、无水印、无 UI。
3. 现有昭明、肃明/清明、北境徽章是否只作为参考或局部痕迹，未被重绘。
4. 半枚日月驿令是否保持半枚、磨损、有限钥匙感。
5. 白册、血牒、盟书、驿道图是否没有可读文字。
6. 清明工具是否避免现代医疗器械感。
7. 白翳是否不是人戴面具，且没有人类头发。
8. 沈维桑是否仍是 17 岁少年猎户，不是成年武将。
9. 晏南枝流亡状态是否隐藏旧帝国标识。
10. 陆青砾、灰墙军、墙下混裔是否没有被设计成正式新徽章或统一国家制服。
11. 群众服装是否旧而完整、有职业信息，未变成破布流民。

## 4. 后台线程

| 批次 | 线程 ID | 状态 |
| --- | --- | --- |
| 核心道具资源板 | `019e890d-54ba-7602-a2eb-897d73cb496f` | 已启动，等待图片回填 |
| 主角与阵营服装资源板 | `019e890d-ae14-76e3-82a1-756235a7673c` | 已启动，等待图片回填 |

## 5. 当前阻塞

无规划阻塞。图片资产仍待后台线程生成与回填。

## 6. 交接建议

图片生成完成并通过 QC 后，将 `art/project-core-prop-costume-asset-index.json` 更新为 `ready_for_prompt_room`，Prompt Room 再引用这些 asset ID 生成镜头级 ComfyUI-ready 提示词。
