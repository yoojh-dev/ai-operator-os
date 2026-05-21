from apps.api.providers.response_normalizer import normalize_response
from apps.api.providers.stream_normalizer import normalize_stream_chunk

from apps.api.providers.contract_adapter import ContractAdapter
from apps.api.providers.stream_contract_adapter import StreamContractAdapter


class ProviderRegistry:

    def __init__(self):
        self.providers = {}

    def get_provider(self, model: str):

        return LiteLLMProvider(model)


class LiteLLMProvider:

    def __init__(self, model: str):
        self.model = model

    def chat(self, messages, stream: bool = False):

        raw = self._call_litellm(messages, stream)

        # -------------------------
        # STREAM PATH
        # -------------------------
        if stream:
            return StreamContractAdapter.from_chunk(raw, self.model)

        # -------------------------
        # NORMAL PATH
        # -------------------------
        return ContractAdapter.from_response(raw, self.model)

    def _call_litellm(self, messages, stream: bool):

        # 실제 LiteLLM 호출 자리 (mock 유지)
        return {
            "model": self.model,
            "choices": [
                {
                    "message": "hello world"
                }
            ],
            "usage": {
                "total_tokens": 42
            },
            "delta": "hello"
        }