from fastapi import FastAPI
from pydantic import BaseModel

from app.ai.llm import generate_response


app = FastAPI(title="DurgeshAI")


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {
        "message": "DKPortfolioAI backend is running"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    response = generate_response(request.message)

    return {
        "response": response
    }