# 第06集：白墙验名 Video Production Plan

- Stage: `pre_asset`
- Shots: 44
- Aspect ratio: `16:9`
- FPS: `24`

## Render Order / 渲染顺序
- `001` `SC001-SH001` `I2V` status=`needs_asset` assets=7
- `002` `SC001-SH002` `I2V` status=`needs_asset` assets=7
- `003` `SC001-SH003` `REFERENCE_IMAGE` status=`needs_asset` assets=7
- `004` `SC001-SH004` `I2V` status=`needs_asset` assets=7
- `005` `SC001-SH005` `I2V` status=`needs_asset` assets=7
- `006` `SC001-SH006` `FLF2V` status=`needs_asset` assets=7
- `007` `SC001-SH007` `REFERENCE_IMAGE` status=`needs_asset` assets=7
- `008` `SC001-SH008` `FLF2V` status=`needs_asset` assets=7
- `009` `SC001-SH009` `I2V` status=`needs_asset` assets=7
- `010` `SC001-SH010` `FLF2V` status=`needs_asset` assets=7
- `011` `SC001-SH011` `FLF2V` status=`needs_asset` assets=7
- `012` `SC002-SH001` `T2V` status=`needs_config` assets=9
- `013` `SC002-SH002` `I2V` status=`needs_asset` assets=9
- `014` `SC002-SH003` `REFERENCE_IMAGE` status=`needs_asset` assets=9
- `015` `SC002-SH004` `I2V` status=`needs_asset` assets=9
- `016` `SC002-SH005` `I2V` status=`needs_asset` assets=9
- `017` `SC002-SH006` `I2V` status=`needs_asset` assets=9
- `018` `SC002-SH007` `REFERENCE_IMAGE` status=`needs_asset` assets=9
- `019` `SC002-SH008` `I2V` status=`needs_asset` assets=9
- `020` `SC002-SH009` `I2V` status=`needs_asset` assets=9
- `021` `SC002-SH010` `I2V` status=`needs_asset` assets=9
- `022` `SC002-SH011` `I2V` status=`needs_asset` assets=9
- `023` `SC003-SH001` `T2V` status=`needs_config` assets=9
- `024` `SC003-SH002` `I2V` status=`needs_asset` assets=9
- `025` `SC003-SH003` `REFERENCE_IMAGE` status=`needs_asset` assets=9
- `026` `SC003-SH004` `I2V` status=`needs_asset` assets=9
- `027` `SC003-SH005` `I2V` status=`needs_asset` assets=9
- `028` `SC003-SH006` `I2V` status=`needs_asset` assets=9
- `029` `SC003-SH007` `REFERENCE_IMAGE` status=`needs_asset` assets=9
- `030` `SC003-SH008` `I2V` status=`needs_asset` assets=9
- `031` `SC003-SH009` `I2V` status=`needs_asset` assets=9
- `032` `SC003-SH010` `FLF2V` status=`needs_asset` assets=9
- `033` `SC003-SH011` `I2V` status=`needs_asset` assets=9
- `034` `SC004-SH001` `T2V` status=`needs_config` assets=10
- `035` `SC004-SH002` `I2V` status=`needs_asset` assets=10
- `036` `SC004-SH003` `REFERENCE_IMAGE` status=`needs_asset` assets=10
- `037` `SC004-SH004` `I2V` status=`needs_asset` assets=10
- `038` `SC004-SH005` `I2V` status=`needs_asset` assets=10
- `039` `SC004-SH006` `I2V` status=`needs_asset` assets=10
- `040` `SC004-SH007` `REFERENCE_IMAGE` status=`needs_asset` assets=10
- `041` `SC004-SH008` `I2V` status=`needs_asset` assets=10
- `042` `SC004-SH009` `I2V` status=`needs_asset` assets=10
- `043` `SC004-SH010` `I2V` status=`needs_asset` assets=10
- `044` `SC004-SH011` `I2V` status=`needs_asset` assets=10

## Unresolved / 未解决项
- `needs_asset`: 需要 art-room 角色、地点、道具或关键参考帧。
- `needs_config`: 尚未提供 ComfyUI checkpoint、LoRA、ControlNet/IPAdapter、工作流模板或节点 ID。
- 精确对白不写入视频提示词，后续由 subtitle/audio 产物承接。
