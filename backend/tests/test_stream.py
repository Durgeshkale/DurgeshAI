from app.ai.llm import generate_stream


message = "Tell me briefly about Durgesh Kale."


print("Streaming response:")
print(" " * 60)


for chunk in generate_stream(message):
    print(chunk, end="", flush=True)


print()
print(" " * 60)
print("Streaming completed!")