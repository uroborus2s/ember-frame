# 地点资产复核重做与补强 QC 复核

- 项目：`severed-homeland`
- 日期：2026-06-07
- 子任务：`019e9fea-a45c-70a3-8244-cbb722eef36c`
- 调度提示词：`art/runs/location-revision-2026-06-07/dispatch-prompt.md`
- 提示词修改方案：`art/reviews/location-prompt-revision-plan-2026-06-07.md`
- 当前 canonical 九宫格：`art/runs/location-revision-2026-06-07/location-canonical-contact-sheet.png`

## 结论

本轮 9 个地点资产通过父任务复核，可进入当前 canonical 使用。所有最终文件均为 PNG、RGB、3840x2160、16:9、无 alpha 通道。

子任务最终落位的 canonical 图与父任务中转候选 PNG 不是字节级一致，因此本报告以当前 canonical 文件为准重新审阅。旧 canonical 字节已能在对应最新 `assets/locations/history/` 版本中追溯，归档链未断。

## 逐项复核

| 资产 | 处理类型 | canonical | history | QC 结论 |
| --- | --- | --- | --- | --- |
| L009 寒鸦 | 复核重做 | `assets/locations/l009m.png` | `assets/locations/history/l009m.v003.png` | 通过。城防、档案桌、寒鸦旗、门禁和雪地纵深可读，黑石堡垒与情报场景明确。 |
| L004 灰烬书院 | 复核重做 | `assets/locations/l004m.png` | `assets/locations/history/l004m.v005.png` | 通过。焚毁书院、木构藏书、封蜡、星盘与人物行动线明确；少量纸页伪字不可读。 |
| L007 锁喉关边墙主门 | 复核重做 | `assets/locations/l007m.png` | `assets/locations/history/l007m.v003.png` | 通过。主门、边墙、粮车、队列和火把检查点清晰，守关压迫感成立。 |
| L010 月下盟书旧驿 | 复核重做 | `assets/locations/l010m.png` | `assets/locations/history/l010m.v004.png` | 通过。旧驿内部、盟书地面痕迹、红帘、低光人物与月夜冷光分层明确；局部纸面纹理不可读。 |
| L011 坍塌烽燧 | 复核重做 | `assets/locations/l011m.png` | `assets/locations/history/l011m.v004.png` | 通过。坍塌塔基、雪坡逃亡、红旗布片、盟书碎片与远队行动线明确。 |
| L006 墙下集市 | 美术补强 | `assets/locations/l006m.png` | `assets/locations/history/l006m.v005.png` | 通过。摊布色彩、黑市桌面、铜币/筹码、人群层级和墙下市井关系明显增强。 |
| L003 金河粮磨区与渡船 | 美术补强 | `assets/locations/l003m.png` | `assets/locations/history/l003m.v005.png` | 通过。金色粮田、青绿河面、码头渡船、粮运和远城空间被拉开，地域识别增强。 |
| L001 残阳坳村落与药屋 | 美术补强 | `assets/locations/l001m.png` | `assets/locations/history/l001m.v003.png` | 通过。药屋、草药田、旧井、村路和暖色山坳关系清晰；右侧布条/纸面纹理不可读。 |
| L005 清明院外署白墙 | 只做色彩处理 | `assets/locations/l005m.png` | `assets/locations/history/l005m.v005.png` | 通过。白墙外署构图保持，冷金、蜡绿、黑旗与室内暖纸光增加层次，未改成暖宫殿。 |

## 风险与备注

- L004、L010、L001 存在少量不可读伪文字纹理，当前未形成可读文本，可接受。
- L005 严格按“只做色彩处理”边界处理：主体白墙、机构气质和构图未重做。
- 子任务额外生成了 1 张未使用原图，未纳入 canonical。
