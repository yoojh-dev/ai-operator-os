from apps.api.providers.model_registry import (
    MODEL_REGISTRY,
)


class ModelRouter:

    def route(
        self,
        messages: list,
        user_model: str | None = None,
    ):

        # user-selected model
        if user_model:

            model_config = (
                MODEL_REGISTRY.get(
                    user_model
                )
            )

            return {
                "selected_model": (
                    user_model
                ),
                "fallbacks": (
                    model_config.get(
                        "fallbacks",
                        [],
                    )
                ),
                "reason": (
                    "user_selected"
                ),
            }

        # auto routing
        last_message = (
            messages[-1]["content"]
            if messages
            else ""
        )

        # simple heuristic
        if len(last_message) < 200:

            selected_model = (
                "gemini/gemini-2.5-flash"
            )

        else:

            selected_model = (
                "openrouter/meta-llama/llama-3.3-70b-instruct"
            )

        model_config = (
            MODEL_REGISTRY.get(
                selected_model
            )
        )

        return {
            "selected_model": (
                selected_model
            ),
            "fallbacks": (
                model_config.get(
                    "fallbacks",
                    [],
                )
            ),
            "reason": (
                "heuristic_router"
            ),
        }