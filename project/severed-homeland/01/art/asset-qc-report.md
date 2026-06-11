# 第01集《白册进村》资产 QC 报告

## 当前结论

B04_E01_STYLE 已完成并通过协调端视觉 QC。SC001 开场四张参考帧已经写入 canonical 路径，当前状态是同一空间候选版待用户视觉 QC；ComfyUI 交付包可以按这组候选帧继续做镜头级测试，但在用户确认前不标记 final approved。

SC002 分镜资产的 2026-06-10 放行结论已于 2026-06-11 撤销。随后生成的 `E01_C016B`、`E01_C017`、`E01_C018` 与 `E01_R005`-`E01_R009` 候选也已被用户视觉 QC 退回：角色一致性仍未满足，身高差设定不成立。当前有效状态不是“等待确认”，而是 `failed_user_visual_qc_identity_height_scale_relock_required_2026-06-11`；不得进入视频制作、ComfyUI 小批量试渲或 director-room prompt refresh。详细失败复核见 `01/art/audits/sc002-inheritance-failure-audit-2026-06-11.md`，本轮退回审计见 `01/art/audits/sc002-character-identity-height-scale-user-rejection-2026-06-11.md`。

补充：2026-06-11 第一轮 prompt-only 重做候选因全局脸型/物种结构继承不足被拒，未写入项目。后续直接从全局母卡 `C016`、`C017` 派生的候选仍未通过本轮用户视觉 QC；下一轮必须先按 `C025 -> C017 -> C016 -> C018 -> C019` 同地平线比例链重生角色状态卡，再按 `4096x2304` 重生 SC002 参考帧。详细记录见 `01/art/audits/c016b-c017-global-inheritance-rebuild-2026-06-11.md`。

## SC002 角色一致性与身高差用户退回 / 2026-06-11

结论：当前 `E01_R005`-`E01_R009` 不能作为视频参考帧使用。重生前必须执行以下硬尺度：`C025` 为普通人族基准；`C017` 为 170-200cm 混血奴兵，SC002 代表值 175-185cm；`C016` 为 190-210cm 基层虫吏，SC002 代表值 195-205cm；`C018` 为 200-230cm 纯虫族小兵，SC002 站立等效 215-230cm；`C019` 为 220-260cm 中阶重甲虫士兵。

验收规则：角色卡必须有脚底同线比例条；参考帧必须在同一泥地/同一车道地平线上读出身高差；不得用桌台、检查台、台阶、粮袋、车板、门槛、前景放大、镜头畸变、裁切或低伏遮挡制造假身高。只要官吏、奴兵、纯虫族小兵和普通人族读成同一身高阶层，或发生职责互换，即失败。

## SC002 角色继承失败撤销历史 / 2026-06-11

结论：本节记录 2026-06-10 放行结论被撤销时的历史状态。后续 2026-06-11 的 C016B/C017 全局主卡重建和 R005-R009 新候选复审也已被用户视觉 QC 继续退回；当前有效结论见上方“SC002 角色一致性与身高差用户退回”。

### 历史失败资产

- `E01_C016B`：历史失败原因是粮税小吏不能作为合格身份锁；现已直接继承全局 `C016` 主卡。
- `E01_C017`：历史失败原因是读成普通人族灰甲押解兵；现已直接继承全局 `C017` 主卡。
- `E01_C018`：继续阻断，后续场次使用前必须按 200-230cm 纯虫族基层武力复核，不能替代奴兵或官吏。
- `E01_R005`-`E01_R009`：历史阻断状态已解除为新版候选，仍需用户视觉 QC 后才能进入视频制作。

### 候选依赖

`E01_C023`、`E01_L003`、`E01_P003`、`E01_P008` 未被本次直接判废，但 SC002 整包批准撤销；它们只能作为候选依赖，等待新角色和新参考帧一起复审。

### 历史禁止项

- 历史失败版不得用于视频，已归档到 `history/`。
- 不得以“尺寸合格、无 alpha、构图大致可读”替代角色继承和导演要求审核。
- 新版 `r005e01.png`-`r009e01.png` 已是当前候选，但仍需用户最终视觉确认。

## SC001 开场资产收口 / 2026-06-08

结论：SC001 开场 3 个镜头所需的第一集上游分集资产中，风格、场景、道具、兽族攻城母卡、伴生兽母卡和三张关键人物状态卡可用于当前参考帧制作。E01_R001-E01_R004 已经生成同一空间候选版；最新硬锁改为：R001/R002 保持同一段锁喉关黑石城墙、同一个城门、同一墙外攻城方向和门楼内钟声，第一镜不强制画出骨钟或钟架；R003/R004 可在后续墙头/门楼空间揭示同一口警钟。

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

- E01_R001 -> 01/assets/reference-frames/r001e01.png，SC001-SH001 FLF2V 首帧：城外攻城方向低机位正中对称史诗建立镜头，兽族联军、伴生兽、攻城车或破门猛犸压向同一面黑石城门；当前风格通过并作为质感标准。
- E01_R002 -> 01/assets/reference-frames/r002e01.png，SC001-SH001 FLF2V 终帧：保持 R001 同一墙外方向和正中中轴压力，更近靠近城门，第一次重撞城门；雪雾、碎冰、旧木屑、门闩震动和黑石边缘反光要更浓烈。骨钟在门楼内，只需要钟声，不要求画面露出钟体或钟架。
- E01_R003 -> 01/assets/reference-frames/r003e01.png，SC001-SH002 I2V 首帧：同一钟架旁，年轻军户被撞门余震晃倒、半倒墙边、武器脱手，旁边破钟横摆，墙外兽潮仍在同一方向压近。
- E01_R004 -> 01/assets/reference-frames/r004e01.png，SC001-SH003 I2V 首帧：同一墙头与同一钟架旁，薛临墙在钟边下达战场命令，身后仍能读出人族墙头和城外攻城压力。

任务包：`01/art/runs/2026-06-07-sc001-reference-frame-dispatch/task-plan.json`。

当前状态：`E01_R001` 当前风格通过并作为质感标准；`E01_R002` 的 canonical `01/assets/reference-frames/r002e01.png` 已正式替换为 closer gate + stronger impact + P017 肃明虫族帝国旗修正版 4096x2304 尾帧，本轮过程 PNG 已删除，旧正式图归档到 `01/assets/reference-frames/history/r002e01.before-suming-flag-closer-impact-replace-20260611.png`；`E01_R003` 旧扶钟构图已废弃，必须重生后再作为 SC001-SH002 首帧；`E01_R004` 可继续作为 SC001-SH003 候选首帧。

持续 QC 锁定：四张参考帧必须保持 16:9 PNG，4096x2304，无 alpha，无水印，无随机可读文字；R001/R002 只能有同一段黑石城墙、同一个城门和同一墙外攻城方向，门楼内钟声不要求画面露钟；R003/R004 才负责在墙头/门楼空间延续同一口破裂警钟。旧帝国徽章只能是残缺、暗淡、旧金色的表面残痕，不允许完整圆形徽章、发光日月徽章或随机可读文字。

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

结论已失效：`SC002` 所需的粮税小吏与混血奴兵分集角色卡曾补齐到 canonical 路径，用于后续 SC002 参考帧继承；但 2026-06-11 用户视觉 QC 已继续退回角色一致性和身高差问题。两张图不得再视为待确认候选，必须按同地平线比例条重生。

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

结论已失效：`SC002-SH001` 与 `SC002-SH002` 所需 I2V 首帧曾按 imagegen-task 隔离流程生成候选，并写入 canonical 路径；但 R005-R009 当前候选已被用户视觉 QC 退回，不再是“等待确认”，必须重生。

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

## SC002 分镜资产历史失效记录 / 2026-06-10

结论已失效：`SC002-SH001` 到 `SC002-SH004` 所需分镜参考帧和上游依赖资产曾在 2026-06-10 被错误标记为可交付。2026-06-11 用户视觉 QC 后，该结论撤销；后续 `r005_r009_regenerated_candidate_after_global_master_rebuild_2026-06-11` 也已被用户继续退回。当前有效状态为 `failed_user_visual_qc_identity_height_scale_relock_required_2026-06-11`。

### 历史依赖资产记录

- `E01_C016B` -> 历史 rejected 版已归档，新 canonical 已直接继承全局 `C016` 主卡。
- `E01_C017` -> 历史 rejected 版已归档，新 canonical 已直接继承全局 `C017` 主卡。
- `E01_C023` -> `01/assets/characters/c023e01.png`，当前为 candidate dependency，等待新角色和新参考帧一起复审。
- `E01_L003` -> `01/assets/locations/l003e01.png`，当前为 candidate dependency，等待新角色和新参考帧一起复审。
- `E01_P003` -> `01/assets/props/p003e01.png`，当前为 candidate dependency，等待新角色和新参考帧一起复审。
- `E01_P008` -> `01/assets/props/p008e01.png`，当前为 candidate dependency，等待新角色和新参考帧一起复审。

### 历史参考帧记录

- `E01_R005` -> 历史 rejected 版已归档，新 canonical 为重做候选。
- `E01_R006` -> 历史 rejected 版已归档，新 canonical 为重做候选。
- `E01_R007` -> 历史 rejected 版已归档，新 canonical 为重做候选。
- `E01_R008` -> 历史 rejected 版已归档，新 canonical 为重做候选。
- `E01_R009` -> 历史 rejected 版已归档，新 canonical 为重做候选。

### 审核记录

失效历史报告见 `01/art/reports/sc002-storyboard-final-qc-2026-06-10.md`。有效失败复核见 `01/art/audits/sc002-inheritance-failure-audit-2026-06-11.md`。当前 SC002 有 blocked image job，必须重做角色卡和参考帧。

## SC002 R005-R009 全局角色继承重做复审 / 2026-06-11

结论已失效：`E01_C016B` 与 `E01_C017` 曾先从全局主卡直接重建，随后 `E01_R005`-`E01_R009` 曾按 SC002 导演要求重新生成并覆盖 canonical 路径；但用户视觉 QC 已继续退回，角色一致性与身高差仍未达标。当前状态为 `failed_user_visual_qc_identity_height_scale_relock_required_2026-06-11`，不得进入视频制作。

### 已重做候选

| Asset | Shot | 用途 | 导演要求 | 美术合格度 | 结论 |
| --- | --- | --- | ---: | ---: | --- |
| `E01_R005` | `SC002-SH001` | I2V 首帧 | 90 | 91 | C016B 虫族粮税小吏脸壳、白官袍、检查台、低位村民和粮袋墙可读 |
| `E01_R006` | `SC002-SH002` | I2V 首帧 | 93 | 94 | C017 混血奴兵腕绑/硬化手继承可读，儿童虫蜡手印已修正 |
| `E01_R007` | `SC002-SH003` | I2V 首帧 | 92 | 93 | C016B 开册、C017 扣腕，职责和身高层级未互换 |
| `E01_R008` | `SC002-SH004` | FLF2V 首帧 | 91 | 92 | 门槛后三分构图、祖牌盒、虫蜡手印、拖粮上车动作成立 |
| `E01_R009` | `SC002-SH004` | FLF2V 终帧 | 94 | 94 | 与 R008 同机位成对，空门槛和远去粮车关系成立 |

### 文件验证

- `01/assets/reference-frames/r005e01.png`
- `01/assets/reference-frames/r006e01.png`
- `01/assets/reference-frames/r007e01.png`
- `01/assets/reference-frames/r008e01.png`
- `01/assets/reference-frames/r009e01.png`

全部为 3840x2160 PNG RGB，无 alpha。旧 canonical 已归档到 `01/assets/reference-frames/history/*before-global-ref-redo-20260611.png`；本轮新 source 已归档到 `01/assets/reference-frames/history/*imagegen-global-ref-source-20260611.png`。废弃的 R006 首版保留为 `01/assets/reference-frames/history/r006e01.rejected-no-child-handprint-source-20260611.png`。

### 当前限制

- 本轮已被用户视觉 QC 退回，不能再视为美术部候选通过。
- `E01_C018` 纯虫族小兵仍保持阻塞，不得把本轮 SC002 结论外推到含 C018 的镜头。
- 详细报告见 `01/art/reports/sc002-r005-r009-global-ref-regeneration-qc-2026-06-11.md`；审计副本见 `01/art/audits/sc002-r005-r009-global-ref-regeneration-qc-2026-06-11.md`。

## SC004-SH001 首帧资产构建记录 / 2026-06-11

结论：`E01_R015` 的镜头资产规划、提示词、依赖和隔离生图提示包已更新，但 `01/assets/reference-frames/r015e01.png` 未生成。`E01_C016A` 已由全局 `C016` 主卡精确复制重建，当前有效状态为 `blocked_pending_remaining_reference_qc_and_hard_reference_binding_2026-06-11`。

### 已完成

- 读取并复核残阳坳全局/本集场景：`L001`、`E01_L001A`。
- 读取并复核主角、官吏、奴兵、纯虫族小兵和村民相关卡：`C001`、`E01_C001`、`C016`、`E01_C016A`、`E01_C017`、`E01_C018`、`E01_C027`。
- `PROMPT_E01_R015` 已补入白册官吏依赖、wide-shot 信息预算、前中后景分层和禁止远景粒子化规则。
- 已创建提示包与压缩参考图目录：`01/art/runs/2026-06-11-sc004-sh001-imagegen-task/`。
- 已恢复 `01/assets/characters/c016e01.png`，SHA-256 与 `assets/characters/c016m.png` 完全一致；并补充 `refs/c016e01-ref.jpg` 作为 SC004-SH001 白册官吏主参考。
- 已追加残阳坳单一空间硬锁：SC004-SC006 所有残阳坳镜头必须在全局 `L001` 同一物理空间内换机位/焦段/遮挡；`E01_L001A/B/C` 只是同一空间内的村口、药屋内景、旧井检查桌区域卡。

### 阻塞

- `E01_C017`、`E01_C018`、`E01_C027` 需通过 SC004 适用性或继承 QC 后才能用于最终视频首帧。
- 当前会话无法把本地 PNG 作为硬参考绑定到生图模型，因此未生成纯文字替代图，也未把 `E01_L001A` 复制成 `r015e01.png`。

### 后续 QC 要点

- 必须同场读到检查桌、旧井、药屋外圈、后山出口和三支白蜡旗。
- 必须读成全局 `L001` 的同一个残阳坳空间，不得重造相似村口、独立药屋、独立旧井或改变村口/检查桌/旧井/药屋/后山出口/白蜡旗相对关系。
- 白册官吏、混血奴兵、纯虫族小兵和残阳坳村民必须层级分明。
- 前景、中景、背景必须清楚分离；远处人群/士兵/屋顶/石墙只能成组概括，不能粒子化或等细节铺满全画面。
- 禁止随机文字、随机徽记、现代元素、透明背景、设定卡背景、全局灰雾、AI speckle、假锐化和视觉信息过载。

# SC002 C018 持械封路重做复审 / 2026-06-11

结论：上一轮 SC002 R005-R009 候选因用户视觉 QC 指出官吏脸型/身高、奴兵手部和纯虫族士兵缺失问题，已撤销视频放行。新版已经重新生成并覆盖 canonical 路径；当前为美术部内部硬项通过、等待用户最终视觉确认，未得到用户确认前不要直接进入视频制作。

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

当前状态不是待确认候选，而是用户视觉 QC 未通过。下一轮必须先重生 C016B/C017/C018 状态卡并加入同地平线比例条，再按 `4096x2304` 重生 `E01_R005`-`E01_R009`；重生完成前 `SC002` 标记为 `failed_user_visual_qc_identity_height_scale_relock_required_2026-06-11`。
