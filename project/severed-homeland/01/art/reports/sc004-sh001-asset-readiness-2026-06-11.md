# SC004-SH001 资产构建报告 / 2026-06-11

## 目标镜头

- Shot: `SC004-SH001`
- Asset: `E01_R015`
- Canonical output: `01/assets/reference-frames/r015e01.png`
- 用途：残阳坳村口封村地理建立镜头，I2V 首帧参考。

## 已读取资产

- 全局场景：`L001` 残阳坳村落与药屋主场景卡。
- 本集场景：`E01_L001A` 残阳坳村口封锁地理场景卡，已存在 `01/assets/locations/l001ae01.png`，3840x2160 PNG。
- 主角：`C001` / `E01_C001` 沈维桑主角与第01集封村状态。`SC004-SH001` 中只作为后续连续性上下文，不设为首帧主焦点。
- 官吏：`C016` 白册官吏母版已存在；`E01_C016A` 已重建到 `01/assets/characters/c016e01.png`，由全局 `assets/characters/c016m.png` 逐字节复制，SHA-256 完全一致，确保继承全局虫族官吏脸型。
- 奴兵：`E01_C017` 已有候选图，但此前 SC002 视觉 QC 撤销了该资产的继承结论，正式用于 `SC004-SH001` 前需复审。
- 士兵：`E01_C018` 纯虫族小兵候选图已存在，但仍需体量/反关节/封路状态复核。
- 群众与道具：`E01_C027`、`E01_P022`、`E01_K004`、`E01_K006` 均已压缩为本次 prompt package 参考图。

## 构建结果

- 已更新 `01/prompts/art-image-prompts.json` 中 `PROMPT_E01_R015`：补入白册官吏依赖、wide-shot 信息预算、前中后景分层和禁止远景粒子化规则。
- 已更新 `01/art/asset-manifest.json`、`01/art/asset-index.json`、`01/art/thread-plan.json`、`01/art/thread-results.json`：`E01_C016A` 现在标记为 `global_c016_master_exact_copy_pending_user_visual_qc_2026-06-11`；`E01_R015` 现在标记为 `blocked_pending_remaining_reference_qc_and_hard_reference_binding_2026-06-11`。
- 已创建隔离生图提示包：
  - `01/art/runs/2026-06-11-sc004-sh001-imagegen-task/e01_r015-prompt-package.md`
  - `01/art/runs/2026-06-11-sc004-sh001-imagegen-task/e01_r015-thread-prompt.md`
  - `01/art/runs/2026-06-11-sc004-sh001-imagegen-task/refs/`
- 已补充 `01/art/runs/2026-06-11-sc004-sh001-imagegen-task/refs/c016e01-ref.jpg`，作为 `SC004-SH001` 的白册官吏主参考。
- 已补充 `01/art/runs/2026-06-11-sc004-sh001-imagegen-task/refs/l001m-ref.jpg`，作为残阳坳全局母空间硬参考；`E01_L001A` 只作为该母空间内的村口封锁区域卡。

## 阻塞项

- `01/assets/reference-frames/r015e01.png` 尚未生成。
- `E01_C017`、`E01_C018`、`E01_C027` 需要 SC004 适用性或上游继承 QC 通过后，才能作为最终视频首帧硬参考。
- 当前会话没有可把本地 PNG 作为硬参考绑定到生图模型的通道，因此未生成纯文字替代图。

## QC 规则

- 残阳坳单一空间硬锁：`SC004-SH001` 必须发生在全局 `L001` 残阳坳村落与药屋主场景卡的同一个物理空间内；村口、检查桌、旧井、药屋外圈、药屋内门缝/药柜暗格、后山出口、低坡路线和白蜡旗封锁点只能是同一空间的不同区域/机位/焦段。
- 允许换机位、焦段、前景遮挡、人物调度、封锁道具和光线；不得重造相似村口、另画独立药屋、移动旧井或检查桌、改变后山出口和白蜡旗方位，或把残阳坳画成另一个村庄。
- 必须同场读到检查桌、旧井、药屋外圈、后山出口和三支白蜡旗。
- 白册官吏、混血奴兵、纯虫族小兵和残阳坳村民必须靠服制、体态、动作职责区分。
- 前景/中景/背景必须分离；远处村民、士兵、屋顶和草地只能做大形和成组轮廓。
- 拒绝随机可读文字、随机徽记、现代元素、透明背景、设定卡背景、全画面等细节、粒子化石头/屋顶/人群和信息过载。

## 推荐下一步

`E01_C016A` 已先按全局 `C016` 主卡精确重建。下一步对 `E01_C017`、`E01_C018`、`E01_C027` 做 SC004 适用性 QC；随后用本报告的 prompt package 开隔离生图任务生成 `E01_R015`。
