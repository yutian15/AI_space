import argparse
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import os

def main():
    parser = argparse.ArgumentParser(description="Merge LoRA/QLoRA weights into base model.")
    parser.add_argument('--base_model', type=str, required=True, help='Path to base model directory')
    parser.add_argument('--lora_weights', type=str, required=True, help='Path to LoRA weights directory')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory to save merged model')
    args = parser.parse_args()

    print(f"Loading base model from {args.base_model}")
    model = AutoModelForCausalLM.from_pretrained(args.base_model)
    tokenizer = AutoTokenizer.from_pretrained(args.base_model)

    print(f"Loading LoRA weights from {args.lora_weights}")
    model = PeftModel.from_pretrained(model, args.lora_weights)
    model = model.merge_and_unload()

    print(f"Saving merged model to {args.output_dir}")
    model.save_pretrained(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)
    print("Merge complete.")

if __name__ == "__main__":
    main() 