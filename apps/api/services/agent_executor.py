from apps.api.execution.coordinator.execution_coordinator import (
    ExecutionCoordinator,
)


class AgentExecutor:
    def __init__(self, coordinator: ExecutionCoordinator):
        self.coordinator = coordinator

    async def execute(self, goal: str):
        return await self.coordinator.run(goal)