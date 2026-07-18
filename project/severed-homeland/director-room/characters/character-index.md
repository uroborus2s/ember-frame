# 《断航故土》第一季角色总卡索引

status: source_canon_locked
owner: project-office
last_updated: 2026-06-21
source_canon_revision: personality_growth_pass_v002
source_bible: `story-original/bible/story-bible.md`
source_character_bible: `story-original/bible/source/characters.md`
official_location: `director-room/characters/`
screenwriting_section_status: ready_for_screenwriting
screenwriting_last_updated: 2026-06-20

## 使用规则

- 本目录为跨部门角色总卡正式归口，按 `project-management.md` 第 14 节执行。
- 原著部只维护每张卡的 `Section 1. 源头 Canon`。
- 编剧部、美术部、配音部、视频生成部只能在各自区块补写，不得覆盖已锁定的源头 Canon。
- 2026-06-20 编剧部已完成 C001-C026 的 `Section 2. 编剧影视化角色卡`；配音部与视频生成部区块仍由对应部门后续填写。
- 2026-06-20 编剧部已将原著 Bible 中的身高体重、体量轮廓、脸/头部特征、服装材质、固定道具和姿态动作同步进 C001-C026 的 `Section 2`，作为导演和美术继续细化前的影视首读锚点。
- 2026-06-21 美术部已按用户最新要求把 C001-C026 的 `Section 3. 美术视觉角色卡` 统一升级为透明 V2 角色生产板规格：五视角全身转面、六表情、色板 / 材质 / 道具格；当前同目录 `c###m.png` 均已复核为 3840x2160 RGBA alpha 透明 V2 正式角色母图。
- 2026-06-21 配音部已完成 C001/C002 的 `Section 4. 配音声音角色卡`、Qwen3-TTS 生成提示词和角色声音母样 preview；正式可见试听文件与角色卡同目录存放，下游优先读取角色卡 Section 4。
- 2026-06-21 配音部已完成 NAR001 纪录片旁白声音母卡、Qwen3-TTS 生成提示词和旁白母样 preview；NAR001 不是剧情人物，作为 voice role 归口在本目录，供旁白 cue 复用。
- 2026-06-21 按 G-P 角色卡闸门，已补齐 C007/C016/C017/C021/C024/C025 的 `Section 4. 配音声音角色卡` 文本锁；C007/C016/C017/C024/C025 已生成角色卡同目录 preview，C021 已生成角色卡同目录 48 kHz stereo 声效方向 preview，全部仍待人工听审和最终规格确认。
- 若下游认为源头 Canon 不足，必须在角色卡 `Section 6. 冲突与变更记录` 或项目办公室返工入口提出 `needs_story_source_fix`。

## 本轮补强说明

- 本轮根据第一季完整原著 v005，对 C001-C026 的 `Section 1. 源头 Canon` 完成性格与成长补强。
- 单人物卡统一补入 `性格底色`、`压力反应 / 说话质地`、`关系变化` 与 `人物弧光 / 完整成长轨迹`。
- 群像与模板卡按其叙事功能补入 `群体性格底色` 或 `关系底色`、压力行为和功能性成长，避免下游把制度层级、北境族群、人族群众画成同一类背景。

## 已建声音母样

| voice_subject_id | display_name | voice_id | preview_audio | status |
| --- | --- | --- | --- | --- |
| C001 | 沈维桑 | `C001-VOICELOCK-V001` | `c001-voice-v001-preview.wav` | preview_audio_visible_with_character_card |
| C002 | 晏南枝 | `C002-VOICELOCK-V001` | `c002-voice-v001-preview.wav` | preview_audio_visible_with_character_card |
| C007 | 白翳 | `C007-VOICELOCK-V001` | `c007-voice-v001-preview.wav` | preview_audio_generated_needs_human_listening_qc |
| C016 | 肃明基层虫吏层级模板 | `C016-VOICELOCK-V001` | `c016-voice-v001-preview.wav` | preview_audio_generated_needs_human_listening_qc |
| C017 | 混血奴兵清污军户模板 | `C017-GROUP-VOICELOCK-V001` | `c017-group-voice-v001-preview.wav` | preview_audio_generated_needs_human_listening_qc |
| C021 | 北境共生兽关系模板 | `C021-CREATURE-SFXLOCK-V001` | `c021-creature-sfx-v001-preview.wav` | preview_audio_generated_needs_human_listening_qc_final_mix_pending |
| C024 | 边墙普通军户群像模板 | `C024-GROUP-VOICELOCK-V001` | `c024-group-voice-v001-preview.wav` | preview_audio_generated_needs_human_listening_qc |
| C025 | 普通人族平民群像模板 | `C025-GROUP-VOICELOCK-V001` | `c025-group-voice-v001-preview.wav` | preview_audio_generated_needs_human_listening_qc |
| NAR001 | 纪录片旁白 | `NAR001-VOICELOCK-V001` | `nar001-voice-v001-preview.wav` | preview_audio_visible_with_character_card_needs_human_listening_qc |

## 已建角色卡

| character_id | display_name | file | type | Section 1 status | source scope | art master |
| --- | --- | --- | --- | --- | --- | --- |
| C001 | 沈维桑 | `C001-shen-weisang.md` | 主角 | locked | Bible + ch001-006, ch031, ch044-048 | `c001m.png` |
| C002 | 晏南枝 | `C002-yan-nanzhi.md` | 主角 | locked | Bible + ch005, ch016, ch026, ch041-046 | `c002m.png` |
| C003 | 陆青砾 | `C003-lu-qingli.md` | 主角组 / 新血派雏形 | locked | Bible + ch024-027, ch043-048 | `c003m.png` |
| C004 | 薛临墙 | `C004-xue-linqiang.md` | 灰墙军代表 | locked | Bible + ch028-032, ch046 | `c004m.png` |
| C005 | 沈照眠 | `C005-shen-zhaomian.md` | 识别者伤口线 | locked | Bible + ch001-004, ch018-020, ch046 | `c005m.png` |
| C006 | 罗青禾 | `C006-luo-qinghe.md` | 起点 / 护送契约 | locked | Bible + ch002-004, ch046 | `c006m.png` |
| C007 | 白翳 | `C007-bai-yi.md` | 制度性反派 | locked | Bible + ch010-012, ch021, ch036, ch045 | `c007m.png` |
| C008 | 厉螳 | `C008-li-tang.md` | 甲军府武力压力 | locked | Bible + ch037-039, ch042-045 | `c008m.png` |
| C009 | 孟归藏 | `C009-meng-guicang.md` | 旧书会证人 | locked | Bible + ch014-017, ch035, ch046 | `c009m.png` |
| C010 | 鹿弥 | `C010-lu-mi.md` | 北境萨满证人 | locked | Bible + ch029, ch033-035, ch041-046 | `c010m.png` |
| C011 | 顾怀章 | `C011-gu-huaizhang.md` | 复翼者旧臣 | locked | Bible + ch022-023, ch041-046 | `c011m.png` |
| C012 | 赫连雪岱 | `C012-helian-xuedai.md` | 北境护卫 | locked | character Bible | `c012m.png` |
| C013 | 乌岚 | `C013-wu-lan.md` | 北境斥候 | locked | character Bible + ch034 | `c013m.png` |
| C014 | 拓跋砚熊 | `C014-tuoba-yanxiong.md` | 北境盾卫工匠 | locked | character Bible | `c014m.png` |
| C015 | 青翎鸦见 | `C015-qingling-yajian.md` | 北境传讯斥候 | locked | character Bible | `c015m.png` |
| C016 | 肃明基层虫吏层级模板 | `C016-suming-insect-clerk-template.md` | 群体模板 | locked | character Bible + ch001, ch007, ch018 | `c016m.png` |
| C017 | 混血奴兵清污军户模板 | `C017-hybrid-slave-soldier-template.md` | 群体模板 | locked | character Bible + ch003, ch007-009 | `c017m.png` |
| C018 | 普通纯虫族小兵模板 | `C018-insect-infantry-template.md` | 群体模板 | locked | character Bible | `c018m.png` |
| C019 | 中阶重甲虫士兵模板 | `C019-heavy-insect-soldier-template.md` | 群体模板 | locked | character Bible | `c019m.png` |
| C020 | 北境攻城兵种群像模板 | `C020-northern-siege-troops-template.md` | 群体模板 | locked | character Bible + ch028-031 | `c020m.png` |
| C021 | 北境共生兽关系模板 | `C021-northern-symbiotic-beasts-template.md` | 群体模板 | locked | character Bible + ch029-035 | `c021m.png` |
| C022 | 沈季衡 | `C022-shen-jiheng.md` | 旧驿测绘者 / 档案人物 | locked | Bible + ch034-040 | `c022m.png` |
| C023 | 人族逃难流民群像模板 | `C023-human-refugees-template.md` | 群体模板 | locked | character Bible + ch007-009, ch032 | `c023m.png` |
| C024 | 边墙普通军户群像模板 | `C024-wall-military-households-template.md` | 群体模板 | locked | character Bible + ch028-032 | `c024m.png` |
| C025 | 普通人族平民群像模板 | `C025-human-civilians-template.md` | 群体模板 | locked | character Bible + ch001-009 | `c025m.png` |
| C026 | 墙下集市无籍者与粮牌黑市群像模板 | `C026-wallfoot-market-stateless-template.md` | 群体模板 | locked | character Bible + ch024-027 | `c026m.png` |

## 功能层说明

C016-C021、C023-C026 是第一季下游生产已经使用的角色/群像模板，属于共享角色总卡的一部分。它们不是单个剧情人物，但必须有源头 Canon，防止下游把肃明压迫层级、北境族群差异、人族群众地域差异画成同一种“灰色敌人/流民/兽潮”。



