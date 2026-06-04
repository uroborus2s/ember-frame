# 第09集：鸣骨岭有笛声 ComfyUI Prompt QC

- Status: `warning`
- Shots checked: 40
- Missing planned assets: 15

## Checks
- bilingual storyboard sections: pass
- JSON prompt records include `_zh` and `_en` surfaces: pass
- production metadata separated from model-visible prompt: pass
- no invented checkpoint, LoRA, ControlNet, IPAdapter, workflow template or node IDs: pass with placeholders
- exact dialogue is not placed into video model prompts: pass

## Warnings
- Art Room reference assets are not present for this pass; `comfyui-asset-prompt-pack.json` marks them as `missing`.
- All ComfyUI workflow bindings remain `needs_config` until model and node templates are supplied.
- Shots with `FLF2V` or `I2V` need approved first/last/reference frames before render.
