class ToolExecutor:
    def __init__(
        self,
        registry,
    ):
        self.registry = registry

    async def execute(
        self,
        tool_name: str,
        arguments: dict,
    ):
        tool = self.registry.get(
            tool_name,
        )

        return await tool.execute(
            arguments,
        )