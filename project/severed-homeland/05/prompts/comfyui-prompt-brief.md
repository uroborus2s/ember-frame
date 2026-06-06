# 第05集：灰烬书院的孩子 ComfyUI Prompt Brief

## Scope

中文：本提示简报基于导演分镜包生成，不假设已有 art-room 资产或具体 ComfyUI 节点。缺失模型、LoRA、参考图和工作流模板全部以占位标记保留。
English: This prompt brief is generated from the director-room storyboard package. It does not assume art-room assets or concrete ComfyUI nodes; missing models, LoRAs, references and workflow templates remain explicit placeholders.

## Global Prompt Rules

- Positive / 正向：超写实、电影级质感、低魔东方史诗、16:9横屏宽屏剧；真实重心、真实速度、自然呼吸、接触反作用和可读运动路径。
- Positive EN: hyper-realistic cinematic low-magic Eastern epic, 16:9 landscape widescreen drama; real body weight, real speed, natural breathing, contact reaction and readable movement paths.
- Negative / 负向：避免塑料CG、过度磨皮、现代服饰、漂浮慢动作、僵硬摆拍、错误族群外观、血腥奇观化、对白文字出现在画面中。
- Negative EN: avoid plastic CGI, over-smoothed skin, modern clothing, floaty slow motion, stiff posing, wrong faction anatomy, gore spectacle, and visible dialogue text in the image.

## Method Mix
- `T2V`: 3
- `I2V`: 31
- `FLF2V`: 2
- `REFERENCE_IMAGE`: 8

## Placeholders / 占位
- `PLACEHOLDER_CHECKPOINT`: 未指定基础模型。
- `PLACEHOLDER_LORA_STACK`: 未指定 LoRA。
- `PLACEHOLDER_WORKFLOW_TEMPLATE`: 未指定工作流模板。
- `assets/placeholders/*.png`: 等待 Art Room 或参考帧生产。
