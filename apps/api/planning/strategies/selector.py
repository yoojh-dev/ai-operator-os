class StrategySelector:
    async def select(
        self,
        goal: str,
    ) -> str:
        goal = goal.lower()

        if "research" in goal:
            return "research"

        if "analyze" in goal:
            return "analysis"

        return "default"