# SC002 C018 持械封路重做复审 / 2026-06-11

结论已被用户视觉 QC 继续退回：新版虽然补了 C018 持械封路，但角色一致性和身高差仍未达标。当前状态为 `failed_user_visual_qc_identity_height_scale_relock_required_2026-06-11`；本报告下方评分只作历史记录，不得作为视频放行依据。有效退回审计见 `01/art/audits/sc002-character-identity-height-scale-user-rejection-2026-06-11.md`。

## 本轮硬性修正

- `E01_C016B`：canonical 保留为全局 `C016` 母卡直继承，用精确母卡锁住脸型、复眼、骨白面壳、触须和白蜡官帽；本轮 prompt-only C016B 生成图因有脸型漂移风险，仅保留在 history，不作为正向身份锁。
- `E01_C017`：重做为混血奴兵扣腕/押车状态卡，重点补清五指人手、硬化指节、骨白腕绑和 170-200cm 人形体态。
- `E01_C018`：重做为纯虫族小兵持械封路状态卡，锁定 200-230cm、非人虫身、反关节腿、爪足、短矛/钩镰和外圈警戒职责。
- `E01_R005`-`E01_R009`：全部加入 C018 持兵器警戒/封路，明确“官吏开册、奴兵扣腕/搬粮、虫兵封路”的层级。

## 新版参考帧评分

| Asset | Shot | 用途 | 导演要求 | 美术合格度 | 关键通过项 |
| --- | --- | --- | ---: | ---: | --- |
| `E01_R005` | `SC002-SH001` | I2V 首帧 | 93 | 94 | 粮袋墙压住上半画面，检查台、泥路、低位村民和金河粮仓空间可读。 |
| `E01_R006` | `SC002-SH002` | I2V 首帧 | 95 | 95 | 扣腕手为 C017 混血奴兵五指人手，硬化甲片、骨白腕绑和真实握压都清楚。 |
| `E01_R007` | `SC002-SH003` | I2V 首帧 | 94 | 94 | 前景白册、骨算盘、税牌、秤钩、虫蜡和湿桌面形成证据层。 |
| `E01_R008` | `SC002-SH004` | FLF2V 首帧 | 95 | 95 | 同一门槛后方机位成立，祖牌盒、儿童蜡手印、散粮和车辙是最大前景。 |
| `E01_R009` | `SC002-SH004` | FLF2V 终帧 | 95 | 95 | 与 R008 维持同轴门槛构图，空门槛、祖牌盒、儿童蜡手印和车辙是主叙事。 |

## 当前文件

- `01/assets/characters/c016be01.png`
- `01/assets/characters/c017e01.png`
- `01/assets/characters/c018e01.png`
- `01/assets/reference-frames/r005e01.png`
- `01/assets/reference-frames/r006e01.png`
- `01/assets/reference-frames/r007e01.png`
- `01/assets/reference-frames/r008e01.png`
- `01/assets/reference-frames/r009e01.png`

全部 current reference frames 已重采样为 3840x2160 PNG、无 alpha。C017/C018 角色卡也已为 3840x2160 PNG、无 alpha；C016B 当前 canonical 沿用 3840x2160 的全局母卡继承文件。

## 保留历史

- `01/assets/characters/history/c016be01.sc002-grain-tax-candidate-rejected-face-risk-20260611.png`
- `01/assets/characters/history/c017e01.before-user-hand-scale-redo-20260611.png`
- `01/assets/characters/history/c017e01.sc002-hand-scale-source-20260611.png`
- `01/assets/characters/history/c018e01.before-armed-guard-scale-redo-20260611.png`
- `01/assets/characters/history/c018e01.armed-guard-scale-source-20260611.png`
- `01/assets/reference-frames/history/r005e01.before-c018-armed-guard-redo-20260611.png`
- `01/assets/reference-frames/history/r006e01.before-c018-armed-guard-redo-20260611.png`
- `01/assets/reference-frames/history/r006e01.rejected-foot-ankle-risk-before-wrist-correction-20260611.png`
- `01/assets/reference-frames/history/r007e01.before-c018-armed-guard-redo-20260611.png`
- `01/assets/reference-frames/history/r008e01.before-c018-armed-guard-redo-20260611.png`
- `01/assets/reference-frames/history/r009e01.before-c018-armed-guard-redo-20260611.png`
- `01/assets/reference-frames/history/r005e01.c018-armed-guard-source-20260611.png`
- `01/assets/reference-frames/history/r006e01.c017-wrist-c018-guard-source-20260611.png`
- `01/assets/reference-frames/history/r007e01.c016-table-c018-guard-source-20260611.png`
- `01/assets/reference-frames/history/r008e01.c018-armed-guard-source-20260611.png`
- `01/assets/reference-frames/history/r009e01.c018-armed-guard-source-20260611.png`

## 视频交付限制

当前状态不是待确认候选，而是用户视觉 QC 未通过。下一轮必须先按同地平线比例条重生 C016B/C017/C018 状态卡，再按 `4096x2304` 重生 `E01_R005`-`E01_R009`；重生完成前 `SC002` 仍标记为 `failed_user_visual_qc_identity_height_scale_relock_required_2026-06-11`。
