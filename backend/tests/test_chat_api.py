from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_chat():
    response = client.post(
        "/api/chat",
        json={
            "message": "What programming languages does Durgesh know?"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "response" in data
    assert isinstance(data["response"], str)


if __name__ == "__main__":
    test_chat()

    print("Chat API test successful!")