# 《断航故土》第01集缺失场景参考图 QC 报告

版本：v01  
日期：2026-06-03  
范围：`episode01_missing_reference_frames_v01`

## 生成结果

本轮 5 张第01集缺失场景/镜头参考图已全部生成并保存到：

`project/severed-homeland/01/assets/reference-frames/`

## 资产清单

- `sc001_sh002_northern_battle_fragment.png`：北境边墙战后压力碎片。为满足图像安全约束，最终图采用“无血、无伤、无尸体”的战后军需/边墙压力版本。
- `sc001_sh003_jinhe_grain_levy_road.png`：金河征粮道，木牌、粮袋、空碗、车辙和虫蜡封牌明确。
- `sc001_sh004_southern_secret_room_relay_table.png`：南方密室旧驿图桌，手、地图、药包、红线、火星和残缺日月痕明确。
- `sc005_zhaomian_threshold_identification.png`：药屋门口失言与识句记号，白册区域留白，药牌不生成可读字。
- `sc008_final_spear_line_well_glint.png`：终段封锁线与井沿月白反光，短矛线和旧井方向成立。

## QC 结论

- 规格：5 张 canonical PNG 均为 `941 x 1672`，RGB，竖屏 9:16 参考图。
- 文字：未发现需要交付的可读文字；白册、药牌、木牌和地图文字位应在 Prompt Room 或后期阶段另行处理。
- 徽章：未新增需要锁定的新徽章；昭明痕迹保持为残缺/旧物，清明标记保持为小型制度物件。
- 连续性：SC005 和 SC008 延续残阳坳药屋、村口、旧井的既有空间和材质语言。

## 后续要求

- Prompt Room 使用这些图作为镜头参考时，不要直接要求模型生成可读文字；白册和药牌文字建议由后期文字层完成。
- SC001-SH002 如需更强战争感，应在制作阶段通过剪辑、音效、烟尘和旗影加强，不建议回到血迹或伤兵画面。
