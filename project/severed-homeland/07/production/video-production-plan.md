# 第07集：墙下无姓人 Video Production Plan

- Stage: `pre_asset`
- Shots: 40
- Aspect ratio: `9:16`
- FPS: `24`

## Render Order / 渲染顺序
- `001` `SC001-SH001` `I2V` status=`needs_asset` assets=7
- `002` `SC001-SH002` `I2V` status=`needs_asset` assets=7
- `003` `SC001-SH003` `REFERENCE_IMAGE` status=`needs_asset` assets=7
- `004` `SC001-SH004` `I2V` status=`needs_asset` assets=7
- `005` `SC001-SH005` `I2V` status=`needs_asset` assets=7
- `006` `SC001-SH006` `I2V` status=`needs_asset` assets=7
- `007` `SC001-SH007` `REFERENCE_IMAGE` status=`needs_asset` assets=7
- `008` `SC001-SH008` `I2V` status=`needs_asset` assets=7
- `009` `SC001-SH009` `I2V` status=`needs_asset` assets=7
- `010` `SC001-SH010` `I2V` status=`needs_asset` assets=7
- `011` `SC002-SH001` `I2V` status=`needs_asset` assets=8
- `012` `SC002-SH002` `I2V` status=`needs_asset` assets=8
- `013` `SC002-SH003` `REFERENCE_IMAGE` status=`needs_asset` assets=8
- `014` `SC002-SH004` `I2V` status=`needs_asset` assets=8
- `015` `SC002-SH005` `I2V` status=`needs_asset` assets=8
- `016` `SC002-SH006` `I2V` status=`needs_asset` assets=8
- `017` `SC002-SH007` `REFERENCE_IMAGE` status=`needs_asset` assets=8
- `018` `SC002-SH008` `I2V` status=`needs_asset` assets=8
- `019` `SC002-SH009` `FLF2V` status=`needs_asset` assets=8
- `020` `SC002-SH010` `I2V` status=`needs_asset` assets=8
- `021` `SC003-SH001` `FLF2V` status=`needs_asset` assets=8
- `022` `SC003-SH002` `I2V` status=`needs_asset` assets=8
- `023` `SC003-SH003` `REFERENCE_IMAGE` status=`needs_asset` assets=8
- `024` `SC003-SH004` `I2V` status=`needs_asset` assets=8
- `025` `SC003-SH005` `I2V` status=`needs_asset` assets=8
- `026` `SC003-SH006` `I2V` status=`needs_asset` assets=8
- `027` `SC003-SH007` `REFERENCE_IMAGE` status=`needs_asset` assets=8
- `028` `SC003-SH008` `I2V` status=`needs_asset` assets=8
- `029` `SC003-SH009` `I2V` status=`needs_asset` assets=8
- `030` `SC003-SH010` `I2V` status=`needs_asset` assets=8
- `031` `SC004-SH001` `T2V` status=`needs_config` assets=7
- `032` `SC004-SH002` `I2V` status=`needs_asset` assets=7
- `033` `SC004-SH003` `REFERENCE_IMAGE` status=`needs_asset` assets=7
- `034` `SC004-SH004` `I2V` status=`needs_asset` assets=7
- `035` `SC004-SH005` `I2V` status=`needs_asset` assets=7
- `036` `SC004-SH006` `I2V` status=`needs_asset` assets=7
- `037` `SC004-SH007` `REFERENCE_IMAGE` status=`needs_asset` assets=7
- `038` `SC004-SH008` `I2V` status=`needs_asset` assets=7
- `039` `SC004-SH009` `I2V` status=`needs_asset` assets=7
- `040` `SC004-SH010` `I2V` status=`needs_asset` assets=7

## Unresolved / 未解决项
- `needs_asset`: 需要 art-room 角色、地点、道具或关键参考帧。
- `needs_config`: 尚未提供 ComfyUI checkpoint、LoRA、ControlNet/IPAdapter、工作流模板或节点 ID。
- 精确对白不写入视频提示词，后续由 subtitle/audio 产物承接。
