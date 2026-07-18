# 提示词部工作流

```text
读取剧本/导演/美术/声音合同
  -> 提取可见目标
  -> 匹配提示词技巧库结构
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

当任务涉及角色卡、场景俯视图、场景九宫格、故事板、导演故事版、分秒视频提示词、微表情或宏大运镜时，先读取 `prompt-technique-library.md`，选择合适结构，再写入正式提示词区。
