class ToolScheduler:

    def __init__(self, executor):

        self.executor = executor

    async def execute_batch(
        self,
        contracts,
    ):

        results = {}

        for contract in contracts:

            result = (
                self.executor
                .execute(contract)
            )

            results[
                contract.node_id
            ] = result

        return results