class LegacyPlannerAdapter:
    def __init__(
        self,
        legacy_planner,
    ):
        self.legacy_planner = legacy_planner

    async def create_plan(
        self,
        goal: str,
    ):
        return await self.legacy_planner.plan(
            goal,
        )