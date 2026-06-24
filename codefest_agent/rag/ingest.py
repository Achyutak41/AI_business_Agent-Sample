from langchain_core.documents import Document
from rag.vector_store import vector_store

def store_businesses(businesses):

    docs = []

    for b in businesses:

        docs.append(
            Document(
                page_content=f"""
                Name: {b['business_name']}
                Phone: {b['phone']}
                Trust Score: {b['trust_score']}
                """
            )
        )

    vector_store.add_documents(docs)