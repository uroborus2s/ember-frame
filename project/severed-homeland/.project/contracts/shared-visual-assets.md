# 公共视觉资产归口契约

owner: project-office
status: active
last_updated: 2026-06-21

## 适用范围

本契约用于全剧可复用、非单一分镜专属的公共视觉资产，例如阵营徽章、旗帜、纹样、印章、封条、石刻符号、常驻道具母版、公共服饰纹样和全剧风格母资产。

角色母资产仍按角色总卡合同归口到 `director-room/characters/`。具体分镜最终图片、视频、配音、音乐和剪辑交接仍回到对应分镜目录。

## 正式归口

公共视觉资产正式库：

```text
art-room/shared-assets/
  asset-index.json
  props/
  overlays/
  style/
```

当前正式图像放在 `art-room/shared-assets/` 下；候选、废弃、返工前和被替换版本放在：

```text
art-room/.work/asset-versions/{asset-id}/
```

正式路径始终指向当前可交接版本；隐藏版本库只做追溯，不作为下游第一入口。

## 阵营旗帜徽章锁定

已锁定三张公共根资产：

| asset_id | faction | formal_asset | version_repo |
| --- | --- | --- | --- |
| P016-zhaoming-emblem-flag-root | 昭明 | `art-room/shared-assets/props/p016m.png` | `art-room/.work/asset-versions/P016-zhaoming-emblem-flag-root/` |
| P017-suming-emblem-flag-root | 肃明/清明 | `art-room/shared-assets/props/p017m.png` | `art-room/.work/asset-versions/P017-suming-emblem-flag-root/` |
| P018-beast-alliance-emblem-flag-root | 北境万兽/兽族联盟 | `art-room/shared-assets/props/p018m.png` | `art-room/.work/asset-versions/P018-beast-alliance-emblem-flag-root/` |

这三张根图形不可重画、重设计或由模型自由生成替代。后续任何涉及三方势力的旗帜、徽章、服饰纹样、封条、石刻、旗号、印章、帐旗和后合成层，都必须从对应根资产派生。

## 透明派生规则

根母版卡可以是中性背景正式参考图；但新制作的独立旗帜、徽章、线控层、抠图层和后合成 overlay 必须使用：

```text
output_spec_id: OUT-PRECISION-OVERLAY
background_policy: transparent_alpha
alpha_policy: required
annotation_policy: forbidden
control_role: precision_overlay
```

透明派生层可以放入：

```text
art-room/shared-assets/overlays/
```

正式分镜只引用这些公共资产；除非该分镜需要独有损坏、遮挡、角度或局部重绘，不在分镜目录重复保存公共母版。
