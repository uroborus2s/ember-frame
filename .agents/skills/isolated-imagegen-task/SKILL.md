---
name: isolated-imagegen-task
description: Run isolated image generation or image editing through a clean prompt-and-reference workflow. Use when Codex needs a generic image generation task that must not read project files, inherit long project context, inspect background documents, write files, or do non-image work; especially after imagegen ServerError, context-too-long failures, repeated image retries, many reference images, or semantic drift from long prompts and stale image history.
---

# Isolated Imagegen Task

## Core Rule

Treat image generation as a clean-room worker task.

The parent task prepares all context. The image task receives only:

- A single image prompt.
- Optional attached reference images that are already selected and compressed.

The image task must return only generated image output. It must not read files, write files, inspect the project, summarize background, run shell commands, search, commit, or perform QC prose.

## Failure This Prevents

Long, image-heavy threads can carry stale large images, old failed prompts, negative prompt debris, and unrelated project history into the image generation call. This can cause `ServerError` or semantic drift even when later references are compressed. A fresh task with only compressed references and a short prompt is the stable path.

## Parent Task Protocol

Use this protocol before opening or continuing an image task.

1. Build a clean input package outside the image task.
2. Select only references needed for the next image.
3. Compress references before sending:
   - Prefer no more than 8 attached images.
   - Long edge at or below 1600 px.
   - Each image at or below 2 MB.
   - Total attached image payload at or below 12 MB.
   - If over budget, crop detail panels or merge references into a contact sheet before sending.
4. Prepare one prompt for one target image:
   - Target length: at or below 1800 Chinese characters or 900 English words.
   - Hard limit: 3000 Chinese characters or 1500 English words.
   - If over the hard limit, compress the prompt before sending.
   - Keep negative constraints short; prefer positive visual locks.
   - Do not include local file paths in the image prompt.
5. Create a fresh child task for the first generation attempt.
6. Record the child task/thread id in the parent task.
7. Retrieve the generated image in the parent task.
8. Do QC in the parent task only.
9. If revision is needed, send the image task only a revised prompt plus the minimal current/reference images.
10. Start a new clean image task instead of continuing when:
    - `imagegen` returns `ServerError`.
    - The child task has already loaded original large images or long background text.
    - More than two revision attempts have accumulated.
    - The target image or reference set changes materially.
    - The child task starts reading files, writing files, or discussing project context.

The parent task owns file lookup, path resolution, image compression, saving/copying final files, audit notes, and user-facing explanation.

## Child Task Rules

When acting as the image task:

- Use only the prompt and attached images in the current task.
- Treat markdown image paths as attachments only; do not open, copy, inspect, or mention the paths.
- Do not use shell, filesystem, search, project files, git, or background documents.
- Do not ask to inspect missing project context.
- Generate exactly the requested image count, preferably one image per task.
- Return only the image artifact. If text is unavoidable, return one compact line containing the generated image id or path and no analysis.
- If the prompt is missing, reply only: `缺少图片提示词，无法生图。`

## Child Task Prompt Template

Use this shape when the parent creates a clean image task:

```text
任务：只根据本消息中的图片提示词和随附参考图生成 1 张图片。

硬限制：
- 不读取文件，不写文件，不搜索，不查看项目背景，不提交 git。
- 参考图只作为视觉附件使用；不要把附件路径写入图片提示词。
- 只调用生图工具并返回图片本身；不要输出构图分析、QC、背景说明或其他行文。

参考图附件：
![reference label](attached-image)

图片提示词：
<prompt without local paths>
```

For a revision:

```text
任务：基于本消息中的修订提示词和随附参考图/上一版图，重新生成 1 张图片。

硬限制同前：不读取文件，不写文件，不搜索，不查看项目背景；只返回图片。

修订提示词：
<revised prompt without local paths>
```

## Anti-Patterns

- Do not ask the image task to "read the project", "load the original large image", "open previous docs", or "save to this path".
- Do not send episode bibles, shot plans, long diagnostics, Git diffs, or unrelated history into the image task.
- Do not generate multiple target images in one child task unless the user explicitly accepts the added risk.
- Do not keep retrying in a child task after a context-related failure.
- Do not put file paths, task ids, or asset registry text into the actual image prompt.
