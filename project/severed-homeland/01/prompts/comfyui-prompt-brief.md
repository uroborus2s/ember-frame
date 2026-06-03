# ComfyUI Prompt Brief - Episode 01 清明香入村

## Scope

Project root: `project/severed-homeland/01`. This Prompt Room run converts the current director-room and art-room handoff into ComfyUI-ready prompt artifacts for 36 shots.

## Production Intent

The episode must feel like a grounded 9:16 low-magic Eastern epic: war pressure and Qingming institutional violence arrive at a family threshold. Prompting must preserve restraint: close/medium-close frames, tactile period materials, cold-white Qingming details, dusk mud/herb colors, and partial Zhaoming relic traces.

## Method Mapping

- `POST_TEXT_CARD` is handled as `post_text_card`; generated video is not required unless a plain black plate is needed.
- `REFERENCE_IMAGE` becomes `i2v_reference_frame` when a reference frame exists.
- `REFERENCE_IMAGE_ASSISTED_I2V` becomes `i2v_reference_frame_asset_assisted`.
- `I2V_WITH_ASSET_REFS` becomes `i2v_asset_refs`.

## Global Locks

- STYLE_GROUNDED_EPIC
- LOC_CANYANGAO_GEOGRAPHY
- RULE_QINGMING_SMOKE_LOW
- RULE_NO_YAN_NANZHI_REVEAL
- RULE_NO_MOON_JADE_FULL_REVEAL

## First Trial Recommendation

Generate `SC001-SH002` first. It already has a locked reference frame and does not require character identity conditioning, making it the safest first I2V test for motion, snow, smoke, wall geometry, and symbol drift.

Input frame: `01/assets/reference-frames/sc001_sh002_northern_battle_fragment.png`.

## Configuration Still Needed

Model checkpoint, I2V workflow template, sampler, scheduler, CFG, steps, FPS, and exact resolution are intentionally marked `needs_config`; no ComfyUI model IDs or node template IDs were invented in this run.
