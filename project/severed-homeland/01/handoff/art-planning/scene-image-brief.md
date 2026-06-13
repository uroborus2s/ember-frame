# SC001 场景图片资源交接简报

## 范围

本交接只覆盖第 01 集 SC001 的四个参考帧槽位：

- `r001e01.png`：`SC001-SH001` 首帧，墙外正中对称攻城建立。
- `r002e01.png`：`SC001-SH001` 尾帧，同一外侧轴线更近撞门。
- `r003e01.png`：`SC001-SH002` 首帧，门楼内 `E01_C024A` 年轻军户被震倒但活着、断矛脱手、同一昭明旧帝国金属警钟横摆。
- `r004e01.png`：`SC001-SH003` 首帧，薛临墙在同一门楼/女墙前低声提醒。

## 空间依据

权威空间文件：

- `01/control/scene-packages/SC001/scene-bible.md`
- `01/control/scene-packages/SC001/layout.yaml`
- `01/control/scene-packages/SC001/blockout-plan.md`
- `01/control/scene-packages/SC001/build_sc001_blockout.py`
- `01/assets/director-room/scenes/SC001/material-lock.json`

R001/R002 必须保持同一墙外攻城方向；R003/R004 必须使用同一门楼、同一昭明旧帝国金属警钟、同一墙顶/女墙关系。墙外攻城剪影必须继承 `C020`、`C021`、`E01_C020` 的兽族士兵与伴生兽关系；警钟残徽只继承 `P016`，`P018` 只允许在攻城方器具、兽皮旗、鞍具或远景盾面上作为小标记。若任何生图候选破坏空间关系，应先返修 `layout.yaml` 和 Blender 低模，而不是只改提示词。

## 场景母版

SC001 已从同一个 Blender 场景导出统一材质/贴图母版：

- `01/assets/director-room/scenes/SC001/master-reference-front.png`
- `01/assets/director-room/scenes/SC001/master-reference-reverse.png`
- `01/assets/director-room/scenes/SC001/key-prop-placement.png`
- `01/assets/director-room/scenes/SC001/blocking-overview.png`

这些图和 R001-R004 的 `shot-guides`、`depth`、`lineart` 使用同一套材质锁。城墙后方城市只作为低细节远景背板使用，不是完整城市 set，也不得改变一墙一门的空间结构。

## 当前工具状态

- Blender：可用，已生成 `.blend`、顶视图、机位图、深度图、线稿图和统一材质/贴图场景母版。
- ComfyUI：Web/API 可达，但 checkpoint 与 ControlNet 列表为空，关键帧生成任务为 `blocked_comfyui_model_missing`。
- Krita/GIMP：已安装，可用于后续 mask、脸、道具、局部修图，但本轮没有生成候选图，因此未调用。

## 图片生成要求

生成候选图时不得直接覆盖现有 `01/assets/reference-frames/r001e01.png` 到 `r004e01.png`。候选图应先输出到：

- `01/assets/director-room/shots/SC001-SH001/candidates/`
- `01/assets/director-room/shots/SC001-SH002/candidates/`
- `01/assets/director-room/shots/SC001-SH003/candidates/`

人工或导演 QC 通过后，再决定是否晋升为 canonical 参考帧。

## 关键负面规则

- 不要第二道城墙、第二个城门、城内侧兽潮、墙内攻城方向、越墙反向、90 度转向、180 度调头。
- 不要把 R001/R002 改成警钟特写；昭明旧帝国金属警钟在第一镜只作为门楼内部钟声存在。
- 不要把 R003/R004 的警钟换位置、换钟架或换高度；不要把它画成骨质/象牙，也不要把 `P018` 兽族徽章画到钟面上。
- 不要把墙外攻城方画成人族军阵、通用单一兽人群或无主怪物潮；必须继承 `C020`/`C021`/`E01_C020`。
- 不要把 R003 年轻军户画成闭眼尸体；他应半睁眼或眯眼、喘息、撑地、屈膝失衡。
- 不要随机旗帜；墙顶旗帜必须继承 P017 肃明虫族帝国黑日白翅旗。
- 不要用风雪遮掉人物重心、手部、断矛、钟链和女墙。
