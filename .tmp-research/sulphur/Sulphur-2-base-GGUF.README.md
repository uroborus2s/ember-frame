---
base_model: SulphurAI/Sulphur-2-base
library_name: gguf
pipeline_tag: text-to-video
tags:
- gguf
- quantized
---

# Sulphur-2-Base (Dev) - GGUF

This repository contains GGUF format model files for [SulphurAI's Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base). 

## Model Details
* **Original Model:** [SulphurAI/Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)
* **Format:** GGUF
* **Architecture:** ltxv
* **Model Size:** 21B parameters

## Available Quantizations

The following quantization tiers are provided to accommodate different hardware capabilities and VRAM constraints. 

| Filename | Quantization Type | Size | Recommended Use |
|:---|:---|:---|:---|
| `sulphur_dev_bf16.gguf` | BF16 (16-bit) | 42.0 GB | Unquantized baseline. Maximum quality and accuracy. Requires massive VRAM. |
| `sulphur_dev-Q8_0.gguf` | Q8_0 (8-bit) | 22.8 GB | Extremely high quality, near unquantized performance. |
| `sulphur_dev-Q6_K.gguf` | Q6_K (6-bit) | 17.8 GB | Very high quality, minimal precision loss. |
| `sulphur_dev-Q5_K_M.gguf` | Q5_K_M (5-bit) | 16.1 GB | Excellent balance of quality and performance. |
| `sulphur_dev-Q5_K_S.gguf` | Q5_K_S (5-bit) | 15.0 GB | Slightly smaller 5-bit variant for strict memory limits. |
| `sulphur_dev-Q4_K_M.gguf` | Q4_K_M (4-bit) | 14.3 GB | Recommended standard. Fast inference with very low quality degradation. |
| `sulphur_dev-Q4_K_S.gguf` | Q4_K_S (4-bit) | 13.2 GB | Smaller 4-bit variant, slightly lower quality than K_M. |
| `sulphur_dev-Q4_0.gguf` | Q4_0 (4-bit) | 13.0 GB | Legacy 4-bit quant. Very fast inference but higher perplexity than K-quants. |
| `sulphur_dev-Q3_K_M.gguf` | Q3_K_M (3-bit) | 11.1 GB | High compression. Best for constrained environments with limited RAM/VRAM. |
| `sulphur_dev-Q3_K_S.gguf` | Q3_K_S (3-bit) | 10.3 GB | Maximum compression. Lowest footprint but highest quality loss. |