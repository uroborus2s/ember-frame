# 顾怀章多状态角色板 QC 报告

日期：2026-06-03

## 结果

通过，作为项目级顾怀章角色参考板 v01 使用。

最终文件：

- `project/severed-homeland/assets/characters/character_gu_huaizhang_multi_state_board.png`

历史文件：

- `project/severed-homeland/assets/characters/history/character_gu_huaizhang_multi_state_board.v001.png`
- `project/severed-homeland/assets/characters/history/character_gu_huaizhang_multi_state_board.v002.png`
- `project/severed-homeland/assets/characters/history/character_gu_huaizhang_multi_state_board.v003.png`

## 校验项

| 项目 | 结论 |
| --- | --- |
| 项目路径 | 通过，最终图已保存到 `assets/characters/` canonical 路径。 |
| 历史版本 | 通过，三张拒稿已保存到 `assets/characters/history/` 并使用 `.v001`、`.v002`、`.v003` 后缀。 |
| 画幅 | 通过，PNG 为 864x1821，符合超高竖版角色板用途。 |
| 多状态 | 通过，包含南方训令装、旧帝国礼学正装、密信行装三种完整全身状态。 |
| 身份锁定 | 通过，年长、瘦削、礼法姿态强，读作晏南枝南方师长与复翼者压力人物，不像皇帝、仙人、术士或武斗角色。 |
| 服装系统 | 通过，朱赤纱袍、宝蓝内层、月白下裳、旧金边、宽袖、短外罩与暗色行装都符合湿热南方旧帝国保存逻辑。 |
| 道具体系 | 通过，红线卷轴、红绳结、油纸卷轴筒、防潮木筒与暗棕漆盒可读。 |
| 既有徽章约束 | 通过，未重新设计昭明徽章，没有清晰公共胸章、完整日月牌或新个人徽章；昭明感主要由色彩层级、破碎金线路径和旧朝材质压力承担。 |
| 文字禁用 | 通过，最终图没有可读文字、标签、UI 或水印。 |
| 风格连续性 | 通过，低魔东方史诗、南方旧帝国朱赤/宝蓝/月白/旧金/暗棕材质与项目风格板一致。 |

## 视觉风险

1. 最终图仍有卷轴筒端面和少量旧五金环扣，这些是道具结构，不应在后续提示中扩展为徽章、印玺或日月符号。
2. 破碎金线路径是生成式纹样近似，不是新的昭明徽章设计。若后续需要徽章近景，应直接使用既有 `emblem_zhaoming_empire.png`。
3. 顾怀章的“南方训令装”和“旧帝国礼学正装”都较华丽，后续镜头提示应保留湿热轻薄和保存旧臣感，避免转成无瑕宫廷正装。

## Handoff

Prompt Room 后续应把该图作为顾怀章身份锁，重点复用：

- 年长、瘦削、礼法强于行动的南方师长气质；
- 朱赤纱袍、宝蓝内层、月白下裳、旧金边与暗色行装切换；
- 红线卷轴、油纸卷轴筒、防潮木筒、暗棕漆盒；
- 破碎金线路径、湿气污痕、旧朝材质压力；
- 不得新增昭明徽章，不得把卷筒端面或五金环扣解释成日月徽章。
