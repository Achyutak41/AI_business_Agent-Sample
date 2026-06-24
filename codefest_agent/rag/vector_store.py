from langchain_chroma import Chroma
from rag.embeddings import embeddings

vector_store = Chroma(
    collection_name="businesses",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)