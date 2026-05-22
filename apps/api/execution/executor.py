class Executor:
    def __init__(
        self,
        node_executor,
    ):
        self.node_executor = node_executor

    async def execute(
        self,
        plan,
    ):
        results = []

        for node in plan.nodes:
            result = await self.node_executor.execute(
                node=node,
            )

            results.append(result)

        return results