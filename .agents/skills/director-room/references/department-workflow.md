# Director Room Workflow

The parent Codex instance is the only coordinator. Child agents should not spawn
more agents, ask the user, or change shared files unless explicitly assigned a
disjoint write set.

If you are a child agent executing a single role card, do not inspect or require
the sub-agent tool. Complete your role and return the artifact envelope. Missing
`spawn_agent` is only a parent-coordinator blocker.

## Default Spawn Pattern

Use a worker sub-agent with a narrow prompt:

```text
You are the <role> in a Codex-native director and prompt room.
Read this task card:
<contents of skills/director-room/agents/<role>.md>

Project contract:
<brief artifact contract summary>

Inputs:
<only the artifacts this role needs>

Return only the structured envelope and complete artifact contents.
Do not edit files directly.
```

Do not set a model override unless the user explicitly requests one. Use the
inherited Codex model.

## Parallelism

Only parallelize independent roles:

- After `{episode-id}/director/director-brief.md`, run `scene-breakdown-agent` and
  `visual-continuity-agent` in parallel.
- Keep `shot-planner-agent` blocked until
  `{episode-id}/shots/scene-breakdown.json` exists.
- Keep `cinematographer-agent` blocked until
  `{episode-id}/shots/shot-list.json` exists.
- Keep `storyboard-agent` blocked until the shot list, camera plan, and visual
  continuity bible exist.
- Keep `generation-strategy-agent` and `shot-prompt-agent` sequential because
  prompt drafts depend on generation-method decisions.
- After `{episode-id}/prompts/comfyui-prompt-brief.md`, run
  `style-preset-agent` and `asset-conditioning-agent` in parallel.
- Keep `shot-prompt-engineer-agent` blocked until the style preset, asset prompt
  pack, shot prompt drafts, camera plan, storyboard plan, visual continuity
  bible, and generation plan exist.
- Keep `workflow-parameter-agent`, `prompt-qc-agent`, and
  `comfyui-feedback-agent` sequential because each depends on the prior prompt
  artifact.
- Keep `edit-planner-agent` blocked until accepted render status exists in
  `{episode-id}/qc/shot-qc-report.json`.
- Keep `audio-planner-agent` blocked until the edit plan or script dialogue map
  exists; audio is planned by dialogue lines, voiceover lines, SFX cues, and
  music cues rather than by one audio file per shot.
- Keep `delivery-qc-agent` blocked until edit and audio manifests exist, or mark
  missing post inputs as `blocked`.

## JSON Context Passing

JSON files are not automatically sent whole to every model call. The parent
coordinator decides the context package for each child role.

- Pass complete small JSON artifacts when they are short enough to fit cleanly.
- For long shot lists, generation plans, or prompt packs, pass the global
  metadata plus only the relevant scene/shot records for that child task.
- Always preserve stable IDs and `source_refs` so a sliced context can be traced
  back to the full project artifact.
- If the user explicitly asks for a whole-artifact review, pass the complete
  JSON when practical; otherwise split by scene or shot family and merge the
  returned artifacts deterministically.
- Never hide omitted context. Tell the child agent what was summarized or
  sliced.

## Parent Responsibilities

The parent Codex coordinator must:

- verify the project root and the five canonical project input files;
- keep pre-asset director outputs separate from post-asset video production
  outputs;
- write project files from returned artifacts;
- append one JSONL record per child agent to
  `{episode-id}/logs/director-room-agent-calls.jsonl`;
- preserve warnings instead of hiding them;
- keep shot IDs stable when repairing JSON formatting;
- validate JSON outputs against local schemas when practical;
- enforce bilingual storyboard and prompt fields;
- enforce separation between `production_metadata` and `model_visible_prompt`;
- prevent video prompts from asking the model to generate exact dialogue;
- summarize the final result for the user.

## Recovery

If a child agent returns `blocked`, the parent should decide whether the missing
input can be inferred safely. If not, ask the user one concise question.

If a child agent returns malformed JSON or missing artifact content, ask that
same agent to resend the envelope once. If it fails again, the parent may repair
formatting only when the creative content is unambiguous; otherwise mark the run
`warning` and continue only if downstream agents can still work.
