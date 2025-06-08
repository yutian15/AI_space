import argparse
import yaml
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model, TaskType
import torch


def load_config(config_path):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser(description="LoRA/QLoRA Finetuning Script")
    parser.add_argument('--config', type=str, required=True, help='Path to config yaml')
    args = parser.parse_args()
    config = load_config(args.config)

    model = AutoModelForCausalLM.from_pretrained(config['model_name_or_path'])
    tokenizer = AutoTokenizer.from_pretrained(config['model_name_or_path'])

    dataset = load_dataset('json', data_files=config['dataset_path'])['train']

    lora_config = LoraConfig(
        r=config.get('lora_r', 8),
        lora_alpha=config.get('lora_alpha', 16),
        lora_dropout=config.get('lora_dropout', 0.05),
        task_type=TaskType.CAUSAL_LM
    )
    model = get_peft_model(model, lora_config)

    training_args = TrainingArguments(
        output_dir=config['output_dir'],
        per_device_train_batch_size=config['per_device_train_batch_size'],
        num_train_epochs=config['epochs'],
        learning_rate=config['learning_rate'],
        fp16=config.get('fp16', False),
        logging_steps=10,
        save_steps=1000,
        save_total_limit=2,
        report_to=[]
    )

    def preprocess(example):
        prompt = example.get('instruction', '')
        if example.get('input', ''):
            prompt += '\n' + example['input']
        inputs = tokenizer(prompt, truncation=True, max_length=config['max_seq_length'])
        labels = tokenizer(example['output'], truncation=True, max_length=config['max_seq_length'])
        inputs['labels'] = labels['input_ids']
        return inputs

    tokenized_dataset = dataset.map(preprocess, remove_columns=dataset.column_names)

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        tokenizer=tokenizer
    )
    trainer.train()
    model.save_pretrained(config['output_dir'])
    tokenizer.save_pretrained(config['output_dir'])

if __name__ == "__main__":
    main() 