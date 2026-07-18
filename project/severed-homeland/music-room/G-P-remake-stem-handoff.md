# G-P 重拍版 Stem 交接

owner: music-room
status: stem_handoff_ready_pending_human_listening_director_mix
version: 20260621v0001

## 1. 归口

过程版本：

```text
music-room/.work/asset-versions/E01-GP-P01-MX001/20260621v0001/
music-room/.work/asset-versions/E01-GP-P02-MX002/20260621v0001/
music-room/.work/asset-versions/E01-GP-P03-MX003/20260621v0001/
music-room/.work/asset-versions/E01-GP-P04-MX004/20260621v0001/
music-room/.work/asset-versions/E01-GP-P05-MX005/20260621v0001/
```

分镜交接：

```text
director-room/season-01/01/G-P/P-01/assets/music/
director-room/season-01/01/G-P/P-02/assets/music/
director-room/season-01/01/G-P/P-03/assets/music/
director-room/season-01/01/G-P/P-04/assets/music/
director-room/season-01/01/G-P/P-05/assets/music/
```

每个目录均含同名 WAV 和 `manifest-20260621v0001.jsonl`。所有 WAV 均已文件级校验为 48 kHz / stereo / 16-bit PCM。

## 2. Stem 清单

### P-01 E01-GP-P01-MX001

- mix: `P-01-E01-GP-P01-MX001-mix-E01-GP-P01-MX001-20260621v0001-48k-stereo.wav`
- stems: `bone_bell_rope`, `gate_stone_stress`, `low_body_pressure`, `snow_heavy_steps`, `creature_breath_pain`, `blizzard_roomtone`, `ballista_winch_iron`, `grain_door_bridge`
- mix rule: 军户头领喊声前半拍，`low_body_pressure`、`creature_breath_pain` 下沉；`bone_bell_rope` 和 `ballista_winch_iron` 保留 1-4 kHz 边缘。

### P-02 E01-GP-P02-MX002

- mix: `P-02-E01-GP-P02-MX002-mix-E01-GP-P02-MX002-20260621v0001-48k-stereo.wav`
- stems: `ledger_pages_tally`, `military_boot_stove_break`, `wheat_grain_mud`, `black_iron_ring_drag`, `wax_press_peel`, `low_process_pulse`
- mix rule: C016 台词区间保留册页边缘，`low_process_pulse` 降至近无；虫蜡剥离尾音不得被音乐盖住。

### P-03 E01-GP-P03-MX003

- mix: `P-03-E01-GP-P03-MX003-mix-E01-GP-P03-MX003-20260621v0001-48k-stereo.wav`
- stems: `white_wall_roomtone`, `child_song_timing_guide_no_voice`, `wax_needle_yellow`, `wood_tag_identification`, `mother_wall_muffle`
- mix rule: `child_song_timing_guide_no_voice` 只用于节奏对齐，最终童声由配音部替换；木牌轻响必须留尾接 P-04。

### P-04 E01-GP-P04-MX004

- mix: `P-04-E01-GP-P04-MX004-mix-E01-GP-P04-MX004-20260621v0001-48k-stereo.wav`
- stems: `rain_roomtone`, `red_thread_snap`, `escape_steps_cloth_blackbox`, `black_box_dossier`, `wall_scrape_old_road`, `white_register_hinge`, `cold_pursuit_pulse`
- mix rule: 白翳台词下方只保留 `rain_roomtone` 和低冷空气感；`white_register_hinge` 是最高优先级离场声。

### P-05 E01-GP-P05-MX005

- mix: `P-05-E01-GP-P05-MX005-mix-E01-GP-P05-MX005-20260621v0001-48k-stereo.wav`
- stems: `chicken_calls`, `wet_pine_steps`, `rabbits_bow_body`, `copper_gong_three`, `village_dawn_roomtone`, `low_pressure_tail`
- mix rule: 第二声鸡叫必须被第一下铜锣切断；铜锣后动作压低，`low_pressure_tail` 只在铜锣后进入。

## 3. 下游执行

- 剪辑部先用 mix 试剪，确认声桥和动作点。
- 终混时以 stem 替换 mix，按对白和现场 Foley 做 ducking。
- 未完成人工听审、对白贴合和导演听审前，不标记为 final master。
