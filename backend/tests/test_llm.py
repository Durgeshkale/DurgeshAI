from app.ai.llm import generate_response


response = generate_response(
    "Say hello and tell me that the LLM connection is working."
)


print("LLM response:")
print(response)