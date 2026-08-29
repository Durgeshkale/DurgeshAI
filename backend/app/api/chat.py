from collections.abc import Generator
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.ai.llm import generate_response, generate_stream
from app.models.chat import ChatRequest, ChatResponse


router = APIRouter(
    prefix="/api",
    tags=["Chat"],
)


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    history = [
        {
            "role": message.role,
            "content": message.content,
        }
        for message in request.history
    ]
    response = generate_response(
        message=request.message,
        history=history
        )

    return ChatResponse(
        response=response
    )

@router.post("/chat/stream")
def chat_stream(request: ChatRequest):
    history = [
        {
            "role": message.role,
            "content": message.content,
        }
        for message in request.history
    ]

    def generate()-> Generator[str, None, None]:
        yield from generate_stream(
            message=request.message,
            history=history,
        )

    return StreamingResponse(
        generate(),
        media_type="text/plain",
    )