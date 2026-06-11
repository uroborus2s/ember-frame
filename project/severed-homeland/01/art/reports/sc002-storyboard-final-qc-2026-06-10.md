# SC002 分镜资产最终 QC / 2026-06-10

> 2026-06-11 撤销说明：本报告的通过结论已被用户视觉 QC 推翻，不再作为有效放行依据。`E01_C016B`、`E01_C017` 未满足角色继承、身高体型和职责层级要求；`E01_R005`-`E01_R009` 当前不得用于视频制作或 director-room prompt refresh。有效结论见 `01/art/audits/sc002-inheritance-failure-audit-2026-06-11.md`。

## 结论

本段为历史记录，已经失效：SC002-SH001 到 SC002-SH004 的分镜参考帧和上游依赖资产曾在 2026-06-10 被错误标记为可交付。2026-06-11 复核后，该结论撤销，当前状态为 `rejected_after_user_visual_qc_identity_inheritance_2026-06-11`。

## 角色与依赖资产

本轮根据 SC002 构图、运镜和连续性要求确认了以下角色与支撑资产：

| 资产 | 路径 | SC002 用途 | QC 结论 |
| --- | --- | --- | --- |
| `E01_C016B` 粮税小吏 | `01/assets/characters/c016be01.png` | `SC002-SH001`, `SC002-SH003` | 虫族低阶税吏身份、高账吏帽、白册夹板、骨算盘、粮牌清楚，可避免误读成人族账房。 |
| `E01_C017` 混血奴兵 | `01/assets/characters/c017e01.png` | `SC002-SH002`, `SC002-SH004` | 低位执行层级、暗色皮甲/布衣、腕绑、扣腕和押车动作参考可读。 |
| `E01_C023` 金河家庭 | `01/assets/characters/c023e01.png` | `SC002-SH002`, `SC002-SH004` | 老人、妇人、孩子、过冬粮、手推车和金河服装差异可读；旧 blocked/rejected 元数据已按现存 canonical 文件复核修正。 |
| `E01_L003` 金河粮仓带 | `01/assets/locations/l003e01.png` | `SC002-SH001`-`SH004` | 粮袋墙、湿木码头、检查桌、泥路、河雾和押车动线可读；场景卡图层不作为最终视频帧。 |
| `E01_P003` 白册 | `01/assets/props/p003e01.png` | `SC002-SH001`, `SC002-SH003` | 白册、空白行列、旧纸、蜡质和湿木托板可读，无随机可读文字。 |
| `E01_P008` 祖牌/封蜡 | `01/assets/props/p008e01.png` | `SC002-SH002`, `SC002-SH004` | 祖牌小盒、粮牌、虫蜡封条、绳结、粮缸和手持尺度可读。 |

## 分镜参考帧

| 镜头 | 资产 | 路径 | imagegen-task 记录 | QC 结论 |
| --- | --- | --- | --- | --- |
| `SC002-SH001` | `E01_R005` | `01/assets/reference-frames/r005e01.png` | `019eb1d4-ad94-7de2-8b7f-ff7c92cf1d92` | 通过：粮袋墙压上半画面，小吏高位，白册/骨算盘/粮牌为制度中心，村民低位，冷雾与材质可读。 |
| `SC002-SH002` | `E01_R006` | `01/assets/reference-frames/r006e01.png` | `019eb1d2-4cb4-7ec2-ae44-d18e0bb46090` | 通过：祖牌小盒、半斗粮、湿泥、儿童手印和奴兵扣腕清楚，处理克制。 |
| `SC002-SH003` | `E01_R007` | `01/assets/reference-frames/r007e01.png` | `019eb1b3-f276-7991-8a87-88436520aac9` | 通过：白册前景、小吏/妇人/奴兵中景、粮袋墙背景三层清楚，无随机可读文字。 |
| `SC002-SH004` 首帧 | `E01_R008` | `01/assets/reference-frames/r008e01.png` | `019eb18d-9329-7ec2-b3d7-5c71281e01b2` | 通过：祖牌和虫蜡手印在前景，粮袋正被拖上车，妇人与孩子低在门槛内。 |
| `SC002-SH004` 终帧 | `E01_R009` | `01/assets/reference-frames/r009e01.png` | `019eb18e-023a-79b1-9445-4ae2546b4b85` clean task 无可取回图；同隔离提示词当前线程 fallback 源图已归档 | 通过：空门槛、祖牌小盒、冷白手印、泥水和远去车辙清楚，可作为 FLF2V 终点。 |

## 技术校验

- `E01_R005`-`E01_R009` 均为 `3840x2160` PNG、无 alpha；按当前 16:9 video reference frame 合同，最终交付前需重生或升采样到 `4096x2304`。
- `E01_C016B`, `E01_C017`, `E01_C023`, `E01_L003`, `E01_P003`, `E01_P008` 均为 PNG，无 alpha，满足各自卡片最低尺寸要求。
- `01/art/asset-index.json`、`01/art/asset-manifest.json`、`01/prompts/art-image-prompts.json` 和 `01/art/thread-results.json` 已写回 SC002 范围内通过状态。
- 未发现需要重做的 SC002 分镜资产；当前无 blocked image job。

## 交接建议

将 SC002 交回 `director-room` 做 prompt refresh：使用 `E01_R005`-`E01_R009` 作为 SC002 I2V/FLF2V 首尾帧，保留本轮通过的依赖资产作为角色、地点和道具参考，不再沿用旧的 `pending_user_visual_qc` 状态。
