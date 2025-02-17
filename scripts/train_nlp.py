import torch
from transformers import BartForConditionalGeneration, BartTokenizer

MODEL_NAME = "facebook/bart-large"

# Load pre-trained BART model and tokenizer
tokenizer = BartTokenizer.from_pretrained(MODEL_NAME)
model = BartForConditionalGeneration.from_pretrained(MODEL_NAME)

# Fine-tuning setup (Dummy example)
# Normally, you'd train on a dataset, but we'll just save it for inference

input_text = "Triton Inference Server allows serving multiple AI models efficiently."
inputs = tokenizer(input_text, return_tensors="pt")

# Run inference
outputs = model.generate(**inputs, early_stopping=True, num_beams=4, no_repeat_ngram_size=3, forced_bos_token_id=0)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("Generated Text:", generated_text)

# Save the model for conversion
model.save_pretrained("models/text_model/1")
tokenizer.save_pretrained("models/text_model/1")
