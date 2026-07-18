# P-01 v0213 slow-action preflight QC

## 用户反馈

用户指出 v0212 审看版存在三个成立问题：

- 镜头转得太快，观看时眼睛被晃花。
- 人物动作像被加快，不是正常真人表演。
- 撞门镜头看不出巨兽到底在撞哪里。

## 导演裁决

反馈成立。v0212 I2V 运动预检不得晋升 `P-01.mp4`，也不得作为正式节奏模板继续制作。

v0213 的导演返工原则：

- 撞门镜头必须先让普通观众看懂“外部巨兽正在撞关闭的黑石粮门 / 铁栅门洞”。
- 推回镜头必须按自然表演速度呈现，禁止用快切、甩镜、加速或补帧掩盖动作不成立。
- 若镜头时长不足，只允许尾帧停顿或补拍，不允许把人物动作整体加速。

## 本轮新增素材

- `video-production-room/.work/asset-versions/P-01-video/20260622v0212-i2v-preflight/P-01-F1D_director_retake_i2v_73f_1024x576_24fps.mp4`
- `video-production-room/.work/asset-versions/P-01-video/20260622v0212-i2v-preflight/P-01-F1D_director_retake_contact.jpg`
- `video-production-room/.work/asset-versions/P-01-video/20260622v0212-i2v-preflight/P-01-F2C_director_retake_i2v_97f_1024x576_24fps.mp4`
- `video-production-room/.work/asset-versions/P-01-video/20260622v0212-i2v-preflight/P-01-F2C_director_retake_contact.jpg`

## 审看版输出

- 视频：`assets/edit/P-01-v0213-slow-action-preflight-review-20260622.mp4`
- 抽帧：`assets/edit/P-01-v0213-slow-action-preflight-review-20260622.contact.jpg`
- 组装 manifest：`video-production-room/.work/asset-versions/P-01-video/20260622v0212-i2v-preflight/P-01-v0213-slow-action-preflight-assembly-manifest.json`

技术检查：

- 时长：12.0 秒
- 帧数：288 帧
- 帧率：24 fps
- 分辨率：1024x576
- 音轨：1 条 AAC 48 kHz stereo

## 镜头 QC

### F1D 撞门

判定：条件通过，仍需最终清烟版。

成立项：

- 巨兽身体和角已经压到关闭门洞前，撞击对象比 F1B / F1C 清楚。
- 黑石拱门、铁栅、巨兽体量在同一画面里，普通观众能读到外部威胁来自门外。
- 机位基本锁定，没有 v0212 的快速转镜问题。

问题：

- 烟尘仍偏重，正式成片需要 F1E 或新美术首帧把接触点再清出来。
- 门体震动和士兵反应仍偏弱，最终版要加强门栅抖动、落石、守兵后撤反应。

### F2C 推回

判定：通过为本轮慢动作表演预检。

成立项：

- C024 双手和身体重量压在退兵背部 / 肩甲，接触关系可读。
- 退兵被推离锁栅 / 粮仓方向，动作速度接近自然真人表演，不再像快放。
- 锁栅和粮仓方向保留在画面右侧，因果关系比 v0212 清楚。

问题：

- 仍不是最终角色表演，正式版需要角色卡身份 QC、面部年龄 / 身高比例 QC。
- 需要与 C024 台词 cue 精确对齐，当前只用于运动节奏预检。

### F4 锁栅 / 粮仓证据

判定：可作为尾部证据占位，不通过为最终镜头。

成立项：

- 铁栅、粮袋和远处城墙方向可读，能补足“粮仓拿不到”的视觉证据。

问题：

- 动态不足，仍偏静态证据镜头。
- 正式版需要 F4B：锁链晃动、火光、粮袋受震、远处弩位和人影压迫同时存在。

## 总导演结论

v0213 通过为 `v0213_slow_action_preflight_review_ready_not_final`。

它修正了 v0212 的两个主要方向：镜头节奏不再快转、人物推回动作不再加速；撞门对象也比 v0212 清楚。但它仍不是最终 `P-01.mp4`，因为 F1D 烟尘仍重，F3 血手绞盘镜头缺失，F4B 动态证据未完成，角色身份和最终交付 QC 尚未通过。

下一步制作命令：

- 视频部重做 F1E：清烟、锁机位、强化巨兽撞门接触点、门栅震动和守兵反应。
- 视频部补 F3：C021 少年流血手拉床弩 / 绞盘，作为“被迫守门”的情感落点。
- 视频部重做 F4B：铁栅锁链、粮仓不可达、远处弩位压迫必须动态成立。
- 导演部收到 F1E / F3 / F4B 后再做完整 P-01 终审，不得直接写入 `P-01.mp4`。

## 2026-06-22 用户复审撤回

用户继续复审指出：v0213 又变成慢动作，人物发糊，巨兽造型来源不清，撞门的墙和城头墙看不出是同一堵墙。

总导演复审：用户反馈成立。上文“v0213 通过为慢动作表演预检”的结论撤回，改判为：

`v0213_user_review_failed_v0214_upstream_rebuild_required`

后续不得继续沿用 v0213 的 F1D / F2C 作为正式视频素材。下一步必须按 `assets/edit/P-01-v0214-user-review-rejection-and-rebuild-order-20260622.md` 补齐 C021 shot-state、同墙空间控制图、F1E 清晰撞门参考帧和 F2D 清晰推回参考帧；视频部只能在这些上游资产通过后做 1x 自然速度短测试。
