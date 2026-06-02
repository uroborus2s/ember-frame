# Project Regional Color System Planning QC Report

Date: 2026-06-02

Scope: Project-level regional color system for 《断航故土》第一季《残阳驿火》, covering 残阳坳、金河、清明院、边墙、北境、南方旧帝国 and auxiliary route regions. This pass creates art direction, a machine-readable palette index, image prompts, and a background-thread plan. No raster image generation was launched.

## Deliverables

- `project/severed-homeland/art/project-regional-color-system.md`
  - Human-readable regional color system and downstream rules.
- `project/severed-homeland/art/project-regional-color-system.json`
  - Machine-readable regional palette index, route progression, and planned image asset list.
- `project/severed-homeland/prompts/project-regional-color-system-image-prompts.json`
  - Tool-neutral image prompts with stable output paths.
- `project/severed-homeland/art/project-regional-color-system-thread-plan.json`
  - Codex background thread plan for later image generation.
- `project/severed-homeland/art/project-regional-color-system-thread-results.json`
  - Current thread status placeholder. Status is `not_started`.
- `project/severed-homeland/assets/style/regional-color-system/.gitkeep`
  - Stable directory placeholder for future regional color-system PNG outputs.

## QC Summary

| Check | Result | Notes |
| --- | --- | --- |
| Project root consistency | PASS | All paths remain under `project/severed-homeland/`. |
| Detached project avoidance | PASS | No separate art-room project was created. |
| Source continuity | PASS | Direction references project background, scenes bible, continuity bible, series outline, and current global style board. |
| Requested regions covered | PASS | Includes 残阳坳、金河、清明院、边墙、北境、南方旧帝国, plus 灰烬书院、墙下集市、旧驿/月下盟书. |
| Regional differentiation | PASS | Each region has a local base palette, power overlay, old-memory/low-magic accents, lighting rules, and forbidden looks. |
| Low-magic boundary | PASS | Accents stay as small glints, broken route lines, incense threads, wax seals, and dry blood marks. |
| 9:16 short-drama fit | PASS | Prompt plan keeps mobile-readable vertical composition and avoids literal map labels. |
| Existing asset safety | PASS | No existing style-board image, faction emblem, or historical asset path is overwritten. |
| Image generation status | PASS | Thread results correctly records no generated images yet and no launched thread IDs. |

## Planned Image Assets

| Asset | Expected Output | Status |
| --- | --- | --- |
| `style_regional_color_route_map_v01` | `project/severed-homeland/assets/style/regional-color-system/style_regional_color_route_map_v01.png` | Pending generation |
| `style_canyang_to_jinhe_palette_v01` | `project/severed-homeland/assets/style/regional-color-system/style_canyang_to_jinhe_palette_v01.png` | Pending generation |
| `style_qingming_institution_palette_v01` | `project/severed-homeland/assets/style/regional-color-system/style_qingming_institution_palette_v01.png` | Pending generation |
| `style_border_to_north_palette_v01` | `project/severed-homeland/assets/style/regional-color-system/style_border_to_north_palette_v01.png` | Pending generation |
| `style_southern_old_empire_palette_v01` | `project/severed-homeland/assets/style/regional-color-system/style_southern_old_empire_palette_v01.png` | Pending generation |

## Risk Notes

- The current global style-board image-generation thread is already in progress in `project-style-board-thread-results.json`; this regional system does not alter that thread.
- The repository has many pre-existing deletions, modifications, and untracked project files unrelated to this regional color-system batch. They are not part of this QC scope.
- Future image generation should inspect outputs for accidental text labels, literal color charts, over-unified grading, high-magic glow, modern industrial/medical cues, and loss of regional differentiation.

## Handoff

Recommended next step: review `project-regional-color-system-image-prompts.json`; if approved, launch the single background thread described in `project-regional-color-system-thread-plan.json`, then update `project-regional-color-system-thread-results.json` with thread ID, generated file paths, dimensions, and retry notes.
