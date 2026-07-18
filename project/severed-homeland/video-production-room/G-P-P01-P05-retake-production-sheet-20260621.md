# Severed Homeland G-P P-01..P-05 Retake Production Sheet

生成部门：video-production-room  
日期：2026-06-21  
范围：G-P 重拍候选视频生产单，只记录/生成候选与 QC，不写最终 `P-XX.mp4`。  
状态：候选生产中，未进入导演终审，未交付剪辑部。

## 1. 读取与约束确认

- 已按 UTF-8 分段读取并确认 EOF：`.agents/skills/video-production-room/SKILL.md` 及其必要引用、`project-management.md`、`project-spec.md`、`.project/status.md`、`.project/blockers.md`、G-P `P-01.md` 到 `P-05.md`。
- 写入范围限制：只写 `project/severed-homeland/video-production-room/**` 与隐藏候选版本库 `video-production-room/.work/asset-versions/**`。
- 禁止项：不改导演分镜正文，不改 voice-room/music-room，不改 `.project/status.md` 或 `.project/blockers.md`，不把未 QC/未导演确认的视频写作最终 `P-XX.mp4`。
- 质量线：G-P 属于叙事关键暴力/逃亡信息段，候选 QC 以 90 为最低线；涉及 P-02 手部强制按印、P-04 逃跑路径、P-05 身份脸锁等关键项时，任何直接失败项均不得通过。

## 2. 当前工具与素材状态

### 2.1 ComfyUI

- 可访问：`http://127.0.0.1:8188/system_stats` 返回 200。
- ComfyUI：0.25.1。
- 设备：NVIDIA GeForce RTX 4080 SUPER，CUDA，约 17GB VRAM。
- 当前可用模型/工作流依据：Wan2.2 I2V 已在旧候选中使用；当前 P-01 v0201 使用 14B I2V 双 UNET、CLIP Vision、UMT5、Wan VAE。
- 已确认工作流路径：`project/video-primer/assets/workflows/wan22/video_wan2_2_14B_i2v.json`。
- 当前缺口：`ffmpeg`、`ffprobe`、`magick` 未在 PATH 中可用；候选抽帧/QC 需用 Python/PyAV/Pillow 或 Comfy 输出辅助。

### 2.2 已有正式图片与控制图

- `director-room/season-01/01/G-P/P-01/P-01.png`
- `director-room/season-01/01/G-P/P-02/P-02.png`
- `director-room/season-01/01/G-P/P-03/P-03.png`
- `director-room/season-01/01/G-P/P-04/P-04.png`
- `director-room/season-01/01/G-P/P-05/P-05.png`
- 控制图：`p01top.svg`、`p02top.svg`、`p03block.svg`、`p04top.svg`、`p05top.svg`。

### 2.3 旧候选与诊断资产

- G-P 旧组合：`G-P-video/20260621v0001/G-P_visual_source_assembly_no_audio_1024x576_16fps.mp4`，仅旧预览，已被用户复审打回。
- G-P 24fps 复查：`G-P-video/20260621v0002-retime-review/G-P_visual_source_assembly_no_audio_1024x576_24fps_retimed_review.mp4`，诊断用途，不可作为清晰度证明。
- P-01 旧候选：v0001、v0101、v0102、v0103。v0103 解决闭门方向，但仍需动作重拍，重点是不能静态。
- P-02 旧候选：v0001、v0101。v0101 可作视觉源参考，但缺 C016/C017 音频、口型、盖印动作尾帧。
- P-03 旧候选：v0001、v0101。v0101 可作视觉源参考，但缺童谣、识别童、C016 音频/口型。
- P-04 旧候选：v0001、v0002、v0101。v0101 可作视觉源参考，但缺 C007 台词/口型、C002 气息、逃跑路线尾帧与道具叠加。
- P-05 旧候选：v0001..v0007。v0006 是侧背脸锁视觉源，v0007 是无音频视觉组装，仍缺鸡鸣、脚步、兔血/弓细节、三声锣和 A-01 转场时机。

## 3. 当前已生成候选

### P-01 v0201 director-retake

- 状态：ComfyUI 生成成功，已归档并完成候选 QC。
- prompt_id：`4ce8e905-2886-4713-939d-0b3232453437`。
- 版本路径：`video-production-room/.work/asset-versions/P-01-video/20260621v0201-director-retake/`。
- 已落工作流：`workflow/P-01_director_retake_api.json`。
- 候选视频：`P-01_director_retake_i2v_97f_1024x576_24fps_preview.mp4`。
- 联系表：`P-01_director_retake_i2v_97f_contact.png`。
- 元数据：`P-01_director_retake_i2v_97f_metadata.json`。
- 参数：1024x576，97 frames，24fps，14 steps，cfg 3.0，seed 206210201。
- 目标动作链：骨铃/烟雪动 -> 兽族撞关震动但粮门不开 -> 饥饿城墙兵被迫拉弩，年轻士兵流血手压住绞盘并用体重拉动。
- 关键负面锁：不得开粮门，不得黑屏/静态，不得只有推镜，不得无绞盘动作，不得怪物占主画面，不得英雄化，不得出现随机文字/UI/箭头/字幕。
- QC：82/100，Visual Retake Candidate Only；不静态、粮门不打开、绞盘动作有改善，但撞关冲击/骨铃/指挥官动作和音频仍不足，不可作最终片。

### P-01 v0104 fallback preview

- 状态：ComfyUI 生成成功，已归档并判定失败备选。
- prompt_id：`910a10b5-4cfb-428d-8483-777eb91590de`。
- 版本路径：`video-production-room/.work/asset-versions/P-01-video/20260621v0104/`。
- 候选视频：`P-01_action_retake_preview_closed_gate_1024x576_49f_16fps_preview.mp4`。
- 联系表：`P-01_action_retake_preview_closed_gate_49f_contact.png`。
- 元数据：`P-01_action_retake_preview_closed_gate_49f_metadata.json`。
- 参数：1024x576，49 frames，16fps，4-step lightx2v LoRA。
- QC：64/100，Fail；运动量够，但中后段有暖光/开门读法风险，且时长偏短，不建议继续。

### P-02 v0201 director-retake

- 状态：ComfyUI 当前运行中，尚未出片，已落 running manifest。
- prompt_id：`41eb271c-ff6c-40b3-bd31-bed70c4a948a`。
- 版本路径：`video-production-room/.work/asset-versions/P-02-video/20260621v0201-director-retake/`。
- 已落工作流：`workflow/P-02_director_retake_api.json`。
- 输出前缀：`severed_homeland/20260621v0201-director-retake/p-02_director_retake_i2v_133f`。
- 参数：1024x576，133 frames，24fps，14 steps，cfg 3.0，seed 206210202。
- 目标动作链：粮罐被夺/粮入泥 -> 母亲或老者护住孩子失败 -> C017 抓住孩子手腕按入湿白虫蜡并留下手印，C016 保持在更高位置只登记/下令。
- QC：待出片；硬看 C017 是否真按手、C016 是否未执行、同地线身高比例是否成立。

## 4. P-01..P-05 重拍候选生产单

### P-01 城墙撞关 / 粮门锁死

- 输入锁：`P-01.png`、`p01top.svg`、P-01 正式分镜、v0103 闭门视觉源。
- 身份与空间锁：C024 饥饿城墙兵；C021 只作为门外压力，不可成为画面主体；粮门在士兵身后保持关闭。
- 动作必达：镜头不能静态；骨铃/烟雪/冲击/士兵反应/流血手拉绞盘要有起点、接触、用力、反应、结束状态。
- 当前候选：v0201 已生成，作为视觉重拍候选；v0104 已生成但因开门暖光风险失败。
- 缺失输入：NAR001、C024 台词、C021 撞击/门震/骨铃/风雪声、最终混音。
- QC 硬失败：黑屏或近似黑屏；只做参考图推镜；粮门打开；怪物成为主角；绞盘/手部用力不可读。

### P-02 强征粮 / 按童手成册

- 输入锁：`P-02.png`、`p02top.svg`、P-02 正式分镜、v0101 视觉源。
- 身份与身高锁：C016 约 200cm，只登记/下令；C017 175-185cm，是执行者；C025 是母亲，保护但失败；小孩保持儿童比例。
- 动作必达：C017 踢翻灶/粮落泥，C016 下令，C017 抓住孩子小手按进湿白虫蜡，母亲失败，老者被拖走。
- 当前新任务：v0201 正在 ComfyUI 运行，候选输出后必须优先检查 C017 按手和身高链。
- 推荐候选路线：从 v0101 视觉源做 I2V/FLF2V，必要时拆成 2 段：征粮破灶段与按手盖印段；按手段优先使用近景/中近景并保持地线。
- 缺失输入：C016、C017、C025 最终音频/口型，虫蜡按印尾帧或控制帧，木牌/册籍覆盖图。
- QC 硬失败：C016 或 C025 变成按手者；儿童手接触不成立；身高链崩坏；小孩成人化；没有白虫蜡/册籍证据。

### P-03 旧童谣 / 识别童

- 输入锁：`P-03.png`、`p03block.svg`、P-03 正式分镜、v0101 视觉源。
- 身份锁：儿童必须保持儿童，不得变成怪物/成人；识别童只负责指出“他会旧歌”。
- 动作必达：孩童唱“白芷晒，薄荷晾，陈皮翻一翻”，第三字“晒”滑入旧调；识别童反应；C016 下令“带走，教成识别童”。
- 推荐候选路线：先做无口型视觉节奏试片，再等 voice-room 给最终童声/识别童/C016 音频后做口型/剪辑型候选。
- 缺失输入：童谣最终音频、识别童台词、C016 台词、口型任务、木牌/识别证据覆盖图。
- QC 硬失败：儿童成人化；童谣识别因果不可读；C016 抢动作或身份漂移；没有“旧歌被识别”的行为证据。

### P-04 旧驿血牒 / 追捕路径

- 输入锁：`P-04.png`、`p04top.svg`、P-04 正式分镜、v0101 视觉源。
- 空间路线锁：红线房后门 -> 雨檐窄廊/侧巷 -> 旧驿道向北；白义在远处/外侧/侧后，不堵门、不在出口轴线上。
- 动作必达：C002 携旧驿血牒沿路线逃离；C007 用白册/缉令赢，不用身体挡门；台词为“她带着旧驿血牒往北逃。封旧驿，活捉.”
- 推荐候选路线：用 v0101 做 FLF2V 或分段 I2V，尾帧必须明确北向旧驿道/追捕方向；可用道具 overlay 辅助血牒/白册/缉令可读性。
- 缺失输入：C007 最终音频/口型，C002 气息，旧箱/日月档/旧道/缉令覆盖图，尾帧。
- QC 硬失败：白义堵门；逃跑路线不成立；C002 没有逃跑方向；C007 没有通过缉令/白册发动追捕；空间轴线混乱。

### P-05 北坡伏笔 / 沈未桑侧背脸锁

- 输入锁：`P-05.png`、`p05top.svg`、P-05 正式分镜、v0006 侧背脸锁视觉源、v0007 无音频视觉组装。
- 身份锁：沈未桑 17 岁少年感，只允许侧脸/背脸/三分之二侧背，不允许生成正脸或成熟男性脸。
- 动作必达：白册特写后鸡鸣；沈未桑从北坡下行，带两只灰兔、兔血与弓，检查道路/人/退路；第二声鸡鸣被三声锣截断，枪尖封住侧路，锣尾接 A-01。
- 推荐候选路线：保留 v0006/v0007 视觉源，优先补 SFX/节奏/尾部阻断，不再用会冒正脸风险的大幅重生图。
- 缺失输入：鸡鸣、脚步、兔血/弓细节声、三声锣、A-01 接点时长。
- QC 硬失败：出现正脸；少年感丢失；没有兔/血/弓证据；没有鸡鸣-锣声节奏；枪尖封路不成立。

## 5. 当前阻塞与下一步命令

- 阻塞 1：ffmpeg/ffprobe 缺失，标准视频探测和剪辑命令不可用。当前可用替代是 Python/PyAV/Pillow 抽帧与元数据读取。
- 阻塞 2：P-01..P-04 缺最终配音/口型/声音设计；P-05 缺 SFX/三声锣/A-01 转场时机。候选可做视觉，不可做最终片。
- 阻塞 3：P-02/P-04 需要更强控制或尾帧，避免角色执行关系和空间路线漂移。
- 下一步命令：P-01 以 v0201 为基础继续补强撞关冲击、骨铃震动、指挥官逼回位和音频；P-02/P-03/P-04 等最终音频/控制帧/尾帧到齐后再生成新候选；P-05 在 v0007 视觉基础上补 SFX、三声锣和 A-01 接点。

## 6. 导演必须打回的问题

- P-01：静态、黑屏、粮门打开、只有推镜、无拉弩/绞盘用力、怪物正面抢画，全部必须打回。
- P-02：C016 或 C025 按孩子手、C017 身高/身份漂移、儿童成人化、白虫蜡按印不可读，全部必须打回。
- P-03：儿童成人化、旧歌识别关系不成立、童谣与“带走”因果断裂，必须打回。
- P-04：白义堵门、C002 逃跑路径不清、追捕方向不是旧驿道向北、C007 不靠白册/缉令而靠身体动作赢，必须打回。
- P-05：沈未桑出现正脸、脸变成熟、无兔血/弓/退路观察、鸡鸣与三声锣节奏缺失，必须打回。
