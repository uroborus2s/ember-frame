# 第02集：火里的逃犯 Video Production Plan

- Stage: `pre_asset`
- Shots: 40
- Aspect ratio: `9:16`
- FPS: `24`

## Render Order / 渲染顺序
- `001` `SC001-SH001` `T2V` status=`needs_config` assets=7
- `002` `SC001-SH002` `I2V` status=`needs_asset` assets=7
- `003` `SC001-SH003` `REFERENCE_IMAGE` status=`needs_asset` assets=7
- `004` `SC001-SH004` `I2V` status=`needs_asset` assets=7
- `005` `SC001-SH005` `I2V` status=`needs_asset` assets=7
- `006` `SC001-SH006` `FLF2V` status=`needs_asset` assets=7
- `007` `SC001-SH007` `REFERENCE_IMAGE` status=`needs_asset` assets=7
- `008` `SC001-SH008` `FLF2V` status=`needs_asset` assets=7
- `009` `SC002-SH001` `I2V` status=`needs_asset` assets=11
- `010` `SC002-SH002` `FLF2V` status=`needs_asset` assets=11
- `011` `SC002-SH003` `REFERENCE_IMAGE` status=`needs_asset` assets=11
- `012` `SC002-SH004` `I2V` status=`needs_asset` assets=11
- `013` `SC002-SH005` `I2V` status=`needs_asset` assets=11
- `014` `SC002-SH006` `FLF2V` status=`needs_asset` assets=11
- `015` `SC002-SH007` `REFERENCE_IMAGE` status=`needs_asset` assets=11
- `016` `SC002-SH008` `FLF2V` status=`needs_asset` assets=11
- `017` `SC003-SH001` `T2V` status=`needs_config` assets=4
- `018` `SC003-SH002` `FLF2V` status=`needs_asset` assets=4
- `019` `SC003-SH003` `REFERENCE_IMAGE` status=`needs_asset` assets=4
- `020` `SC003-SH004` `I2V` status=`needs_asset` assets=4
- `021` `SC003-SH005` `I2V` status=`needs_asset` assets=4
- `022` `SC003-SH006` `FLF2V` status=`needs_asset` assets=4
- `023` `SC003-SH007` `REFERENCE_IMAGE` status=`needs_asset` assets=4
- `024` `SC003-SH008` `FLF2V` status=`needs_asset` assets=4
- `025` `SC004-SH001` `T2V` status=`needs_config` assets=8
- `026` `SC004-SH002` `I2V` status=`needs_asset` assets=8
- `027` `SC004-SH003` `REFERENCE_IMAGE` status=`needs_asset` assets=8
- `028` `SC004-SH004` `FLF2V` status=`needs_asset` assets=8
- `029` `SC004-SH005` `I2V` status=`needs_asset` assets=8
- `030` `SC004-SH006` `I2V` status=`needs_asset` assets=8
- `031` `SC004-SH007` `REFERENCE_IMAGE` status=`needs_asset` assets=8
- `032` `SC004-SH008` `I2V` status=`needs_asset` assets=8
- `033` `SC005-SH001` `T2V` status=`needs_config` assets=10
- `034` `SC005-SH002` `I2V` status=`needs_asset` assets=10
- `035` `SC005-SH003` `REFERENCE_IMAGE` status=`needs_asset` assets=10
- `036` `SC005-SH004` `I2V` status=`needs_asset` assets=10
- `037` `SC005-SH005` `I2V` status=`needs_asset` assets=10
- `038` `SC005-SH006` `I2V` status=`needs_asset` assets=10
- `039` `SC005-SH007` `REFERENCE_IMAGE` status=`needs_asset` assets=10
- `040` `SC005-SH008` `I2V` status=`needs_asset` assets=10

## Unresolved / 未解决项
- `needs_asset`: 需要 art-room 角色、地点、道具或关键参考帧。
- `needs_config`: 尚未提供 ComfyUI checkpoint、LoRA、ControlNet/IPAdapter、工作流模板或节点 ID。
- 精确对白不写入视频提示词，后续由 subtitle/audio 产物承接。
