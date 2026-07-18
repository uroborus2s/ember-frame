# Severed Homeland G-P Retake Candidate QC

生成部门：video-production-room  
日期：2026-06-21  
范围：G-P P-01..P-05 重拍候选与旧视频诊断 QC。  
结论：当前未生成任何最终 `P-XX.mp4`；本报告只用于候选筛选和导演打回依据。

## 1. 工具状态

- ComfyUI 在线：`http://127.0.0.1:8188` 可访问。
- ComfyUI 版本：0.25.1。
- GPU：NVIDIA GeForce RTX 4080 SUPER，运行 P-01 v0201 时利用率 100%。
- `ffmpeg`/`ffprobe`/`magick`：PATH 中不可用。
- 替代 QC：`.venv` Python 可用，`av`、`PIL`、`imageio` 可用；本报告的视频元数据和帧差使用 PyAV/Pillow 抽检。

## 2. 当前新启动候选

### P-01 v0201 director-retake

- prompt_id：`4ce8e905-2886-4713-939d-0b3232453437`。
- 状态：ComfyUI success，已归档候选视频。
- 版本路径：`video-production-room/.work/asset-versions/P-01-video/20260621v0201-director-retake/`。
- 工作流：`workflow/P-01_director_retake_api.json`。
- 候选视频：`P-01_director_retake_i2v_97f_1024x576_24fps_preview.mp4`。
- 联系表：`P-01_director_retake_i2v_97f_contact.png`。
- 元数据：`P-01_director_retake_i2v_97f_metadata.json`。
- 参数：1024x576，97 frames，24fps，14 steps，cfg 3.0，seed 206210201。
- 元数据：1024x576，97 frames，24fps，4.0417s，无音频。
- 抽样帧差 MAD：0-12 = 4.72；12-24 = 3.10；24-36 = 7.01；36-48 = 7.99；48-60 = 7.41；60-72 = 7.47；72-84 = 7.57；84-96 = 5.19。
- 视觉判断：不再是静帧；粮门保持关闭，没有读成暖色开仓；前景士兵有明显身体位移和绞盘接触，P-01“不可静态”的核心问题得到缓解。
- 未达项：撞关冲击、骨铃震动、指挥官逼回位不够清楚；缺 NAR001、C024 台词、撞门/骨铃/风雪声与最终混音。
- QC 分数：82/100，Visual Retake Candidate Only，未通过成片线。
- 判定：可作为 P-01 重拍候选继续给导演看方向，但不能交剪辑为最终镜头。

### P-01 v0104 fallback preview

- prompt_id：`910a10b5-4cfb-428d-8483-777eb91590de`。
- 状态：ComfyUI success，已归档备选视频。
- 候选视频：`video-production-room/.work/asset-versions/P-01-video/20260621v0104/P-01_action_retake_preview_closed_gate_1024x576_49f_16fps_preview.mp4`。
- 联系表：`P-01_action_retake_preview_closed_gate_49f_contact.png`。
- 元数据：`P-01_action_retake_preview_closed_gate_49f_metadata.json`。
- 参数：1024x576，49 frames，16fps，4-step lightx2v LoRA。
- 元数据：1024x576，49 frames，16fps，3.0625s，无音频。
- 抽样帧差 MAD：0-6 = 3.90；6-12 = 4.25；12-18 = 5.62；18-24 = 6.35；24-30 = 6.91；30-36 = 7.32；36-42 = 6.17；42-48 = 5.65。
- 视觉判断：有明显运动和人物位移，但中后段出现门内暖光/开门读法风险，违背“粮仓锁死”；时长也短于 P-01 4-5s 目标。
- QC 分数：64/100，Fail。
- 判定：只作失败备选和参数对照，不建议继续。

### P-02 v0201 director-retake

- prompt_id：`41eb271c-ff6c-40b3-bd31-bed70c4a948a`。
- 状态：ComfyUI running，尚未返回视频输出。
- 版本路径：`video-production-room/.work/asset-versions/P-02-video/20260621v0201-director-retake/`。
- 工作流：`workflow/P-02_director_retake_api.json`。
- 输出前缀：`severed_homeland/20260621v0201-director-retake/p-02_director_retake_i2v_133f`。
- 参数：1024x576，133 frames，24fps，14 steps，cfg 3.0，seed 206210202。
- Prompt 锁：C016 站得更高、只登记/下令；C017 执行脏活，抓孩子手腕按入湿白虫蜡；同一地线保持 C016 > C017 > 平民/儿童的高度链。
- QC 状态：待视频落盘；出片后必须先判 C017 按手、儿童比例、湿白虫蜡手印和 C016 未执行。

## 3. 已有候选诊断 QC

### P-01 v0103 controlled closed gate visual source

- 路径：`video-production-room/.work/asset-versions/P-01-video/20260621v0103/P-01_controlled_closed_gate_visual_source_1024x576_49f.mp4`
- 元数据：1024x576，49 frames，16fps，3.0625s，无音频。
- 抽样帧差 MAD：frame 0-12 = 1.04；12-24 = 1.16；24-36 = 1.07；36-48 = 1.11。
- 视觉判断：粮门关闭方向比 v0101/v0102 更安全，但运动量近似静帧；骨铃、撞关、士兵反应、流血手拉绞盘均不可读。
- QC 分数：58/100，Fail。
- 直接失败项：P-01 不可静态；必须有动作链。该版本不得进入剪辑或最终交付。

### G-P formal visual source overview P-01 row

- 路径：`video-production-room/.work/asset-versions/G-P-formal-visual-source-v0101-contact-overview.png`
- 视觉判断：P-01 后段出现暖色粮仓/开门感，与“粮仓锁死”“退下去也是饿死”冲突。
- QC 分数：52/100，Fail。
- 直接失败项：粮门打开或读成粮仓可进入，必须打回。

### P-05 v0007 formal visual assembly no audio

- 路径：`video-production-room/.work/asset-versions/P-05-video/20260621v0007/P-05_formal_visual_assembly_no_audio_1024x576_16fps.mp4`
- 元数据：1024x576，123 frames，16fps，7.6875s，无音频。
- 抽样帧差 MAD：0-12 = 5.19；12-24 = 6.88；24-36 = 7.04；36-48 = 8.07；48-60 = 34.19；60-72 = 21.15；72-96 = 19.67；96-122 = 34.27。
- 视觉判断：沈未桑保持侧背脸/侧影方向，少年轮廓、弓、两只灰兔、路径观察和侧路枪尖基本可读；没有生成正脸。
- 缺口：没有鸡鸣、脚步、兔血/弓细节声、三声锣，也没有 A-01 转场声尾；只有视觉组装。
- QC 分数：86/100，Visual Candidate Only，未通过成片线。
- 处理建议：不要大幅重生图，优先补 SFX、节奏、锣声和 A-01 接点；若重生，必须保持“只侧背脸且少年感”。

## 4. 分镜级 QC 要点

- P-01：当前旧候选全部不能过；v0201 必须证明不是静态、不是黑屏、粮门不开、拉弩/绞盘动作可读。
- P-02：新候选必须证明 C017 按孩子手，C016 只登记/命令；同一地线身高比例不可漂。
- P-03：必须等童谣、识别童、C016 台词/口型；无音频视觉只能做节奏试片。
- P-04：必须保留红线房后门到雨檐窄廊/侧巷再往北旧驿道的逃跑路线；白义不得堵门。
- P-05：现有视觉候选可继承，但必须补鸡鸣、脚步、兔血/弓、三声锣和 A-01 转场。

## 5. 当前判定

- 可继续：P-01 v0201 可作为视觉重拍候选继续导演复核；P-02 v0201 当前正在运行，待出片后按 C017 按手硬锁 QC；P-05 v0007 可作为视觉基础继续补音效/节奏。
- 不可继续：P-01 v0104、P-01 v0103 与 G-P v0002/retime review 不能作为成片或清晰度证明。
- 待补 QC：P-02/P-03/P-04 需在最终音频、控制帧/尾帧到齐后再生成新候选；P-05 需补 SFX 和 A-01 接点后再做声音/剪辑 QC。
