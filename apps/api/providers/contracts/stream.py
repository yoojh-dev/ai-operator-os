class StreamContract:
    @classmethod
    def from_raw(
        cls,
        raw,
        model: str,
    ):
        return {
            "model": model,
            "delta": raw,
        }