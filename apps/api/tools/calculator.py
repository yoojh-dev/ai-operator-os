from apps.api.tools.base import BaseTool


class CalculatorTool(BaseTool):

    name = "calculator"

    description = "Simple calculator"

    def run(self, args: dict):

        a = args.get("a", 0)
        b = args.get("b", 0)
        operation = args.get("operation", "add")

        if operation == "add":
            return a + b

        if operation == "subtract":
            return a - b

        if operation == "multiply":
            return a * b

        if operation == "divide":

            if b == 0:
                raise ValueError(
                    "division by zero"
                )

            return a / b

        raise ValueError(
            f"Unknown operation: {operation}"
        )

    def openai_schema(self):

        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {
                            "type": "number"
                        },
                        "b": {
                            "type": "number"
                        },
                        "operation": {
                            "type": "string",
                            "enum": [
                                "add",
                                "subtract",
                                "multiply",
                                "divide"
                            ]
                        }
                    },
                    "required": [
                        "a",
                        "b",
                        "operation"
                    ]
                }
            }
        }