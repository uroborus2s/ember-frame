# 《断航故土》孟归藏角色资产 QC

Date: 2026-06-03

Scope: 孟归藏项目级多状态角色板。

## Final Asset

| Asset ID | File | Status |
|---|---|---|
| `character_meng_guizang_multi_state_board_v01` | `project/severed-homeland/assets/characters/character_meng_guizang_multi_state_board.png` | pass |

## History

| File | Reason |
|---|---|
| `project/severed-homeland/assets/characters/history/character_meng_guizang_multi_state_board.v001.png` | retained first pass: robe damage read closer to ragged fugitive costuming and the half-burned eyebrow was less explicit |

## QC Checks

| Check | Result | Notes |
|---|---|---|
| Character identity | pass | Final board reads as a 35 to 45 year old human dead-book archivist rather than a wizard, priest, court scholar, commander, or beggar. |
| Three-state continuity | pass | Ashen Academy guide, archive-reveal, and marsh/flight archive-guard states share the same face, robe, book-box harness, and archive tool system. |
| Costume system | pass with note | Deep grey scholar travel robe remains complete and professional with controlled scorched edges. Some hem damage remains visually present; downstream shot prompts should keep damage localized and avoid further raggedness. |
| Bible anchors | pass | Half-burned eyebrow, blackened book box, bone-fragment page clips, paper packets, wax pouches, old book cords, and ash-marked hands are visible. |
| Archive-prop readability | pass | Book box, bone clips, pouches, cords, charred paper, and material swatches are readable as a reusable production reference. |
| Badge rule | pass | No clean Zhaoming, Suming/Qingming, or new Old Book Society emblem appears as wearable identity. Circular and seal-like traces stay as damaged archive evidence. |
| Text/watermark | pass | No visible labels, readable text, UI, or watermark. |
| Low-magic boundary | pass | No glowing book, levitating pages, spell circle, or high-magic effect. |
| History hygiene | pass | Rejected first pass is stored under `assets/characters/history/` with a `.v001` suffix; canonical output path contains only the selected final. |

## Handoff Notes

Prompt Room should use `character_meng_guizang_multi_state_board_v01` as the primary Meng Guizang identity and wardrobe reference. For shot prompts, preserve the complete scholar-robe silhouette, the half-burned eyebrow, the smoke-black book-box harness, and the bone-clip/page-pouch system. Any Zhaoming or Qingming symbol language must remain broken archive evidence, never a clean badge or a new Old Book Society logo.
