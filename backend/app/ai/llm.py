import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error")

#register as client
client = Groq(api_key = my_api_key)

model = "openai/gpt-oss-120b"

from app.ai.context import get_candidate_context
from app.ai.prompts import SYSTEM_PROMPT

def generate_response(
        message: str,
        history: list[dict[str, str]] | None = None
) -> str:

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
        }
    ]

    if history:
        messages.extend(history)

    messages.append(
        {
            "role": "user",
            "content": message,
        }
    )

    response = client.chat.completions.create(
        model=model,
        temperature=0.1,
        messages=messages,
    )

    return response.choices[0].message.content