# ComfyUI Prompting Guide

Use this guide for the unified Director Room prompt pass. It defines the
expected shape of bilingual ComfyUI-ready prompt artifacts without requiring a
runnable ComfyUI graph.

## Bilingual Contract

Every human-facing storyboard section and every JSON prompt record must include
Chinese and English content:

- Use `_zh` fields for Chinese prompt text.
- Use `_en` fields for English prompt text.
- Do not put only one language in the main field and translate it in notes.
- Keep meaning aligned, but do not force word-by-word translation when English
  prompt tokens need model-friendly phrasing.

## Prompt Layers

Every final video prompt record has two top-level surfaces:

- `production_metadata`: process fields for planning, workflow binding, QC,
  editing, and repair. Include `episode_id`, `shot_id`, `segment_id`,
  `generation_method`, `duration`, `fps`, `aspect_ratio`, `asset_refs`,
  `first_frame_ref`, `last_frame_ref`, `audio_refs`, `workflow_hint`,
  `source_refs`, and `continuity_refs`.
- `model_visible_prompt`: the text intended for the image or video model. It
  must not contain output filenames, `shot_id`, `generation_method`, `asset_id`,
  `episode_id`, workflow IDs, or process-only source refs.

Build `model_visible_prompt` from six stable sections:

1. visible goal;
2. style and image quality;
3. subject content;
4. composition and motion;
5. visible continuity constraints;
6. negative prompt.

For bilingual records, each section should have aligned Chinese and English
text. The video model may be told that a character is speaking, breathing, or
moving their lips lightly, but exact dialogue text belongs in subtitles and
audio files, not in the video prompt.

Build supporting prompt text from stable layers:

1. identity and subject: character, wardrobe, props, visible state;
2. action and emotion: filmable behavior, gesture, expression, interaction;
3. environment: location, time, weather, geography, foreground/background;
4. camera and motion: shot size, lens feel, angle, camera movement, framing;
5. lighting and color: key light, contrast, palette, practical sources;
6. style and continuity: visual locks, material language, recurring motifs,
   forbidden contradictions;
7. quality intent: rendering quality and medium tokens that fit the chosen model
   family.

Keep global style and global negative text in reusable presets. Keep per-shot
prompts limited to what changes for that shot.

## Operator-Facing Copy Prompts

The post-asset ComfyUI package must include an assembled Markdown handoff:

```text
{episode-id}/prompts/comfyui-render-prompts.md
```

This file is the production copy surface for ComfyUI operators. Do not make
operators concatenate JSON fields by hand. For every shot, include these four copy-ready blocks:

```text
positive_prompt_zh
negative_prompt_zh
positive_prompt_en
negative_prompt_en
```

Readable headings are allowed in `comfyui-render-prompts.md`, but the skill
should not hardcode project-specific labels, lighting rules, or style language.
Choose headings from the current project handoff convention or from the stable
`model_visible_prompt` sections. A common mapping is style/image quality, visible
goal, subject content, composition/motion, continuity constraints, and negative
modules; adapt names to the project and language.

Avoid duplicate style anchors in the assembled Markdown. For example, if
`global_positive_prefix` already contains the format and style anchor, strip
that same lead phrase from the shot-level style section before writing the
copy-ready prompt. Keep authoring guidance and QC-only rules out of the final
model-visible prompt text.

Assemble each positive prompt from:

```text
global_positive_prefix_{lang}
+ visible_goal_{lang}
+ style_quality_{lang}
+ subject_content_{lang}
+ composition_motion_{lang}
+ visible_continuity_{lang}
+ global_positive_suffix_{lang}
```

Assemble each negative prompt from:

```text
global_negative_{lang}
+ negative_prompt_{lang}
```

Keep `comfyui-shot-prompts.json` as the structured source of truth for review,
QC, and automated repair. Keep `comfyui-render-prompts.md` as a derived handoff
for direct prompt-node copying. If the two disagree, fix the structured source
and regenerate the Markdown.

## Storyboard Prompt Structure

The storyboard plan must use this bilingual section structure:

```text
1. 基础设定 / Basic Setup
2. 氛围和画质 / Atmosphere and Image Quality
   2.1 风格核心 / Style Core
   2.2 视觉基调 / Visual Tone
   2.3 色彩和影调 / Color and Tonal Range
3. 画面内容 / Shot Panels
   分镜一 / Shot 1
     景别 / Shot Size:
     构图 / Composition:
     运镜手法 / Camera Movement:
     画面内容 / Visual Content:
     光线与色彩 / Lighting and Color:
     连续性锚点 / Continuity Anchors:
```

The content under each label must include Chinese and English. Use one compact
paragraph per language when a field is long.

## Generation Method Mapping

- `T2V`: use text prompt plus optional style references. Use when no exact
  reference frame is required and identity risk is low.
- `I2V`: use an image reference or first frame plus prompt. Use when identity,
  costume, location, or composition continuity matters.
- `FLF2V`: use first and last frames plus prompt. Use when motion destination,
  pose transition, or screen direction must be constrained.
- `REFERENCE_IMAGE`: use image generation or still-frame workflows with asset
  references. Use for character sheets, inserts, location plates, and reusable
  visual targets.
- `REDRAW`: use masks, redraw regions, or inpainting-style conditioning. Use
  when only part of an existing image or frame should change.

## Art Asset Output Format

When Art Room outputs are present, Director Room must preserve each asset's
`output_format` contract:

- neutral master cards, turnaround sheets, and detail crop sheets are identity,
  scale, material, and continuity references;
- transparent cutouts are masks, overlays, compositing inputs, or redraw
  controls;
- only `video_reference_frame` and `shot_override_frame` deliverables may be
  used as I2V/FLF2V scene frames;
- video reference frames and shot overrides must keep foreground, midground, and
  background, camera angle, screen direction, lighting, and action state visible
  in the shot prompt.

Do not describe a transparent cutout, neutral card, turnaround sheet, or detail
crop sheet as the shot's first frame, last frame, or full scene reference.

## Negative Prompt Strategy

Create negatives as modules:

- global image quality negatives;
- character identity negatives;
- anatomy and face artifact negatives;
- prop/location contradiction negatives;
- motion and temporal artifact negatives for video;
- method-specific negatives for masks, redraw, or first/last-frame drift.

Do not use a single generic negative prompt for every shot when method risks are
different. Provide both `negative_prompt_zh` and `negative_prompt_en`.

## Parameter Planning

Record production settings as a plan, not as hidden prose:

- `workflow_family`: a stable family name such as `t2v_text_only`,
  `i2v_reference`, `flf2v_transition`, `reference_image_still`, or
  `redraw_masked_region`.
- `node_binding_hints`: where positive prompt, negative prompt, image inputs,
  masks, LoRA stack, ControlNet inputs, IPAdapter references, and output path
  should be connected.
- `parameter_profile`: resolution, sampler, scheduler, steps, CFG, seed policy,
  denoise, frame count, FPS, motion bucket, reference weights, and batch notes.

If a model, LoRA, or workflow template is unknown, write a placeholder and mark
the shot or family as `needs_config`.

## JSON Context Passing

JSON artifacts are persistent handoff files, not an instruction to paste the
entire project into every model call.

- Send complete JSON only when it is small and directly needed.
- For long JSON, send the relevant scene or shot records, plus global metadata,
  schemas, and source refs.
- Return complete target artifacts from the parent coordinator after merging
  child outputs.
- Preserve `shot_id`, `generation_method`, `continuity_refs`, and `source_refs`
  exactly across slices.

## Feedback Tuning

When ComfyUI render feedback exists, diagnose by failure type:

- identity drift: strengthen character tokens, reference image binding, LoRA or
  IPAdapter weight, or reduce denoise;
- composition mismatch: reorder subject/action/camera terms, add framing
  constraints, or switch to I2V/FLF2V when reference control is required;
- motion failure: simplify action, split the shot, lower motion intensity, or
  add first/last-frame constraints;
- style mismatch: adjust style preset first before editing every shot;
- artifacts: adjust negative modules and then sampler/CFG/steps if needed;
- missing prop/location detail: strengthen asset references and continuity
  locks, then add local per-shot tokens.

Change the smallest effective surface and record every change in
`{episode-id}/prompts/comfyui-tuning-log.json`.
