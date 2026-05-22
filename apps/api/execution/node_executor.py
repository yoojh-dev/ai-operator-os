class NodeExecutor:
    def __init__(
        self,
        tool_executor,
    ):
        self.tool_executor = tool_executor

    async def execute(
        self,
        node,
    ):
        if node.type == "tool":
            return await self.tool_executor.execute(
                tool_name=node.tool,
                arguments=node.arguments,
            )

        raise ValueError(
            f"Unsupported node type: {node.type}"
        )