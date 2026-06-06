# B06_COSTUMES 资产 QC 报告

## 状态

- 项目根目录：`project/severed-homeland`
- 批次：`B06_COSTUMES`
- 状态：`complete`
- 完成日期：2026-06-05
- 生成方式：当前线程使用内置 imagegen 直接生成；旧后台线程 `019e964c-1f23-7bc1-b92f-62ff9658b209` 曾因 TooManyRequests 阻塞，未写入目标图。K004-K006 在本轮重新生成并写入 canonical 路径。

## 最终资产

| ID | 文件 | 路径 | QC |
| --- | --- | --- | --- |
| K001 | `k001m.png` | `assets/costumes/k001m.png` | passed |
| K002 | `k002m.png` | `assets/costumes/k002m.png` | passed |
| K003 | `k003m.png` | `assets/costumes/k003m.png` | passed |
| K004 | `k004m.png` | `assets/costumes/k004m.png` | passed |
| K005 | `k005m.png` | `assets/costumes/k005m.png` | passed |
| K006 | `k006m.png` | `assets/costumes/k006m.png` | passed |

## 合同验证

- 文件格式：六张均为 PNG。
- 分辨率：六张均为 3840x2160。
- 画幅：16:9 landscape widescreen。
- 透明策略：六张均无 alpha。
- 文件名：`k001m` 到 `k006m` basename 均为 5 字符，符合短文件码规则。
- 版本策略：旧拒稿只保留在 `assets/costumes/history/` 并使用 `.v001` / `.v002` 后缀；canonical 路径只保留最终确认图；未创建版本目录。
- 资产类型：六张均为 neutral costume-system board，不是最终视频帧。

## 视觉 QC

- K001 保留沈维桑灰褐猎衣、火后焦黑状态、旧驿逃亡层、灰麻披风、旧皮肩护、雪线绑腿和左肩旧伤穿戴限制。
- K002 区分晏南枝流亡遮蔽外袍、深墨蓝内层、红线束发、藏匿月白玉片与旧帝国身份揭示正装。
- K003 区分沈照眠村中浅灰短襦/草药绿小围裙与清明院白色儿童袍，保留烧焦发绳和草药袋锚点。
- K004 区分白翳高官、基层虫吏、奴兵和短军袍士兵层级；黑日白翼徽记可读，已避免旧稿的虫甲胸牌漂移。
- K005 区分北境鹿族、狼族、白熊、牛族、雪羽斥候的材质、阶层和职能；作为北境粗粝材质层级板通过，但后续角色卡继承时必须保持可穿戴裁片、包边和缝线，不能放大为乞丐破布或灾民碎布。
- K006 区分残阳坳、金河、逃荒家庭、旧都渡口、边墙军户和南缘遗民的人族地域服装；旧感通过补丁、针脚、污渍和磨损表达，没有使用碎布条贫困速记。

## 更新记录

- `art/series-thread-plan.json`：B06 状态改为 `complete`，记录 final files、K004-K006 源图、hash 和 QC。
- `art/series-thread-results.json`：B06 线程结果改为 `complete`，移除 B06 blocked item，并记录 K005 继承限制。
- `assets/asset-index.json`：K001-K006 状态改为 `complete` / `generated_qc_passed` / `passed`。
- `prompts/series-art-image-prompts.json`：K001-K006 prompt metadata 状态改为 `complete` / `passed`，K004-K006 记录本轮 imagegen 源图。
- `art/series-asset-plan.md`：人读版状态改为 `partial_b06_complete_downstream_pending`。

## 后续

B06 已解除 B01_CORE_CHARACTERS 与 B02_NORTHERN_AND_FACTION_TEMPLATES 的服装依赖；下一个可派发批次是 B01 或 B02。
