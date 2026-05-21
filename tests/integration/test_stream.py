from tests.conftest import client


def test_stream_completion():

    with client.stream(
        "POST",
        "/v1/chat/completions",
        json={
            "model": (
                "gemini/gemini-2.5-flash"
            ),
            "stream": True,
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "Tell short story"
                    ),
                }
            ],
        },
    ) as response:

        assert response.status_code == 200

        chunks = []

        for line in (
            response.iter_lines()
        ):

            if not line:
                continue

            chunks.append(line)

        assert len(chunks) > 0

        assert (
            "data: [DONE]"
            in chunks[-1]
        )