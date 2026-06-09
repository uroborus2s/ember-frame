# SC001 开场资产就绪报告

日期：2026-06-07

范围：第 01 集 `SC001-SH001` 到 `SC001-SH003`，即锁喉关外墙开场钩子。

## 结论

SC001 所需第一集上游分集资产中，风格、场景、道具、人物状态卡和 4 张横屏参考帧均已进入后资产交付使用状态。历史上三张人物状态卡曾等待用户 QC，现已按用户确认作为 SC001 ComfyUI 交付包输入。

## 已确认上游资产

| 资产 | 路径 | 结论 |
| --- | --- | --- |
| E01_F001 | `01/assets/style/f001e01.png` | 已通过，整体风格与材质板可用 |
| E01_F005 | `01/assets/style/f005e01.png` | 已通过，横屏构图与局部因果板可用 |
| E01_L007 | `01/assets/locations/l007e01.png` | 可用，锁喉关外墙、骨钟、门闩、枪线、拒马、动线清楚 |
| E01_P021 | `01/assets/props/p021e01.png` | 可用，骨钟、裂缝、浅日月刻痕、断矛、冻血和手部尺度清楚 |

## 第二轮人物候选 / 待用户 QC

| 资产 | 路径 | 当前尺寸 | 第二轮处理 |
| --- | --- | --- | --- |
| E01_C020 | `01/assets/characters/c020e01.png` | 3640x2048 | 用大块脏白毛皮、浅盾面、骨角面具、浅狼皮、锈红布条和火光/雪雾背分离解决黑墙前黑块化 |
| E01_C024A | `01/assets/characters/c024ae01.png` | 2048x2048 | 用浅灰围巾、麻绳腰带、棕皮包、红褐臂带/背片、暖色脸手和雪缘高光保证年轻军户远景可读 |
| E01_C004 | `01/assets/characters/c004e01.png` | 3072x2048 | 重新绑定全局 `C004` 薛临墙母卡，保留黑发束髻和短须，同时用浅围巾、骨饰、赤褐腰带和枪杆/雪边分离黑墙 |

状态：三张均为 `candidate_ready_pending_user_qc`。任务包：`01/art/runs/2026-06-07-sc001-character-rework/task-plan.json`。

## 已创建但阻塞的参考帧任务

| 任务 | 输出 | 用途 | 依赖 |
| --- | --- | --- | --- |
| SC001_E01_REFERENCE_FRAMES:E01_R001 | `01/assets/reference-frames/r001e01.png` | `SC001-SH001` FLF2V 首帧 | E01_F001, E01_F005, E01_C020, E01_L007, E01_P021 |
| SC001_E01_REFERENCE_FRAMES:E01_R002 | `01/assets/reference-frames/r002e01.png` | `SC001-SH001` FLF2V 终帧 | E01_F001, E01_F005, E01_C020, E01_L007, E01_P021 |
| SC001_E01_REFERENCE_FRAMES:E01_R003 | `01/assets/reference-frames/r003e01.png` | `SC001-SH002` I2V 首帧 | E01_F001, E01_F005, E01_C020, E01_C024A, E01_L007, E01_P021 |
| SC001_E01_REFERENCE_FRAMES:E01_R004 | `01/assets/reference-frames/r004e01.png` | `SC001-SH003` I2V 首帧 | E01_F001, E01_F005, E01_C004, E01_L007 |

任务提示词来源：`01/prompts/art-image-prompts.json`。

任务包路径：`01/art/runs/2026-06-07-sc001-reference-frame-dispatch/task-plan.json`。

历史阻塞条件：`E01_C020`、`E01_C024A`、`E01_C004` 第二轮候选通过用户 QC 后，才允许生成 `E01_R001` 到 `E01_R004`。当前交付状态按用户确认处理为已解除；`r001e01.png` 到 `r004e01.png` 已存在于 `01/assets/reference-frames/`，尺寸均为 3840x2160。

## 后续收口

1. 先对 `E01_C020`、`E01_C024A`、`E01_C004` 第二轮候选做人审。
2. 通过后解除 `E01_R001` 到 `E01_R004` 的阻塞并生成参考帧。
3. 参考帧生成时继续执行黑墙远景可读性约束：大色块、雪雾背分离、火光/冷边缘光、人物不贴黑墙死角。
4. 对四张参考帧做视觉 QC。
5. 通过后把 `01/art/asset-index.json` 与 `01/art/asset-manifest.json` 中 E01_R001 到 E01_R004 更新为 `complete_qc_passed`。
6. 再运行 director-room 的 post-asset pass，生成 SC001 或第 01 集范围的 ComfyUI 交付包。

## 2026-06-08 场景修正

- SC001 四张参考帧必须属于同一个墙头警钟空间：人族守城方在墙头，兽族联盟攻城方在墙外/墙下。
- 骨钟是城墙上的守城警钟，安装在墙头木铁警钟架中；撞门/撞墙冲击传上城墙，使警钟震响。
- 昭明旧帝国日月徽章只能是残缺淡金旧痕：被裂缝、铜锈、雪泥吃掉，不能完整展示。
- R001/R002 表现警钟被震响前后；R003 转到同一警钟旁年轻军户扶钟；R004 转到同一墙头空间中薛临墙低声提醒敌人逼近。
- 薛临墙台词更新为：敌人上来了。语气要求：压低、急促但不慌，像把墙头所有人的视线从骨钟拉回门线。

## 2026-06-08 ComfyUI 交付收口

- `SC001-SH001` 已从“短推拉战场远景”修正为“斜侧攻城升镜”：R001 从攻城方斜后侧低机位看同一面黑石墙，R002 顺同一面墙斜爬上墙头后约 45 度转向人族女墙空间。
- R001-R004 当前硬锁：同一面黑石城墙、同一个墙头钟架、同一口破骨钟；R002/R003/R004 必须继承 R001 里墙头警钟的位置和钟架方向。
- 城外只能出现面向同一面城墙攻来的兽族士兵和伴生兽，不得出现第二道城墙、第二个门楼、第二个钟架或城外人族。
- 兽族士兵与伴生兽必须继承 `assets/characters/c020m.png`、`assets/characters/c021m.png`、`01/assets/characters/c020e01.png`，需要读出多兵种与多伴生兽，而不是单一种类或泛化兽群。
- `SC001-SH001` 前推期间读时代事件旁白：肃明历1226年，北境十三部落联盟大举入寇。
- `SC001-SH002` 末尾落压迫对句旁白：北关五百载，白骨未成尘。
- `SC001-SH001` 使用 `E01_R001` / `E01_R002` 作为 FLF2V 首尾参考帧。
- `SC001-SH002` 使用 `E01_R003` 作为 I2V 首帧。
- `SC001-SH003` 使用 `E01_R004` 作为 I2V 首帧。
- ComfyUI 交付包已落到 `01/prompts/comfyui-prompt-brief.md`、`01/prompts/comfyui-style-preset.json`、`01/prompts/comfyui-asset-prompt-pack.json`、`01/prompts/comfyui-shot-prompts.json`、`01/prompts/comfyui-workflow-plan.json` 与 `01/reports/comfyui-prompt-qc.md`。
- 剩余阻塞不是资产，而是 ComfyUI checkpoint、LoRA、ControlNet、IPAdapter、workflow template 与 node ID 配置。
