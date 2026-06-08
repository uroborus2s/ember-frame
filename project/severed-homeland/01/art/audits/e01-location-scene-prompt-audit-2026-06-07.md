# E01 Location Scene Prompt Audit

Date: 2026-06-07

## Scope

Checked all `location_episode_scene_card` prompt records in `01/prompts/art-image-prompts.json`:

- `E01_L007` 锁喉关外墙序幕场景卡
- `E01_L003` 金河粮仓带征粮场景卡
- `E01_L014` 南林南缘红线伏笔第01集场景卡
- `E01_L001A` 残阳坳村口封锁地理场景卡
- `E01_L001B` 罗青禾药屋内景与暗格场景卡
- `E01_L001C` 残阳坳旧井检查桌场景卡

## Result

Status: targeted_assets_completed_parent_qc_passed

The six scene prompts now satisfy the dispatch requirements:

- `production_metadata.reference_inputs` points to the required series master location card and episode style references.
- The visible prompt includes the scene inheritance hard lock and the no-text-only generation rule.
- `output_path` routes to `01/assets/locations/`.
- `output_format.background_policy` is `scene_context`.
- `output_format.alpha_policy` is `forbidden`.
- `output_format.canvas_aspect_ratio` is `16:9`.
- `output_format.deliverable_kind` is `location_scene_card`.
- `output_format.composition_layers` includes explicit `foreground`, `midground`, and `background`.
- Foreground and midground layers explicitly derive from the referenced series master scene card.
- Required master/style files exist on disk.

## Repair Applied

Updated `01/prompts/art-image-prompts.json`, `01/art/asset-manifest.json`, `01/art/location-designs.json`, and `01/art/thread-plan.json` to align the scene card output contract:

- Changed scene prompt deliverable kind from the previous extended wording to schema-compatible `location_scene_card`.
- Added foreground, midground, and background layer descriptions for all six location scene cards.
- Added `output_format_requirements` to `location-designs.json`.
- Updated B02 thread-plan output contract to require `16:9` and foreground/midground/background scene layers.
- Removed cross-location template residue from all six scene prompts. `E01_L007`, `E01_L003`, and `E01_L014` no longer carry wrong `残阳坳`/药屋/旧井/后山出口 background instructions; `E01_L001A/B/C` no longer carry unrelated `骨钟`/粮袋墙/红线桌 action-zone residue.
- Repaired `E01_L014` after visual audit found the old prompt and old `history/l014e01.v003.png` candidate treated L014 as a sealed interior room while the approved L014 series master is a southern rainforest red-line exterior. The current prompt now derives foreground, midground, and background from the L014 rainforest/rope-bridge/red-line-marker master and forbids sealed interior room drift.
- Promoted `history/l003e01.v003.png` to `01/assets/locations/l003e01.png` after parent QC confirmed the card is 3840x2160 RGB, no alpha, and visibly derives from the L003 Jinhe granary/river-dock master. The active single-asset L003 child thread stalled without writing a canonical file.

## Dispatch Order

Completed in this order:

1. `E01_L007` -> `01/assets/locations/l007e01.png` (parent QC passed after label correction)
2. `E01_L003` -> `01/assets/locations/l003e01.png` (parent QC passed; canonical promoted from reviewed `history/l003e01.v003.png`)
3. `E01_L014` -> `01/assets/locations/l014e01.png` (parent QC passed; regenerated from L014 rainforest red-line master)
4. `E01_L001A` -> `01/assets/locations/l001ae01.png` (parent QC passed; regenerated from L001 village-gate blockade master geography)
5. `E01_L001B` -> `01/assets/locations/l001be01.png` (parent QC passed after masking text-like cloth/paper/detail-panel marks)
6. `E01_L001C` -> `01/assets/locations/l001ce01.png` (parent QC passed after masking text-like medicine-house cloth/window-paper/check-table register marks)

Each generation task must use the listed master/style images as hard references. If the worker cannot bind or equivalently use the local reference images, it must return `blocked` and must not create a text-only replacement.

## Final QC

All six canonical files are `3840x2160` PNG, RGB, no alpha:

- `E01_L007`: inherits the L007 black-stone gate and snow-wall master geography.
- `E01_L003`: inherits the L003 Jinhe granary, wet-wood dock, grain-sack wall, and checkpoint geography.
- `E01_L014`: inherits the L014 rainforest, rope bridge, wet-stone platform, red-line marker, fire ring, scroll tubes, and valley geography; old sealed interior candidate remains rejected in history.
- `E01_L001A`: inherits the L001 village/check-table/old-well/medicine-house/back-mountain-exit geography and keeps the white wax flags, blockade line, and queue readable.
- `E01_L001B`: inherits the L001 medicine-house subspace; the medicine cabinet, hidden compartment, door line, and exterior blockade pressure remain readable without drifting into a separate mechanism room.
- `E01_L001C`: inherits the L001 old-well/check-table/medicine-house/village-entry geography; old well remains the case center and foreground, midground, and background zones remain readable.
