# 导演与 AIGC 学习源索引

本索引用于把外部导演、分镜、编剧和 AIGC 制作经验转化为导演部可执行规则。使用时只吸收判断结构、工作流和质量门槛，不复制课程、影评、论文或项目文本。

## 职业导演与摄影训练

### AFI Conservatory Directing

- 链接：`https://conservatory.afi.com/directing/`
- 可学习：导演必须对文本、表演、镜头、运动、剪辑、声音和观众体验做有理由的决定。
- 落地方式：导演学院要求每个镜头写清戏剧目的、观众感受和非任意技法理由。

### AFI Conservatory Cinematography Curriculum

- 链接：`https://conservatory.afi.com/cinematography-curriculum/`
- 可学习：摄影不是漂亮画面，而是叙事、光线、构图、运动和后期工作流的统一。
- 落地方式：摄影方案必须解释景别、焦段、光线和运动如何服务人物状态。

### Moving Pictures: Mise-en-Scene

- 链接：`https://movingpictures.pressbooks.com/chapter/6-2-mise-en-scene/`
- 可学习：场面调度包含布景、道具、服装、表演、光线、构图和空间关系。
- 落地方式：场景坐标和视觉连续性必须让人物、空间、道具和光线共同讲故事。

## 分镜与视觉叙事

### ACMI Storyboards

- 链接：`https://www.acmi.net.au/education/school-program-and-resources/storyboards/`
- 可学习：分镜要从脚本、镜头表、景别、角度、角色运动和镜头运动出发。
- 落地方式：分镜医生检查每个分镜是否有可见行动、主体焦点、入镜状态、出镜状态和删镜损失。

### Pixar in a Box: The Art of Storytelling

- 链接：`https://www.khanacademy.org/computing/pixar/storytelling`
- 可学习：故事要经过结构、角色、分镜、反馈和重做，不是一次生成。
- 落地方式：观众盲测 QC 把“反馈和重做”固化为五问盲测和返工循环。

### StudioBinder Storyboard and Shot List Guides

- 链接：`https://www.studiobinder.com/blog/how-to-make-storyboard/`
- 链接：`https://www.studiobinder.com/blog/shot-list-template/`
- 可学习：分镜和镜头表需要景别、角度、运动、动作、说明和剪辑意图。
- 落地方式：转场医生要求每个相邻分镜有入点、出点、切点和转场动机。

## 编剧与可拍性

### 当前 `screenwriting` skill

- 链接：`.agents/skills/screenwriting/SKILL.md`
- 可学习：每个分镜剧本必须写清观众必须看见、可见行动、声音意图、转场依据和禁止误读。
- 落地方式：导演部不得替编剧修故事，但必须把编剧交接中的可见行动和转场依据转化为镜头判断。

### 当前 `story-original` skill

- 链接：`.agents/skills/story-original/SKILL.md`
- 可学习：故事源头必须有世界观、人物欲望、情节因果和文学魅力。
- 落地方式：当导演阶段发现剧本无法拍、人物目标不清或分镜没有行动时，应退回上游，而不是硬用美图掩盖。

## AIGC 制作与多 Agent 项目

### ViMax

- 链接：`https://github.com/HKUDS/ViMax`
- 可学习：多 agent 视频生产需要先有角色、场景、分镜、参考图选择、首尾帧和镜头生成链路。
- 落地方式：导演部先给分镜目的、空间调度、首尾状态和参考需求；视频生成部再执行。

### MovieAgent

- 链接：`https://github.com/HITsz-TMG/MovieAgent`
- 可学习：自动电影生成应拆成编剧、导演、分镜、场景、摄影等角色，并把场景、相机、摄影提示逐级规划。
- 落地方式：导演学院吸收其分层规划思想，但当前项目仍以总导演签署为最高门槛。

### Toonflow

- 链接：`https://github.com/HBAI-Ltd/Toonflow-app` 和本地 `.tmp-research/Toonflow-app`
- 可学习：故事板、素材关联、工作台状态和资产绑定必须进入生成流程。
- 落地方式：导演部只声明参考需求和 QC，后续部门必须证明实际使用了角色、场景、首尾帧和控制证据。

### ComfyUI Examples

- 链接：`https://github.com/comfyanonymous/ComfyUI_examples`
- 可学习：可复现工作流应通过模板和图像内嵌元数据管理，而不是口头说“用了某流程”。
- 落地方式：导演部不写节点参数，但要要求下游回传可审计生产证据。

### LTX-Video

- 链接：`https://github.com/Lightricks/LTX-Video`
- 可学习：长镜头、控制条件、提示词质量和运动控制都影响最终可剪性。
- 落地方式：导演部把长运镜拆成首尾状态、运动段落、空间锚点和剪辑出口。

### Wan2.2

- 链接：`https://github.com/Wan-Video/Wan2.2`
- 可学习：强视频模型能提高画面和运动质量，但仍需要首尾帧、参考图、镜头目的和控制证据。
- 落地方式：导演部不因模型强就放弃分镜医生、转场医生和观众盲测。

### OpenMontage

- 链接：`https://github.com/calesthio/OpenMontage`
- 可学习：AIGC 生产系统可以把参考视频分析、任务规划、工具选择、自审和审计证据组织成流水线。
- 落地方式：可借鉴其流程审计思路，但必须先通过当前项目的导演签署和项目办公室契约。

## 采用规则

学习源进入项目时必须被改写成以下之一：

- 一个镜头判断问题；
- 一个分镜字段；
- 一个转场合同字段；
- 一个 AIGC 生产证据需求；
- 一个 QC 失败条件；
- 一个返工命令模板。

不能落到以上任一项的外部资料，不进入正式导演流程。
