# 第 01 集 G-P 制作启动台账

owner: project-office
status: formal_visual_source_assembly_ready_audio_overlay_final_blocked
last_updated: 2026-06-21

## 1. 启动结论

G-P/P-01 至 P-05 已完成导演签署，可作为下游文字依据。总导演已向美术、提示词、配音、音乐、视频生成、剪辑和交付部门下达制作命令，并按角色卡硬参考完成图像生成、审片、打回、用户反馈复审和返工晋升。最新用户反馈后，P-05 旧正脸漂移视频版本已撤回，v0006 face-lock 与 v0007 无声视觉装配通过导演身份 QC；P-01 v0101/v0102 粮门打开版本撤回，v0103 controlled closed-gate visual source 通过空间逻辑 QC；P-02/P-03/P-04 v0101 可作为 visual source 候选继续声音 / overlay 准备；G-P v0001 无声 visual source 总装已完成。正式成片仍因声音听审、final 音频、口型 / 声画时间、精确 overlay、终混、剪辑和最终 QC 而阻塞。

## 2. 分镜状态

| 分镜 | 导演 | 美术 | 提示词 | 配音 | 音乐 | 视频 | 剪辑 | 交付 |
|---|---|---|---|---|---|---|---|---|
| P-01 | locked | formal_reference_frame_promoted | video_shoot_prompt_package_ready | blocked_C024_NAR001_listening_qc_C021_final_mix | music_cue_ready_C021_preview_generated_missing_final_audio | controlled_closed_gate_visual_source_v0103_pass_needs_audio_overlay_final_qc | waiting_video | waiting_edit |
| P-02 | locked | formal_reference_frame_promoted_after_C017_pressing_actor_retake | video_shoot_prompt_package_ready_C017_chain_locked | blocked_C016_C017_C025_listening_qc_and_cutting | music_cue_ready_missing_audio | formal_visual_source_v0101_pass_needs_audio_overlay_final_qc | waiting_video | waiting_edit |
| P-03 | locked | formal_reference_frame_promoted_after_scale_retake | video_shoot_prompt_package_ready | blocked_child_song_recording_C016_C025_listening_qc | music_cue_ready_missing_audio | formal_visual_source_v0101_pass_needs_child_song_audio_overlay_final_qc | waiting_video | waiting_edit |
| P-04 | locked | formal_reference_frame_promoted_after_escape_motion_retake | video_shoot_prompt_package_ready | blocked_C007_C002_listening_qc_and_cutting | music_cue_ready_missing_audio | formal_visual_source_v0101_pass_needs_audio_overlay_final_qc | waiting_video | waiting_edit |
| P-05 | locked | formal_reference_frame_promoted_after_age_identity_retake | video_shoot_prompt_package_ready | blocked_C001_C025_listening_qc_and_sfx | music_cue_ready_missing_audio | face_lock_visual_assembly_v0007_pass_needs_sfx_overlay_final_qc | waiting_video | waiting_edit |

## 3. 当前交接

- 导演部 -> 美术部：formal_reference_frames_all_approved
- 导演部 -> 提示词部：video_shoot_prompt_package_ready_for_video_preflight
- 导演部 -> 配音部：blocked_pending_character_voice_locks_listening_qc_and_final_audio
- 导演部 -> 音乐部：music_cue_ready_C021_preview_generated_missing_final_audio_files
- 导演部 -> 视频生成部：formal_visual_source_assembly_ready_audio_overlay_final_blocked
- 导演部 -> 剪辑部：waiting_for_video_qc_passed
- 导演部 -> 成片交付部：waiting_for_edit_approved

## 4. 开拍准入

视频组已经接令，但正式生成镜头前必须满足：

- 美术部完成每镜正式参考帧，并证明已使用角色卡母图作为硬身份参考；（P-01 至 P-05 已完成，P-02 C017 按手返工已通过）
- 提示词部完成图片/视频提示词和负面约束；
- 配音部完成可见说话人、旁白或无口型声明；有声音角色必须先通过角色声音卡或 preview 听审；
- 音乐部完成每镜声音入点、退出点和静默策略；
- 项目办公室确认素材能回到对应分镜目录。

## 5. 已派发子任务

- 美术参考帧/资产需求回填子任务：completed，负责 P-01 至 P-05 的 `## 2. 美术资产区`。
- 图片/视频提示词框架回填子任务：completed，负责 P-01 至 P-05 的 `## 3. 图片提示词区`。
- 两个子任务写入范围已分开；提示词已基于最新正式参考帧完成本轮视频拍摄提示词包回填。
- 提示词二轮锁定子任务：completed，负责读取美术区后把 `## 3. 图片提示词区` 推进到视频前置可用状态或提出返工。
- 配音与口型子任务：completed_text_plan，负责 P-01 至 P-05 的 `## 4. 配音与口型区`；最终音频仍待生成。
- 音乐与声音节奏子任务：completed_text_plan，负责 P-01 至 P-05 的 `## 5. 音乐与声音节奏区`；最终音乐 / 声效仍待生成。
- 视频生成 v0001 子任务：completed_candidate_generation，已逐镜写入 `## 6. 视频生成区`、新增视频部准入报告并生成 ComfyUI / Wan2.2 低清运动候选；当前仍缺角色声音锁 / 听审、final 音频、精确 overlay、部分尾帧 / 裁切控制和正式 QC，候选不得冒充成片。

## 6. 导演 QC 准备

下一轮导演审判标准：

- 美术区必须提供可供首帧/参考帧制作的资产清单、控制图需求和美术 QC。
- 提示词区必须吸收美术区，不再停留在单纯等待美术；不得发明模型、LoRA、ControlNet、IPAdapter 或采样参数。
- 配音区必须明确可见说话人、旁白、无口型镜头和待生成音频清单。
- 音乐区必须有 cue 入点/退出点、静默策略、环境声重点和与对白边界。
- 四项都达到可执行状态后，视频生成部才允许进入正式 preflight；否则打回对应部门。

## 7. 导演 QC 结论

date: 2026-06-21
status: preflight_ready_but_missing_generated_reference_frames

- 美术区：P-01 至 P-05 均为 `art_reference_plan_ready`，通过文字/计划层 QC。
- 提示词区：P-01 至 P-05 均为 `prompt_ready_for_video_preflight`，未发现需退回美术的 `needs_art_fix`。
- 配音区：P-01 至 P-05 均为 `voice_plan_ready`，可进入视频口型/无口型 preflight。
- 音乐区：P-01 至 P-05 均为 `music_cue_ready`，可进入视频节奏 preflight。
- 总导演裁决：四个前置文本区块通过，允许视频生成部执行逐镜 preflight；但不得生成正式视频，直到真实首帧/参考帧、必要控制图和音频文件路径齐全。

## 8. 视频 preflight 回传与导演裁决

date: 2026-06-21
status: blocked_missing_generated_reference_frames_control_assets_and_audio

- P-01：缺真实 `P-01.png`、黑石主门顶视图、床弩 / 粮门低模、手部握持参考、巨兽冲击方向控制图和旁白/头领喊话音频。
- P-02：缺真实 `P-02.png`、灶屋正交平面、虫蜡 / 木牌 / 白册精确控制、麦粒泥水材质参考和小吏台词音频。
- P-03：缺真实 `P-03.png`、白墙验声站位图、儿童队列低模 / 故事板、虫蜡特写、识字木牌 overlay、儿童晒药名试唱 / final 音频。
- P-04：缺真实 `P-04.png`、红线密室平面、黑匣 / 血牒 / 旧驿 / 追捕令 overlay、白翳参考、C007 voice_id 锁定和台词音频。
- P-05：缺真实 `P-05.png`、残阳坳北坡顶视图、沈维桑姿态、灰兔 / 兔血参考和鸡叫 / 脚步 / 兔子碰弓身 / 铜锣声音文件。
- 总导演裁决：视频部不通过开拍准入，打回上游补资产是正确结果；下一轮由美术优先生成 P-01 至 P-05 的参考帧候选，音频侧同步排查可用生成入口。未补齐前不得让视频部生成正式镜头。

## 9. 成品完成前待决

- 每个分镜最终图片必须回到对应 `{shot-id}.png`。
- 每个分镜最终视频必须回到对应 `{shot-id}.mp4`。
- 分镜级配音、音乐和剪辑交接必须回到对应 `assets/` 子目录。
- 项目最终帧率、编码、码率、声道、响度、字幕和封装格式仍待交付阶段确认。

## 10. 美术参考帧与导演控制图回传

date: 2026-06-21
status: historical_withdrawn_to_composition_candidates_resolved_by_section_14

本节为第一次美术回传后的历史裁决；后续已按角色卡硬参考重制，并在第 14 节晋升为正式参考帧。

- P-01：候选图保留在 `art-room/.work/asset-versions/P-01-reference-frame/`；正式 `P-01.png` 撤回。`assets/control/p01top.svg` 可作主门、平台、粮门、床弩、低机位和人物身高比例草图。
- P-02：候选图保留在 `art-room/.work/asset-versions/P-02-reference-frame/`；正式 `P-02.png` 撤回。`assets/control/p02top.svg` 可作灶屋平面、角色职责、身高层级和低机位视线草图。
- P-03：候选图保留在 `art-room/.work/asset-versions/P-03-reference-frame/`；正式 `P-03.png` 撤回。`assets/control/p03block.svg` 可作白墙、儿童队列、验声桌、识别童、母亲侧位和成人 / 儿童身高比例草图。
- P-04：候选图保留在 `art-room/.work/asset-versions/P-04-reference-frame/`；正式 `P-04.png` 撤回。`assets/control/p04top.svg` 可作红线室、后门、晏南枝动线、白翳静止点和追兵入场方向草图。
- P-05：候选图保留在 `art-room/.work/asset-versions/P-05-reference-frame/`；正式 `P-05.png` 撤回。`assets/control/p05top.svg` 可作北坡、村口、绕沟小路、矛尖封路、沈维桑下坡路径和视线草图。
- 总导演裁决：候选图只能辅助构图讨论，不得交视频部作为 first_frame / identity / style。下一轮美术必须把对应角色卡图片作为硬身份输入重出正式帧，并由导演重新 QC。

## 11. 角色卡闸门回传

date: 2026-06-21
status: character_visual_cards_ready_reference_frame_regeneration_completed_voice_gate_pending

- G-P 直接相关 C001、C002、C007、C016、C017、C021、C024、C025 均有 3840x2160 RGBA alpha V2 角色母图，并在角色卡内写明身高 / 比例 / 三视图或五视角要求。
- C001、C002、NAR001 仅有 24 kHz preview 音频，需人工听审，不能当最终声音锁。
- C007、C016、C017、C024、C025 的声音母卡 v001 preview 已生成；C021 48 kHz stereo 声效方向 preview 已生成；P-03 儿童旧歌文本已锁为 `白芷晒，薄荷晾，陈皮翻一翻。`；全部 preview / 声效仍需人工听审、切分、分层或终混。
- 总导演裁决：角色卡母图重制正式参考帧已完成并进入第 14 节；下一步先做声音听审、分镜台词切分、P-03 儿童旧歌试唱 / 断声点 / 口型时间和 C021 声效分层 / 终混判断。声音与口型闸门未过前，视频生成不得开拍。

## 13. P-03 儿童旧歌导演锁定

date: 2026-06-21
status: child_song_text_director_locked_recording_pending

- locked_text: `白芷晒，薄荷晾，陈皮翻一翻。`
- trigger: 第三字“晒”附近轻轻滑出旧调，随即被虫蜡针和流程打断。
- director_reason: 该句短、可唱、像孩子晒药名，不扩写成完整旧歌，也不把孩子怪物化；能准确服务“旧声刚露头就被制度归档”的镜头目的。
- next_required_department_action: 配音部生成儿童试唱候选，标出“晒”滑调点、虫蜡针打断点、识别童判定与木牌声对齐点；人工听审前不得标 final。

## 12. C021 声效预览回传

date: 2026-06-21
status: preview_audio_generated_needs_human_listening_qc

- 过程版本：`music-room/.work/asset-versions/C021-CREATURE-SFXLOCK-V001/20260621v0001-preview.wav`
- 角色卡可见小样：`director-room/characters/c021-creature-sfx-v001-preview.wav`
- 规格：48 kHz stereo PCM WAV，8.000s，preview only。
- 总导演裁决：该小样满足“有可听方向供角色卡闸门听审”的最低要求，但不满足成片要求；音乐 / 声效部仍需拆分低频体量、骨铃 / 绳环、门体受压、雪地质感和兽息层，完成与骨钟、床弩、军户喊声和粮门声桥的避让测试。

## 14. 正式参考帧导演终审与晋升

date: 2026-06-21
status: partially_superseded_by_section_15

- P-01：第一轮候选因粮门外露和压迫点偏弱打回；第二轮 `20260621v0004.png` 通过，晋升为 `director-room/season-01/01/G-P/P-01/P-01.png`。
- P-02：`20260621v0002.png` 通过，晋升为 `director-room/season-01/01/G-P/P-02/P-02.png`。
- P-03：`20260621v0002.png` 通过，晋升为 `director-room/season-01/01/G-P/P-03/P-03.png`；儿童旧歌仍按第 13 节走配音试唱和口型时间。
- P-04：`20260621v0002.png` 通过，晋升为 `director-room/season-01/01/G-P/P-04/P-04.png`；后续视频必须继续锁住 C002 身形和 C007 白翳压迫关系。
- P-05：第一轮候选因灰兔 / 兔血 / 肩弓 / 铜锣叙事点不足打回；第二轮 `20260621v0003.png` 通过，晋升为 `director-room/season-01/01/G-P/P-05/P-05.png`。
- 总导演裁决：本节为二轮审片当时结论，已被第 15 节和后续 P-04 复审部分推翻。P-01 保留通过；P-02/P-03/P-04/P-05 撤回重制。

## 15. 用户反馈复审与正式帧撤回

date: 2026-06-21
status: P02_P03_P04_P05_reference_frames_withdrawn_retake_ordered

- P-02：撤回 `P-02.png`，正式目录文件已移除。原因：C016 粮税虫吏读成普通人形账房，未达到角色卡 190-210cm / 代表约 200cm 的身高比例，也没有在同一地平线清楚压过 C025 成人和 C017 奴兵。已追单图像线程重制。
- P-03：撤回 `P-03.png`，正式目录文件已移除。原因：C016 验声虫吏被桌面、弯腰姿态和前景成人压低，等级身高链不清。已追单图像线程重制。
- P-04：撤回 `P-04.png`，正式目录文件已移除。原因：白翳站在门口导致出口被读成堵死，晏南枝像站住抱匣对峙，观众看不出她从红线密室后门、雨檐窄廊 / 侧巷向旧驿方向逃走。已追单图像线程重制。
- P-05：撤回 `P-05.png`，正式目录文件已移除。原因：画面人物不像 17 岁沈维桑，脸型、体量和气质偏二十多到三十岁猎户，C001 年龄 / 身份锁失败。已追单图像线程重制。
- 总导演裁决：用户反馈成立；本节撤回已由后续第 16 节返工晋升解决。

## 16. 用户反馈返工候选终审与晋升

date: 2026-06-21
status: P02_P03_P04_P05_retake_approved_and_promoted

- P-02：`20260621v0003.png` 通过并晋升为 `director-room/season-01/01/G-P/P-02/P-02.png`。C016 粮税虫吏身高比例成立，高于 C017/C025。
- P-03：`20260621v0003.png` 通过并晋升为 `director-room/season-01/01/G-P/P-03/P-03.png`。C016 验声虫吏高度成立，儿童队列和母亲被拦保留。
- P-04：`20260621v0003.png` 通过并晋升为 `director-room/season-01/01/G-P/P-04/P-04.png`。逃跑路线从红线密室后门到雨檐窄廊 / 侧巷可读，白翳不再堵门。
- P-05：`20260621v0004.png` 通过并晋升为 `director-room/season-01/01/G-P/P-05/P-05.png`。沈维桑少年感回归，灰兔、兔血、村口、铜锣和封路矛尖保留。
- 总导演裁决：G-P 五镜正式参考帧再次全部通过。提示词部可以基于新晋升帧刷新 copy-ready 图片 / 视频提示词；视频生成部仍不得开拍，直到配音、声效、口型时间、精确 overlay 和提示词锁定全部回传。

## 17. 二次用户反馈复审

date: 2026-06-21
status: P02_P04_reference_frames_withdrawn_retake_ordered

- P-02：撤回 `P-02.png`，正式目录文件已移除。虫蜡板当前读成神秘 / 惩罚道具，未清楚表达“征粮册 / 木牌 -> 孩子小手 -> 湿白虫蜡掌纹”的制度留押凭证关系。下一候选必须让虫蜡板目的直接可读。
- P-04：撤回 `P-04.png`，正式目录文件已移除。当前逃跑路线仍容易被读成门外堵死，观众无法确认晏南枝如何从红线密室后门经雨檐窄廊 / 侧巷逃向旧驿方向。下一候选必须把可通行侧路拍出来，白翳不得站在出口轴线上。
- 总导演裁决：反馈成立。本节为撤回当时裁决，已由第 18 节返工晋升解决；最新状态以第 18 节为准。

## 18. 二次反馈返工终审与晋升

date: 2026-06-21
status: formal_reference_frames_approved_after_language_and_motion_retake

- P-02：`20260621v0004.png` 通过并晋升为 `director-room/season-01/01/G-P/P-02/P-02.png`。虫蜡板目的清楚：册页 / 木牌、孩子小手、湿白虫蜡掌纹共同构成征粮制度的留押凭证，不再读成神秘惩罚板。
- P-04：`20260621v0005.png` 通过并晋升为 `director-room/season-01/01/G-P/P-04/P-04.png`。晏南枝从左侧后门 / 雨檐窄廊方向切出，白翳在右侧外院远处静止下令，不堵出口轴线；逃跑运动和可通行侧路清楚。
- 总导演裁决：本节为当时通过结论，已被第 19 节 P-02 C017 执行者复审推翻；最新状态以第 19 节为准。

## 19. P-02 C017 按手执行者复审撤回

date: 2026-06-21
status: P02_reference_frame_withdrawn_C017_actor_retake_ordered

- P-02：撤回 `P-02.png`，正式目录文件已移除。原因：`20260621v0004.png` 中按住孩子手的人物不像 C017 混血奴兵，读成未登记成人 / 陌生执行者，导致“C016 登记下令、C017 执行按手、C025 母亲无力护子”的制度职责链断裂。
- 返工命令：下一候选必须明确 C017 的蜡灰青短军袍、暗绿黑护布、硬化蜡布肩胸片、骨白虫蜡腕绑、黑日烙牌 / 编号木牌、低位金钱马尾、人手五指硬化指节；C016 只登记，不亲手按孩子；C025 母亲只护子失败，不施暴。
- 总导演裁决：本节撤回已由第 20 节解决；最新状态以第 20 节为准。

## 20. P-02 C017 按手执行者返工终审与晋升

date: 2026-06-21
status: P02_C017_pressing_actor_retake_approved_and_promoted

- P-02：`20260621v0005.png` 通过并晋升为 `director-room/season-01/01/G-P/P-02/P-02.png`。按手者读成 C017 混血奴兵，具备虫化头面、短军袍、硬化腕甲和执行姿态；C016 在中间登记 / 划册，C025 母亲护子失败。
- 总导演裁决：G-P 五镜正式参考帧再次全部通过。本节返工已经进入第 21 节提示词回填与视频准入复核；最新状态以第 21 节为准。

## 21. 提示词回填与视频准入复核

date: 2026-06-21
status: superseded_by_section_22_comfy_retake_candidates_passed

- 提示词部已完成 P-01 至 P-05 的 copy-ready 视频拍摄提示词包回填，并锁定 P-02：C017 混血奴兵按住孩子手；C016 只登记 / 下令；C025 母亲只护子失败。
- 视频生成部已完成真实拍摄准入报告 `video-production-room/G-P-P01-P05-admission-report.md` 和首轮生成 QC `video-production-room/G-P-P01-P05-v0001-comfy-qc.md`。五张正式参考帧均存在、可解码，实测 3840x2160；ComfyUI / Wan2.2 已生成 P-01 至 P-05 v0001 低清运动候选。
- v0001 素材位于 `video-production-room/.work/asset-versions/P-01-video/20260621v0001/` 至 `P-05-video/20260621v0001/`；P-01/P-02/P-03 可作为下一轮节奏和运动基底，P-04 只证明逃跑路线可读但晏南枝动作过快，P-05 地理与年龄基本守住但灰兔 / 兔血 / 铜锣 / 矛尖证据偏弱。
- 配音部确认 P-01 至 P-05 的 `assets/voice/` 目录为空，现有 wav 仅为隐藏 preview / candidate，不能作为 final；音乐 / 声效 final 与精确 overlay / 尾帧仍未齐。
- 总导演裁决：本节 v0001 裁决已由第 22 节 P-04/P-05 返工候选回传更新；v0001 不允许晋升为正式 `P-XX.mp4` 或完整成片。

## 22. ComfyUI 第二轮返工候选与导演裁决

date: 2026-06-21
status: comfy_motion_candidates_p04_p05_retake_passed_audio_lipsync_overlay_final_blocked

- 视频生成部追加 P-04 v0002：`video-production-room/.work/asset-versions/P-04-video/20260621v0002/P-04_escape_action_retake_i2v_49f_00001_.mp4`。导演裁决：通过运动候选，C002 从后门出线进入雨檐 / 侧巷的逃跑动作可读，C007 仍在远处外院，不堵出口轴线。
- 视频生成部追加 P-05 v0002 宽景：`video-production-room/.work/asset-versions/P-05-video/20260621v0002/P-05_prop_evidence_retake_i2v_49f_00001_.mp4`。导演裁决：通过宽景候选，C001 年龄和残阳坳地理稳定。
- 视频生成部追加 P-05 v0003 灰兔 / 兔血插入镜：`video-production-room/.work/asset-versions/P-05-video/20260621v0003/P-05_rabbit_blood_insert_i2v_49f_00001_.mp4`。导演裁决：通过证据候选，灰兔、兔血、弓身、手部和村口压力可读；建议 P-05 后续正式视频采用 v0002 宽景 + v0003 插入镜组合。
- 总导演裁决：G-P 五镜均已有可回看的视频候选基底，但没有任何镜头可复制到导演正式目录作为 `P-XX.mp4`。下一步必须先完成 final 配音 / 声效、口型 / 声画时间、精确 overlay、终混、剪辑预览和交付规格。

## 23. P-05 正脸漂移修复与 formal visual source 批次

date: 2026-06-21
status: formal_visual_source_assembly_ready_audio_overlay_final_blocked

- 用户反馈成立：旧 P-05 宽景视频候选把沈维桑正面脸型重塑，和 C001 角色卡的 17 岁窄长少年脸不一致。该版本撤回，不得作为主角正式镜头。
- 视频生成部重跑 P-05 v0006：`video-production-room/.work/asset-versions/P-05-video/20260621v0006/P-05_formal_visual_source_face_lock_1024x576_49f_00001_.mp4`。导演裁决：通过 face-lock visual source；沈维桑保持侧面 / 背侧轮廓，不再转成陌生正脸。
- 视频生成部装配 P-05 v0007：`video-production-room/.work/asset-versions/P-05-video/20260621v0007/P-05_formal_visual_assembly_no_audio_1024x576_16fps.mp4`。导演裁决：通过无声视觉装配；宽景、灰兔 / 兔血插入镜和村口封锁关系成立。
- P-01 v0101/v0102 均因粮门打开失败被撤回；视频部生成 v0103 controlled closed-gate visual source：`video-production-room/.work/asset-versions/P-01-video/20260621v0103/P-01_controlled_closed_gate_visual_source_1024x576_49f.mp4`。导演裁决：通过空间逻辑 QC，粮门全程闭锁，不露暖仓洞 / 粮袋堆。
- P-02/P-03/P-04 v0101 通过 visual source 候选；G-P v0001 无声 visual source 总装完成：`video-production-room/.work/asset-versions/G-P-video/20260621v0001/G-P_visual_source_assembly_no_audio_1024x576_16fps.mp4`，约 19.94 秒。
- 总导演裁决：正式视频制作已经进入 visual source 总装阶段，但仍没有任何镜头可复制为导演正式 `P-XX.mp4`。final 音频、口型 / 声画时间、精确 overlay、终混、剪辑和交付 QC 全部通过前，不得宣称成片完成。
