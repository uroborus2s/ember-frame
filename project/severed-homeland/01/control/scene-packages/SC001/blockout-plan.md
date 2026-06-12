# SC001 低模搭建与导出计划

## 目的

用同一个 Blender 场景验证 `r001e01.png`、`r002e01.png`、`r003e01.png`、`r004e01.png` 四个参考帧是否来自同一面锁喉关黑石城墙、同一个城门、同一座门楼和同一口骨钟。低模不是最终美术图，而是空间、机位、深度、线稿和后续生图 ControlNet/参考图的证据。

## 搭建顺序

1. 按 `layout.yaml` 建立坐标系、墙体、城门、女墙、门楼主体、门楼木架、钟架、骨钟、旗帜、攻城梁/猛犸角、兽族剪影、守军枪线。
2. 放置年轻军户、脱手断矛、薛临墙和墙顶守军剪影。
3. 建立四个摄像机：
   - `CAM_R001_EXTERIOR_WIDE`
   - `CAM_R002_EXTERIOR_CLOSER_IMPACT`
   - `CAM_R003_GATEHOUSE_AFTERSHOCK`
   - `CAM_R004_XUE_REAR_THREE_QUARTER`
4. 同场景导出顶视图和机位图，用于证明相对位置。
5. 同场景逐摄像机导出导演视角图、深度图、线稿图。
6. 写入 `blockout-export-manifest.json`，记录每个输出的生成状态、工具、输入和阻塞原因。

## 必须导出的文件

- `blockout.blend`
- `top-view.png`
- `camera-map.png`
- `shot-guides/r001_camera.png`
- `shot-guides/r002_camera.png`
- `shot-guides/r003_camera.png`
- `shot-guides/r004_camera.png`
- `depth/r001_depth.png`
- `depth/r002_depth.png`
- `depth/r003_depth.png`
- `depth/r004_depth.png`
- `lineart/r001_lineart.png`
- `lineart/r002_lineart.png`
- `lineart/r003_lineart.png`
- `lineart/r004_lineart.png`

## 质量门槛

- R001 与 R002 必须同轴：两个摄像机都在墙外负 `y` 侧，朝同一城门推进。
- R002 必须比 R001 更靠近城门，且目标仍落在同一城门撞击点。
- R003 必须位于门楼内侧，按前景断矛、中景军户、后景骨钟三层组织。
- R004 必须从门楼后侧看向薛临墙与外侧女墙，后景仍可保留同一骨钟空间锚点。
- 顶视图中攻城方向只能从 `y<0` 向 `y=0`，不得出现城内侧兽潮。
- 骨钟位置在所有可见镜头中必须保持 `[-4.8, 5.7, 13.2]` 附近，不得漂移。
- 旗帜位置必须在墙顶外侧两端，且作为 P017 肃明旗位，不得替换阵营。

## 当前执行状态

本机当前未发现可执行 Blender：

- `command -v blender`：无输出。
- `/Applications/Blender.app/Contents/MacOS/Blender`：不存在。
- `bpy` Python 模块：不可用。

因此本轮已生成可复跑的 Blender Python 脚本 `build_sc001_blockout.py`，但实际 `.blend` 和 PNG 导出必须等待 Blender 安装或路径配置后执行。不得把未生成的控制图标记为 `ready`。
