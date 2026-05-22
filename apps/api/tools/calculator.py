class CalculatorTool:
    async def execute(
        self,
        arguments: dict,
    ):
        expression = arguments["expression"]

        return {
            "result": eval(expression),
        }