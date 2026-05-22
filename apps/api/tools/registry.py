from apps.api.tools.calculator import CalculatorTool


class ToolRegistry:
    def __init__(self):
        self.tools = {
            "calculator": CalculatorTool(),
        }

    def get(
        self,
        name: str,
    ):
        tool = self.tools.get(name)

        if tool is None:
            raise ValueError(
                f"Tool not found: {name}"
            )

        return tool