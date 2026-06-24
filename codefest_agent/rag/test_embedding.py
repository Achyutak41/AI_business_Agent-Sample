# test_embedding.py

from rag.embeddings import embeddings

result = embeddings.embed_query(
    "hello world"
)

print(len(result))