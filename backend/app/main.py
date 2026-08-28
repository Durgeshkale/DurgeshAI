from fastapi import FastAPI

from app.api.chat import router as chat_router


app = FastAPI(
    title="DurgeshAI",
    description="AI-powered portfolio assistant for Durgesh Kale.",
    version="1.0.0",
)

app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "message": "DurgeshAI backend is running"
    }