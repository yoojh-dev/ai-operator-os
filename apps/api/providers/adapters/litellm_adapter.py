from apps.api.providers.transports.litellm_transport import (
    LiteLLMTransport,
)

from apps.api.providers.contracts.response import (
    ResponseContract,
)

from apps.api.providers.contracts.stream import (
    StreamContract,
)


class LiteLLMAdapter:
    def __init__(self):
        self.transport = LiteLLMTransport()

    async def chat(
        self,
        model: str,
        messages: list,
        stream: bool = False,
    ):
        raw = await self.transport.chat(
            model=model,
            messages=messages,
            stream=stream,
        )

        if stream:
            return StreamContract.from_raw(
                raw,
                model,
            )

        return ResponseContract.from_raw(
            raw,
            model,
        )