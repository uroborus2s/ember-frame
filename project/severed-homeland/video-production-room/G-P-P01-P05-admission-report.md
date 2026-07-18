# G-P P-01..P-05 真实拍摄准入报告

owner: video-production-room
status: superseded_by_comfy_retake_candidates_audio_lipsync_overlay_final_blocked
last_updated: 2026-06-21

## 1. 执行结论

第 01 集 G-P/P-01 至 P-05 的本文件为 ComfyUI 启动前准入报告，现已被 `G-P-P01-P05-v0001-comfy-qc.md` 更新。此前检查确认五张正式参考帧均存在、可解码、满足 3840x2160 / 16:9；提示词部已完成本轮 copy-ready 视频拍摄提示词包回填。2026-06-21 后续确认 ComfyUI `127.0.0.1:8188` 已可调用，并已生成 P-01 至 P-05 低清运动候选；P-04 v0002 与 P-05 v0002+v0003 返工候选已通过导演运动 / 证据层 QC。当前仍缺 final 分镜级音频、口型时间表和精确 overlay / 后合成控制包，正式成片仍不得交付。

因此当前已有视频部隐藏版本库 v0001/v0002/v0003 候选，但没有生成导演正式目录中的 `P-01.mp4` 至 `P-05.mp4`。不得用低清候选、静态图、控制图、低模、假动效、preview 或候选音频冒充成片。

## 2. 正式参考帧检查

| 分镜 | 正式参考帧 | 文件状态 | 实测尺寸 | 准入判断 |
|---|---|---|---|---|
| P-01 | `director-room/season-01/01/G-P/P-01/P-01.png` | 存在，可解码 | 3840x2160 | 可作为首帧 / identity / style 输入；仍需 final 音频、口型时间、尾帧或手部 / 粮门落点控制 |
| P-02 | `director-room/season-01/01/G-P/P-02/P-02.png` | 存在，可解码 | 3840x2160 | 可作为首帧 / identity / style 输入；必须锁定 C017 按孩子手、C016 登记 / 下令、C025 母亲护子失败 |
| P-03 | `director-room/season-01/01/G-P/P-03/P-03.png` | 存在，可解码 | 3840x2160 | 可作为首帧 / identity / style 输入；仍需儿童旧歌 final、识别童 / 小吏口型时间和木牌 overlay |
| P-04 | `director-room/season-01/01/G-P/P-04/P-04.png` | 存在，可解码 | 3840x2160 | 可作为首帧 / identity / style 输入；仍需白翳 final 台词、喘息、尾帧和黑匣 / 血牒 / 旧驿 / 白册 overlay |
| P-05 | `director-room/season-01/01/G-P/P-05/P-05.png` | 存在，可解码 | 3840x2160 | 可作为首帧 / identity / style 输入；无口型需求，但仍需鸡叫、脚步、兔子碰弓、铜锣 final 声画时间 |

## 3. 控制图与 overlay 检查

| 分镜 | 已有 control-only 文件 | 缺口 |
|---|---|---|
| P-01 | `assets/control/p01top.svg` | 粮门窄缝 / 手部拉床弩落点尾帧；头领喊话粗口型时间 |
| P-02 | `assets/control/p02top.svg` | 虫蜡手印板多视图；木牌 / 白册精确 overlay；麦粒泥水材质裁切；C016 三段口型时间 |
| P-03 | `assets/control/p03block.svg` | 虫蜡泛黄特写；识字木牌精确 overlay；儿童旧歌、识别童和小吏口型时间 |
| P-04 | `assets/control/p04top.svg` | 黑匣裂口多视图；日月血牒 / 旧驿图 / 追捕令 / 白册 overlay；白册合页尾帧；白翳口型时间 |
| P-05 | `assets/control/p05top.svg` | 灰兔道具 / 兔血状态细节；铜锣后停机尾帧；鸡叫 / 铜锣 / 脚步声画时间 |

控制图只允许作为 control-only。其箭头、编号、路径线和标注不得进入最终视频。

## 4. 工具能力检查

| 项目 | 检查结果 | 结论 |
|---|---|---|
| `ffmpeg` | PATH 未发现 | 阻塞：无法封装、转码、抽帧或做 mp4 技术 QC |
| `ffprobe` | PATH 未发现 | 阻塞：无法验证 duration / fps / resolution / audio stream |
| ComfyUI CLI / `comfy` | PATH 未发现 | 无可调用后端 |
| Wan / Wan2.x CLI | PATH 未发现 | 无可调用后端 |
| 常见本地服务端口 | `127.0.0.1:8188`, `7860`, `8000`, `3000`, `5000` 均不可达或超时 | 未发现运行中的视频生成服务 |
| 进程检查 | 未发现 Python / ComfyUI / Wan / ffmpeg 生成进程 | 未发现可接管后台 |

本机有 `nvidia-smi`，但 GPU 存在不等于视频生成后端可调用；当前不能推定有 I2V / FLF2V 能力。

## 5. 音频与口型检查

五个正式分镜目录的 `assets/voice/` 与 `assets/music/` 当前均没有 final 文件。隐藏版本库仅发现以下候选或 preview，不能作为 final：

| 来源 | 文件 | 当前判断 |
|---|---|---|
| voice-room `.work` | `P-01-VO-NAR001-001/20260621v0001-candidate.wav` | 24 kHz mono 候选，需听审、切头尾、转 48 kHz final |
| voice-room `.work` | `P-02-VO-C016-CLERK-001/20260621v0001-candidate.wav` | 24 kHz mono 候选，需听审并切三段口型时间 |
| voice-room `.work` | `P-04-VO-C007-BAIYI-001/20260621v0001-candidate.wav` | 24 kHz mono 候选，需听审并切两段口型时间 |
| music-room `.work` | `C021-CREATURE-SFXLOCK-V001/20260621v0001-preview.wav` | C021 声效方向 preview，不是 P-01 final stem 或终混 |

P-05 已明确无对白、无口型需求；但鸡叫、湿松针脚步、兔子碰弓、铜锣三下仍是声画同步必需输入，缺失前不能生成声画最终版。

## 6. 分镜级阻塞

| 分镜 | 当前准入状态 | 需要补齐 |
|---|---|---|
| P-01 | blocked | 可调用视频后端；`ffmpeg` / `ffprobe`；NAR001 旁白 final、C024 头领喊话 final 与粗口型时间、军户 Foley、C021 分镜 final stem；粮门 / 手部落点控制或尾帧 |
| P-02 | blocked | 可调用视频后端；`ffmpeg` / `ffprobe`; C016 小吏 final 与三段口型时间、C025 老人 / 孩子反应声 final；木牌 / 白册 / 虫蜡 overlay；虫蜡手印尾帧；严格锁 C017 执行按手 |
| P-03 | blocked | 可调用视频后端；`ffmpeg` / `ffprobe`; 儿童旧歌 final、识别童与小吏 final、母亲气口 final；字级或句级口型时间；识字木牌 overlay；木牌落点尾帧 |
| P-04 | blocked | 可调用视频后端；`ffmpeg` / `ffprobe`; C007 白翳 final 与两段口型时间、C002 喘息 final、追兵底噪 final；黑匣 / 血牒 / 旧驿 / 追捕令 / 白册 overlay；白册合页尾帧 |
| P-05 | blocked | 可调用视频后端；`ffmpeg` / `ffprobe`; 鸡叫、脚步、兔子碰弓、铜锣 final 声画时间；铜锣后停机尾帧；A-01 接剪余音确认 |

## 7. 部门补齐清单

| 责任方 | 需要补什么 |
|---|---|
| 项目办公室 / 工具环境 | 提供或启动可调用 I2V / FLF2V / Wan / ComfyUI 后端；安装或暴露 `ffmpeg` 与 `ffprobe`；确认本批是否允许 1080p preview，最终 fps / 编码 / 码率 / 声道 / 响度 / 字幕规格 |
| 配音部 | 输出 P-01..P-05 分镜级 final 48 kHz 音频；为可见说话人提供 start/end、停顿、气口、字句切分和 lipsync handoff |
| 音乐 / 声音组 | 输出 P-01 C021 final stem、P-02..P-05 环境声 / Foley / SFX final；特别是 P-05 鸡叫、湿松针脚步、兔子碰弓、铜锣三下 |
| 提示词部 | 本轮 copy-ready 视频拍摄提示词包已回填；后续仅在视频后端确定后做格式适配，不得改写 P-02 C017 执行 / C016 登记 / C025 护子的职责链 |
| 美术 / 后期资产 | 补 P-02 / P-03 / P-04 精确文字和符号 overlay，补必要尾帧 / 插入帧 / 道具多视图；控制图标注不得入最终画面 |
| 导演部 / 剪辑部 | 确认每镜推荐时长、头尾余量、尾帧是否必需，以及 P-05 铜锣余音接 A-01 的剪辑需求 |

## 8. 真实生成命令状态

未启动任何镜头生成命令。原因不是“质量未达标后失败”，而是生成前硬阻塞：当前没有可调用视频后端、没有 `ffmpeg` / `ffprobe`，且 final 音频 / 口型 / overlay 交接不完整。

下一次只有在工具能力和上游输入全部补齐后，才允许在 `video-production-room/.work/asset-versions/{shot-id}/` 建立版本库并启动真实 I2V / FLF2V 生成；通过 QC 与导演认可后，最终视频才可回到对应分镜目录命名为 `{shot-id}.mp4`。
