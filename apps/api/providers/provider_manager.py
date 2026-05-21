from typing import Generator

from apps.api.providers.litellm_provider import (
    call_llm,
    stream_llm,
)


class LiteLLMProvider:

    def call(
        self,
        model: str,
        messages: list,
        tools=None,
    ):
        return call_llm(
            model=model,
            messages=messages,
            tools=tools,
        )

    def stream(
        self,
        model: str,
        messages: list,
        tools=None,
    ) -> Generator:

        yield from stream_llm(
            model=model,
            messages=messages,
            tools=tools,
        )


class ProviderRegistry:

    def __init__(self):

        self.default_provider = LiteLLMProvider()

    def get_provider(self, model: str):

        if model.startswith("gemini"):
            return self.default_provider

        if model.startswith("openai"):
            return self.default_provider

        if model.startswith("openrouter"):
            return self.default_provider

        return self.default_provider