from tests.conftest import client


def test_chat_completion():

    response = client.post(
        "/v1/chat/completions",
        json={
            "model": (
                "gemini/gemini-2.5-flash"
            ),
            "messages": [
                {
                    "role": "user",
                    "content": "hello",
                }
            ],
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "choices" in data

    assert (
        data["choices"][0]
        ["message"]
        ["content"]
    )