# P-01 v0214 I2V 短段测试导演 QC

日期：2026-06-22  
总导演结论：已开始真实视频制作，并生成 F1E / F2D 短段测试；当前仍不得晋升最终 `P-01.mp4`。

## 输入包

- 上游制作包：`art-room/.work/asset-versions/P-01-v0214-upstream-rebuild-20260622/`
- C021 身份引用：`source-refs/p01c021ref.png`
- 同墙空间图：`controls/p01gate.png`
- F1E 首帧候选：`reference-frames/p01f1e.png`
- F2D 首帧候选：`reference-frames/p01f2d.png`
- 运动故事板：`controls/p01story.png`

## 视频测试输出

- 测试 manifest：`video-production-room/.work/asset-versions/P-01-video/20260622v0214-i2v-short-tests/P-01-v0214-i2v-short-tests-manifest.json`
- F1E R1 视频：`video-production-room/.work/asset-versions/P-01-video/20260622v0214-i2v-short-tests/P-01-F1E_director_retake_i2v_97f_1024x576_24fps.mp4`
- F1E R1 抽帧：`video-production-room/.work/asset-versions/P-01-video/20260622v0214-i2v-short-tests/P-01-F1E_director_retake_contact.jpg`
- F1E R2 manifest：`video-production-room/.work/asset-versions/P-01-video/20260622v0214-i2v-short-tests/P-01-v0214-f1e-r2-manifest.json`
- F1E R2 视频：`video-production-room/.work/asset-versions/P-01-video/20260622v0214-i2v-short-tests/P-01-F1E-R2_director_retake_i2v_61f_1024x576_24fps.mp4`
- F1E R2 抽帧：`video-production-room/.work/asset-versions/P-01-video/20260622v0214-i2v-short-tests/P-01-F1E-R2_director_retake_contact.jpg`
- F2D 视频：`video-production-room/.work/asset-versions/P-01-video/20260622v0214-i2v-short-tests/P-01-F2D_director_retake_i2v_73f_1024x576_24fps.mp4`
- F2D 抽帧：`video-production-room/.work/asset-versions/P-01-video/20260622v0214-i2v-short-tests/P-01-F2D_director_retake_contact.jpg`

## 分段 QC

### F1E R1

状态：`failed_director_qc`

通过项：

- 城门、墙顶和守军仍在同一画面，基础空间没有完全漂移。
- C021 体量压力存在。

失败项：

- 烟尘开始生成类似巨兽脸 / 幽影的形状，观众会误读为随机怪物显形，不是 C021 实体撞门。
- 撞门接触点不够物理，门和墙的受力不够明确。
- 运动指标偏低，整体仍偏“烟动图”，不够像真正撞击。

裁决：不得进入剪辑，不得作为最终 F1E。

### F1E R2

状态：`conditional_geography_pass_motion_fail`

通过项：

- 修掉了 R1 的烟雾怪脸问题，C021 仍是画面左侧实体局部。
- 同墙关系较 R1 更清楚：城门、黑石墙、墙顶士兵在一个空间里。
- 镜头没有乱甩，观众不会眼花。

失败项：

- 冲击动作仍不够强，门体震动和士兵受力反应不足。
- 运动指标 `mean_abs_delta=0.4837`，对于“巨兽撞门”这个动作镜头偏低。

裁决：可作为 F1E 地理 / 气氛 plate 参考，不得作为最终动作镜头。下一步 F1E 必须采用更强控制：3D/低模撞击预演、门体震动 mask、后期物理 shake / debris 或更明确 FLF2V 尾帧。

### F2D

状态：`conditional_action_pass_not_final`

通过项：

- 老军户抓肩、推回、年轻军户手触铁栅 / 锁门方向成立。
- 动作是正常 1x 推搡，没有再变慢动作。
- 退路封死的叙事功能比旧版更清楚。

风险项：

- 后半段人物转身时有运动糊和形体不稳，建议正式剪辑只取前 0.0-2.0 秒，或重跑一个更短更稳版本。
- 仍需与正式台词、撞门声和音乐压力重新同步。

裁决：可作为 F2D 动作候选进入下一轮剪辑测试，但不是最终成片素材。

## 下一步导演命令

1. 视频部不得组装最终 `P-01.mp4`。
2. F1E 必须继续返工，不允许用 R1 或 R2 冒充正式撞门镜头。
3. F2D 可以进入短剪测试，但只能短用前段，并保留重跑权。
4. 下一轮优先做 `P-01-F1E-R3`：以同墙图和 F1E 首帧为基础，加入低模/后期物理震动控制，让门体、碎雪、城墙和士兵反应同时发生。
