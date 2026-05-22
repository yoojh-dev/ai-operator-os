class DecompositionEngine:
    async def decompose(
        self,
        goal: str,
        strategy: str,
    ):
        if strategy == "analysis":
            return [
                {
                    "tool": "weather",
                    "arguments": {
                        "query": goal,
                    },
                }
            ]

        return [
            {
                "tool": "calculator",
                "arguments": {
                    "expression": "1 + 1",
                },
            }
        ]