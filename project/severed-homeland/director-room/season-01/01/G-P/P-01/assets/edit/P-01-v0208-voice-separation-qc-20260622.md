# P-01 v0208 旁白 / 城楼军令声源分离 QC

## 用户问题

用户指出：`粮仓锁死` 这一句和旁白连在一起，听感像同一个人，分不清谁是谁。

导演判定：用户意见成立。`粮仓锁死！` 不是旁白，是 C024 在城楼现场向军户下达的军令；v0207 把旁白和现场军令的声线、空间与时距压得过近，属于声画身份失败。

## v0208 修正

- NAR001：非画内纪录片旁白，入点 00:00:00.85，时长 5.487 秒，低、稳、居中、干净。
- 声桥：00:00:06.40-00:00:07.25 使用门体、绞盘、锁链硬声桥，切断旁白语流。
- C024：画内城楼军令，入点 00:00:07.25，时长 4.184 秒，右前方定位、窄频、带风雪空间和压迫感。
- 审片字幕：临时标注 `【旁白】` 与 `【城楼军令】`，只用于本轮 QC 明确声源，不代表最终正片字幕设计。

## 输出文件

- 审看视频：`assets/edit/P-01-v0208-voice-separated-director-previs-subtitled-20260622.mp4`
- 无硬字幕版：`assets/edit/P-01-v0208-voice-separated-director-previs-20260622.mp4`
- 声音混合：`assets/edit/P-01-v0208-voice-separated-audio-mix-20260622.wav`
- NAR001 分离候选：`assets/voice/P-01-VO-NAR001-001-v0208-doc-separated-48k.wav`
- C024 现场军令候选：`assets/voice/P-01-VO-C024-HEAD-001-v0208-onsite-shout-48k.wav`
- 接触表：`assets/edit/P-01-v0208-contact-sheet-20260622.jpg`
- 视频部 manifest：`video-production-room/.work/asset-versions/P-01-video/20260622v0208/render-manifest.json`

## 导演结论

v0208 通过为 `speaker_separation_previs_review`：旁白和 C024 不再同时段发声，中间有明确声音断点，C024 不再作为居中旁白处理。

v0208 不通过为最终成片：画面仍是低模预演，C024 仍使用既有候选源声。若用户听感仍认为 C024 与旁白像同一个人，下一步必须回配音部重新选声或重录 C024，而不是继续用同一素材做 EQ 微调。
