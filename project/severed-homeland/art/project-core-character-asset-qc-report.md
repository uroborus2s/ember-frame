# 《断航故土》项目级核心角色资产 QC

Date: 2026-06-03

Scope: 沈维桑、晏南枝、沈照眠项目级多状态角色板。

## Final Asset

| Asset ID | File | Status |
|---|---|---|
| `character_shen_weisang_multi_state_board_v01` | `project/severed-homeland/assets/characters/character_shen_weisang_multi_state_board.png` | pass |
| `character_yan_nanzhi_multi_state_board_v01` | `project/severed-homeland/assets/characters/character_yan_nanzhi_multi_state_board.png` | pass |
| `character_shen_zhaomian_multi_state_board_v01` | `project/severed-homeland/assets/characters/character_shen_zhaomian_multi_state_board.png` | pass |

## History

| File | Reason |
|---|---|
| `project/severed-homeland/assets/characters/history/character_shen_weisang_multi_state_board.v001.png` | archived: prior corrected no-badge version before adding clearer activated gold-red dark pattern behavior |
| `project/severed-homeland/assets/characters/history/character_shen_weisang_multi_state_board.v002.png` | archived: prior version with activated close-ups before adding a distinct activated character-state panel |
| `project/severed-homeland/assets/characters/history/character_yan_nanzhi_multi_state_board.v001.png` | rejected: character read too masculine and included a large background emblem-like diagram |
| `project/severed-homeland/assets/characters/history/character_yan_nanzhi_multi_state_board.v002.png` | archived: corrected female beauty version before stronger real-person face reference pass |
| `project/severed-homeland/assets/characters/history/character_yan_nanzhi_multi_state_board.v003.png` | archived: oval-plus-soft-diamond face pass with insufficient first-version recognizability |
| `project/severed-homeland/assets/characters/history/character_yan_nanzhi_multi_state_board.v004.png` | archived: prior final before returning more strongly to the first-version v04 face identity |
| `project/severed-homeland/assets/characters/history/character_yan_nanzhi_multi_state_board.v005.png` | archived: prior final still read closer to guazi/melon-seed than true classical oval face |
| n/a | 沈照眠本次无保留中间稿；内置生成源文件保留在 Codex 默认生成目录，并记录于 `project-core-character-thread-results.json` |

## QC Checks

## Shen Weisang QC Checks

| Check | Result | Notes |
|---|---|---|
| Age and body lock | pass | Final board reads as a 17-year-old lean hunter and guide, not an adult hardman, king, general, or warlord. |
| Three-state continuity | pass | Canyang Ao hunter, post-fire fugitive, and border snowline states preserve one face, silhouette, bow/quiver logic, route pouch, short knife, and hunter posture. |
| Costume system inheritance | pass | Uses grey-brown short layers, washed herb-green inner garment, old leather wrist guards, charred hem, grey hemp snowline cloak, old leather shoulder protection, and wrapped lower legs. |
| Hidden relay-token logic | pass | The half relay token is treated as hidden contraband inside a plain unmarked pouch; no visible token emblem is shown as clothing identity. |
| No old-empire badge | pass | No sun, moon, crescent, compass, medallion, Zhaoming badge, official order, or old-empire insignia appears on shoulder guards, chest straps, cloak, pouch exterior, bow case, belt front, or background. |
| Gold-red dark pattern | pass | The board preserves dormant dark-gold crack/thread texture and adds a distinct activated state group. Activated marks glow warm gold with a gold-red ember core around eye, shoulder/shoulder-blade, hidden seam, and charred hem detail areas. The marks read as bloodline or half-formed martial-vein residue, not faction symbols. |
| Low-magic boundary | pass | Activation remains close-up and localized; no large wings, spell circle, divine aura, whole-body glow, or high-magic attack effect. |
| Text/watermark | pass | No visible labels, readable text, UI, or watermark. |

| Check | Result | Notes |
|---|---|---|
| Adult female identity | pass | Final board clearly reads as an 18-year-old woman rather than a male or androgynous model. |
| Beauty lock | pass | Face, hair, neck, hands, and silhouette support “冷艳、贵气、美艳绝伦”的角色方向 without becoming a generic AI beauty. |
| Face recognizability | pass | Final face returns more strongly to the first-version v04 reference while correcting away from guazi/melon-seed: softly rounded forehead, balanced midface width, fuller living cheeks, gradual cheek-to-jaw curve, short rounded non-pointed chin, heavier guarded eyelids, realistic skin texture, and clearer identity. |
| Three-state continuity | pass | Fugitive concealment, old empire formal reveal, and border snowline states share the same face, hair cord, and posture logic. |
| Costume system inheritance | pass | Uses mist purple/cold grey travel state, vermilion/royal blue formal state, and dark grey snowline cloak from existing costume system. |
| Prop continuity | pass | Moon-white jade, blood-writ packet, black lacquer case, and hidden proof-object handling align with the carry-prop board. |
| Badge rule | pass with note | No new large Zhaoming badge or background emblem is present. Small ornamental clasps and fabric motifs should be treated as inherited ornament, not redesigned faction marks. |
| Text/watermark | pass | No visible labels, readable text, UI, or watermark. |
| History hygiene | pass | Earlier Yan Nanzhi iterations are retained under `assets/characters/history/` with `.v001` through `.v005`; only the current accepted image remains at the canonical output path. |

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

Prompt Room should use `character_shen_weisang_multi_state_board_v01` as the primary Shen Weisang identity reference. For shot prompts, preserve his 17-year-old hunter identity, keep the half relay token hidden, and describe the gold-red dark pattern as dormant under skin/cloth until brief old-relay or martial-vein activation makes it glow in localized warm-gold / gold-red cracks.

Prompt Room should use `character_yan_nanzhi_multi_state_board_v01` as the primary Yan Nanzhi character identity reference. For shot prompts, preserve the corrected female beauty lock, the first-version v04 face recognizability, the true classical oval face rather than guazi/melon-seed taper, and keep old empire proof objects hidden in fugitive and snowline states.

Prompt Room should use `character_shen_zhaomian_multi_state_board_v01` as the primary Shen Zhaomian character identity reference. For shot prompts, preserve child proportions, keep the herb pouch and burnt hair cord as family-memory anchors, and show Qingming institutional pressure through the white child robe and insect-wax ring rather than any new badge.
