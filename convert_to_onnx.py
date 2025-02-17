import torch
import onnx
from transformers import BartForConditionalGeneration, BartTokenizer

MODEL_DIR = "models/text_model/1"
ONNX_PATH = f"{MODEL_DIR}/model.onnx"

# Load model and tokenizer
model = BartForConditionalGeneration.from_pretrained(MODEL_DIR)
tokenizer = BartTokenizer.from_pretrained(MODEL_DIR)

# Example input
input_text = "How does Triton work?"
inputs = tokenizer(input_text, return_tensors="pt")

# Export to ONNX
torch.onnx.export(
    model, 
    (inputs["input_ids"], inputs["attention_mask"]),
    ONNX_PATH,
    export_params=True,
    opset_version=14,
    input_names=["input_ids", "attention_mask"],
    output_names=["output"],
    dynamic_axes={
        "input_ids": {0: "batch_size", 1: "sequence_length"},
        "attention_mask": {0: "batch_size", 1: "sequence_length"},  
        "output": {0: "batch_size"}
    },
)

print(f"✅ Model converted to ONNX: {ONNX_PATH}")
