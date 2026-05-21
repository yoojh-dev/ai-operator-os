import json
import time
import uuid


def stream_response(
    stream,
    model: str,
):

    chunk_id = (
        f"chatcmpl-{uuid.uuid4().hex}"
    )

    created = int(time.time())

    for chunk in stream:

        delta = chunk.delta

        payload = {
            "id": chunk_id,
            "object": (
                "chat.completion.chunk"
            ),
            "created": created,
            "model": model,
            "choices": [
                {
                    "index": 0,
                    "delta": {
                        "role": (
                            delta.role
                        ),
                        "content": (
                            delta.content
                        ),
                    },
                    "finish_reason": (
                        chunk.finish_reason
                    ),
                }
            ],
        }

        yield (
            "data: "
            f"{json.dumps(payload)}\n\n"
        )

    yield "data: [DONE]\n\n"