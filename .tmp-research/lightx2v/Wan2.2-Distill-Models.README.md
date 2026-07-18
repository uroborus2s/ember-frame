---
license: apache-2.0
tags:
  - diffusion-single-file
  - comfyui
  - distillation
  - LoRA
  - video
  - video genration
base_model:
  - Wan-AI/Wan2.2-I2V-A14B
pipeline_tags: 
  - image-to-video
  - text-to-video
library_name: diffusers
---
# 🎬 Wan2.2 Distilled Models

### ⚡ High-Performance Video Generation with 4-Step Inference

*Distillation-accelerated version of Wan2.2 - Dramatically faster speed with excellent quality*

![img_lightx2v](https://cdn-uploads.huggingface.co/production/uploads/680de13385293771bc57400b/tTnp8-ARpj3wGxfo5P55c.png)

---

[![🤗 HuggingFace](https://img.shields.io/badge/🤗-HuggingFace-yellow)](https://huggingface.co/lightx2v/Wan2.2-Distill-Models)
[![GitHub](https://img.shields.io/badge/GitHub-LightX2V-blue?logo=github)](https://github.com/ModelTC/LightX2V)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)

---

## 🔥 News

- 2026.04.12: We are excited to release the [Wan2.2-I2V-A14B-4step-720p-high](https://huggingface.co/lightx2v/Wan2.2-Distill-Models/blob/main/wan2.2_i2v_A14b_high_noise_lightx2v_4step_720p_260412.safetensors) and [Wan2.2-I2V-A14B-4step-720p-low](https://huggingface.co/lightx2v/Wan2.2-Distill-Models/blob/main/wan2.2_i2v_A14b_low_noise_lightx2v_4step_720p_260412.safetensors) models. Compared to previous iterations, this version was trained on a high-quality 720p dataset and features an optimized low-noise training algorithm. These enhancements significantly boost the model's performance in fine-grained detail rendering and visual texture.


## 🌟 What's Special?

<table>
<tr>
<td width="50%">

### ⚡ Ultra-Fast Generation
- **4-step inference** (vs traditional 50+ steps)
- Approximately **2x faster** using LightX2V than ComfyUI
- Near real-time video generation capability

</td>
<td width="50%">

### 🎯 Flexible Options
- **Dual noise control**: High/Low noise variants
- Multiple precision formats (BF16/FP8/INT8)
- Full 14B parameter models

</td>
</tr>
<tr>
<td width="50%">

### 💾 Memory Efficient
- FP8/INT8: **~50% size reduction**
- CPU offload support
- Optimized for consumer GPUs

</td>
<td width="50%">

### 🔧 Easy Integration
- Compatible with LightX2V framework
- ComfyUI support
- Simple configuration files

</td>
</tr>
</table>

---

## 📦 Model Catalog

### 🎥 Model Types

<table>
<tr>
<td align="center" width="50%">

#### 🖼️ **Image-to-Video (I2V) - 14B Parameters**
Transform static images into dynamic videos with advanced quality control

- 🎨 **High Noise**: More creative, diverse outputs
- 🎯 **Low Noise**: More faithful to input, stable outputs

</td>
<td align="center" width="50%">

#### 📝 **Text-to-Video (T2V) - 14B Parameters**
Generate videos from text descriptions

- 🎨 **High Noise**: More creative, diverse outputs
- 🎯 **Low Noise**: More stable and controllable outputs
- 🚀 Full 14B parameter model

</td>
</tr>
</table>

### 🎯 Precision Versions

| Precision | Model Identifier | Model Size | Framework | Quality vs Speed |
|:---------:|:-----------------|:----------:|:---------:|:-----------------|
| 🏆 **BF16** | `lightx2v_4step` | ~28.6 GB | LightX2V | ⭐⭐⭐⭐⭐ Highest Quality |
| ⚡ **FP8** | `scaled_fp8_e4m3_lightx2v_4step` | ~15 GB | LightX2V | ⭐⭐⭐⭐ Excellent Balance |
| 🎯 **INT8** | `int8_lightx2v_4step` | ~15 GB | LightX2V | ⭐⭐⭐⭐ Fast & Efficient |
| 🔷 **FP8 ComfyUI** | `scaled_fp8_e4m3_lightx2v_4step_comfyui` | ~15 GB | ComfyUI | ⭐⭐⭐ ComfyUI Ready |

### 📝 Naming Convention

```bash
# Format: wan2.2_{task}_A14b_{noise_level}_{precision}_lightx2v_4step.safetensors

# I2V Examples:
wan2.2_i2v_A14b_high_noise_lightx2v_4step.safetensors                       # I2V High Noise - BF16
wan2.2_i2v_A14b_high_noise_scaled_fp8_e4m3_lightx2v_4step.safetensors      # I2V High Noise - FP8
wan2.2_i2v_A14b_low_noise_int8_lightx2v_4step.safetensors                  # I2V Low Noise - INT8
wan2.2_i2v_A14b_low_noise_scaled_fp8_e4m3_lightx2v_4step_comfyui.safetensors  # I2V Low Noise - FP8 ComfyUI

```
> 💡 **Browse All Models**: [View Full Model Collection →](https://huggingface.co/lightx2v/Wan2.2-Distill-Models/tree/main)

---

## 🚀 Usage

### Method 1: LightX2V (Recommended ⭐)

**LightX2V is a high-performance inference framework optimized for these models, approximately 2x faster than ComfyUI with better quantization accuracy. Highly recommended!**

#### Quick Start

1. Download model (using I2V FP8 as example)
```bash
huggingface-cli download lightx2v/Wan2.2-Distill-Models \
    --local-dir ./models/wan2.2_i2v \
    --include "wan2.2_i2v_A14b_high_noise_scaled_fp8_e4m3_lightx2v_4step.safetensors"
```

```bash
huggingface-cli download lightx2v/Wan2.2-Distill-Models \
    --local-dir ./models/wan2.2_i2v \
    --include "wan2.2_i2v_A14b_low_noise_scaled_fp8_e4m3_lightx2v_4step.safetensors"
```

> 💡 **Tip**: For T2V models, follow the same steps but replace `i2v` with `t2v` in the filenames

2. Clone LightX2V repository

```bash
git clone https://github.com/ModelTC/LightX2V.git
cd LightX2V
```

3. Install dependencies

```bash
pip install -r requirements.txt
```
Or refer to [Quick Start Documentation](https://lightx2v-zhcn.readthedocs.io/zh-cn/latest/getting_started/quickstart.html) to use docker

4. Select and modify configuration file

Choose appropriate configuration based on your GPU memory:

**80GB+ GPUs (A100/H100)**
- I2V: [wan_moe_i2v_distill.json](https://github.com/ModelTC/LightX2V/blob/main/configs/wan22/wan_moe_i2v_distill.json)

**24GB+ GPUs (RTX 4090)**
- I2V: [wan_moe_i2v_distill_4090.json](https://github.com/ModelTC/LightX2V/blob/main/configs/wan22/wan_moe_i2v_distill_4090.json)


5. Run inference (using [I2V]((https://github.com/ModelTC/LightX2V/blob/main/scripts/wan22/run_wan22_moe_i2v_distill.sh)) as example)
```bash
cd scripts
bash wan22/run_wan22_moe_i2v_distill.sh
```

> 📝 **Note**: Update model paths in the script to point to your Wan2.2 model. Also refer to [LightX2V Model Structure Documentation](https://lightx2v-zhcn.readthedocs.io/zh-cn/latest/getting_started/model_structure.html)


#### LightX2V Documentation
- **Quick Start Guide**: [LightX2V Quick Start](https://lightx2v-zhcn.readthedocs.io/zh-cn/latest/getting_started/quickstart.html)
- **Complete Usage Guide**: [LightX2V Model Structure Documentation](https://lightx2v-zhcn.readthedocs.io/zh-cn/latest/getting_started/model_structure.html)
- **Configuration File Instructions**: [Configuration Files](https://github.com/ModelTC/LightX2V/tree/main/configs/distill)
- **Quantized Model Usage**: [Quantization Documentation](https://lightx2v-zhcn.readthedocs.io/zh-cn/latest/method_tutorials/quantization.html)
- **Parameter Offloading**: [Offload Documentation](https://lightx2v-zhcn.readthedocs.io/zh-cn/latest/method_tutorials/offload.html)

---

### Method 2: ComfyUI

Please refer to [workflow](https://huggingface.co/lightx2v/Wan2.2-Distill-Models/blob/main/wan2.2_moe_i2v_scale_fp8_comfyui.json)



## ⚠️ Important Notes

**Other Components**: These models only contain DIT weights. Additional components needed at runtime:
   - T5 text encoder
   - CLIP vision encoder
   - VAE encoder/decoder
   - Tokenizer

   Please refer to [LightX2V Documentation](https://lightx2v-zhcn.readthedocs.io/zh-cn/latest/getting_started/model_structure.html) for instructions on organizing the complete model directory.


## 🤝 Community

- **GitHub Issues**: https://github.com/ModelTC/LightX2V/issues
- **HuggingFace**: https://huggingface.co/lightx2v/Wan2.2-Distill-Models

If you find this project helpful, please give us a ⭐ on [GitHub](https://github.com/ModelTC/LightX2V)

</div>
