from datasets import load_dataset
from sentence_transformers import SentenceTransformer
import pickle

# Load sentence transformer model
ST = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")

# Function to load embeddings from a pickle file
def load_embeddings(file_path='variables/dataset_embedding.pickle'):
    with open(file_path, 'rb') as file:
        dataset = pickle.load(file)
    return dataset

# Function to search using FAISS index
def search(query: str, data, k: int = 3):
    embedded_query = ST.encode(query)
    scores, retrieved_examples = data.get_nearest_examples(
        "embeddings", embedded_query, k=k
    )
    return scores, retrieved_examples
