from rag.rag_chain import ask, test_ask ,check_ask

while True:
    question = input("\nAsk: ")

    if question.lower() == "exit":
        break

    answer = check_ask(question)

    print("\nAnswer:")
    print(answer)