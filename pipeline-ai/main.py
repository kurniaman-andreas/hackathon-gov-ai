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

# from huggingface_hub import login, HfApi
# from embedding import load_embeddings, search
# from generate import format_prompt, generate

# def main():
#     # Ganti dengan token Hugging Face kamu
#     token = "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"

#     # Login menggunakan token
#     try:
#         login(token)
#         print("Login ke Hugging Face berhasil!")

#         # Cek apakah token memiliki akses ke model
#         api = HfApi()
#         api.model_info("meta-llama/Llama-3.2-1B-Instruct")  # Cek akses ke model
#         print("Akses model berhasil.")
#     except Exception as e:
#         print(f"Terjadi kesalahan: {str(e)}")
#         return

#     # Load the dataset and add FAISS index
#     dataset = load_embeddings()
#     data = dataset["train"]
#     data = data.add_faiss_index("embeddings")

#     # Function for the chatbot
#     def rag_chatbot(prompt: str, k: int = 2):
#         scores, retrieved_documents = search(prompt, data, k)
#         formatted_prompt = format_prompt(prompt, retrieved_documents, k)
#         return generate(formatted_prompt)

#     # Example usage
#     response = rag_chatbot("Explain to me the current state of Indonesia's politics. As well as who is the next president?", k=2)
#     print(response)

# if __name__ == "__main__":
#     main()
