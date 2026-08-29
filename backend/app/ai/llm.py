import os
from pathlib import Path
from collections.abc import Generator

from dotenv import load_dotenv
from groq import Groq

from app.ai.context import get_candidate_context
from app.ai.prompts import SYSTEM_PROMPT


load_dotenv(Path(__file__).resolve().parents[2] / ".env")


my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set")


# Register Groq client
client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"


def build_messages(
    message: str,
    history: list[dict[str, str]] | None = None,
) -> list[dict[str, str]]:

    candidate_context = get_candidate_context()

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "system",
            "content": (
                "Here is the verified candidate information. "
                "Use this information as the only source of truth:\n\n"
                f"{candidate_context}"
            ),
        },
    ]

    if history:
        messages.extend(history)

    messages.append(
        {
            "role": "user",
            "content": message,
        }
    )

    return messages


def generate_response(
    message: str,
    history: list[dict[str, str]] | None = None,
) -> str:

    messages = build_messages(message, history)

    response = client.chat.completions.create(
        model=model,
        temperature=0.1,
        messages=messages,
    )

    return response.choices[0].message.content or ""


def generate_stream(
    message: str,
    history: list[dict[str, str]] | None = None,
) -> Generator[str, None, None]:

    messages = build_messages(message, history)

    stream = client.chat.completions.create(
        model=model,
        temperature=0.1,
        messages=messages,
        stream=True,
    )

    for chunk in stream:
        content = chunk.choices[0].delta.content

        if content:
            yield content