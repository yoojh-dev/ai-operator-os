from apps.api.planning.agents.research_planner import ResearchPlanner
from apps.api.planning.agents.execution_planner import ExecutionPlanner
from apps.api.planning.agents.tool_planner import ToolPlanner


class MultiPlannerCoordinator:

    def __init__(self, provider):

        self.research = ResearchPlanner(provider)
        self.execution = ExecutionPlanner(provider)
        self.tool = ToolPlanner(provider)

    def create_plan(self, model: str, messages: list):

        research = self.research.create_plan(model, messages)
        execution = self.execution.create_plan(model, messages)
        tool = self.tool.create_plan(model, messages)

        return {
            "research": self._wrap(research),
            "execution": self._wrap(execution),
            "tool": self._wrap(tool),
        }

    def _wrap(self, result):

        return [{"action": result, "input": {}}]