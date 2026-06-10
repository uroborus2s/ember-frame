# SC003 四张核心参考帧高分优化复评 / 2026-06-11

## 结论

本轮继续优化 `E01_R010`-`E01_R013` 四张 SC003 核心参考帧，目标为每张导演要求不低于 `92/100`，美术合格度高于 `95/100`。`E01_R014` 继续排除在四图评分外，只作为 `SC003-SH004` 终帧/转场候选另行管理。

四张高分版已覆盖 canonical 路径，均为 `3840x2160` PNG、RGB、无 alpha。当前结论：四张均达到目标阈值，可作为 SC003 视频拍摄候选首帧进入后续 director-room prompt refresh 与 I2V/FLF2V 测试；最终成片仍建议原生 4K 复刻以减少重采样细节损失。

## 高分评分

| Asset | Shot | 导演要求 | 美术合格度 | 结论 |
| --- | --- | ---: | ---: | --- |
| `E01_R010` | `SC003-SH001` 红线地图建立 | 94 | 96 | 通过 |
| `E01_R011` | `SC003-SH002` 顾/晏对峙 | 92 | 96 | 通过 |
| `E01_R012` | `SC003-SH003` 血牒未接 | 94 | 96 | 通过 |
| `E01_R013` | `SC003-SH004` 红线北端转场首帧 | 93 | 96 | 通过 |

平均分：导演要求 `93.25/100`，美术合格度 `96/100`。综合状态：`passed_highscore_target_92_director_95plus_art_2026-06-11`。

## 复评意见

- `E01_R010`：红线成为明确主叙事，旧驿图、湿油布、藤桥、石台和雨夜空间层级完整。低位暖侧光与右上冷雨反光让纸、线、铜、木、水分材质成立，美术质感达到高分阈值。
- `E01_R011`：红线重新成为顾怀章与晏南枝之间的权力边界。玉片降为右侧阴影中的小面积冷边，不再抢走主叙事；顾怀章暖侧光、晏南枝冷暗部、雨夜背景三层关系清楚。
- `E01_R012`：血牒越过红线、指尖停住、空隙可读，动作因果清楚。纸纤维、蜡封、潮痕、手背、湿桌和冷暖分界细节充分，避免了血牒圣旨化和玉片法器化。
- `E01_R013`：红线北端、线钉和雨滴位于上三分之一附近，图形转场目标清楚。晏南枝只保留远处虚焦遮面轮廓，没有手或玉片抢焦；低位暖边与冷雨反光共同强化线端材质。

## 光影结论

本轮不需要再叠加额外光效。后续视频阶段只锁定并微调现有光型：

- `R010`：低位油灯暖侧光擦纸面、红线、铜钉和湿木；右上冷雨反光点水滴与油布。
- `R011`：顾怀章保持暖侧光，晏南枝只吃窄冷边；玉片亮度不可超过红线和顾怀章压图手。
- `R012`：暖冷交界落在红线与未接触空隙处；血牒不发光、不漂浮。
- `R013`：油灯压暗，只保留红线纤维和雨滴边缘；冷反光勾纸裂和虚焦剪影，不用丁达尔遮挡线端。

## 已写入文件

- `01/assets/reference-frames/r010e01.png`
- `01/assets/reference-frames/r011e01.png`
- `01/assets/reference-frames/r012e01.png`
- `01/assets/reference-frames/r013e01.png`

## 保留历史

- `01/assets/reference-frames/history/r010e01.before-highscore-20260611.png`
- `01/assets/reference-frames/history/r011e01.before-highscore-20260611.png`
- `01/assets/reference-frames/history/r012e01.before-highscore-20260611.png`
- `01/assets/reference-frames/history/r013e01.before-highscore-20260611.png`
- `01/assets/reference-frames/history/r010e01.highscore-source-20260611.png`
- `01/assets/reference-frames/history/r011e01.highscore-source-20260611.png`
- `01/assets/reference-frames/history/r012e01.highscore-source-20260611.png`
- `01/assets/reference-frames/history/r013e01.highscore-source-20260611.png`
