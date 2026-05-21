from apps.api.tools.calculator import (
    CalculatorTool,
)


class ToolRegistry:

    def __init__(self):

        self.tools = {}

        self.register(
            CalculatorTool()
        )

    def register(self, tool):

        self.tools[tool.name] = tool

    def get(self, tool_name):

        return self.tools.get(tool_name)

    def list_tools(self):

        return list(
            self.tools.values()
        )

    def openai_schemas(self):

        return [
            tool.openai_schema()
            for tool in (
                self.tools.values()
            )
        ]