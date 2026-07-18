# G-P P-01..P-05 ComfyUI 视频 QC

owner: video-production-room + director-room
status: v0001_v0002_v0003_motion_candidates_generated_not_final
date: 2026-06-21

## 1. 工具与参数

- ComfyUI: `http://127.0.0.1:8188`，`system_stats` 可访问。
- workflow: Wan2.2 I2V，基于 `project/video-primer/assets/workflows/wan22/video_wan2_2_14B_i2v.json` 展开为 API prompt。
- models: `wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors`、`wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors`、两套 4-step I2V LoRA、`umt5_xxl_fp8_e4m3fn_scaled.safetensors`、`wan_2.1_vae.safetensors`。
- common output: 640x368, 49 frames, 16 fps, about 3.0625s, no final audio.
- contact overview: `video-production-room/.work/asset-versions/G-P-video-v0001-contact-overview.png`
- P-04/P-05 retake overview: `video-production-room/.work/asset-versions/G-P-P04-P05-v0002-contact-overview.png`
- P-05 insert overview: `video-production-room/.work/asset-versions/P-05-video/20260621v0003/P-05_rabbit_blood_insert_contact.png`

## 2. 输出清单

| shot | prompt_id | seed | hidden video path | QC |
|---|---:|---:|---|---|
| P-01 | `c4addf7e-5eba-4a1d-b7c2-12294efda076` | `1225057856` | `video-production-room/.work/asset-versions/P-01-video/20260621v0001/P-01_action_i2v_49f_00001_.mp4` | motion_candidate_pass_not_final |
| P-02 | `ae2cbb5e-45ca-48bb-9937-c0962ff7e4dc` | `667849806` | `video-production-room/.work/asset-versions/P-02-video/20260621v0001/P-02_action_i2v_49f_00001_.mp4` | motion_candidate_pass_not_final |
| P-03 | `eb5ec124-5c84-49c8-be84-cfae07c38b8c` | `134185335` | `video-production-room/.work/asset-versions/P-03-video/20260621v0001/P-03_action_i2v_49f_00001_.mp4` | motion_candidate_pass_not_final |
| P-04 | `aed47842-51f2-4ace-8f2f-e974945a32b7` | `1710700544` | `video-production-room/.work/asset-versions/P-04-video/20260621v0001/P-04_action_i2v_49f_00001_.mp4` | route_candidate_conditional_retake_needed |
| P-05 | `66dfc284-9d7a-4a15-9028-f640fa7baa17` | `773265299` | `video-production-room/.work/asset-versions/P-05-video/20260621v0001/P-05_action_i2v_49f_00001_.mp4` | geography_candidate_conditional_retake_needed |
| P-04 retake | `e5705c8d-c2ca-4fcf-8547-aaf4df082ce8` | `206214041` | `video-production-room/.work/asset-versions/P-04-video/20260621v0002/P-04_escape_action_retake_i2v_49f_00001_.mp4` | motion_candidate_pass_not_final |
| P-05 wide retake | `0e147458-9995-45a4-9fc3-6031e2be3747` | `206215052` | `video-production-room/.work/asset-versions/P-05-video/20260621v0002/P-05_prop_evidence_retake_i2v_49f_00001_.mp4` | geography_age_candidate_pass_not_final |
| P-05 rabbit/blood insert | `cca90541-a221-4600-ab8d-9608620db3dc` | `206215153` | `video-production-room/.work/asset-versions/P-05-video/20260621v0003/P-05_rabbit_blood_insert_i2v_49f_00001_.mp4` | insert_candidate_pass_not_final |

## 3. 导演 QC

### P-01

- 通过点：黑石边墙、骨钟、床弩 / 绞盘和粮门压力基本保住；镜头有可用的低速压迫运动。
- 未通过成片点：低清、无 final 声音；粮门与人物动作还没有精确声画点，不能交剪辑当正式镜头。

### P-02

- 通过点：C017 仍读作深色混血奴兵并在后段进入按孩子手动作；C016 白袍虫吏在后方登记；C025 母亲仍是保护者，不是按手者。用户指出的角色职责错误在运动里基本没有复发。
- 未通过成片点：本条更像 P-02-S03 按手入蜡素材；踹灶、拖老人、麦粒落泥没有完整拍出，且没有 C016 final 台词和三段口型时间。

### P-03

- 通过点：白墙、儿童队列、识别流程、C016 高位登记和母亲被压制关系稳定；儿童没有明显成人化。
- 未通过成片点：儿童旧歌、虫蜡变色、识字木牌和口型时间仍缺 final 声音 / overlay，不能作为正式成片。

### P-04

- v0001 通过点：红线室到雨檐 / 侧巷的可通行逃跑路线在运动里成立；C007 白翳在远处外院，不堵出口轴线。
- v0001 未通过点：C002 晏南枝后段离画太快，黑匣和奔跑持匣连续性弱；该条只可作为逃跑路线候选，不可升正式。
- v0002 返工裁决：通过运动候选。C002 从红线室后门出线、进入雨檐 / 侧巷的连续逃跑动作保住；C007 留在远处外院，出口轴线打开。仍不是成片，因为缺 C007 final 台词 / 口型时间、C002 喘息、黑匣 / 旧驿 / 白册 overlay、尾帧和终剪规格。

### P-05

- v0001 通过点：残阳坳北坡到村口的空间稳定，C001 沈维桑没有变成明显中年猎户。
- v0001 未通过点：灰兔、兔血、旧铜锣和封路矛尖在运动里不够强；少年身份与道具证据需要更近或更明确的镜头。
- v0002 返工裁决：宽景运动通过候选。C001 年龄和残阳坳地理继续稳定，村口压力可读；但宽景仍不能独立承担灰兔 / 兔血证据。
- v0003 插入镜裁决：通过候选。以正式 P-05 帧裁切首帧生成腰侧证据插入镜，灰兔、兔血、弓身、手部和村口压力均可读。该插入镜可与 v0002 宽景组合成 P-05 正式视频的镜头方案，但仍缺鸡叫、脚步、兔子碰弓、铜锣三下 final 声画时间与终混。

## 4. 总导演裁决

G-P 已经真正开始视频拍摄。v0001/v0002/v0003 是可回看的低清运动候选，不是完整成片，不得复制到 `director-room/season-01/01/G-P/{shot-id}/{shot-id}.mp4`。当前导演裁决：

- 以 P-01/P-02/P-03 为可用运动基准做高规格或分段重跑。
- P-04 v0002 通过运动候选，可作为后续正式镜头基底。
- P-05 采用 v0002 宽景 + v0003 灰兔 / 兔血插入镜组合方案，可作为后续正式镜头基底。
- 在配音、音乐 / 声效、overlay、尾帧和交付规格完成前，成片交付仍保持 blocked。
