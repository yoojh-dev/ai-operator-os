class LiteLLMTransport:
    async def chat(
        self,
        model: str,
        messages: list,
        stream: bool = False,
    ):
        return {
            "model": model,
            "choices": [
                {
                    "message": {
                        "content": "hello world",
                    }
                }
            ],
            "usage": {
                "total_tokens": 42,
            },
        }