from embedding import load_embeddings, search
from generate import format_prompt, generate

# Load the dataset and add FAISS index
dataset = load_embeddings()
data = dataset["train"]
data = data.add_faiss_index("embeddings")

# Function for the chatbot
def rag_chatbot(prompt: str, k: int = 2):
    scores, retrieved_documents = search(prompt, data, k)
    formatted_prompt = format_prompt(prompt, retrieved_documents, k)
    return generate(formatted_prompt)

# Example usage
response = rag_chatbot("Explain to me the current state of Indonesia's politics. As well as who is the next president?", k=2)
print(response)
