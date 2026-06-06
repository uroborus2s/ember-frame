# 全资产提示词长度与质量审查

- 项目：`project/severed-homeland`
- 版本：`series-prompt-length-quality-review-v3-2026-06-06`
- 日期：2026-06-06
- 源文件：`prompts/series-art-image-prompts.json`
- 审查范围：72 条全剧资产提示词（C/L/P/K/F）
- 字符统计口径：按 Unicode code point 计数；中文标点和换行计入字符。

## 本轮修复说明

- 按用户要求跳过 `C001`、`C002`。
- 已压缩非 `C001`/`C002` 的 C/K/L/F 参考图规则，避免重复写入完整暖多色规则。
- 已将 `P001-P015` 的“使用磨损”病句改为“长期使用痕迹”。
- 灰褐、黑灰、冷灰等场景/材质色不再按中风险处理；只有成为主色调或让主体背景融合时才算问题。

## 主要发现

### F1 HIGH - C001/C002 皮肤修复锁仍保留，本轮按要求未处理

- 资产：C001, C002
- 说明：这些提示词含“只允许调整肤色/脸手/不要改服装”或类似约束，会阻止按新暖多色合同重做服饰颜色；用户指定本轮先不处理。

### F2 LOW - 剩余低风险重复句或精确符号规则重复

- 资产：C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018, C019, C020, C021, C022, L001, L002, L003, L004, L005, L006, L007, L008, L009, L010, L011, L012, L013, L014, L015, L016, K001, K002, K003, K005, K006, F001, F002, F003, F005, F006
- 说明：多为“精确符号留给线控”一类低风险重复；不影响本轮中风险重复和病句修复目标。

## 类型统计

| 类型 | 数量 | positive 平均长度 | ChatGPT 平均长度 | positive 最大长度 | 高风险数 | 中风险数 | 低风险数 | 无明显问题 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| character | 26 | 1144 | 1618 | 2225 | 2 | 0 | 17 | 7 |
| location | 16 | 847 | 1297 | 861 | 0 | 0 | 16 | 0 |
| prop | 18 | 690 | 974 | 871 | 0 | 0 | 0 | 18 |
| costume | 6 | 976 | 1493 | 1050 | 0 | 0 | 5 | 1 |
| style | 6 | 765 | 1225 | 827 | 0 | 0 | 5 | 1 |

## 最长提示词 Top 12

| 资产 | 类型 | positive | negative | ChatGPT | model-visible | 问题摘要 |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| C001 | character | 2225 | 414 | 2918 | 2636 | high；皮肤修复锁冲突；场景/材质灰褐提示；全局规则重复；重复句5 |
| C002 | character | 1630 | 350 | 2240 | 1977 | high；皮肤修复锁冲突；场景/材质灰褐提示；全局规则重复；参考规则重复；重复句3 |
| C024 | character | 1572 | 271 | 2052 | 1840 | 无明显问题 |
| C026 | character | 1552 | 252 | 2013 | 1801 | 无明显问题 |
| C025 | character | 1540 | 246 | 1995 | 1783 | 无明显问题 |
| C023 | character | 1512 | 264 | 1985 | 1773 | 无明显问题 |
| C022 | character | 1395 | 367 | 1971 | 1759 | low |
| K006 | costume | 1050 | 328 | 1587 | 1375 | low |
| C008 | character | 1073 | 265 | 1547 | 1335 | low |
| K001 | costume | 1041 | 297 | 1547 | 1335 | low；场景/材质灰褐提示 |
| C016 | character | 1050 | 273 | 1532 | 1320 | low |
| C020 | character | 1045 | 242 | 1496 | 1284 | low；重复句1 |

## 所有资产提示词字符长度

| 资产 | 类型 | 子类型 | model-visible 总长 | copy positive | copy negative | ChatGPT prompt | Gemini prompt | reference instructions | 问题摘要 |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| C001 | character | character_master_card | 2636 | 2225 | 414 | 2918 | 3110 | 234 | high；皮肤修复锁冲突；场景/材质灰褐提示；全局规则重复；重复句5 |
| C002 | character | character_master_card | 1977 | 1630 | 350 | 2240 | 2432 | 215 | high；皮肤修复锁冲突；场景/材质灰褐提示；全局规则重复；参考规则重复；重复句3 |
| C003 | character | character_master_card | 1001 | 782 | 222 | 1213 | 1405 | 164 | 无明显问题 |
| C004 | character | character_master_card | 1106 | 887 | 222 | 1318 | 1510 | 164 | 无明显问题 |
| C005 | character | character_master_card | 989 | 766 | 226 | 1201 | 1393 | 164 | 无明显问题 |
| C006 | character | character_master_card | 1216 | 977 | 242 | 1428 | 1620 | 164 | low；重复句1 |
| C007 | character | character_master_card | 1240 | 1001 | 242 | 1452 | 1644 | 164 | low；重复句1 |
| C008 | character | character_master_card | 1335 | 1073 | 265 | 1547 | 1739 | 164 | low |
| C009 | character | character_master_card | 1165 | 926 | 242 | 1377 | 1569 | 164 | low |
| C010 | character | character_master_card | 1213 | 974 | 242 | 1425 | 1617 | 164 | low |
| C011 | character | character_master_card | 1204 | 965 | 242 | 1416 | 1608 | 164 | low；重复句1 |
| C012 | character | character_master_card | 1208 | 969 | 242 | 1420 | 1612 | 164 | low |
| C013 | character | character_master_card | 1185 | 946 | 242 | 1397 | 1589 | 164 | low；场景/材质灰褐提示 |
| C014 | character | character_master_card | 1230 | 991 | 242 | 1442 | 1634 | 164 | low |
| C015 | character | character_master_card | 1204 | 965 | 242 | 1416 | 1608 | 164 | low |
| C016 | character | character_master_card | 1320 | 1050 | 273 | 1532 | 1724 | 164 | low |
| C017 | character | character_master_card | 1238 | 999 | 242 | 1450 | 1642 | 164 | low |
| C018 | character | character_master_card | 1220 | 981 | 242 | 1432 | 1624 | 164 | low |
| C019 | character | character_master_card | 1224 | 985 | 242 | 1436 | 1628 | 164 | low；重复句1 |
| C020 | character | character_master_card | 1284 | 1045 | 242 | 1496 | 1688 | 164 | low；重复句1 |
| C021 | character | character_master_card | 1280 | 1041 | 242 | 1492 | 1684 | 164 | low；重复句1 |
| C022 | character | character_master_card | 1759 | 1395 | 367 | 1971 | 2163 | 164 | low |
| C023 | character | character_master_card | 1773 | 1512 | 264 | 1985 | 2177 | 164 | 无明显问题 |
| C024 | character | character_master_card | 1840 | 1572 | 271 | 2052 | 2244 | 164 | 无明显问题 |
| C025 | character | character_master_card | 1783 | 1540 | 246 | 1995 | 2187 | 164 | 无明显问题 |
| C026 | character | character_master_card | 1801 | 1552 | 252 | 2013 | 2205 | 164 | 无明显问题 |
| L001 | location | location_master_scene_card | 1092 | 854 | 241 | 1304 | 1496 | 164 | low |
| L002 | location | location_master_scene_card | 1079 | 841 | 241 | 1291 | 1483 | 164 | low |
| L003 | location | location_master_scene_card | 1099 | 861 | 241 | 1311 | 1503 | 164 | low |
| L004 | location | location_master_scene_card | 1090 | 852 | 241 | 1302 | 1494 | 164 | low |
| L005 | location | location_master_scene_card | 1083 | 845 | 241 | 1295 | 1487 | 164 | low |
| L006 | location | location_master_scene_card | 1081 | 843 | 241 | 1293 | 1485 | 164 | low |
| L007 | location | location_master_scene_card | 1094 | 856 | 241 | 1306 | 1498 | 164 | low |
| L008 | location | location_master_scene_card | 1085 | 847 | 241 | 1297 | 1489 | 164 | low |
| L009 | location | location_master_scene_card | 1088 | 850 | 241 | 1300 | 1492 | 164 | low |
| L010 | location | location_master_scene_card | 1090 | 852 | 241 | 1302 | 1494 | 164 | low |
| L011 | location | location_master_scene_card | 1078 | 840 | 241 | 1290 | 1482 | 164 | low |
| L012 | location | location_master_scene_card | 1096 | 858 | 241 | 1308 | 1500 | 164 | low |
| L013 | location | location_master_scene_card | 1068 | 830 | 241 | 1280 | 1472 | 164 | low |
| L014 | location | location_master_scene_card | 1081 | 843 | 241 | 1293 | 1485 | 164 | low |
| L015 | location | location_master_scene_card | 1087 | 849 | 241 | 1299 | 1491 | 164 | low |
| L016 | location | location_master_scene_card | 1071 | 833 | 241 | 1283 | 1475 | 164 | low |
| P001 | prop | prop_master_card | 768 | 621 | 150 | 902 | 1094 | 86 | 无明显问题 |
| P002 | prop | prop_master_card | 791 | 644 | 150 | 925 | 1117 | 86 | 无明显问题 |
| P003 | prop | prop_master_card | 770 | 623 | 150 | 904 | 1096 | 86 | 无明显问题 |
| P004 | prop | prop_master_card | 768 | 621 | 150 | 902 | 1094 | 86 | 无明显问题 |
| P005 | prop | prop_master_card | 764 | 617 | 150 | 898 | 1090 | 86 | 无明显问题 |
| P006 | prop | prop_master_card | 789 | 642 | 150 | 923 | 1115 | 86 | 无明显问题 |
| P007 | prop | prop_master_card | 827 | 680 | 150 | 961 | 1153 | 86 | 无明显问题 |
| P008 | prop | prop_master_card | 784 | 637 | 150 | 918 | 1110 | 86 | 无明显问题 |
| P009 | prop | prop_master_card | 799 | 652 | 150 | 933 | 1125 | 86 | 无明显问题 |
| P010 | prop | prop_master_card | 796 | 649 | 150 | 930 | 1122 | 86 | 无明显问题 |
| P011 | prop | prop_master_card | 817 | 670 | 150 | 951 | 1143 | 86 | 无明显问题 |
| P012 | prop | prop_master_card | 787 | 640 | 150 | 921 | 1113 | 86 | 无明显问题 |
| P013 | prop | prop_master_card | 847 | 700 | 150 | 981 | 1173 | 86 | 无明显问题 |
| P014 | prop | prop_master_card | 836 | 689 | 150 | 970 | 1162 | 86 | 无明显问题 |
| P015 | prop | prop_master_card | 888 | 741 | 150 | 1022 | 1214 | 86 | 无明显问题 |
| P016 | prop | prop_master_card | 1007 | 860 | 150 | 1157 | 1349 | 94 | 无明显问题 |
| P017 | prop | prop_master_card | 1009 | 862 | 150 | 1159 | 1351 | 94 | 无明显问题 |
| P018 | prop | prop_master_card | 1018 | 871 | 150 | 1168 | 1360 | 94 | 无明显问题 |
| K001 | costume | style_reference | 1335 | 1041 | 297 | 1547 | 1739 | 164 | low；场景/材质灰褐提示 |
| K002 | costume | style_reference | 1255 | 956 | 302 | 1467 | 1659 | 164 | low |
| K003 | costume | style_reference | 1181 | 887 | 297 | 1393 | 1585 | 164 | low |
| K004 | costume | style_reference | 1278 | 965 | 316 | 1490 | 1682 | 164 | 无明显问题 |
| K005 | costume | style_reference | 1264 | 954 | 313 | 1476 | 1668 | 164 | low |
| K006 | costume | style_reference | 1375 | 1050 | 328 | 1587 | 1779 | 164 | low |
| F001 | style | style_reference | 1009 | 761 | 251 | 1221 | 1413 | 164 | low |
| F002 | style | style_reference | 1008 | 760 | 251 | 1220 | 1412 | 164 | low |
| F003 | style | style_reference | 996 | 748 | 251 | 1208 | 1400 | 164 | low |
| F004 | style | style_reference | 1075 | 827 | 251 | 1287 | 1479 | 164 | 无明显问题 |
| F005 | style | style_reference | 996 | 748 | 251 | 1208 | 1400 | 164 | low |
| F006 | style | style_reference | 992 | 744 | 251 | 1204 | 1396 | 164 | low |

## 处理建议

1. 本轮目标已完成：非 C001/C002 的重复规则和 P001-P015 病句已清理。
2. 后续如果要继续降低风险，再处理 C001/C002 的皮肤修复遗留锁和重复 hard reference。
3. 保留“不要灰褐主调”，不把灰褐当禁色；当前规则仍按“可按场景/材质使用，但不得主导”执行。
