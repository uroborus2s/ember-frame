# 视频生成部工作流

视频生成部工作流以“导演签署、资产准入、技术选择、短段生成、严格 QC、可剪辑交接”为主线。它不追求一次生成整段长镜头，而追求每个镜头的身份、空间、动作、声音和剪辑功能都可控。

## 总流程

```text
读取项目办公室/共享镜头文件交接
  -> 工具能力检查
  -> 上游准入检查
  -> 技术选择与 technique_profile
  -> 分段生成计划
  -> I2V / FLF2V / V2V / lipsync 执行
  -> contact sheet / 首尾帧 / 动作 / 口型 / 可剪辑性 QC
  -> 返工、重跑、降级、阻塞或通过 QC
  -> 剪辑交接
  -> failure ledger 和经验沉淀
```

## 一、工具能力检查

先检查当前可用工具、模型和硬件，再决定镜头策略。工具能力报告必须写清：

```text
tool_name
tool_version_or_model_ref
supported_modes: T2V / I2V / FLF2V / V2V / lipsync / inpaint / interpolation
native_fps
native_resolution
max_frames_or_duration
control_support: first_frame / last_frame / pose / depth / lineart / mask / audio
known_limits
recommended_use
forbidden_use
```

不得发明未验证模型、LoRA、ControlNet、节点名称或平台能力。工具不可用时，产出计划并标记 blocked。

## 二、上游准入检查

每个镜头生成前必须检查：

```text
导演签署:
  镜头目的、观众感受、景别、机位、运镜、动作、转场和 QC 是否明确。

美术资产:
  通过 QC 的首帧是否存在；尾帧是否按镜头需求存在；
  角色状态、场景母图、九宫格、道具状态和光线是否通过 QC。

提示词资产:
  视频拍摄提示词、负面提示词、资产引用、控制图引用和禁止漂移项是否齐全。

配音资产:
  可见说话人是否有 lipsync handoff、dialogue cue、音频路径、起止时间、气口和停顿。

控制资产:
  复杂空间、动作或运镜是否有低模、深度图、线稿、pose、mask、motion guide 或 dynamic previs。

剪辑需求:
  时长、头尾余量、接剪方向、节奏点、是否需要 clean plate 或 alternate take。
```

准入不通过时，不进入生成；只记录阻塞原因和上游返工建议。

## 三、技术选择

视频生成部必须先判断问题类型，再选择技术：

```text
静态氛围轻动 -> I2V，短时长，低运动强度
明确动作起止 -> FLF2V，首尾帧都必须通过 QC
复杂调度/多人/打斗/追逐 -> 3D/低模预演 + pose/depth/lineart + 分段 I2V/FLF2V
说话近景 -> 口型工具或口型专段，先保证音频时间权威
同一镜头局部错误 -> mask / 局部重跑 / V2V，不破坏已通过区域
镜头只需测试运动 -> T2V 或低模预演，不得直接当最终镜头
源视频身份或空间错误 -> 重跑源视频，不用后期修饰硬救
```

每个镜头写入 `technique_profile`，说明选择理由和 fallback。

## 四、分段生成计划

默认原则：

- 3-5 秒分段优先；
- 原生 24fps 优先；
- 尾帧必需时用 FLF2V；
- 低清源优先重跑；
- 不用光流掩盖源问题；
- 复杂长镜头先用低模或 story animatic 验证，再生成最终素材。

分段计划必须记录：

```text
segment_id
duration
start_state
end_state
first_frame_ref
last_frame_ref
audio_range
motion_goal
camera_goal
overlap_or_handle_frames
edit_point
```

## 五、执行与记录

执行时必须记录：

```text
input_refs
tool_name
tool_version_or_model_ref
prompt_ref
negative_prompt_ref
control_refs
audio_ref
seed_or_run_id_when_available
output_path
failure_reason_when_failed
```

试错、失败、备选和返工前版本进入项目办公室指定的隐藏版本库，不得在明面目录创建 `raw/`、`rejected/` 或 `approved/` 作为正式生产结构。导演认可后的最终分镜视频只回到对应导演部分镜目录，并由 `{shot-id}.md` 引用。

## 六、QC 与返工

QC 顺序：

```text
首帧一致性
  -> 角色身份
  -> 场景空间
  -> 道具状态
  -> 动作重心和受力
  -> 镜头运动
  -> 画质和稳定性
  -> 口型和声画同步
  -> 随机文字/标注/UI
  -> 可剪辑性
  -> manifest 完整性
```

失败时按原因选择：

```text
角色漂移 -> 加强身份参考、缩短分段、换首帧、回美术补状态卡
空间漂移 -> 回场景九宫格、低模、深度或线稿；必要时回导演补空间调度
动作不自然 -> 拆动作、补 pose/轨迹/低模预演、降低运动强度
镜头不符 -> 重写视频提示词或使用 FLF2V/camera path
口型失败 -> 回配音部确认时间权威，或使用口型专用流程
画质失败 -> 重跑源，不用补帧/锐化遮盖
可剪辑性失败 -> 重新生成头尾余量、alternate take 或 clean plate
```

## 七、剪辑交接

只有通过视频 QC 并被导演认可、或按项目办公室质量门标记可交付的素材，才可以交给剪辑部。交接位置由项目根目录 `project-management.md` 决定；若项目采用导演部分镜目录，最终视频回到对应 `{shot-id}.mp4`，过程版本留在隐藏版本库。交接必须包含：

```text
render-manifest.json
shot-qc-report.json
failure-ledger.json
导演部分镜目录中的最终视频路径
隐藏版本库中必要的追溯路径
handoff-to-edit.md
```

`handoff-to-edit.md` 必须说明每个镜头的可用段、推荐入点出点、头尾余量、音频引用、已知风险和禁止剪辑硬救的问题。
