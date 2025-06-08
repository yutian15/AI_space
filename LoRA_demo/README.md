# LoRA/QLoRA/SFT/Prompt Tuning 大模型微调与参数合并框架

## 项目简介

本项目为 Hugging Face 上的大型语言模型（LLM）提供一套完整的微调（如 QLoRA、LoRA、SFT、Prompt Tuning 等）与参数合并的解决方案。微调后的模型可进一步转换为 gguf 格式，并通过 Ollama 部署（本项目不包含 gguf 转换与 Ollama 部署代码）。

## 功能流程

1. **模型下载与加载**  
   支持从 Hugging Face 直接下载并加载大模型。

2. **模型微调**  
   支持 QLoRA、LoRA、SFT、Prompt Tuning（如 Prefix Tuning、P-Tuning v2 等）等主流微调方法，适配大模型低资源高效训练。

3. **参数合并**  
   微调完成后，将 LoRA/QLoRA 等 Adapter 权重与原始模型权重合并，生成完整权重文件，便于后续部署。

4. **（可选）模型格式转换与部署**  
   本项目不包含 gguf 格式转换与 Ollama 部署代码，但微调与合并后的模型可直接用于后续流程。

## 代码结构

```
LoRA_demo/
├── README.md
├── requirements.txt
├── configs/
│   ├── train_lora.yaml
│   ├── train_sft.yaml
│   └── train_prompt_tuning.yaml
├── scripts/
│   ├── download_model.py
│   ├── train_lora.py
│   ├── train_sft.py
│   ├── train_prompt_tuning.py
│   ├── merge_lora.py
│   └── utils.py
└── data/
    └── train.jsonl   # 推荐的数据格式，每行为一个 JSON 对象
```

## 数据格式说明

- 训练数据采用 `train.jsonl` 格式，每行为一个 JSON 对象。例如：

  ```jsonl
  {"instruction": "请将下面的英文翻译成中文。", "input": "Hello, world!", "output": "你好，世界！"}
  {"instruction": "写一个 Python 函数实现斐波那契数列。", "input": "", "output": "def fib(n): ..."}
  ```

## 快速开始

1. **安装依赖**

   ```bash
   pip install -r requirements.txt
   ```

2. **下载模型**

   ```bash
   python scripts/download_model.py --model_name <huggingface-model-name> --output_dir <local-model-dir>
   ```

3. **准备数据**  
   将训练数据放入 `data/train.jsonl`，格式如上。

4. **模型微调**

   - LoRA/QLoRA 微调：
     ```bash
     python scripts/train_lora.py --config configs/train_lora.yaml
     ```
   - SFT 微调：
     ```bash
     python scripts/train_sft.py --config configs/train_sft.yaml
     ```
   - Prompt Tuning 微调（如 Prefix Tuning、P-Tuning v2）：
     ```bash
     python scripts/train_prompt_tuning.py --config configs/train_prompt_tuning.yaml
     ```

5. **参数合并**

   ```bash
   python scripts/merge_lora.py --base_model <local-model-dir> --lora_weights <lora-weights-dir> --output_dir <merged-model-dir>
   ```

6. **（可选）模型格式转换与部署**  
   微调并合并后的模型可用于 gguf 格式转换和 Ollama 部署，具体流程请参考相关工具文档。

## 参考

- [Hugging Face Transformers](https://github.com/huggingface/transformers)
- [QLoRA: Efficient Finetuning of Quantized LLMs](https://github.com/artidoro/qlora)
- [Ollama](https://github.com/ollama/ollama)

---

如需根据实际代码进一步完善 README，请补充具体实现细节和参数说明。 