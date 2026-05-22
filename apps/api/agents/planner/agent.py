from types import SimpleNamespace


class PlannerAgent:
    async def plan(
        self,
        context,
    ):
        return SimpleNamespace(
            nodes=[
                SimpleNamespace(
                    type="tool",
                    tool="calculator",
                    arguments={
                        "expression": "1 + 1",
                    },
                )
            ]
        )