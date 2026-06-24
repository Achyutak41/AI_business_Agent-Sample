from rag.llm import llm
from rag.retriever import retriever

def ask(question):

    docs = retriever.invoke(question)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content
def check_ask(question):

    docs = retriever.invoke(question)

    if "highest trust score" in question.lower():

        best_score = -1
        best_name = ""

        for doc in docs:

            text = doc.page_content

            name = ""
            score = 0

            for line in text.split("\n"):

                if "Name:" in line:
                    name = line.replace(
                        "Name:",
                        ""
                    ).strip()

                if "Trust Score:" in line:
                    score = int(
                        line.replace(
                            "Trust Score:",
                            ""
                        ).strip()
                    )

            if score > best_score:
                best_score = score
                best_name = name

        return (
            f"{best_name} "
            f"has the highest trust score "
            f"of {best_score}/10."
        )

    # normal LLM flow
def test_ask(question):
    print("QUESTION:", question)

    docs = retriever.invoke(question)

    print("DOCS FOUND:", len(docs))

    for d in docs:
        print(d.page_content[:200])

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    print("CONTEXT LENGTH:", len(context))

    response = llm.invoke(
        f"""
        Context:
        {context}

        Question:
        {question}
        """
    )

    return response.content