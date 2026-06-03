# 《断航故土》白翳角色板 QC 报告 v01

Scope: Project-level Bai Yi / 白翳 multi-state character reference board.

## Created Asset

| Asset ID | Path | Dimensions | SHA-256 |
| --- | --- | --- | --- |
| `character_bai_yi_multi_state_board_v01` | `project/severed-homeland/assets/characters/character_bai_yi_multi_state_board.png` | 863x1822 | `66bb36c8a85c6f4e4182a150bc8345f019f3b1563808e81b6b68102cc792ae6d` |

## History

| History File | Reason | SHA-256 |
| --- | --- | --- |
| `project/severed-homeland/assets/characters/history/character_bai_yi_multi_state_board.v001.png` | Superseded first pass with overly inhuman/ugly face plate anatomy. | `f6411ebba3a6d719802bd7642424f4ef6d84cfb1f34b5aef98d08477f7af3e7a` |
| `project/severed-homeland/assets/characters/history/character_bai_yi_multi_state_board.v002.png` | Superseded near-human face pass because compound eyes needed stronger visual recognizability. | `372dfcac67c2c3b7b09fd411888bb7cae7f70b826b55612262bf0ba8bdf9b18f` |
| `project/severed-homeland/assets/characters/history/character_bai_yi_multi_state_board.v003.png` | Superseded stronger compound-eye pass because bald insectoid designs now require a rear money-tail / rat-tail pigtail. | `394434db41c795c5b992e91decbd70de663a0b262806a30e785e0901b588a5c5` |

## Locked References Checked

| Reference | Result |
| --- | --- |
| `assets/style/faction-emblems/emblem_suming_qingming_state.png` | Used as locked institutional badge language; not modified. |
| `assets/style/faction-symbol-boards/symbol_suming_qingming_system_v01.png` | Used for seal, register, collar, and small robe-mark logic; not modified. |
| `assets/style/base-material-boards/material_qingming_insect_wax_white_v01.png` | Used for wax-white, bone-white, membrane, register, and cold-gold material language; not modified. |
| `assets/props/prop_qingming_white_register.png` | Used for white-register prop continuity; not modified. |
| `assets/props/prop_qingming_court_tool_board.png` | Used for insect-wax needle and incense tool continuity; not modified. |

## Visual QC

| Check | Result | Notes |
| --- | --- | --- |
| Three character states present | PASS | Inspector robe, formal pseudo-human ruler robe, and pursuit official robe are all visible as one continuous identity. |
| Corrected near-human face | PASS | Face is now cold, handsome, and close to human official proportions rather than an ugly insect skull or white mask. |
| Compound-eye recognizability | PASS | Eyes are larger black almond-shaped compound-eye surfaces with clearer dark mass and close-up texture, while still set into a refined human face. |
| Rear pigtail requirement | PASS | Back-head detail includes a single thin low rear pigtail under the official hat, distinct from full human hair or a modern ponytail. |
| Insect traits retained | PASS | Strong black compound eyes, over-2-meter slender vertical proportions, elongated hands, wing-membrane cape, and subtle neck/chitin undertone keep upper-intelligence insect identity readable. |
| Qingming wardrobe continuity | PASS | Dustless white official robe, bone-white collar, wing-membrane cape, cold-gold pins, white register, wax needle, and incense line are present. |
| Emblem safety | PASS | The generated marks are small institutional usages; no existing emblem file was overwritten or replaced. |
| No visible text or labels | PASS | The board reads as an unlabeled production collage. |
| No black-armor drift | PASS | Pursuit state stays white and official rather than becoming a combat warlord. |
| Low-magic boundary | PASS | Qingming incense is a thin physical tracking line, not a spell attack. |
| File placement | PASS | Final confirmed asset is saved at the canonical output path. |

## Validation Performed

- `jq empty` on all new JSON planning files.
- Visual inspection with local image view.
- `sips -g pixelWidth -g pixelHeight` confirmed 863x1822 PNG dimensions.
- `shasum -a 256` recorded the final asset checksum.
- `file` confirmed PNG image data.

## Handoff Notes

Prompt Room should reference `character_bai_yi_multi_state_board_v01` as the stable Bai Yi identity lock. For shot prompts, keep the near-human cold handsome face, large black almond-shaped compound eyes with visible micro-lens texture, single thin rear money-tail / rat-tail pigtail, over-2-meter slender body, white official silhouette, thin wing membrane, white register, wax needle, and cold-white incense thread. Do not re-explain or redraw the Qingming emblem; cite the locked emblem and symbol-system files when a mark is needed.
