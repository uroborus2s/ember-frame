# 本地 ComfyUI + Wan2.2 AI 视频影视制作教程

这是一个面向初学者的本地 ComfyUI + Wan2.2 AI 视频影视制作教程项目。课程以 Markdown 文档为主，目标是从安装、模型准备、首次生成逐步推进到一个可复现的 AI 视频项目。

## 阅读入口

零基础读者先走“第 0 实操入口”，遇到安装或模型问题再回到对应章节；有经验读者可以先看大纲和审校记录。

1. [第 0 实操入口：从零创建第一个 ComfyUI + Wan2.2 项目](01-foundation/chapter-00-zero-to-first-project.md)
2. [本地环境与 ComfyUI 基础](01-foundation/index.md)
3. [Wan2.2 核心视频生成](02-wan22-core/index.md)
4. [影视化镜头语言与素材准备](03-cinematic-language/index.md)
5. [高级工作流、优化与后期](04-advanced-workflows/index.md)
6. [完整项目实战与作品交付](05-production-projects/index.md)
7. [Short Drama Factory 工具设计包](06-short-drama-factory/index.md)
8. [课程大纲](course-outline.md)
9. [出版级审校记录](publication-review-log.md)
10. [商业出版准入门禁](publication-release-gate.md)

## 当前进度

状态口径：

- `出版修订中`：结构和正文已进入读者版审校，但仍需按出版标准复核。
- `待实测补图/待产出验证`：已有跟做草稿，必须补齐真实输出、截图、参数、耗时、显存和评分记录后才能标为成稿。

发行口径：在 [商业出版准入门禁](publication-release-gate.md) 的 P0 证据项完成前，本教程只能标为内测版、公开修订稿或待实测教材，不能标为商业发行版。

| 章节 | 状态 | 文件 |
| --- | --- | --- |
| 第 0 章：课程地图、学习成果与本地制作边界 | 出版修订中 | [chapter-00-course-map.md](00-course-guide/chapter-00-course-map.md) |
| 第 0 实操入口：从零创建第一个 ComfyUI + Wan2.2 项目 | 待实测补图/待产出验证 | [chapter-00-zero-to-first-project.md](01-foundation/chapter-00-zero-to-first-project.md) |
| 第 1 章：AI 视频生成基本原理 | 出版修订中 | [chapter-01-ai-video-principles.md](01-foundation/chapter-01-ai-video-principles.md) |
| 第 2 章：安装 ComfyUI 与启动本地服务 | 待实测补图/待产出验证 | [chapter-02-install-comfyui-local-service.md](01-foundation/chapter-02-install-comfyui-local-service.md) |
| 第 3 章：ComfyUI 界面与节点图基础 | 待实测补图/待产出验证 | [chapter-03-comfyui-interface-and-nodes.md](01-foundation/chapter-03-comfyui-interface-and-nodes.md) |
| 第 4 章：模型文件、显存与存储管理 | 待实测补图/待产出验证 | [chapter-04-model-files-vram-storage.md](01-foundation/chapter-04-model-files-vram-storage.md) |
| 第 5 章：第一次生成：从静态图到短视频测试 | 待实测补图/待产出验证 | [chapter-05-first-generation-image-to-short-video.md](01-foundation/chapter-05-first-generation-image-to-short-video.md) |
| 第 6 章：Wan2.2 模型家族与任务选择 | 待实测补图/待产出验证 | [chapter-06-wan22-model-family-task-selection.md](02-wan22-core/chapter-06-wan22-model-family-task-selection.md) |
| 第 7 章：T2V 文本生成视频基础 | 待实测补图/待产出验证 | [chapter-07-t2v-text-to-video-basics.md](02-wan22-core/chapter-07-t2v-text-to-video-basics.md) |
| 第 8 章：提示词工程：从描述到可控镜头 | 待实测补图/待产出验证 | [chapter-08-prompt-engineering-controllable-shot.md](02-wan22-core/chapter-08-prompt-engineering-controllable-shot.md) |
| 第 9 章：采样参数、种子、步数与分辨率 | 待实测补图/待产出验证 | [chapter-09-sampling-seed-steps-resolution.md](02-wan22-core/chapter-09-sampling-seed-steps-resolution.md) |
| 第 10 章：I2V 图生视频：让一张图动起来 | 待实测补图/待产出验证 | [chapter-10-i2v-make-image-move.md](02-wan22-core/chapter-10-i2v-make-image-move.md) |
| 第 11 章：TI2V 混合输入：文本与图像共同控制 | 待实测补图/待产出验证 | [chapter-11-ti2v-text-image-control.md](02-wan22-core/chapter-11-ti2v-text-image-control.md) |
| 第 12 章：FLF2V 首尾帧视频：控制开始与结束 | 待实测补图/待产出验证 | [chapter-12-flf2v-first-last-frame.md](02-wan22-core/chapter-12-flf2v-first-last-frame.md) |
| 第 13 章：质量评估与批量对比 | 待实测补图/待产出验证 | [chapter-13-quality-evaluation-batch-comparison.md](02-wan22-core/chapter-13-quality-evaluation-batch-comparison.md) |
| 第 14 章：镜头语言基础：景别、机位与运动 | 待实测补图/待产出验证 | [chapter-14-shot-language-scale-angle-motion.md](03-cinematic-language/chapter-14-shot-language-scale-angle-motion.md) |
| 第 15 章：构图、光线与色彩 | 待实测补图/待产出验证 | [chapter-15-composition-light-color.md](03-cinematic-language/chapter-15-composition-light-color.md) |
| 第 16 章：动作设计与运动可控性 | 待实测补图/待产出验证 | [chapter-16-action-design-motion-control.md](03-cinematic-language/chapter-16-action-design-motion-control.md) |
| 第 17 章：角色一致性与主体保持 | 待实测补图/待产出验证 | [chapter-17-character-consistency-subject-hold.md](03-cinematic-language/chapter-17-character-consistency-subject-hold.md) |
| 第 18 章：分镜脚本与镜头清单 | 待实测补图/待产出验证 | [chapter-18-storyboard-shot-list.md](03-cinematic-language/chapter-18-storyboard-shot-list.md) |
| 第 19 章：参考图与素材准备 | 待实测补图/待产出验证 | [chapter-19-reference-image-asset-preparation.md](03-cinematic-language/chapter-19-reference-image-asset-preparation.md) |
| 第 20 章：读懂并修改 ComfyUI 工作流 | 待实测补图/待产出验证 | [chapter-20-read-modify-comfyui-workflow.md](04-advanced-workflows/chapter-20-read-modify-comfyui-workflow.md) |
| 第 21 章：低显存与速度优化 | 待实测补图/待产出验证 | [chapter-21-low-vram-speed-optimization.md](04-advanced-workflows/chapter-21-low-vram-speed-optimization.md) |
| 第 22 章：风格控制、LoRA 与扩展节点 | 待实测补图/待产出验证 | [chapter-22-style-control-lora-extensions.md](04-advanced-workflows/chapter-22-style-control-lora-extensions.md) |
| 第 23 章：视频后期：剪辑、补帧、放大、调色与声音 | 待实测补图/待产出验证 | [chapter-23-post-production-edit-upscale-audio.md](04-advanced-workflows/chapter-23-post-production-edit-upscale-audio.md) |
| 第 24 章：错误排查与可复现项目管理 | 待实测补图/待产出验证 | [chapter-24-troubleshooting-reproducible-project.md](04-advanced-workflows/chapter-24-troubleshooting-reproducible-project.md) |
| 第 25 章：手工队列批量实验与结果筛选 | 待实测补图/待产出验证 | [chapter-25-batch-experiments-result-selection.md](04-advanced-workflows/chapter-25-batch-experiments-result-selection.md) |
| 第 26 章：项目一：15 秒产品广告短片 | 待实测补图/待产出验证 | [chapter-26-project-product-ad-15s.md](05-production-projects/chapter-26-project-product-ad-15s.md) |
| 第 27 章：项目二：30 秒叙事氛围短片 | 待实测补图/待产出验证 | [chapter-27-project-narrative-atmosphere-30s.md](05-production-projects/chapter-27-project-narrative-atmosphere-30s.md) |
| 第 28 章：项目三：音乐/预告片风格混剪 | 待实测补图/待产出验证 | [chapter-28-project-music-trailer-montage.md](05-production-projects/chapter-28-project-music-trailer-montage.md) |
| 第 29 章：毕业作品：个人 AI 视频制作流程包 | 待实测补图/待产出验证 | [chapter-29-capstone-ai-video-production-package.md](05-production-projects/chapter-29-capstone-ai-video-production-package.md) |
| Short Drama Factory 工具设计包 | 方案草案 | [index.md](06-short-drama-factory/index.md) |
