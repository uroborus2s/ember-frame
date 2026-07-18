# P-01 v0207 Director Previs QC

日期：2026-06-22

## 返工原因

用户复审成立：v0206 配音过快，旁白失去历史纪录片的平缓与厚重；C024 台词挤压，听感抢拍；摄影晃动和雪线干扰导致画面疲劳。

## v0207 修复

- 总时长从 9.5 秒扩为 12.0 秒。
- NAR001 从 2.8 秒压缩候选改为 4.787 秒纪录片节奏候选。
- C024 从 2.3 秒压缩候选改为 4.032 秒分段喊话候选。
- 配乐 / 环境声在对白窗口明显 duck，不抢 1-3 kHz 清晰度。
- 摄影改为稳定推移 / 侧向跟拍，只保留撞门受力，不做连续乱晃。
- 雪线数量和干扰降低。
- 字幕按慢速气口拆分，便于审看。

## 输出

- 审看视频：`assets/edit/P-01-v0207-stable-director-previs-subtitled-20260622.mp4`
- 无硬字幕版：`assets/edit/P-01-v0207-stable-director-previs-20260622.mp4`
- 声音混合：`assets/edit/P-01-v0207-full-audio-mix-20260622.wav`
- 关键帧检查：`assets/edit/P-01-v0207-contact-sheet-20260622.jpg`
- manifest：`video-production-room/.work/asset-versions/P-01-video/20260622v0207/render-manifest.json`

## 导演判断

v0207 通过为 `stable_audio_picture_previs_review`。它修复了声音节奏和晃动问题，可以作为 P-01 继续审看和下游正式风格生成前的节奏基准。

不通过为最终风格成片：低模人物只证明空间与镜头路线，不证明最终角色卡脸型、服装、表演细节和 Comfy/I2V 画面质量。正式成片仍需以角色卡和美术首尾帧进入最终视频生成 QC。
