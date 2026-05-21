from apps.api.tools.registry import (
    TOOL_REGISTRY,
)


def build_openai_tools():

    return [
        tool["schema"]
        for tool in TOOL_REGISTRY.values()
    ]