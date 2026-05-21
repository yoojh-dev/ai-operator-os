# apps/api/execution/runtime/node_executor.py

class NodeExecutor:

    def __init__(self, provider, tool_registry):

        self.provider = provider
        self.tool_registry = tool_registry

    async def execute(self, node, messages, tools=None):

        # TOOL EXECUTION
        if node.tool:

            tool = self.tool_registry.get(node.tool)

            if not tool:
                raise Exception(f"Unknown tool: {node.tool}")

            return tool.execute(**(node.input or {}))

        # LLM EXECUTION
        response = self.provider.call(
            model=node.model or "default",
            messages=messages + [
                {
                    "role": "user",
                    "content": node.action,
                }
            ],
            tools=tools,
        )

        return response.message.content