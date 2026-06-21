# 提示词部工作流

```text
读取剧本/导演/美术/声音合同
  -> 提取可见目标
  -> 绑定资产和控制图
  -> 写图片提示词
  -> 写视频拍摄提示词
  -> 写负面提示词
  -> QC
  -> 交接
```

提示词必须分离：

```text
production_metadata
model_visible_prompt
copy_ready
negative_prompt
```

