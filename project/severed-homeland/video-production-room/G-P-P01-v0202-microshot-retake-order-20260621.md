# G-P P-01 v0202 Micro-Shot Retake Order

owner: video-production-room + director-room
status: superseded_by_v0204_walltop_firing_retake_order
date: 2026-06-21

superseded_by: `G-P-P01-v0204-walltop-firing-retake-order-20260622.md`

director_note: v0202 拆镜方法已打回。它没有明确床弩位于门楼 / 墙顶射击平台，也没有锁死床弩射界朝城外，容易导向隔墙射击错误。不得继续按本令开拍。

## 1. Director Rejection

P-01 v0201 is rejected. It is technically more visible than earlier failures, but it does not stage the storyboard effect. The shot does not make the audience feel the northern beast impact as an event, the locked grain door as a conflict, or the wall soldiers as people forced back into death.

Do not continue the same single-frame long I2V route for P-01. Do not promote v0201 or v0104 into edit.

## 2. New Method

P-01 v0202 must be built from micro-shots. Each micro-shot owns one action proof, then edit and sound stitch them into the P-01 cold-open beat.

| micro_id | duration target | function | must show | direct fail |
|---|---:|---|---|---|
| P-01A | about 3s | bone bell and gate impact | bell jerks, rope snaps, black gate takes hit, snow dust falls, soldiers react | bell still, gate static, only atmosphere |
| P-01B | about 3s | locked grain and command pressure | locked grain door behind soldiers, C024 forces retreating soldiers back to ballista | grain door as decoration, no commander pressure |
| P-01C | about 3s | blood hand winch action | wrapped bleeding hand contacts frozen iron, body weight drops, winch bites, rope tightens | hand only rests, no resistance or result |
| P-01D | about 3s | trapped end state | taut weapon line, closed door behind, impact outside, soldiers trapped between hunger and death | open door, monster spectacle, heroic charge |

## 3. Current Run

- tool: `video-production-room/.work/tools/run_gp_director_retake_i2v.py`
- tag: `20260621v0202-p01-microshots`
- first queued micro-shot: `P-01A`
- prompt_id: `18348e76-e3ac-42b2-9444-ada34a027a77`
- output root: `video-production-room/.work/asset-versions/P-01-video/20260621v0202-p01-microshots/`

## 4. Sound And Edit Rule

NAR001 only gives the era coordinate. C024 lands in P-01B. Bone bell and low-frequency gate impact land in P-01A. Winch iron and rope tension land in P-01C. P-01D exits into P-02 with low gate pressure, not explanatory narration.

## 5. Promotion Rule

No micro-shot becomes final by itself. Promotion requires director visual QC, voice/music/SFX timing, edit preview, delivery specs, and final approval.
