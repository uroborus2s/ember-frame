# 厉螳多状态角色板 QC 报告

日期：2026-06-03

## 结果

通过，作为项目级厉螳角色参考板 v02-face-anthro-lock 使用。

最终文件：

- `project/severed-homeland/assets/characters/character_li_tang_multi_state_board.png`

历史文件：

- `project/severed-homeland/assets/characters/history/character_li_tang_multi_state_board.v001.png`
- `project/severed-homeland/assets/characters/history/character_li_tang_multi_state_board.v002.png`

## 校验项

| 项目 | 结论 |
| --- | --- |
| 项目路径 | 通过，最终图已保存到 `assets/characters/` canonical 路径。 |
| 历史版本 | 通过，早期版本已保存到 `assets/characters/history/` 并使用 `.v001`、`.v002` 后缀。 |
| 画幅 | 通过，PNG 为 941x1672，符合 9:16 竖屏角色板。 |
| 多状态 | 通过，包含寒鸦堡军控常态、臂刀展开战斗态、边墙雪线巡压态。 |
| 非人形约束 | 通过，三角虫头、窄复眼、黑绿甲壳、反关节腿、爪足和臂刀机制清楚。 |
| 半拟人面部 | 通过，正面头部比 v01 更强调类人眉弓、鼻脊/吻脊、甲壳颧面和下颌甲；仍保留暗色复眼、骨白护颚、触须根、三角额板和虫化颈膜。 |
| 服装/装备系统 | 通过，旧铁束具、暗绿军令带、骨白虫蜡封印条、黑色短披挂、短矛和铁闸令牌可读。 |
| 既有徽章约束 | 通过，肃明/清明白翅覆黑日只作为小型牌面/军阶引用，没有重做为新大徽章。 |
| 文字禁用 | 通过，最终图没有可读文字、标签、UI 或水印。 |
| 风格连续性 | 通过，低魔东方史诗、黑绿甲壳、旧铁、虫蜡、黑石雪线与项目风格板一致。 |

## 视觉风险

1. 小型军阶牌是生成式近似引用，不是像素级复制现有 PNG。后续若要用于近景特写，应在 Prompt Room 或贴图阶段把 `emblem_suming_qingming_state.png` 作为精确输入材质。
2. 本次曾有一张候选图把身体推向人形盔甲战士并放大胸前徽章，已拒绝，未写入 canonical 路径。
3. 当前 canonical 图保留原有低伏虫体和反关节腿；第一状态仍有可读的双足压迫感，但已通过虫头、爪足、臂刀、甲壳胸背和小型牌面把“人类将军黑甲化”风险压低到可接受范围。

## Handoff

Prompt Room 后续应把该图作为厉螳身份锁，重点复用：

- 三角头部与窄复眼；
- 半拟人化眉弓、鼻脊/吻脊、甲壳颧面和下颌甲；
- 胸背宽厚前倾体态；
- 黑绿甲壳、旧铁束具、骨白虫蜡封印条；
- 折叠臂刀与反关节腿；
- 小型白翅覆黑日军阶牌，不得放大或重新设计。
