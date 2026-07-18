# 提示词部当前入口

owner: prompt-room
status: G-P_P01-P05_video_shoot_prompt_package_ready_for_video_preflight
last_updated: 2026-06-21

## 1. 当前任务

第 01 集 G-P/P-01 至 P-05 已由总导演签署。提示词部已根据对应分镜文档的导演签署区、美术资产区、角色卡和导演回看记录完成视频拍摄提示词包补齐；正式提示词结论已写回对应分镜文档 `## 3. 图片提示词区` 的 `### 3.6 视频拍摄提示词包（直接交视频生成部）`，可供视频生成部做 preflight。

## 2. 总导演提示词命令

| 分镜 | 提示词任务 | 禁止偏移 |
|---|---|---|
| P-01 | 图片提示词先锁黑石墙、骨钟、巨兽冲击来源、少年军户流血手、紧闭粮门；视频提示词锁短促冲击和手部/粮门切换 | 不写英雄热血，不让巨兽夺走主体 |
| P-02 | 图片提示词锁灶屋、木牌、白册、虫蜡手印板、麦粒泥水；视频提示词锁 C017 按孩子手、C016 登记/下令、C025 母亲护子失败、踹灶、麦粒滚泥、虫蜡剥离 | 不拍成普通抢劫；绝不能把按手执行者生成成 C016、C025 或未登记成人平民 |
| P-03 | 图片提示词锁白墙、儿童队列、虫蜡针、木牌、母亲贴墙；视频提示词锁静止构图和虫蜡颜色变化 | 不血腥猎奇，不怪物化识别童 |
| P-04 | 图片提示词锁红线密室、黑匣、血牒残纹、旧驿残图、白翳；视频提示词锁晏南枝动、白翳静 | 不用旁白百科解释身份 |
| P-05 | 图片提示词锁残阳坳北坡、沈维桑、灰兔、村口、封路矛尖；视频提示词锁白册合页转鸡叫、铜锣截断 | 不拍成普通山村风景空镜 |

所有提示词必须 tool-neutral，不写具体模型、插件、控制模块、采样或节点参数。精确文字、木牌字、印章和字幕走后期合成或控制资产，不交给模型自由生成。

## 3. 输入入口

- `director-room/season-01/01/G-P/group-main.md`
- `director-room/season-01/01/G-P/P-01/P-01.md`
- `director-room/season-01/01/G-P/P-02/P-02.md`
- `director-room/season-01/01/G-P/P-03/P-03.md`
- `director-room/season-01/01/G-P/P-04/P-04.md`
- `director-room/season-01/01/G-P/P-05/P-05.md`

## 4. 硬规则

- 不改剧情、不改人物身份、不重设空间关系。
- 不写具体模型、插件、控制模块、采样或节点参数。
- 过程提示词、失败尝试和候选版本进入 `prompt-room/.work/`；正式结论写回对应分镜共享文档。

## 5. G-P/P-01 至 P-05 回填状态

status: video_shoot_prompt_package_ready_for_video_preflight
last_updated: 2026-06-21

已完成 P-01 至 P-05 的 `## 3. 图片提示词区` 视频拍摄提示词包回填。每个分镜均新增 `production_metadata`、`model_visible_prompt`、`copy_ready`、`negative_prompt`、`character_lock`、`camera_lock`、`space_lock`、`asset_conditioning`、`control_refs`、`handoff_to_video` 和 `prompt_qc`，并明确 first_frame 使用 `director-room/season-01/01/G-P/P-xx/P-xx.png`。

P-02 当前硬锁：C017 混血奴兵是按住孩子小手进入湿白虫蜡的执行者；C016 粮税虫吏只在白册 / 征粮册旁开册、划名、下令、登记；C025 母亲是护子失败的受害保护者。视频生成部 preflight 必须先核验该职责链，再进入 I2V / FLF2V 技术执行。本轮未发现需要退回美术部的 `needs_art_fix` 项。
