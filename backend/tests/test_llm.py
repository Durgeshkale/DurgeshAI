from app.ai.llm import generate_response


questions = [
    "Introduce Durgesh",
    "Does Durgesh know Python?",
    "Write an SQL query to find the top 10 employees by salary.",
    "Explain quantum mechanics",
]


for question in questions:
    print("\nQuestion:")
    print(question)

    response = generate_response(question)

    print("\nAnswer:")
    print(response)

    print("\n" + " " * 60)