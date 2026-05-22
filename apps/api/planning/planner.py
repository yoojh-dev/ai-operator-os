from apps.api.planning.planner_context import PlannerContext


class Planner:
    def __init__(
        self,
        pipeline,
    ):
        self.pipeline = pipeline

    async def create_plan(
        self,
        goal: str,
    ):
        context = PlannerContext(
            goal=goal,
        )

        return await self.pipeline.run(
            context,
        )