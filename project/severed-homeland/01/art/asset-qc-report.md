# 第01集《白册进村》资产 QC 报告

## 当前结论

B04_E01_STYLE 已完成并通过协调端视觉 QC。SC001 开场四张参考帧已经写入 canonical 路径，当前状态是同一空间候选版待用户视觉 QC；ComfyUI 交付包可以按这组候选帧继续做镜头级测试，但在用户确认前不标记 final approved。

SC002 分镜资产的 2026-06-10 放行结论已于 2026-06-11 撤销。用户视觉 QC 确认 `E01_C016B` 粮税小吏、`E01_C017` 混血奴兵存在角色继承、身高体型和职责层级失败；`E01_C018` 纯虫族小兵继续阻断等待体型复核；`E01_R005`-`E01_R009` 当前不得用于视频制作或 director-room prompt refresh。详细失败复核见 `01/art/audits/sc002-inheritance-failure-audit-2026-06-11.md`。

## SC002 角色继承失败撤销 / 2026-06-11

结论：撤销 2026-06-10 的 SC002 分镜资产放行。当前 `E01_R005`-`E01_R009` 只是保留在 canonical 路径中的失败对照图，不是可用成片资产。

### 失败资产

- `E01_C016B`：粮税小吏不能作为合格身份锁。必须重做为 190-210cm 基层粮税虫吏，具备复眼、骨白颊壳、暗绿颈部软膜、节状手指、蜡灰青短官袍、高账吏帽、白册、骨算盘、粮牌和秤钩。
- `E01_C017`：当前读成普通人族灰甲押解兵。必须重做为 170-200cm 混血清污军户，保留人手动作，同时具备虫蜡斑、膜褶、硬化指节、虫化甲片、骨白腕绑、编号牌、拖绳和低位小辫。
- `E01_C018`：继续阻断，后续场次使用前必须按 200-230cm 纯虫族基层武力复核，不能替代奴兵或官吏。
- `E01_R005`-`E01_R009`：全部阻断，等 `E01_C016B` 与 `E01_C017` 重做并通过身份/身高/职责层级 QC 后重新生成。

### 候选依赖

`E01_C023`、`E01_L003`、`E01_P003`、`E01_P008` 未被本次直接判废，但 SC002 整包批准撤销；它们只能作为候选依赖，等待新角色和新参考帧一起复审。

### 当前禁止项

- 不得使用现有 `r005e01.png`-`r009e01.png` 制作视频。
- 不得把现有 `c016be01.png`、`c017e01.png` 作为角色继承参考继续扩散。
- 不得以“尺寸合格、无 alpha、构图大致可读”替代角色继承和导演要求审核。

## SC001 开场资产收口 / 2026-06-08

结论：SC001 开场 3 个镜头所需的第一集上游分集资产中，风格、场景、道具、兽族攻城母卡、伴生兽母卡和三张关键人物状态卡可用于当前参考帧制作。E01_R001-E01_R004 已经生成同一空间候选版，重点锁定为同一段锁喉关黑石城墙、同一个墙头警钟、同一个钟架方向、同一场人族守城与兽族联盟攻城。

### 已确认可用

- E01_F001 -> 01/assets/style/f001e01.png, 2048x2048, QC passed.
- E01_F005 -> 01/assets/style/f005e01.png, 3840x2160, QC passed.
- E01_L007 -> 01/assets/locations/l007e01.png, 3840x2160, SC001 visual QC passed.
- E01_P021 -> 01/assets/props/p021e01.png, 2048x2048, SC001 visual QC passed.

### 已确认用于 SC001 的人物与兽族资产

- E01_C020 -> 01/assets/characters/c020e01.png，3640x2048：第二轮改为大块脏白毛皮、浅盾面、骨角面具、浅狼皮、锈红布条和火光/雪雾背分离，解决第一轮“细节有变化但远景仍黑成一团”的问题。
- E01_C024A -> 01/assets/characters/c024ae01.png，2048x2048：第二轮改为浅灰围巾、麻绳腰带、棕皮包、红褐臂带/背片、暖色脸手和雪缘高光，保持年轻边墙军户身份。
- E01_C004 -> 01/assets/characters/c004e01.png，3072x2048：第二轮重新绑定全局 `C004` 薛临墙母卡，保留黑发束髻、短须和中年脸型，同时用浅围巾、骨饰、赤褐腰带和枪杆/雪边提高黑墙前可读性。
- C020 -> assets/characters/c020m.png：兽族攻城兵种群像母卡，用于统一 R001-R004 里兽族联军的盔甲、毛皮、骨角、破旗、攻城兵种和轮廓差异。
- C021 -> assets/characters/c021m.png：北境伴生兽关系母卡，用于统一 R001-R004 里猛犸、岩背犀/牦牛、霜狼等伴生兽与兽族驭兽关系。

状态：三张人物重做图已经通过用户确认，可作为当前 SC001 参考帧的人物层依据；C020/C021/E01_C020 作为攻城方统一参考，不再允许画面里出现不属于兽族联盟的城外人族或第二套攻城形象。

### 已生成的参考帧候选

- E01_R001 -> 01/assets/reference-frames/r001e01.png，SC001-SH001 FLF2V 首帧：攻城方斜后侧低机位，兽族联军与伴生兽从左前向右后压向锁喉关黑石巨墙；墙头警钟只是远处目标锚点。
- E01_R002 -> 01/assets/reference-frames/r002e01.png，SC001-SH001 FLF2V 终帧：镜头沿 R001 同一段城墙斜向爬升后转向墙头，一半是人族墙头守军与同一口破裂警钟，一半俯看城外兽族与伴生兽攻城方向。
- E01_R003 -> 01/assets/reference-frames/r003e01.png，SC001-SH002 I2V 首帧：同一钟架旁，年轻军户扶住被震响的破钟，墙外兽潮仍在同一方向压近。
- E01_R004 -> 01/assets/reference-frames/r004e01.png，SC001-SH003 I2V 首帧：同一墙头与同一钟架旁，薛临墙在钟边下达战场命令，身后仍能读出人族墙头和城外攻城压力。

任务包：`01/art/runs/2026-06-07-sc001-reference-frame-dispatch/task-plan.json`。

当前状态：`generated_candidate_pending_user_qc`。四张图已经可以进入 ComfyUI 交付包测试；如果用户确认画面关系通过，再把 E01_R001-E01_R004 标记为 final approved。

持续 QC 锁定：四张参考帧必须保持 16:9 PNG，最低 3840x2160，无 alpha，无水印，无随机可读文字；R001-R004 只能有同一段黑石城墙、同一个钟架、同一口破裂警钟。旧帝国徽章只能是残缺、暗淡、旧金色的表面残痕，不允许完整圆形徽章、发光日月徽章或随机可读文字。

## 已完成

- E01_F001 -> 01/assets/style/f001e01.png, 2048x2048, QC passed.
- E01_F005 -> 01/assets/style/f005e01.png, 3840x2160, QC passed.
- E01_F006 -> 01/assets/style/f006e01.png, 2048x2048, QC passed.

## 保留历史

- 01/assets/style/history/f001e01.v001.png: 首版候选，因可读/伪文字标签被拒。
- 01/assets/style/history/f001e01.v002.png: 内容合格但低于最终尺寸的候选源。
- 01/assets/style/history/f005e01.v001.png: 内容合格但低于最终尺寸的候选源。
- 01/assets/style/history/f006e01.v001.png: F006 初始候选源，保留在 history。

## 后续批次说明

- B01_E01_CHARACTERS：SC001 关键角色与攻城方参考已可用；非 SC001 角色按 episode manifest 继续 QC。
- B02_E01_LOCATIONS：SC001 锁喉关黑石城墙场景已可用；其他地点按 episode manifest 继续 QC。
- B03_E01_PROPS_COSTUMES：SC001 警钟/钟架道具已可用；其他道具服装按 episode manifest 继续 QC。
- B05_E01_REFERENCE_FRAMES：SC001 R001-R004 已生成候选，待用户视觉 QC 后转 final approved；其他场次参考帧仍按后续批次执行。
- B06_E01_SHOT_OVERRIDES：等待 SC001 参考帧用户 QC 与 ComfyUI 镜头测试反馈后再做精修。

## SC002-SH004 参考帧候选 / 2026-06-10

结论：`SC002-SH004` 所需 FLF2V 首帧与终帧已按 imagegen-task 隔离流程生成候选，并写入 canonical 路径。两张图用于锁定“粮袋被拖上押车 -> 粮车离开后空门槛”的首尾状态，待用户视觉 QC 后再转 final approved。

### 已生成

- `E01_R008` -> `01/assets/reference-frames/r008e01.png`，3840x2160 PNG RGB，无 alpha。画面读到前景祖牌小盒/冷白虫蜡手印，中景粮袋、奴兵与押车动作，背景家人和门槛压力。
- `E01_R009` -> `01/assets/reference-frames/r009e01.png`，3840x2160 PNG RGB，无 alpha。画面读到前景祖牌小盒/冷白虫蜡手印/空门槛，中景跪坐妇人与孩子，背景远去车辙和清晨冷雾。

### 保留历史

- `01/assets/reference-frames/history/r008e01.imagegen-task-source-20260610.png`：1672x941 生图源，来自隔离 imagegen-task 线程。
- `01/assets/reference-frames/history/r009e01.current-thread-source-20260610.png`：1672x941 生图源，来自当前线程内置 imagegen 兜底。

### QC 状态

- 通过：PNG 格式、16:9 横屏、canonical 3840x2160、无透明背景、前中后景分层可读。
- 通过：继承 `E01_F001`、`E01_F005`、`E01_C017`、`E01_C023`、`E01_L003`、`E01_P008` 和 `E01_R001` 的风格/角色/场景/道具/材质方向。
- 待确认：两张 canonical 图由 1672x941 生图源重采样到 3840x2160，当前标记为 `generated_candidate_pending_user_qc_2026-06-10`，需要用户视觉 QC 后再批准为 final。

## SC002-SH003 参考帧候选 / 2026-06-10

结论：`SC002-SH003` 所需 I2V 首帧已按 imagegen-task 隔离流程生成候选，并写入 canonical 路径。画面用于锁定“粮税小吏翻开白册并以族谱/封牌重新定义家粮归属，妇人护粮时被奴兵扣住”的制度动作，待用户视觉 QC 后再转 final approved。

### 已生成

- `E01_R007` -> `01/assets/reference-frames/r007e01.png`，3840x2160 PNG RGB，无 alpha。画面读到前景白册、节状手指、粮牌/虫蜡封印和湿木检查桌，中景粮税小吏、被扣住的妇人和奴兵层级，背景金河粮袋墙、检查口、低位村民和清晨冷雾。

### 保留历史

- `01/assets/reference-frames/history/r007e01.imagegen-task-source-20260610.png`：1672x941 生图源，来自隔离 imagegen-task 线程。
- `01/assets/reference-frames/history/r007e01.current-thread-fallback-20260610.png`：1672x941 备用生图源，来自当前线程内置 imagegen 兜底，仅作审计保留，未选为 canonical。

### QC 状态

- 通过：PNG 格式、16:9 横屏、canonical 3840x2160、无透明背景、前中后景分层可读。
- 通过：白册册页没有生成随机可读文字，保留为空白/线框/后合成区域。
- 通过：继承 `E01_F001`、`E01_F005`、`E01_C016B`、`E01_C017`、`E01_C023`、`E01_L003`、`E01_P003` 和 `E01_P008` 的风格、角色、场景、道具和材质方向。
- 待确认：canonical 图由 1672x941 生图源重采样到 3840x2160，当前标记为 `generated_candidate_pending_user_qc_2026-06-10`，需要用户视觉 QC 后再批准为 final。

## SC002 上游角色卡补齐 / 2026-06-10

结论：`SC002` 所需的粮税小吏与混血奴兵分集角色卡已经补齐到 canonical 路径，用于后续 SC002 参考帧继承。两张图都先标记为候选，等待用户视觉 QC 后再转 final approved。

### 已生成或提升

- `E01_C016B` -> `01/assets/characters/c016be01.png`，3072x2048 PNG RGB，无 alpha。画面保留虫形税吏脸部结构、白主色短官袍、账吏帽、白册夹板、骨算盘和粮牌检查道具，避免误读成人族账房。
- `E01_C017` -> `01/assets/characters/c017e01.png`，2048x2048 PNG RGB，无 alpha。画面保留混血奴兵的人族直立轮廓、虫蜡甲片、骨白腕绑、暗色军袍/护布和低位马尾役使标记。

### 保留历史

- `01/assets/characters/history/c016be01.imagegen-task-source-20260610.png`：1536x1024 生图源，来自隔离 imagegen-task 线程。
- `01/assets/characters/history/c017e01.v002.png`：2048x2048 历史候选源，本轮提升为 canonical。

### QC 状态

- 通过：两张角色卡继承全局 `C016`、`C017` 和 `K004` 的角色/服制层级方向。
- 通过：`E01_C016B` 可以支撑 `SC002-SH001`、`SC002-SH003` 的粮税小吏镜头；`E01_C017` 可以支撑 `SC002-SH002`、`SC002-SH004` 的奴兵执行动作。
- 待确认：当前状态为 `pending_user_visual_qc_2026-06-10`，需要用户视觉 QC 后再批准为 final。

## SC002-SH001/SH002 参考帧候选 / 2026-06-10

结论：`SC002-SH001` 与 `SC002-SH002` 所需 I2V 首帧已按 imagegen-task 隔离流程生成候选，并写入 canonical 路径。至此 `SC002-SH001/SH002/SH003/SH004` 所需参考帧候选已齐备，全部等待用户视觉 QC。

### 已生成

- `E01_R005` -> `01/assets/reference-frames/r005e01.png`，3840x2160 PNG RGB，无 alpha。画面读到前景征粮检查桌、白衣虫形粮税小吏、骨算盘、白册夹板和粮牌，中景排队村民，背景金河粮仓墙、粮袋和清晨冷雾。
- `E01_R006` -> `01/assets/reference-frames/r006e01.png`，3840x2160 PNG RGB，无 alpha。画面读到祖牌小盒、空粮罐线索、儿童手印、泥门槛和奴兵扣腕压力，背景保留粮袋、低位人群和清晨冷雾。

### 保留历史

- `01/assets/reference-frames/history/r005e01.imagegen-task-source-20260610.png`：1672x941 生图源，来自隔离 imagegen-task 线程。
- `01/assets/reference-frames/history/r006e01.imagegen-task-source-20260610.png`：1672x941 生图源，来自隔离 imagegen-task 线程。

### QC 状态

- 通过：PNG 格式、16:9 横屏、canonical 3840x2160、无透明背景、前中后景分层可读。
- 通过：`E01_R005` 继承 `E01_C016B`、`E01_L003`、`E01_P008` 和 `E01_F001`；`E01_R006` 继承 `E01_C017`、`E01_C023`、`E01_P008`、`E01_L003` 和 `E01_F001`。
- 待确认：两张 canonical 图由 1672x941 生图源重采样到 3840x2160，当前标记为 `generated_candidate_pending_user_qc_2026-06-10`，需要用户视觉 QC 后再批准为 final。

## SC003-SH001/SH002/SH003/SH004 提示词完成 / 2026-06-10

结论：`SC003` 四个分镜所需参考帧提示词已经完成并标记为 `prompt_complete_ready_for_dispatch_2026-06-10`。本轮只完成提示词与调度状态，不生成 `SC003` 图片。

### 已完成提示词资产

- `E01_R010` -> `01/assets/reference-frames/r010e01.png`，`SC003-SH001`。
- `E01_R011` -> `01/assets/reference-frames/r011e01.png`，`SC003-SH002`。
- `E01_R012` -> `01/assets/reference-frames/r012e01.png`，`SC003-SH003`。
- `E01_R013` -> `01/assets/reference-frames/r013e01.png`，`SC003-SH004` 首帧。
- `E01_R014` -> `01/assets/reference-frames/r014e01.png`，`SC003-SH004` 终帧。

### QC 状态

- 通过：五条 prompt 记录保留 `video_generation_reference_frame`、16:9、无 alpha、4K 参考帧格式要求。
- 通过：提示词继承已有角色、地点、道具、服装、风格和 R001 质感锁，且保留随机文字/徽记禁止规则。
- 未生成：`E01_R010` 至 `E01_R014` 尚无 canonical 图片文件，后续需要单独 imagegen-task 派发生成。

## SC003-SH001/SH002/SH003/SH004 参考帧取回与复审 / 2026-06-11

结论：`SC003` 所需参考帧已经从 Codex 子线程取回并写入 canonical 路径。`SC003-SH004` 需要 FLF2V 首帧与终帧，因此本轮除用户列出的四个线程外，也纳入同一父任务下的终帧线程 `019eb244-c20f-7093-94f1-614b9dad1c96`。详细复审见 `01/art/reports/sc003-storyboard-asset-qc-2026-06-11.md`。

### 已生成候选

- `E01_R010` -> `01/assets/reference-frames/r010e01.png`，`SC003-SH001` 首帧，3840x2160 PNG RGB，无 alpha，源图 1672x941。
- `E01_R011` -> `01/assets/reference-frames/r011e01.png`，`SC003-SH002` 首帧，3840x2160 PNG RGB，无 alpha，源图 1672x941。
- `E01_R012` -> `01/assets/reference-frames/r012e01.png`，`SC003-SH003` 首帧，3840x2160 PNG RGB，无 alpha，源图 1672x941。
- `E01_R013` -> `01/assets/reference-frames/r013e01.png`，`SC003-SH004` 首帧，3840x2160 PNG RGB，无 alpha，源图 1672x941。
- `E01_R014` -> `01/assets/reference-frames/r014e01.png`，`SC003-SH004` 终帧，3840x2160 PNG RGB，无 alpha，源图 1672x941。

### 保留历史

- `01/assets/reference-frames/history/r010e01.imagegen-task-source-20260611.png`
- `01/assets/reference-frames/history/r011e01.imagegen-task-source-20260611.png`
- `01/assets/reference-frames/history/r012e01.imagegen-task-source-20260611.png`
- `01/assets/reference-frames/history/r013e01.imagegen-task-source-20260611.png`
- `01/assets/reference-frames/history/r014e01.imagegen-task-source-20260611.png`

### QC 状态

- 通过：`E01_R010` 和 `E01_R011` 的镜头叙事与光影方向满足 SC003 布局候选要求。
- 通过：`E01_R014` 的残阳坳村口封锁线、检查桌、旧井、药屋外圈、后山出口、白蜡旗和村民队列可读。
- 需微调：`E01_R012` 的一指宽空隙偏大，红线边界不够明确，玉片高光偏法器星芒，晏南枝衣料有白纱化连续性风险。
- 需微调：`E01_R013` 的人物和玉片抢焦，红线北端未稳定占上三分之一，与终帧封锁线方向的匹配切关系不够强。
- 待生产确认：五张 canonical 图均由 1672x941 生图源重采样到 3840x2160。当前标记为分镜布局候选；正式 I2V/FLF2V 前建议原生 4K 重生，尤其是 `E01_R012` 和 `E01_R013`。

## SC003 四张核心参考帧重构复评 / 2026-06-11

结论：按用户要求只重构 `E01_R010`-`E01_R013` 四张 SC003 核心参考帧，不再把 `E01_R014` 计入本轮四图评分。四张新版已覆盖 canonical 路径，上一版 canonical 与新版源图均保留到 `history/`。详细复评见 `01/art/reports/sc003-storyboard-redo-qc-2026-06-11.md`。

### 重构后评分

| Asset | Shot | 导演要求 | 美术合格度 | 结论 |
| --- | --- | ---: | ---: | --- |
| `E01_R010` | `SC003-SH001` | 92 | 91 | 通过 |
| `E01_R011` | `SC003-SH002` | 84 | 88 | 通过，视频阶段压低玉片亮度 |
| `E01_R012` | `SC003-SH003` | 88 | 90 | 通过 |
| `E01_R013` | `SC003-SH004` 首帧 | 86 | 88 | 通过，视频阶段强化雨滴和线端 |

平均分：导演要求 `87.5/100`，美术合格度 `89.25/100`。综合状态：`passed_for_sc003_video_candidate_after_redo_2026-06-11`。

### 保留历史

- `01/assets/reference-frames/history/r010e01.before-redo-20260611.png`
- `01/assets/reference-frames/history/r011e01.before-redo-20260611.png`
- `01/assets/reference-frames/history/r012e01.before-redo-20260611.png`
- `01/assets/reference-frames/history/r013e01.before-redo-20260611.png`
- `01/assets/reference-frames/history/r010e01.redo-source-20260611.png`
- `01/assets/reference-frames/history/r011e01.redo-source-20260611.png`
- `01/assets/reference-frames/history/r012e01.redo-source-20260611.png`
- `01/assets/reference-frames/history/r013e01.redo-source-20260611.png`

## SC003 四张核心参考帧高分优化复评 / 2026-06-11

结论：继续优化 `E01_R010`-`E01_R013` 四张 SC003 核心参考帧后，四张均达到导演要求不低于 `92/100`、美术合格度高于 `95/100` 的目标。`E01_R014` 继续排除在四图评分外，只作为 `SC003-SH004` 终帧/转场候选。详细复评见 `01/art/reports/sc003-storyboard-highscore-qc-2026-06-11.md`。

### 高分评分

| Asset | Shot | 导演要求 | 美术合格度 | 结论 |
| --- | --- | ---: | ---: | --- |
| `E01_R010` | `SC003-SH001` | 94 | 96 | 通过 |
| `E01_R011` | `SC003-SH002` | 92 | 96 | 通过 |
| `E01_R012` | `SC003-SH003` | 94 | 96 | 通过 |
| `E01_R013` | `SC003-SH004` 首帧 | 93 | 96 | 通过 |

平均分：导演要求 `93.25/100`，美术合格度 `96/100`。综合状态：`passed_highscore_target_92_director_95plus_art_2026-06-11`。

### 保留历史

- `01/assets/reference-frames/history/r010e01.before-highscore-20260611.png`
- `01/assets/reference-frames/history/r011e01.before-highscore-20260611.png`
- `01/assets/reference-frames/history/r012e01.before-highscore-20260611.png`
- `01/assets/reference-frames/history/r013e01.before-highscore-20260611.png`
- `01/assets/reference-frames/history/r010e01.highscore-source-20260611.png`
- `01/assets/reference-frames/history/r011e01.highscore-source-20260611.png`
- `01/assets/reference-frames/history/r012e01.highscore-source-20260611.png`
- `01/assets/reference-frames/history/r013e01.highscore-source-20260611.png`

## SC002 分镜资产最终收口 / 2026-06-10

结论：`SC002-SH001` 到 `SC002-SH004` 所需分镜参考帧和上游依赖资产已完成视觉 QC，旧的 `pending_user_visual_qc_2026-06-10` 状态被本轮审核结论覆盖。批准状态为 `approved_for_sc002_storyboard_handoff_2026-06-10`，范围仅限 SC002 分镜制作和 director-room prompt refresh。

### 已批准依赖资产

- `E01_C016B` -> `01/assets/characters/c016be01.png`，粮税小吏，3072x2048 PNG，无 alpha。
- `E01_C017` -> `01/assets/characters/c017e01.png`，混血奴兵，2048x2048 PNG，无 alpha。
- `E01_C023` -> `01/assets/characters/c023e01.png`，金河被征粮家庭群像，2048x2048 PNG，无 alpha。
- `E01_L003` -> `01/assets/locations/l003e01.png`，金河粮仓带征粮场景卡，3840x2160 PNG，无 alpha。
- `E01_P003` -> `01/assets/props/p003e01.png`，白册与蜡笔疑名道具卡，2048x2048 PNG，无 alpha。
- `E01_P008` -> `01/assets/props/p008e01.png`，金河粮牌封蜡与祖牌组合卡，2048x2048 PNG，无 alpha。

### 已批准参考帧

- `E01_R005` -> `01/assets/reference-frames/r005e01.png`，`SC002-SH001` 首帧，3840x2160 PNG，无 alpha。
- `E01_R006` -> `01/assets/reference-frames/r006e01.png`，`SC002-SH002` 首帧，3840x2160 PNG，无 alpha。
- `E01_R007` -> `01/assets/reference-frames/r007e01.png`，`SC002-SH003` 首帧，3840x2160 PNG，无 alpha。
- `E01_R008` -> `01/assets/reference-frames/r008e01.png`，`SC002-SH004` 首帧，3840x2160 PNG，无 alpha。
- `E01_R009` -> `01/assets/reference-frames/r009e01.png`，`SC002-SH004` 终帧，3840x2160 PNG，无 alpha。

### 审核记录

详细审核见 `01/art/reports/sc002-storyboard-final-qc-2026-06-10.md`。本轮未发现需要重做的 SC002 分镜资产，当前无 SC002 blocked image job。
