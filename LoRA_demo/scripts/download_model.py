import argparse
from transformers import AutoModelForCausalLM, AutoTokenizer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download Hugging Face model and tokenizer.")
    parser.add_argument('--model_name', type=str, required=True, help='Hugging Face model name')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory to save model')
    args = parser.parse_args()

    print(f"Downloading model {args.model_name} to {args.output_dir} ...")
    model = AutoModelForCausalLM.from_pretrained(args.model_name)
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    model.save_pretrained(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)
    print("Download complete.") 