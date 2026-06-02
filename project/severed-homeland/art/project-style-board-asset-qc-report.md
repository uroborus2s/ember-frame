# Project Style Board QC Report

Date: 2026-06-03

Scope: Project-level global style board for 《断航故土》第一季《残阳驿火》. This pass corrects the generated style-board assets so faction marks reference the current stable emblem PNGs instead of newly invented emblem geometry.

## Deliverables

- `project/severed-homeland/art/project-style-board-low-magic-eastern-epic.md`
  - Added the hard rule that faction emblems must use current stable PNGs as visual references.
- `project/severed-homeland/art/project-style-board-manifest.json`
  - Marks the four style-board assets as generated with native emblem-reference regeneration.
- `project/severed-homeland/prompts/project-style-board-image-prompts.json`
  - Adds stable emblem references and forbids invented faction marks, pasted square samples, and sticker overlays.
- `project/severed-homeland/art/project-style-board-thread-plan.json`
  - Updates future worker instructions to use the current emblem PNGs as original visual references.
- `project/severed-homeland/art/project-style-board-thread-results.json`
  - Records the superseded initial outputs and the final native regeneration pass.
- `project/severed-homeland/assets/style/project-style-board/*.png`
  - Four regenerated vertical PNG style boards using the current faction emblem images as references.

## Current Emblem References

| Faction | Stable Reference |
| --- | --- |
| Suming State / Qingming Court | `project/severed-homeland/assets/style/faction-emblems/emblem_suming_qingming_state.png` |
| Zhaoming Empire | `project/severed-homeland/assets/style/faction-emblems/emblem_zhaoming_empire.png` |
| Northern Beastfolk Tribal Alliance | `project/severed-homeland/assets/style/faction-emblems/emblem_northern_beastfolk_alliance_wanshou.png` |

## QC Summary

| Check | Result | Notes |
| --- | --- | --- |
| Project root consistency | PASS | All paths remain under `project/severed-homeland/`. |
| Detached project avoidance | PASS | No separate art-room project was created. |
| Existing emblem safety | PASS | Current stable emblem PNGs were used as references only; they were not edited or overwritten. |
| Native regeneration | PASS | Final stable style-board outputs are regenerated images, not post-hoc sticker composites. |
| 9:16 short-drama fit | PASS | Four outputs are 941x1672 vertical PNGs. |
| Low-magic boundary | PASS | Effects remain subtle residues, wax, smoke, blood marks, and old relay traces. |
| Emblem reference integration | PASS WITH NOTE | Emblems are integrated as prop/material motifs, but fine geometry can still be model-simplified. Future revisions should continue with reference-image editing iterations if pixel-level emblem fidelity is required. |
| Text/watermark | PASS | Direct inspection found no intended text labels, captions, UI, or watermarks. |

## Generated Image Assets

| Asset | Output | Status |
| --- | --- | --- |
| `style_global_mood_low_magic_eastern_epic_v01` | `project/severed-homeland/assets/style/project-style-board/style_global_mood_low_magic_eastern_epic_v01.png` | Native regenerated with emblem references |
| `style_vertical_composition_9x16_v01` | `project/severed-homeland/assets/style/project-style-board/style_vertical_composition_9x16_v01.png` | Native regenerated with emblem references |
| `style_material_palette_v01` | `project/severed-homeland/assets/style/project-style-board/style_material_palette_v01.png` | Native regenerated with emblem references |
| `style_low_magic_vfx_v01` | `project/severed-homeland/assets/style/project-style-board/style_low_magic_vfx_v01.png` | Native regenerated with emblem references |

## Correction Notes

- Initial style-board generations allowed the image model to invent or simplify faction symbols, especially black-sun and sun-and-moon marks.
- A deterministic overlay correction attempt was discarded because it read as pasted reference cards rather than production art.
- Final stable outputs were regenerated natively using the style-board images plus the three current stable emblem PNGs as visual references.
- Future art-room runs must not use generated emblem-like marks unless they clearly derive from the current stable PNG references.

## Validation

- Parsed JSON artifacts with Node.js.
- Checked all four PNGs with `sips` and `file`: 941x1672, RGB, non-interlaced.
- Recorded SHA-256 hashes in `project-style-board-thread-results.json`.
- Performed direct visual inspection of regenerated outputs and reference-emblem integration.

## Handoff

Prompt Room and downstream asset-generation threads should use `project-style-board-image-prompts.json` together with the three current stable emblem PNGs. If a downstream image needs exact emblem geometry, use reference-image editing/generation rather than prompt-only description or post-hoc sticker compositing.
