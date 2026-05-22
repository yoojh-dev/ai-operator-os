from apps.api.providers.adapters.litellm_adapter import (
    LiteLLMAdapter,
)


class ProviderRouter:
    def __init__(self):
        self.default_adapter = LiteLLMAdapter()

    def route(
        self,
        model: str,
    ):
        return self.default_adapter