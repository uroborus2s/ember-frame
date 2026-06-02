# Project Base Material Board Planning QC Report

Date: 2026-06-02

Scope: Project-level base material boards for 《断航故土》, covering 昭明旧物、清明院虫蜡白、边墙黑石雪线、金河蒸汽生产、北境骨木皮草. This pass creates the written material system, manifest, image prompts, background-thread plan, thread result record, asset index, and five stable PNG material-board assets.

## Deliverables

- `project/severed-homeland/art/project-base-material-boards.md`
  - Human-readable material-board design direction.
- `project/severed-homeland/art/project-base-material-board-manifest.json`
  - Machine-readable manifest for the material-board batch.
- `project/severed-homeland/prompts/project-base-material-board-image-prompts.json`
  - Tool-neutral image prompts with stable output paths.
- `project/severed-homeland/art/project-base-material-board-thread-plan.json`
  - Codex background thread dispatch plan.
- `project/severed-homeland/art/project-base-material-board-thread-results.json`
  - Final generation and archive result record. Status is `completed`.
- `project/severed-homeland/art/project-base-material-board-asset-index.json`
  - Material-board asset index for downstream departments. Status is `completed`.
- `project/severed-homeland/assets/style/base-material-boards/`
  - Stable output directory for generated PNGs.

## Generated PNG Assets

| Asset | Output | Dimensions | SHA-256 |
| --- | --- | --- | --- |
| `material_zhaoming_relic_v01` | `project/severed-homeland/assets/style/base-material-boards/material_zhaoming_relic_v01.png` | 941x1672 | `0b1a3a444c37e540e5a0d0f81ad29c7d1865f43ea15a9bfd6631460f05837f76` |
| `material_qingming_insect_wax_white_v01` | `project/severed-homeland/assets/style/base-material-boards/material_qingming_insect_wax_white_v01.png` | 941x1672 | `db2e83ac717ecabad25e8bb7c4edc3e1e9f9c682294b4ec7297e16fa9d2fa54c` |
| `material_border_wall_blackstone_snowline_v01` | `project/severed-homeland/assets/style/base-material-boards/material_border_wall_blackstone_snowline_v01.png` | 941x1672 | `dd5a8c6ee11353d27348877876e824df63a3380eff72f5f64f07b75564fa78ec` |
| `material_jinhe_steam_production_v01` | `project/severed-homeland/assets/style/base-material-boards/material_jinhe_steam_production_v01.png` | 941x1672 | `f92b4ee130766c186004de4aeecf3f7af302323410b9ffc07f39d7afb3c1a0a2` |
| `material_northern_bonewood_fur_v01` | `project/severed-homeland/assets/style/base-material-boards/material_northern_bonewood_fur_v01.png` | 941x1672 | `e915d8607300e83940ab3bd7561bfe5082186e66d13aa56a0a2fae60a6953414` |

## QC Summary

| Check | Result | Notes |
| --- | --- | --- |
| Project root consistency | PASS | All paths remain under `project/severed-homeland/`. |
| Detached project avoidance | PASS | No separate art-room project was created. |
| Source continuity | PASS | Direction references project bibles, current global style board, regional color system, and current faction emblems. |
| Requested boards covered | PASS | Includes all five requested material boards. |
| Current faction emblem safety | PASS | Prompts require stable current emblem PNGs as references only and forbid edits to emblem files. |
| Existing asset safety | PASS | No existing global style-board, regional color, faction emblem, or history asset path is overwritten. |
| Visual differentiation | PASS | Each board has its own material language, color logic, forbidden looks, and downstream usage. |
| Low-magic boundary | PASS | Effects remain small physical traces, glints, wax lines, or survival fire. |
| 9:16 production fit | PASS | Prompt plan keeps vertical tactile still-life composition and avoids labeled material charts. |
| Image generation status | PASS | Five accepted cache candidates were archived to stable PNG output paths. |
| PNG format validation | PASS | `file` reports all five stable outputs as PNG image data, 941 x 1672, 8-bit/color RGB, non-interlaced. |
| Dimension validation | PASS | `sips` reports all five stable outputs as 941 x 1672. |
| Visual inspection | PASS | Accepted assets show tactile still-life material boards with no visible text, labels, UI, watermark, or standalone new emblem. |

## Planned Image Assets

| Asset | Expected Output | Status |
| --- | --- | --- |
| `material_zhaoming_relic_v01` | `project/severed-homeland/assets/style/base-material-boards/material_zhaoming_relic_v01.png` | Created |
| `material_qingming_insect_wax_white_v01` | `project/severed-homeland/assets/style/base-material-boards/material_qingming_insect_wax_white_v01.png` | Created |
| `material_border_wall_blackstone_snowline_v01` | `project/severed-homeland/assets/style/base-material-boards/material_border_wall_blackstone_snowline_v01.png` | Created |
| `material_jinhe_steam_production_v01` | `project/severed-homeland/assets/style/base-material-boards/material_jinhe_steam_production_v01.png` | Created |
| `material_northern_bonewood_fur_v01` | `project/severed-homeland/assets/style/base-material-boards/material_northern_bonewood_fur_v01.png` | Created |

## Risk Notes

- Existing repository status contains many unrelated deletions, modifications, and untracked project files. They are outside this material-board scope and were not reverted.
- Background thread `019e88ed-bc0f-7d80-9de9-00c71e0690b7` was still active when the stable archive copy began and had not written the stable paths; after final hash validation it was observed idle.
- Earlier cache candidates were rejected by the generation thread for emblem-like drift or word-like marks. Only accepted candidates are referenced by the asset index.
- Existing repository status contains many unrelated deletions, modifications, and untracked project files. They remain outside this material-board scope and were not reverted.

## Handoff

Recommended next step: use these five material boards as shared references for character costumes, location boards, prop sheets, and shot prompt packs. For future prompt-room work, reference the stable PNG paths above rather than generation-cache paths.
