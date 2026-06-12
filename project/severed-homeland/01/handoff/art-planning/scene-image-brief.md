# SC001 场景图片资源交接简报

## 范围

本交接只覆盖第 01 集 SC001 的四个参考帧槽位：

- `r001e01.png`：`SC001-SH001` 首帧，墙外正中对称攻城建立。
- `r002e01.png`：`SC001-SH001` 尾帧，同一外侧轴线更近撞门。
- `r003e01.png`：`SC001-SH002` 首帧，门楼内年轻军户半倒、断矛脱手、同一骨钟横摆。
- `r004e01.png`：`SC001-SH003` 首帧，薛临墙在同一门楼/女墙前低声提醒。

## 空间依据

权威空间文件：

- `01/control/scene-packages/SC001/scene-bible.md`
- `01/control/scene-packages/SC001/layout.yaml`
- `01/control/scene-packages/SC001/blockout-plan.md`
- `01/control/scene-packages/SC001/build_sc001_blockout.py`

R001/R002 必须保持同一墙外攻城方向；R003/R004 必须使用同一门楼、同一骨钟、同一墙顶/女墙关系。若任何生图候选破坏空间关系，应先返修 `layout.yaml` 和 Blender 低模，而不是只改提示词。

## 当前工具状态

- Blender：不可用，本轮未能导出 `.blend`、顶视图、机位图、深度图和线稿图。
- ComfyUI：本地服务和节点配置不可用，关键帧生成任务为 `needs_config`。
- Krita/GIMP：已安装，可用于后续 mask、脸、道具、局部修图，但本轮没有生成候选图，因此未调用。

## 图片生成要求

生成候选图时不得直接覆盖现有 `01/assets/reference-frames/r001e01.png` 到 `r004e01.png`。候选图应先输出到：

- `01/assets/director-room/shots/SC001-SH001/candidates/`
- `01/assets/director-room/shots/SC001-SH002/candidates/`
- `01/assets/director-room/shots/SC001-SH003/candidates/`

人工或导演 QC 通过后，再决定是否晋升为 canonical 参考帧。

## 关键负面规则

- 不要第二道城墙、第二个城门、城内侧兽潮、墙内攻城方向、越墙反向、90 度转向、180 度调头。
- 不要把 R001/R002 改成骨钟特写；骨钟在第一镜只作为门楼内部钟声存在。
- 不要把 R003/R004 的骨钟换位置、换钟架或换高度。
- 不要随机旗帜；墙顶旗帜必须继承 P017 肃明虫族帝国黑日白翅旗。
- 不要用风雪遮掉人物重心、手部、断矛、钟链和女墙。
