from fastapi import APIRouter

from app.ai.llm import generate_response
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