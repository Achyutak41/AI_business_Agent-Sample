# test_retriever.py

from rag.retriever import retriever

docs = retriever.invoke(
    "best dental clinic"
)

print(docs)