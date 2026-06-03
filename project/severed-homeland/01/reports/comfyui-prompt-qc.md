# ComfyUI Prompt QC - Episode 01 清明香入村

## Run Summary

- Mode: parent-only Prompt Room run. Child-agent delegation was not used in this thread because the current tool policy requires an explicit user request for sub-agent delegation.
- Shots processed: 36
- Status counts: needs_config=36
- Workflow families: post_text_card=1, i2v_reference_frame=3, i2v_asset_refs=24, i2v_reference_frame_asset_assisted=8
- Feedback tuning: no feedback inputs found, tuning log written with `status=no_feedback`.

## Validation Performed

- Parsed all generated JSON outputs successfully.
- Confirmed `production/generation-plan.json`, `prompts/shot-prompts-draft.json`, and `shots/shot-list.json` each contain 36 shot records.
- Confirmed every generated shot card has `shot_id`, `generation_method`, `workflow_family`, positive/negative prompt, asset refs, parameter profile, continuity refs, source refs, and status.
- Confirmed reference frame files currently used by the first trial shot exist.

## Open Configuration

All video shots remain `needs_config` until the ComfyUI production department chooses a concrete video model checkpoint, I2V workflow template, sampler, scheduler, CFG, steps, FPS, and final 9:16 resolution profile.

## Missing Assets

No missing assets were detected from declared reference frame paths and manifest asset IDs. Some manifest paths are project-level shared assets and should be resolved from `project/severed-homeland/assets/` during production.

## First Video Trial: SC001-SH002

- Workflow family: `i2v_reference_frame`
- Input frame: `01/assets/reference-frames/sc001_sh002_northern_battle_fragment.png`
- Output target: `comfyui/renders/SC001-SH002/SC001-SH002.mp4`
- Main risk: first-frame drift, too much battle scale, fake/readable symbols, or wall geometry changing.

## Handoff Recommendation

Send `SC001-SH002` to ComfyUI production first. If the motion test succeeds, continue the rest of `PG01-intro-montage`; if it fails, tune the I2V workflow before moving to character-heavy shots.
