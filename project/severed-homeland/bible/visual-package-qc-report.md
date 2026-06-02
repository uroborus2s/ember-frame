# 项目级视觉统一包 QC 报告

检查对象：

- `bible/visual-style.md`
- `bible/style-continuity-bible.json`
- `bible/asset-registry.json`
- `bible/character-visual-locks.json`
- `bible/location-visual-locks.json`
- `bible/prop-visual-locks.json`
- `prompts/project-visual-prompts.json`
- `assets/characters/.gitkeep`
- `assets/locations/.gitkeep`
- `assets/props/.gitkeep`
- `assets/costumes/.gitkeep`
- `assets/style/.gitkeep`

## 结论

状态：pass。

项目级视觉统一包已经可以作为后续角色设定图、场景概念图、道具板、分镜参考帧和 Prompt Room 的统一输入。

## 已锁定内容

1. 全剧视觉方向：低魔东方史诗奇幻，写实电影质感，克制法术表现。
2. 全剧画幅：9:16 竖屏，优先中近景、近景、道具特写和窄空间追逐。
3. 派系视觉：昭明旧物、肃明清明院、边墙灰墙军、墙下混裔、北境寻灾源派。
4. 角色视觉锁：沈维桑、晏南枝、白翳、沈照眠、陆青砾、薛临墙，以及罗青禾、孟归藏、鹿弥、厉螳、顾怀章。
5. 场景视觉锁：残阳坳、旧驿暗道、金河粮磨、灰烬书院、清明院外署、墙下集市、锁喉关、鸣骨岭、寒鸦堡、月下盟书旧驿、坍塌烽燧。
6. 道具视觉锁：半枚日月驿令、月白玉片、日月血牒残段、清明白册、虫蜡针、清明香、驿道图、盟书残页、骨哨/骨笛、粮牌、黑市木牌。
7. 资产 ID：所有首批角色、地点、道具和风格板都有稳定 ID，可供后续引用。
8. 项目级图片提示词：已生成工具中立 prompt，不含 ComfyUI 节点、采样器或模型参数。

## 未完成内容

1. 未生成实际图片资产。
2. 未生成第01集专属参考帧。
3. 未生成 director-room 镜头表、storyboard 或 shot-list。
4. 未生成 ComfyUI-ready prompt。

## 风险与控制

### warning：子代理备选方案包含南林中段

当前主方案将南林/隐歌谷放到第二季接口。视觉统一包也按主方案控制第一季主视觉，不把南林巨树、精灵树城、东海龙船或瀛洲兽纹作为第一季主资产。

### warning：角色资产生成时容易过度华丽

沈维桑、晏南枝、白翳是最高风险角色。生成图片时必须遵守：

1. 沈维桑不穿英雄铠甲。
2. 晏南枝不穿完整公主/皇室礼服。
3. 白翳不变成全虫怪物。

### warning：边墙大场景容易超出 AI 生成控制

锁喉关、巨兽撞门和烽燧坍塌应优先使用局部画面、影子、雪、门震、骨钟和近景动作。

## 推荐下一步

推荐路线 A：先生成项目级参考图。

1. 生成全剧风格板。
2. 生成六个一级角色设定图：沈维桑、晏南枝、白翳、沈照眠、陆青砾、薛临墙。
3. 生成五个一级场景概念图：残阳坳、旧驿暗道、清明院外署、锁喉关、月下盟书旧驿。
4. 生成核心道具板。

推荐路线 B：先写第01集完整剧本。

1. 用 writer-room 扩写第01集 `script-v01.md` 和 `final-script.md`。
2. 用 director-room 生成镜头表。
3. 再由 art-room 生成第01集专属参考帧和 shot overrides。

当前建议：先走路线 A。因为项目级参考图能显著降低后续剧本、分镜和提示词阶段的视觉漂移。
