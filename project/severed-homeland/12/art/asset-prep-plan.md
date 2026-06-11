# Episode 12 Targeted Art Prep Plan

## Scope

Targeted Art Room pass for `SC003-SH002` only.

The required deliverable is one video-generation reference frame for the I2V shot:

| Asset ID | Shot | Subtype | Output | Priority | Status |
| --- | --- | --- | --- | --- | --- |
| `E12_R024` | `SC003-SH002` | `reference_frame` | `12/assets/reference-frames/r024e12.png` | critical | generated candidate, pending 4K contract |

## Creation Order

1. `PROMPT_E12_R024` image prompt record in `12/prompts/art-image-prompts.json`.
2. `E12_R024` reference frame generation through isolated `imagegen-task`.
3. Parent task copies the generated PNG into `12/assets/reference-frames/r024e12.png`.
4. Parent task records dimensions, SHA-256, source image path, and QC status.

## Dependencies

`E12_R024` depends on these approved series-level assets:

- `C001` Shen Weisang identity, face, body, wardrobe, left-shoulder injury, short knife.
- `C002` Yan Nanzhi exile wardrobe, red hair tie, blood-record pressure.
- `C003` Lu Qingli agile gray-blue street outfit and broken pottery charm.
- `C010` Lu Mi deer-shaman features, blood-salt pouch, snow herb bag.
- `C007` Bai Yi tall insectoid Qingming official silhouette.
- `L011` collapsed beacon tower and snow-slope escape geography.
- `P002` blood record and moon-white jade fragment.
- `P006` blood-salt pouch and snow herb bag.
- `P007` alliance fragment and multi-clan marks.
- `P012` broken pottery charm and hidden pouch logic.
- `F005` 16:9 widescreen action-causality style board.

## Output Format

```json
{
  "deliverable_kind": "video_generation_reference_frame",
  "file_format": "png",
  "minimum_resolution": "4096x2304",
  "background_policy": "video_frame",
  "alpha_policy": "forbidden",
  "canvas_aspect_ratio": "16:9",
  "required_views": [
    "single cinematic medium frame",
    "micro low-angle pressure framing",
    "handheld short-follow feeling",
    "foreground/midground/background separation",
    "lighting, weather, camera angle, and action state visible in-frame"
  ],
  "composition_layers": {
    "foreground": "snow mud, hand or short-knife trace, broken pottery charm pouch or blood-record oil-paper corner",
    "midground": "Shen Weisang low near the half-height collapsed exit, broken steps, falling stones, readable escape action",
    "background": "snow-slope entrance, collapsed beacon tower pressure, wind snow, distant Bai Yi pursuit silhouette"
  }
}
```

## Current Candidate Note

The built-in imagegen candidate is saved at `12/assets/reference-frames/r024e12.png` with actual resolution `1672x941`. It passes the targeted composition/continuity read but remains below the `4096x2304` reference-frame contract. Before final ComfyUI/video handoff, regenerate or upscale to `4096x2304` and re-run QC.

## Additional Scope: SC002-SH001

This run also adds the FLF2V first/last frame pair for `SC002-SH001`.

| Asset ID | Shot | Subtype | Output | Priority | Status |
| --- | --- | --- | --- | --- | --- |
| `E12_R001` | `SC002-SH001` | `reference_frame` | `12/assets/reference-frames/r001e12.png` | critical | complete, 4K upscaled from imagegen candidate |
| `E12_R002` | `SC002-SH001` | `reference_frame` | `12/assets/reference-frames/r002e12.png` | critical | complete, 4K upscaled from imagegen candidate |

Creation order:

1. `PROMPT_E12_R001_SC002_SH001_FIRST_FRAME` in `12/prompts/art-image-prompts.json`.
2. Generate `E12_R001` through an isolated prompt-only `imagegen-task`.
3. Archive the original `1672x941` source to `12/assets/reference-frames/history/r001e12.v001-imagegen-source-20260610.png`.
4. Save the 4K canonical PNG to `12/assets/reference-frames/r001e12.png`.
5. `PROMPT_E12_R002_SC002_SH001_LAST_FRAME` in `12/prompts/art-image-prompts.json`.
6. Generate `E12_R002` through a separate isolated prompt-only `imagegen-task`.
7. Archive the original `1672x941` source to `12/assets/reference-frames/history/r002e12.v001-imagegen-source-20260610.png`.
8. Save the 4K canonical PNG to `12/assets/reference-frames/r002e12.png`.

Dependencies:

- `C001`, `K001`: Shen Weisang identity, hunter wardrobe, left-shoulder limitation.
- `C002`, `K002`: Yan Nanzhi fugitive robe, red-thread hair, restrained posture.
- `C003`: Lu Qingli grey-blue short jacket, small survivor body, broken pottery identity.
- `C010`, `P006`: Lu Mi deer-clan shaman features and bone-flute support.
- `C007`, `K004`, `P004`: Bai Yi and Qingming insect-wax white institutional pressure.
- `L011`: broken tower, cracked steps, snow, collapse, half-height exit.
- `P002`, `P007`: old record bundle, alliance fragment, abstract old marks.

Output format for both assets:

```json
{
  "deliverable_kind": "video_generation_reference_frame",
  "file_format": "png",
  "minimum_resolution": "4096x2304",
  "background_policy": "video_frame",
  "alpha_policy": "forbidden",
  "canvas_aspect_ratio": "16:9",
  "required_views": [
    "single cinematic frame matching project delivery ratio",
    "foreground/midground/background separation",
    "lighting, weather, camera angle, and action state visible in-frame"
  ],
  "composition_layers": {
    "foreground": "broken stair edge, cloth or rope-buckle pressure, wet snow, red-brown weathering, and old evidence props",
    "midground": "Lu Qingli caught at the stair, Shen Weisang moving toward her, Yan Nanzhi readable nearby",
    "background": "broken tower interior, half-height exit, hanging alliance fragment, Lu Mi and Bai Yi pressure silhouettes, windblown snow"
  }
}
```
