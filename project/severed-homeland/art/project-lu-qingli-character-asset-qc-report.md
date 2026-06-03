# 《断航故土》陆青砾角色板 QC 报告 v01

Scope: Project-level Lu Qingli / 陆青砾 multi-state character reference board.

## Created Asset

| Asset ID | Path | Dimensions | SHA-256 |
| --- | --- | --- | --- |
| `character_lu_qingli_multi_state_board_v01` | `project/severed-homeland/assets/characters/character_lu_qingli_multi_state_board.png` | 864x1821 | `6bc1224e5aaf22185ae94a508ff7ae0a1f9b0fd0640379de77b966557140814e` |

## Locked References Checked

| Reference | Result |
| --- | --- |
| `assets/style/project-style-board/style_global_mood_low_magic_eastern_epic_v01.png` | Used for restrained low-magic, tactile production-board style; not modified. |
| `assets/style/project-style-board/style_material_palette_v01.png` | Used for material realism and swatch language; not modified. |
| `assets/style/regional-color-system/style_border_to_north_palette_v01.png` | Used for Wallfoot-to-snowline color continuity; not modified. |
| `assets/style/faction-symbol-boards/symbol_wallfoot_hybrids_system_v01.png` | Used as object-symbol reference only; no formal Wallfoot badge created. |
| `assets/props/prop_wallfoot_trade_tokens.png` | Used for black wood pass, broken pottery charm, grey-blue cord, old yellow cloth, and hidden-pocket continuity; not modified. |
| `assets/style/base-material-boards/material_border_wall_blackstone_snowline_v01.png` | Used for borrowed snowline scarf, leather knee guard, frost, and border material; not modified. |

## Visual QC

| Check | Result | Notes |
| --- | --- | --- |
| Three character states present | PASS | Wallfoot market, escape light, and borrowed snowline states are visible as one continuous identity. |
| Age and body lock | PASS | Character reads as a petite 15-16-year-old girl with compact, fast-moving posture. |
| Wallfoot costume continuity | PASS | Grey-blue short jacket, terracotta layer, old yellow pocket cloth, compact belt, and repair stitching are present. |
| Object-based identity | PASS | Black wood pass, broken pottery charm, hidden pocket, narrow knife, and trade-cord logic are visible. |
| Hybrid-trait restraint | PASS | Ear-back dark-green scale arcs appear in close detail only; no monsterized anatomy. |
| Badge safety | PASS | No new formal Wallfoot emblem or personal crest is created; existing faction emblem files were not modified. |
| No visible text or labels | PASS | The board reads as an unlabeled production collage with no readable captions. |
| Snowline overlay | PASS | Borrowed scarf, short leather knee protection, snow dust, and frost are present without turning her into a Grey Wall soldier. |
| File placement | PASS | Final confirmed asset is saved at the canonical output path. |

## Validation Performed

- `jq empty` on all new JSON planning and result files.
- Visual inspection with local image view.
- `sips -g pixelWidth -g pixelHeight` confirmed 864x1821 PNG dimensions.
- `shasum -a 256` recorded the final asset checksum.
- `file` confirmed PNG image data.

## Handoff Notes

Prompt Room should reference `character_lu_qingli_multi_state_board_v01` as the first stable Lu Qingli identity lock. For shot prompts, preserve the grey-blue short jacket, terracotta inner layer, old yellow pocket cloth, black wood pass, broken pottery charm, hidden pocket stitching, narrow knife, back-near-wall body language, and tiny ear-back scale arcs. Do not introduce a Wallfoot badge, new faction emblem, or clean old-imperial symbol for her.
