from apps.api.schemas.llm_contract import LLMContract


class StreamContractAdapter:

    @staticmethod
    def from_chunk(chunk, model: str) -> LLMContract:

        if chunk is None:
            return LLMContract(
                content="",
                delta=None,
                model=model,
                stream=True,
                usage={},
                raw=None,
            )

        if isinstance(chunk, dict):

            delta = chunk.get("delta")

            if delta is None:
                delta = chunk.get("content")

            return LLMContract(
                content="",
                delta=str(delta),
                model=model,
                stream=True,
                usage=chunk.get("usage", {}),
                raw=chunk,
            )

        return LLMContract(
            content="",
            delta=str(chunk),
            model=model,
            stream=True,
            usage={},
            raw=chunk,
        )