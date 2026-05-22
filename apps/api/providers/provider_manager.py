from apps.api.providers.routing.provider_router import (
    ProviderRouter,
)


class ProviderManager:
    def __init__(self):
        self.router = ProviderRouter()

    async def chat(
        self,
        model: str,
        messages: list,
        stream: bool = False,
    ):
        adapter = self.router.route(
            model,
        )

        return await adapter.chat(
            model=model,
            messages=messages,
            stream=stream,
        )