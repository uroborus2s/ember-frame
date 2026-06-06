# 第04集：金河磨齿 Video Production Plan

- Stage: `pre_asset`
- Shots: 40
- Aspect ratio: `16:9`
- FPS: `24`

## Render Order / 渲染顺序
- `001` `SC001-SH001` `T2V` status=`needs_config` assets=4
- `002` `SC001-SH002` `I2V` status=`needs_asset` assets=4
- `003` `SC001-SH003` `REFERENCE_IMAGE` status=`needs_asset` assets=4
- `004` `SC001-SH004` `I2V` status=`needs_asset` assets=4
- `005` `SC001-SH005` `I2V` status=`needs_asset` assets=4
- `006` `SC001-SH006` `I2V` status=`needs_asset` assets=4
- `007` `SC001-SH007` `REFERENCE_IMAGE` status=`needs_asset` assets=4
- `008` `SC001-SH008` `I2V` status=`needs_asset` assets=4
- `009` `SC001-SH009` `I2V` status=`needs_asset` assets=4
- `010` `SC001-SH010` `I2V` status=`needs_asset` assets=4
- `011` `SC002-SH001` `I2V` status=`needs_asset` assets=7
- `012` `SC002-SH002` `I2V` status=`needs_asset` assets=7
- `013` `SC002-SH003` `REFERENCE_IMAGE` status=`needs_asset` assets=7
- `014` `SC002-SH004` `I2V` status=`needs_asset` assets=7
- `015` `SC002-SH005` `I2V` status=`needs_asset` assets=7
- `016` `SC002-SH006` `I2V` status=`needs_asset` assets=7
- `017` `SC002-SH007` `REFERENCE_IMAGE` status=`needs_asset` assets=7
- `018` `SC002-SH008` `I2V` status=`needs_asset` assets=7
- `019` `SC002-SH009` `I2V` status=`needs_asset` assets=7
- `020` `SC002-SH010` `I2V` status=`needs_asset` assets=7
- `021` `SC003-SH001` `T2V` status=`needs_config` assets=6
- `022` `SC003-SH002` `I2V` status=`needs_asset` assets=6
- `023` `SC003-SH003` `REFERENCE_IMAGE` status=`needs_asset` assets=6
- `024` `SC003-SH004` `I2V` status=`needs_asset` assets=6
- `025` `SC003-SH005` `I2V` status=`needs_asset` assets=6
- `026` `SC003-SH006` `I2V` status=`needs_asset` assets=6
- `027` `SC003-SH007` `REFERENCE_IMAGE` status=`needs_asset` assets=6
- `028` `SC003-SH008` `I2V` status=`needs_asset` assets=6
- `029` `SC003-SH009` `I2V` status=`needs_asset` assets=6
- `030` `SC003-SH010` `I2V` status=`needs_asset` assets=6
- `031` `SC004-SH001` `T2V` status=`needs_config` assets=9
- `032` `SC004-SH002` `I2V` status=`needs_asset` assets=9
- `033` `SC004-SH003` `REFERENCE_IMAGE` status=`needs_asset` assets=9
- `034` `SC004-SH004` `I2V` status=`needs_asset` assets=9
- `035` `SC004-SH005` `I2V` status=`needs_asset` assets=9
- `036` `SC004-SH006` `I2V` status=`needs_asset` assets=9
- `037` `SC004-SH007` `REFERENCE_IMAGE` status=`needs_asset` assets=9
- `038` `SC004-SH008` `I2V` status=`needs_asset` assets=9
- `039` `SC004-SH009` `I2V` status=`needs_asset` assets=9
- `040` `SC004-SH010` `I2V` status=`needs_asset` assets=9

## Unresolved / 未解决项
- `needs_asset`: 需要 art-room 角色、地点、道具或关键参考帧。
- `needs_config`: 尚未提供 ComfyUI checkpoint、LoRA、ControlNet/IPAdapter、工作流模板或节点 ID。
- 精确对白不写入视频提示词，后续由 subtitle/audio 产物承接。
