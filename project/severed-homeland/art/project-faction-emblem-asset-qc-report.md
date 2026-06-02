# Project Faction Emblems Current QC Report

Date: 2026-06-02

Scope: Maintain one current public art reference emblem per faction for the Zhaoming Empire, Suming State / Qingming Court, and Northern Beastfolk Tribal Alliance. Zhaoming and Northern Beastfolk use the accepted v02 revisions as current images; Suming keeps the approved v01 image. Earlier v03/v04 faction flag sheets were not used as source images or redraw bases.

## Deliverables

- `project/severed-homeland/prompts/project-faction-emblem-prompts.json`
  - Historical v01 prompt source.
- `project/severed-homeland/prompts/project-faction-emblem-prompts-v02.json`
  - Current prompt source for the accepted Zhaoming and Northern revisions, with Suming reused from v01.
- `project/severed-homeland/art/project-faction-emblem-thread-plan.json`
  - Historical v01 background thread plan and thread IDs.
- `project/severed-homeland/art/project-faction-emblem-thread-plan-v02.json`
  - Current v02 background thread plan and thread IDs.
- `project/severed-homeland/art/project-faction-emblem-thread-results.json`
  - Historical v01 thread outputs, generation IDs, and asset paths.
- `project/severed-homeland/assets/style/faction-emblems/emblem_zhaoming_empire.png`
  - Current Zhaoming Empire emblem, v02.
- `project/severed-homeland/assets/style/faction-emblems/emblem_suming_qingming_state.png`
  - Current Suming State / Qingming Court emblem, v01.
- `project/severed-homeland/assets/style/faction-emblems/emblem_northern_beastfolk_alliance_wanshou.png`
  - Current Northern Beastfolk Tribal Alliance Wanshou emblem, v02.
- `project/severed-homeland/assets/style/faction-emblems/history/asset-history.md`
  - Current version table and historical archive policy.

## Current Image Policy

- Active downstream references must use the stable unversioned PNG files directly under `project/severed-homeland/assets/style/faction-emblems/`.
- When an emblem is revised, archive the previous current PNG to `project/severed-homeland/assets/style/faction-emblems/history/` with the next `_vNN` filename before replacing the stable current file.
- Do not point prompts, shot plans, or production docs at historical files unless the task is explicitly comparing old versions.

## QC Summary

| Asset | Current Version | Result | Notes |
| --- | --- | --- | --- |
| Zhaoming Empire | v02 | PASS | Single centered maritime sun-and-moon emblem. The current image reads as an advanced imperial astrolabe/compass seal with gold sun rays, moon-white ring, and deep vermilion craft language. |
| Suming State / Qingming Court | v01 | PASS | Single centered emblem. The outer insect motif is thin and subordinate, not oversized. The black sun's white halo contains visible black seepage, soot cracks, and overflow. |
| Northern Beastfolk Tribal Alliance | v02 | PASS | Single centered Wanshou alliance emblem. The current image uses bone, antler, old wood, hide cord, ash, and pigment, with no metal or advanced technology cues. |

## Technical Verification

- All three current output files exist in `project/severed-homeland/assets/style/faction-emblems/`.
- All three output files are PNG images at `1254x1254`, RGB, non-interlaced.
- Superseded Zhaoming v01 and Northern v01 files exist in `project/severed-homeland/assets/style/faction-emblems/history/`.
- Visual inspection confirms each current file is one standalone emblem image.
- No image contains text, captions, watermark, multi-panel sheet layout, flag sheet layout, character portrait, or a modern national flag treatment.
