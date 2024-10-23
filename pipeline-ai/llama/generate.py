from model import tokenizer, model, terminators
from config import SYS_PROMPT

# Function to format prompt
def format_prompt(prompt, retrieved_documents, k):
    PROMPT = f"Question:{prompt}\nContext:"
    for idx in range(k):
        PROMPT += f"{retrieved_documents['text'][idx]}\n"
    return PROMPT

# Function to generate text from the model
def generate(formatted_prompt):
    formatted_prompt = formatted_prompt[:2000]
    messages = [{"role": "system", "content": SYS_PROMPT}, {"role": "user", "content": formatted_prompt}]
    
    input_ids = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(model.device)

    outputs = model.generate(
        input_ids,
        max_new_tokens=1024,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.6,
        top_p=0.9,
    )

    response = outputs[0][input_ids.shape[-1]:]
    return tokenizer.decode(response, skip_special_tokens=True)
