---
name: director-room
description: Codex-native director room, storyboard, prompt engineering, render QC, edit planning, AI voice/audio, and post-production planning department for reading a fixed ./project/{project-name}/{episode-id} script package and turning it into a pre-asset shot package, post-asset video production package, bilingual ComfyUI-ready prompt pack, render manifest, QC reports, edit plan, dialogue/audio plan, and delivery QC handoff. Use when Codex needs a 导演分镜部, Director Room, Shot Planning Department, storyboard plan, 分镜说明, 中英文提示词, ComfyUI-ready prompts, shot-level image or video prompt packs, AI 配音, 剪辑, 后期, or direct script-to-video-production planning from a project root containing per-episode final scripts and project-level character/scene bibles.
---

# Director Room

Use this skill when the user provides or points to `./project/{project-name}/` and
an episode ID such as `01`. The parent Codex instance acts as the unified
director-and-prompt coordinator, verifies the fixed project and episode input
contract, and delegates each planning role to a bounded Codex sub-agent task
card.

## Department Boundary

Story-scene design is not director-room shot planning. Upstream scene design
defines locations, dramatic purpose, visible action, and filmability. This skill
normalizes that material and converts the finished script package directly into
production units: scenes, shots, bilingual storyboard panels, continuity locks,
generation methods, bilingual prompt drafts, and ComfyUI-ready bilingual prompt
artifacts.

This skill also owns the former prompt-engineering pass. Do not run or require a separate prompt-room skill for the same episode.
Prompt outputs are generated from the final script package plus this skill's own
director, camera, storyboard, continuity, and generation outputs. Art-room
assets may be used when they already exist, but they are optional and must not
be required for the first script-to-prompt pass.

Default pipeline:

```text
creative brief
  -> final script package
  -> director-room pre-asset shot package
  -> art-room assets
  -> director-room post-asset video production package
  -> comfyui-production
  -> director-room render QC / edit / AI voice / post-production
```

## Operating Model

- Treat Codex as the runtime. Do not implement a Python agent loop and do not
  call a project LLM provider for the department agents.
- The parent coordinator uses `multi_agent_v1.spawn_agent` when available.
  Spawn child agents only because the user explicitly requested a Codex-native
  department or multi-agent shot planning workflow.
- A child agent executing one role card must not require `spawn_agent`; it
  should perform its assigned role and return the artifact envelope.
- Keep the parent in charge of input checks, orchestration, artifact assembly,
  validation, quality gates, and user-facing questions.
- Keep child agents focused on one role and one handoff. Pass only the required
  artifact text and that role's task card.
- Have child agents return structured artifact content. The parent writes the
  actual files into the project folder unless the user explicitly requests
  direct worker edits.
- If the parent coordinator has no sub-agent tool, state that the exact "each
  agent is Codex" requirement is blocked and ask whether to continue with
  parent-only simulation.

## Project Input

Read from a single project root:

```text
./project/{project-name}/
```

Before running department agents for `{episode-id}`, verify these canonical
files exist:

```text
bible/characters.md
bible/scenes.md
{episode-id}/script/final-script.md
{episode-id}/reports/continuity-report.md
{episode-id}/reports/script-score.md
```

If the user gives a project directory with equivalent legacy names, normalize
them into these fixed paths inside that same project directory before planning.
Do not create a detached director-room input folder, and do not treat loose
files as the default input. If a required source category is missing and cannot
be inferred safely from the project directory, ask one concise question. Do not
modify source artifacts after the fixed project input is established.

Optional project-level inputs:

```text
bible/continuity.md
bible/visual-style.md
production/series-video-rules.md
assets/asset-index.json
```

If `production/series-video-rules.md` is missing during a series setup pass,
create it before episode planning. The file fixes aspect ratio, frame rate,
shot style, motion limits, quality floor, prohibited visual/audio choices,
render feedback format, and AI audio/post-production rules.

## Outputs

Required department handoff outputs:

```text
{episode-id}/director/director-brief.md
{episode-id}/director/camera-plan.md
{episode-id}/shots/scene-breakdown.json
{episode-id}/shots/shot-list.json
{episode-id}/storyboard/storyboard-plan.md
{episode-id}/continuity/visual-continuity-bible.json
{episode-id}/production/generation-plan.json
{episode-id}/production/video-production-plan.md
{episode-id}/prompts/shot-prompts-draft.json
```

Required post-asset video production outputs:

```text
{episode-id}/prompts/comfyui-prompt-brief.md
{episode-id}/prompts/comfyui-style-preset.json
{episode-id}/prompts/comfyui-asset-prompt-pack.json
{episode-id}/prompts/comfyui-shot-prompts.json
{episode-id}/prompts/comfyui-workflow-plan.json
{episode-id}/prompts/comfyui-render-prompts.md
{episode-id}/prompts/comfyui-tuning-log.json
{episode-id}/reports/comfyui-prompt-qc.md
```

Required render, edit, audio, and post outputs when those stages are requested
or downstream feedback is present:

```text
{episode-id}/production/render-manifest.json
{episode-id}/qc/shot-qc-report.json
{episode-id}/qc/episode-qc-report.md
{episode-id}/edit/edit-plan.md
{episode-id}/edit/edit-decision-list.json
{episode-id}/audio/voice-bible.md
{episode-id}/audio/dialogue-plan.json
{episode-id}/audio/audio-manifest.json
{episode-id}/audio/audio-qc.md
{episode-id}/audio/dialogue/
{episode-id}/audio/sfx/
{episode-id}/audio/music/
{episode-id}/post/post-production-plan.md
{episode-id}/post/subtitle-script.md
{episode-id}/post/sound-plan.md
{episode-id}/post/color-plan.md
{episode-id}/post/delivery-qc-report.md
```

Supporting coordinator outputs:

```text
{episode-id}/logs/director-room-agent-calls.jsonl
```

## References

Load only what is needed:

- `references/artifact-contract.md`: child-agent envelope and artifact rules.
- `references/department-workflow.md`: spawn pattern, parallelism, and recovery.
- `references/comfyui-prompting-guide.md`: bilingual prompt structure, method
  mapping, JSON context passing, parameter planning, and feedback tuning rules.
- `agents/*.md`: one task card per child agent. Do not treat
  `agents/openai.yaml` as a role card.
- `schemas/*.json`: structural contracts for JSON outputs and tests.

## Workflow

1. Verify the project root and the five canonical project input files. If needed,
   normalize equivalent files inside the same project directory.
   Create `production/series-video-rules.md` for series setup when missing and
   requested.
2. Run `director-agent` to produce
   `{episode-id}/director/director-brief.md`.
3. Run `scene-breakdown-agent` and `visual-continuity-agent`. They may run in
   parallel after the director brief exists.
4. Run `shot-planner-agent` after
   `{episode-id}/shots/scene-breakdown.json`.
5. Run `cinematographer-agent` after `{episode-id}/shots/shot-list.json`.
6. Run `storyboard-agent` after `{episode-id}/director/camera-plan.md` and
   `{episode-id}/continuity/visual-continuity-bible.json`.
7. Run `generation-strategy-agent` after the shot list, camera plan,
   storyboard plan, and visual continuity bible exist.
8. Run `shot-prompt-agent` after
   `{episode-id}/production/generation-plan.json`.
9. Create or update `{episode-id}/production/video-production-plan.md` as the
   pre-asset plan, with unresolved assets marked explicitly.
10. After Art Room assets exist, read `assets/asset-index.json`,
    `{episode-id}/art/asset-index.json`, `{episode-id}/art/asset-qc-report.md`,
    `{episode-id}/prompts/art-image-prompts.json`, and canonical image paths,
    including each asset's `output_format`, then run `prompt-director-agent` to produce
   `{episode-id}/prompts/comfyui-prompt-brief.md`.
11. Run `style-preset-agent` and `asset-conditioning-agent`. They may run in
    parallel after the prompt brief exists.
12. Run `shot-prompt-engineer-agent` after the prompt brief, style preset, asset
    prompt pack, shot prompt drafts, shot list, camera plan, storyboard plan,
    visual continuity bible, and generation plan exist.
13. Run `workflow-parameter-agent` after
    `{episode-id}/prompts/comfyui-shot-prompts.json`.
14. Assemble `{episode-id}/prompts/comfyui-render-prompts.md` from the style
    preset and shot prompt records. This Markdown file is the operator-facing
    copy surface and must include complete `positive_prompt_zh`,
    `negative_prompt_zh`, `positive_prompt_en`, and `negative_prompt_en` blocks
    for every shot. Headings or sections may be used when a project wants a
    clearer handoff, but do not hardcode project-specific visual rules, labels,
    or style text into the skill. Do not require ComfyUI operators to manually
    concatenate JSON fields.
15. Refresh `{episode-id}/production/video-production-plan.md` as the post-asset
    video production plan with concrete asset refs, render order, risks, and
    unresolved config placeholders.
16. Run `prompt-qc-agent` to produce
    `{episode-id}/reports/comfyui-prompt-qc.md`.
17. If ComfyUI render feedback is present, run `comfyui-feedback-agent`.
    Otherwise still write `{episode-id}/prompts/comfyui-tuning-log.json` with
    `status="no_feedback"`.
18. When render outputs exist, register them in
    `{episode-id}/production/render-manifest.json` and classify shots in
    `{episode-id}/qc/shot-qc-report.json`.
19. When accepted shots exist, run `edit-planner-agent` to produce
    `{episode-id}/edit/edit-plan.md` and
    `{episode-id}/edit/edit-decision-list.json`.
20. Run `audio-planner-agent` for AI voice, subtitles, sound, and music planning.
    Manage dialogue by dialogue lines, voiceover lines, SFX cues, and music
    cues, not by one audio file per shot.
21. Run `delivery-qc-agent` to produce post-production plans, episode QC, audio
    QC, and delivery QC artifacts.
22. Validate JSON outputs against the local schemas when practical. Repair only
   formatting mistakes; do not invent story facts during repair.
23. Return the output paths, warnings, unresolved config or asset dependencies,
    and the recommended handoff to ComfyUI production.

## Agent Sequence

Use these task cards:

```text
agents/director-agent.md
agents/scene-breakdown-agent.md
agents/shot-planner-agent.md
agents/cinematographer-agent.md
agents/storyboard-agent.md
agents/visual-continuity-agent.md
agents/generation-strategy-agent.md
agents/shot-prompt-agent.md
agents/prompt-director-agent.md
agents/style-preset-agent.md
agents/asset-conditioning-agent.md
agents/shot-prompt-engineer-agent.md
agents/workflow-parameter-agent.md
agents/prompt-qc-agent.md
agents/comfyui-feedback-agent.md
agents/edit-planner-agent.md
agents/audio-planner-agent.md
agents/delivery-qc-agent.md
```

## Quality Rules

- Preserve the script's story, character intent, and continuity. Do not rewrite
  plot, add new beats, or solve script problems by changing the script.
- Keep shot IDs stable and machine-friendly. Use `SC###-SH###` unless the
  project already has a stronger convention.
- Make every shot filmable: visible action, clear subject, camera plan, lighting
  intent, audio note, continuity anchors, and generation method.
- Separate the pre-asset shot package from the post-asset video production
  package. `shot-prompts-draft` is an intermediate artifact for Art Room asset
  planning; final prompt engineering happens after asset QC and produces
  `comfyui-*` prompt artifacts.
- Choose generation methods explicitly: `T2V`, `I2V`, `FLF2V`,
  `REFERENCE_IMAGE`, or `REDRAW`. Include rationale and required assets.
- Keep production metadata separate from model-visible prompt text.
  `shot_id`, `generation_method`, `asset_id`, `episode_id`, `output_file`, and
  workflow identifiers belong in metadata, not in the visible prompt body.
- Post-asset ComfyUI delivery must provide both structured prompt records and
  copy-ready operator prompts. `comfyui-shot-prompts.json` is the structured
  source of truth; `comfyui-render-prompts.md` is the assembled Markdown handoff
  with complete positive and negative prompt blocks ready for ComfyUI nodes.
- Preserve visual continuity over isolated shot beauty. Character appearance,
  wardrobe, props, geography, screen direction, and scene lighting must remain
  coherent across adjacent shots.
- Respect Art Room `output_format` when using assets for video generation.
  Neutral master cards and turnaround/detail sheets are identity references;
  transparent cutouts are for masks, overlays, or compositing; video reference
  frames and shot overrides are the only asset formats that may serve as
  first/last/reference frames. Do not pass a transparent cutout or isolated card
  sheet as an I2V/FLF2V scene frame, and reject video reference frames that do
  not clearly separate foreground, midground, and background.
- Flag impossible, expensive, or ambiguous shots instead of hiding risk.
- QC statuses must be machine-readable: `accepted`, `needs_redraw`,
  `needs_regenerate`, `needs_prompt_tuning`, `needs_asset_fix`,
  `needs_script_fix`, `needs_audio_fix`, or `blocked`.
- Storyboard and prompt outputs must be bilingual. Human-readable storyboard
  sections must include Chinese and English labels/content. JSON prompt records
  must include Chinese and English prompt fields, not only translated comments.
- Do not invent checkpoint IDs, LoRA IDs, ControlNet model names, IPAdapter
  presets, or node template IDs. Use user-provided or project-provided IDs; when
  missing, write explicit placeholders and mark the shot as `needs_config`.
- When passing JSON artifacts to child agents or model calls, pass complete
  small JSON files. For large files, pass the global summary plus the relevant
  scene/shot records and preserve `source_refs`; do not assume every child needs
  the entire project JSON blob.
- JSON context rule: pass complete small JSON files, slice large JSON by scene
  or shot family, and keep source refs.
- Do not recommend direct video-model generation of precise dialogue. Video
  prompts may describe a speaking state, weak lip movement, breath, and acting
  intent, but exact text comes from `script/final-script.md`,
  `post/subtitle-script.md`, and `audio/dialogue-plan.json`.
- Audio uses short final filenames such as `audio/dialogue/d001.wav`,
  `audio/sfx/sfx001.wav`, and `audio/music/mx001.wav`; discarded takes belong
  in takes/history records and must be indexed in `audio/audio-manifest.json`.

## Final Response

After the run, report:

- director-room project root
- artifacts created
- blocked or warning items
- bilingual prompt artifacts created
- copy-ready ComfyUI render prompt Markdown created
- prompts or shots that need model/config/asset decisions
- validation performed
- ComfyUI production handoff recommendation
