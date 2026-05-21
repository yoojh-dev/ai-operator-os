class ToolGuard:

    SAFE_TOOLS = {
        "calculator",
        "weather",
        "search",
    }

    def allow(self, tool_name: str):

        return tool_name in self.SAFE_TOOLS