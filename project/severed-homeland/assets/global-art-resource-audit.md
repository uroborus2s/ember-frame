# 全局美术资源审计表

项目：《断航故土》

审计范围：项目级全局可复用美术资源。此表不包含分集专属参考帧、镜头覆盖图、ComfyUI-ready prompt 或 episode-level shot assets。

状态定义：

- `recommended`：当前推荐使用。
- `usable`：可作为气氛/材质/体态参考，但不是最终标准。
- `needs_regeneration`：存在关键规则不一致，需要重生成或后期叠加确定性徽章。
- `missing`：尚未生成。
- `rejected`：已确认不符合要求，不进入推荐资产。
- `deferred`：非当前全局核心包，等分集导演输出或第二批资产再做。

## P0 徽章与阵营识别

| 资源 | 应有要求 | 当前文件 | 状态 | 问题/处理 |
|---|---|---|---|---|
| v3徽章锁定图 | 同时锁定昭明“日轮托白月”和肃明“白翅覆黑日” | `assets/style/v03/style_emblem_lock_v03.png` | recommended | 已用确定性 SVG/PNG 建立，不再依赖 AI 自由生成 |
| 昭明日月合徽 | 月白弧月放入金色日轮内部，融成单一徽章 | `assets/style/v03/symbol_zhaoming_sunmoon_v03.png` | recommended | 后续所有昭明徽章必须以此为准 |
| 肃明白翅覆黑日 | 黑日有冷白/暗灰日晕，抽象白翅覆盖，月纹被抹去 | `assets/style/v03/symbol_suming_whitewing_blackhalo_v03.png` | recommended | 后续所有肃明徽章必须以此为准 |
| 昭明/肃明旗帜对照板 | 旗帜层面区分两派，且必须直接使用 v3 双徽规则 | `assets/style/v04/style_faction_flags_v04.png` | recommended | 已改为确定性 PNG/SVG，不再使用 AI 自由渲染的 v03 作为精确标准 |

## P1 风格板

| 资源 | 应有要求 | 当前文件 | 状态 | 问题/处理 |
|---|---|---|---|---|
| 全剧总风格板 | 低魔东方史诗、旧文明被覆盖、逃亡与边墙质感 | `assets/style/v01/style_global_mood_v01.png` | usable | 气氛可用，不承担精确徽章标准 |
| 昭明旧物材质板 | 白石、磨损铜、旧金、朱赤残旗、v3日月合徽 | `assets/style/v03/style_zhaoming_relic_v03.png` | usable | 已用确定性 v3合徽叠加修正；徽章准确，但叠加痕迹明显，后续需自然融合精修 |
| 清明院材质板 | 虫蜡白、清明白册、抽象白翅覆黑日日晕 | `assets/style/v02/style_qingming_court_v02.png` | recommended | 已按黑日日晕与抽象白翅重做 |
| 边墙雪线材质板 | 黑石、骨钟、灰麻、旧铁、雪风 | `assets/style/v01/style_border_wall_v01.png` | usable | 气氛可用；若出现旧日月布条，需套用 v3合徽 |

## P1 主要角色

| 资源 | 应有要求 | 当前文件 | 状态 | 问题/处理 |
|---|---|---|---|---|
| 沈维桑 | 17岁少年，剑眉星目，猎户逃亡者 | `assets/characters/v02/char_shen_weisang_v02_sheet.png` | usable | 少年感可用；令牌特写仍需用 v3合徽，必要时生成 `char_shen_weisang_v03` |
| 晏南枝 | 女性流亡皇族公主，粗布清冷整洁，周秦式礼法气质 | `assets/characters/v03/char_yan_nanzhi_v03_sheet.png` | recommended | 当前推荐 |
| 白翳 | 虫族清明院监察者，保留几丁质面部、复眼、翼膜；肃明抽象白翅覆黑日日晕小徽 | 外形基准：`assets/characters/v01/char_bai_yi_v01_sheet.png`；徽章规则参考：`assets/characters/v03/char_bai_yi_v03_sheet.png` | needs_regeneration | v01 是正确虫族方向；v03 只是确定性 v3 肃明徽章叠加修正版，贴合痕迹明显，不能当自然成稿；v02 废弃 |
| 沈照眠 | 儿童，两状态：村童/清明识别者 | `assets/characters/v01/char_shen_zhaomian_v01_sheet.png` | usable | 当前可用 |
| 陆青砾 | 墙下混裔少女，灰蓝短袄、碎陶护符、细鳞痕 | `assets/characters/v01/char_lu_qingli_v01_sheet.png` | usable | 当前可用 |
| 薛临墙 | 边墙老军户，骨哨、长枪、反面旧日月布条 | `assets/characters/v01/char_xue_linqiang_v01_sheet.png` | usable | 人物可用；若布条徽章可见，需按 v3 重做或叠加 |

## P2 次级角色

| 资源 | 应有要求 | 当前文件 | 状态 | 问题/处理 |
|---|---|---|---|---|
| 罗青禾 | 村医与旧驿暗号保管者 | 无 | missing | 第二批角色资产 |
| 孟归藏 | 灰烬书院/旧书会证人 | 无 | missing | 第二批角色资产 |
| 鹿弥 | 北境寻灾源派角色 | 无 | missing | 第二批角色资产 |
| 厉螳 | 螳族军官，区别于白翳 | 无 | missing | 第二批角色资产 |
| 顾怀章 | 南方旧帝国礼法压力声音 | 无 | deferred | 第一季多为记忆/信件/指令接口，可后置 |

## P1 核心场景

| 资源 | 应有要求 | 当前文件 | 状态 | 问题/处理 |
|---|---|---|---|---|
| 残阳坳 | 土墙、旧井、药屋、猎户生活、屠村后火灰 | `assets/locations/v01/loc_canyang_ao_v01_board.png` | usable | 当前可用 |
| 旧驿暗道 | 白石拱、驿道网格、v3日月合徽、残光 | `assets/locations/v03/loc_old_relay_tunnel_v03_board.png` | recommended | 已重做，主要徽章符合 v3合徽 |
| 清明院外署 | 白墙、白册、记忆蜂巢、冷洁暴力、v3肃明徽 | `assets/locations/v02/loc_qingming_outer_office_v02_board.png` | recommended | 已按黑日日晕与抽象白翅重做 |
| 锁喉关 | 黑石边墙、旧阵基被肃明覆盖、骨钟、雪夜 | `assets/locations/v03/loc_suohou_pass_v03_board.png` | usable | 已用确定性 v3合徽叠加修正旧阵基；徽章准确，但叠加痕迹明显，后续需自然融合精修 |
| 月下盟书旧驿 | 星图厅、月白盟书石台、多族印、裂开日月合徽 | `assets/locations/v03/loc_moon_oath_relay_v03_board.png` | usable | 已用确定性 v3合徽叠加修正；徽章准确，但叠加痕迹明显，后续需自然融合精修 |

## P2 次级场景

| 资源 | 应有要求 | 当前文件 | 状态 | 问题/处理 |
|---|---|---|---|---|
| 金河粮磨区 | 蒸汽生产、封存武器接口 | 无 | missing | 第二批场景资产 |
| 灰烬书院 | 烧毁书院、碎星图、虫蜡封存 | 无 | missing | 第二批场景资产 |
| 墙下集市 | 灰蓝混杂区、粮牌、窄巷、窑洞 | 无 | missing | 第二批场景资产 |
| 鸣骨岭 | 雪岭、骨孔、冰蓝小火 | 无 | missing | 第二批场景资产 |
| 寒鸦堡 | 旧人族堡垒被虫族军署占用 | 无 | missing | 第二批场景资产 |
| 坍塌烽燧 | 结尾逃生、残旗、雪坡 | 无 | missing | 第二批场景资产 |

## P1 道具

| 资源 | 应有要求 | 当前文件 | 状态 | 问题/处理 |
|---|---|---|---|---|
| 核心道具板 | 驿令、月白玉、白册、虫蜡针、旧驿图、血牒残段、盟书残页 | `assets/props/v04/prop_core_set_v04.png` | usable | v04 已用确定性 v3合徽修正主要昭明旧物；但合成痕迹明显，适合规则参考，最终还需自然融合精修 |
| 边墙/墙下道具板 | 骨哨、骨笛、粮牌、黑市木牌、反面日月布条、铁令 | `assets/props/v03/prop_border_set_v03.png` | usable | 已用确定性 v3合徽叠加修正布条；徽章准确，但叠加痕迹明显，后续需自然融合精修 |

## P2 服装状态板

| 资源 | 应有要求 | 当前文件 | 状态 | 问题/处理 |
|---|---|---|---|---|
| 沈维桑服装状态 | 村猎户/火后逃亡/雪线边墙 | 无独立服装板 | deferred | 角色 sheet 暂可覆盖，分集分镜后再细化 |
| 晏南枝服装状态 | 清冷整洁粗布旅装/隐藏旧帝国内层/雪线状态 | 无独立服装板 | deferred | `char_yan_nanzhi_v03` 暂可覆盖 |
| 白翳清明官服 | 白袍、抽象白翅覆黑日日晕小徽、虫蜡针 | 无独立服装板 | needs_regeneration | 可与白翳角色 v2 一起处理 |
| 边墙通用服装 | 灰麻、旧铁、雪泥、骨扣 | 无独立服装板 | deferred | 第二批或分集资产处理 |

## 逐项处理顺序

1. 已完成：建立 v3 徽章锁定图、独立 SVG/PNG 符号，以及确定性 `style_faction_flags_v04` 旗帜锁定板。
2. 已建立规则参考：核心道具板已更新到 `prop_core_set_v04`，主要昭明旧物使用确定性 v3合徽；自然融合完成稿仍需精修。
3. 已建立规则参考：白翳回到 v01 虫族监察者方向，并新增 `char_bai_yi_v03` 作为 v3 肃明徽章叠加参考；但自然融合完成稿仍需重生成。
4. 已完成：重做或合成修正旧驿暗道、锁喉关、月下盟书旧驿，保证旧阵基和盟书空间使用 v3日月合徽。
5. 已完成：合成修正昭明旧物材质板；但自然融合程度不够，需后续精修。
6. 已完成：重做清明院外署 location 级场景板，区别于清明院材质板。
7. 下一项：对所有 `usable_composited_v03` / `usable_symbol_locked_composite` 资产做自然融合精修。
8. 后置：第二批角色、第二批场景、服装状态板与分集专属参考帧。
