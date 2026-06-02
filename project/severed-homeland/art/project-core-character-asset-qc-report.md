# 《断航故土》项目级核心角色资产 QC

Date: 2026-06-03

Scope: 晏南枝多状态角色板与本次新增的沈照眠多状态角色板。沈维桑角色板按既有项目级计划和资产文件保留。

## Final Asset

| Asset ID | File | Status |
|---|---|---|
| `character_yan_nanzhi_multi_state_board_v01` | `project/severed-homeland/assets/characters/character_yan_nanzhi_multi_state_board.png` | pass |
| `character_shen_zhaomian_multi_state_board_v01` | `project/severed-homeland/assets/characters/character_shen_zhaomian_multi_state_board.png` | pass |

## History

| File | Reason |
|---|---|
| `project/severed-homeland/assets/characters/history/character_yan_nanzhi_multi_state_board.v001.png` | rejected: character read too masculine and included a large background emblem-like diagram |
| n/a | 沈照眠本次无保留中间稿；内置生成源文件保留在 Codex 默认生成目录，并记录于 `project-core-character-thread-results.json` |

## QC Checks

| Check | Result | Notes |
|---|---|---|
| Adult female identity | pass | Final board clearly reads as an 18-year-old woman rather than a male or androgynous model. |
| Beauty lock | pass | Face, hair, neck, hands, and silhouette now support “冷艳、贵气、美艳绝伦”的角色方向. |
| Three-state continuity | pass | Fugitive concealment, old empire formal reveal, and border snowline states share the same face, hair cord, and posture logic. |
| Costume system inheritance | pass | Uses mist purple/cold grey travel state, vermilion/royal blue formal state, and dark grey snowline cloak from existing costume system. |
| Prop continuity | pass | Moon-white jade, blood-writ packet, black lacquer case, and hidden proof-object handling align with the carry-prop board. |
| Badge rule | pass with note | No new large Zhaoming badge or background emblem is present. Small ornamental clasps and fabric motifs should be treated as inherited ornament, not redesigned faction marks. |
| Text/watermark | pass | No visible labels, readable text, UI, or watermark. |
| History hygiene | pass | Rejected image was moved to `assets/characters/history/` and renamed with `.v001`. |

## Shen Zhaomian QC Checks

| Check | Result | Notes |
|---|---|---|
| Child age lock | pass | Three full-body states all read as an 8-10-year-old child rather than a teenager or adult. |
| Three-state continuity | pass | Village herb-child, post-fire missing-child anchor, and Qingming Court child-white identifier states share the same face, hair, pouch, and body scale. |
| Costume system inheritance | pass | Uses light grey village garment, herb-green apron/pouch, burnt hair cord, and clean Qingming white child robe with narrow sleeves. |
| Prop continuity | pass | Burnt hair cord, herb pouch, blank herb tags, and insect-wax identification ring align with `prop_shen_zhaomian_child_relics.png` and episode-02 continuity. |
| Badge rule | pass | No new Qingming badge, Zhaoming emblem, Sun-Moon mark, child crest, or large institutional logo is introduced. |
| Text/watermark | pass | No visible labels, readable herb-tag writing, UI, or watermark. |
| Child-safety presentation | pass with note | The post-fire state is emotionally distressed and dirtier than the ideal shot-level baseline, but it avoids gore, torture display, and horror-victim framing. Downstream prompts should keep distress localized and preserve complete child garment structure. |
| History hygiene | pass | No rejected or alternate image remains in the project asset directory. |

## Handoff Notes

Prompt Room should use `character_yan_nanzhi_multi_state_board_v01` as the primary Yan Nanzhi character identity reference. For shot prompts, preserve the corrected female beauty lock and keep old empire proof objects hidden in fugitive and snowline states.

Prompt Room should use `character_shen_zhaomian_multi_state_board_v01` as the primary Shen Zhaomian character identity reference. For shot prompts, preserve child proportions, keep the herb pouch and burnt hair cord as family-memory anchors, and show Qingming institutional pressure through the white child robe and insect-wax ring rather than any new badge.
