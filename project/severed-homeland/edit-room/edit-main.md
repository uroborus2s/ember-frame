# 剪辑部当前入口

owner: edit-room
status: v0002_failed_diagnostic_waiting_rewrite
last_updated: 2026-06-21

## 1. 当前任务

第 01 集 G-P 已进入下游制作准备。根据用户复审，v0001 虽有旁白和配乐，但五句解释性旁白、声画关系和戏剧冲突读法失败；总导演撤回 v0001 声音叙事策略。剪辑部已生成 G-P director cut preview v0002 clarity rewrite：31.000s、1024x576、24fps、48 kHz stereo。最新用户复审继续判定 v0002 仍不可读：P-01 像静态边墙图片，旧台词不直接，战争、强行征粮、儿童训化和追捕压力没有被镜头动作打出来。总导演已撤回 v0002 clarity approval；v0002 现在只保留为失败诊断样片，不是叙事纠错通过版，更不是最终 4K 成片。正式剪辑必须等待新剧本台词、新源镜头、final 配音、final 音乐 / 声效 stem、precision overlays 和交付 QC。

当前预览：

- `edit-room/.work/asset-versions/G-P-edit-preview/20260621v0002-clarity-rewrite/G-P_director_cut_preview_v0002_1024x576_24fps_clarity_rewrite.mp4`
- QC: `edit-room/G-P-director-cut-preview-v0002-qc.md`
- v0001 保留为失败诊断证据：`edit-room/G-P-director-cut-preview-v0001-qc.md`

## 2. 总导演剪辑命令

剪辑部现在接收节奏命令，但不得用剪辑掩盖视频或上游资产缺口。

G-P 的剪辑链必须保持：

```text
P-01 北方兽族撞关 / 粮仓锁死 / 军户被迫拉弩
-> P-02 边墙缺粮 / 强行征粮 / 全户入册
-> P-03 旧歌触发 / 孩子被带走教成识别童
-> P-04 旧驿血牒 / 追捕线北上
-> P-05 白册合页落到残阳坳 / 鸡叫被铜锣截断
```

任何粗剪如果删掉四个制度伤害动作中的一个，直接判定返工。

## 3. G-P 剪辑铁律

冷开必须保留四个制度伤害动作：北墙战争、边墙征粮、清明籍验声、南缘追捕。不得为了快而删掉任一因果证据。

## 3.1 G-P Director Cut Preview v0001

status: withdrawn_narration_strategy_kept_as_diagnosis

| 分镜 | 时间 | 剪辑目的 |
|---|---:|---|
| P-01 | 0.0-5.0s | 粮门闭锁、骨钟、绞盘手可读；不再黑屏 |
| P-02 | 5.0-11.0s | 登记、按手、掌印、母亲护子失败 |
| P-03 | 11.0-17.0s | 旧歌、虫蜡针打断、归档 |
| P-04 | 17.0-22.5s | 后门逃出、跨门槛重心 |
| P-05 | 22.5-31.0s | 侧背少年、兔血、封路、铜锣余音 |

旁白 / 音乐当前为 preview，不可作为 final 交付音频。

## 3.2 G-P Director Cut Preview v0002 Failed Diagnostic

status: failed_user_review_dialogue_and_visual_storytelling_rewrite_required

| 分镜 | 时间 | 失败原因 / 新剪辑方向 |
|---|---:|---|
| P-01 | 0.0-5.0s | 失败：像静态边墙图，旧台词听不懂。下一版必须先建立“北方兽族撞关 / 粮仓锁死 / 军户被迫拉弩”。 |
| P-02 | 5.0-11.0s | 失败：征粮仍不够直接。下一版必须按“掀粮 -> 拖老人 -> C017 按孩子手入虫蜡”剪动作链。 |
| P-03 | 11.0-17.0s | 失败：旧声入册偏设定。下一版必须让观众看懂“孩子因旧歌被带走，教成识别童”。 |
| P-04 | 17.0-22.5s | 失败：追捕令偏公文。下一版必须用旧驿血牒、后门逃跑、白册追捕令剪出危险证据北上。 |
| P-05 | 22.5-31.0s | 等前四镜重拍后重新接剪；不能让 P-05 独自承担世界观落点。 |

v0002 不通过叙事清晰度修正，也不通过动作表演 QC。下一版剪辑必须等待编剧 / 导演重写后的配音和视频部重拍 / 升级源镜头。

## 4. 归口规则

过程剪辑和候选版本进入 `edit-room/.work/`；导演认可后的剪辑交接回到对应分镜目录 `assets/edit/`。
