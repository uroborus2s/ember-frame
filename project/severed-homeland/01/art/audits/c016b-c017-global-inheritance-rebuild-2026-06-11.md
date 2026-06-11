# C016B/C017 全局继承重做记录 / 2026-06-11

## 结论

用户指出 2026-06-11 第一轮 prompt-only 候选仍然发生全局角色脸型/物种结构漂移。该候选未写入项目 canonical 路径，状态为 rejected-not-imported。

当前 `E01_C016B` 与 `E01_C017` 已改为从全局母卡直接派生：

- `E01_C016B` -> `01/assets/characters/c016be01.png`，直接复制 `assets/characters/c016m.png`。
- `E01_C017` -> `01/assets/characters/c017e01.png`，直接复制 `assets/characters/c017m.png`。

这次处理优先满足“脸型、头壳、复眼、颈膜、混血甲片、低位辫发等全局身份不漂移”。但 2026-06-11 用户视觉 QC 已继续退回当前候选：角色一致性与身高差仍未达标。两张图不再是“等待确认”，而是必须按同地平线比例条重生；`R005`-`R009` 继续阻断，不能直接进入视频制作。

## 文件记录

| 资产 | 当前 canonical | 来源 | 当前状态 |
| --- | --- | --- | --- |
| `E01_C016B` | `01/assets/characters/c016be01.png` | `assets/characters/c016m.png` | `failed_user_visual_qc_identity_height_scale_relock_required_2026-06-11` |
| `E01_C017` | `01/assets/characters/c017e01.png` | `assets/characters/c017m.png` | `failed_user_visual_qc_identity_height_scale_relock_required_2026-06-11` |

## 历史保留

- `01/assets/characters/history/c016be01.v003.png`：上一版 rejected canonical。
- `01/assets/characters/history/c017e01.v003.png`：上一版 rejected canonical。

## 未导入候选

- `/Users/uroborus/.codex/generated_images/019eb1fe-0fd9-79c3-be1d-eeff4ef34224/ig_0e81b3de853913eb016a29a5a1511c8191a60563a1d3a87828.png`：prompt-only C016B 候选，因全局脸型/头壳继承不足未导入。
- `/Users/uroborus/.codex/generated_images/019eb1fe-0fd9-79c3-be1d-eeff4ef34224/ig_0e81b3de853913eb016a29a696d610819189d8190199c4ce25.png`：prompt-only C017 候选，因全局身份继承风险未导入。

## 后续门槛

1. 用户确认 `c016be01.png` 与 `c017e01.png` 是否可作为 SC002 上游角色卡。
2. 若通过，再重做 `R005`-`R009`；不得复用旧 SC002 参考帧。
3. 若用户要求 episode-specific 外观变化，必须在全局母卡基础上做局部编辑，不能再用纯文字重造角色。
