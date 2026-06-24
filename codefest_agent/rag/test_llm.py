# test_llm.py

from rag.llm import llm

response = llm.invoke(
    "Give me the five best dental clinic in thanjavur"
)

print(response.content)