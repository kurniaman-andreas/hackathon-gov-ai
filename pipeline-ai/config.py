import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

# BitsAndBytesConfig for model
from transformers import BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True, 
    bnb_4bit_use_double_quant=True, 
    bnb_4bit_quant_type="nf4", 
    bnb_4bit_compute_dtype=torch.bfloat16
)

# Model ID and system prompt
model_id = "meta-llama/Llama-3.2-1B-Instruct"
SYS_PROMPT = """You take the role of a pirate. Speak like a pirate."""
