class ExecutionCoordinator:
    def __init__(
        self,
        planner,
        executor,
    ):
        self.planner = planner
        self.executor = executor

    async def run(
        self,
        goal: str,
    ):
        plan = await self.planner.create_plan(
            goal=goal,
        )

        return await self.executor.execute(
            plan=plan,
        )