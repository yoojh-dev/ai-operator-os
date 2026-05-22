class ResponseContract:
    @classmethod
    def from_raw(
        cls,
        raw,
        model: str,
    ):
        return {
            "model": model,
            "content": raw["choices"][0]["message"]["content"],
            "usage": raw.get("usage", {}),
        }