from tests.conftest import client


def test_tool_calling():

    response = client.post(
        "/v1/chat/completions",
        json={
            "model": (
                "gemini/gemini-2.5-flash"
            ),
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "What is 25 * 12?"
                    ),
                }
            ],
            "tools": [
                {
                    "type": "function",
                    "function": {
                        "name": (
                            "calculator"
                        ),
                        "description": (
                            "Evaluate math expressions"
                        ),
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "expression": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "expression"
                            ],
                        },
                    },
                }
            ],
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "choices" in data