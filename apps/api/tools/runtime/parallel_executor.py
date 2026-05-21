from apps.api.tools.runtime.scheduler import (
    ToolScheduler,
)

from apps.api.tools.runtime.executor import (
    ToolExecutor,
)

from apps.api.tools.runtime.tool_contract import (
    ToolContract,
)


class ParallelToolExecutor:

    def __init__(self, registry):

        self.executor = (
            ToolExecutor(
                registry
            )
        )

        self.scheduler = (
            ToolScheduler(
                self.executor
            )
        )

    async def execute(
        self,
        tool_calls,
        trace_id="runtime-trace",
    ):

        contracts = []

        for tc in tool_calls:

            contracts.append(
                ToolContract(
                    name=tc.function.name,
                    args=tc.function.arguments,
                    trace_id=trace_id,
                    node_id=tc.id,
                )
            )

        results = (
            await self.scheduler
            .execute_batch(
                contracts
            )
        )

        return results