# 第01集《白册进村》资产 QC 报告

## 当前结论

B04_E01_STYLE 已完成并通过协调端视觉 QC。SC001 开场四张参考帧已经写入 canonical 路径，当前状态是同一空间候选版待用户视觉 QC；ComfyUI 交付包可以按这组候选帧继续做镜头级测试，但在用户确认前不标记 final approved。

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
