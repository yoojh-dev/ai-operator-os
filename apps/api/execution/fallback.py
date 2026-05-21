from apps.api.core.logging import log_event
from apps.api.execution.agent_loop import (
    AgentLoop,
)


class FallbackExhausted(Exception):
    pass


class FallbackExecutor:

    def __init__(self, provider_registry):

        self.provider_registry = provider_registry

    def execute(
        self,
        request_id: str,
        selected_model: str,
        fallbacks: list[str],
        messages: list,
        stream: bool = False,
        tools=None,
    ):

        candidate_models = [
            selected_model,
            *fallbacks,
        ]

        last_error = None

        for model in candidate_models:

            log_event(
                "model_execution_attempt",
                request_id=request_id,
                model=model,
            )

            try:

                provider = self.provider_registry.get_provider(
                    model
                )

                if stream:

                    return provider.stream(
                        model=model,
                        messages=messages,
                        tools=tools,
                    )

                agent = AgentLoop(provider)

                response = agent.run(
                    model=model,
                    messages=messages,
                    tools=tools,
                )

                log_event(
                    "model_execution_success",
                    request_id=request_id,
                    model=model,
                )

                return response, model

            except Exception as e:

                last_error = e

                log_event(
                    "model_execution_failed",
                    request_id=request_id,
                    model=model,
                    error=str(e),
                )

        raise FallbackExhausted(str(last_error))