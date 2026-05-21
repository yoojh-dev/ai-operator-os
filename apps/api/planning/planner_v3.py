from typing import Any, Dict, List
import uuid


class PlannerV3:

    def __init__(self, memory=None, strategy=None):
        self.memory = memory
        self.strategy = strategy

    def plan(self, goal: str, context: Dict[str, Any]) -> List[Dict[str, Any]]:

        # 1. simple strategy selection (internal)
        strategy = self._select_strategy(goal, context)

        # 2. optional memory injection
        memory_context = self._retrieve_memory(goal)

        # 3. build execution plan
        plan = []

        steps = self._decompose(goal, strategy)

        for step in steps:

            plan.append({
                "node_id": str(uuid.uuid4()),
                "tool_contract": {
                    "name": step["tool"],
                    "args": step.get("args", {}),
                    "trace_id": context.get("trace_id"),
                    "node_id": step.get("node_id", str(uuid.uuid4())),
                },
                "meta": {
                    "strategy": strategy,
                    "memory_hint": memory_context,
                }
            })

        return plan

    def _select_strategy(self, goal: str, context: Dict[str, Any]) -> str:

        # simple deterministic strategy selection
        if "analyze" in goal:
            return "analysis"
        if "code" in goal:
            return "code"
        return "default"

    def _retrieve_memory(self, goal: str):

        if not self.memory:
            return None

        try:
            return self.memory.search(goal)
        except Exception:
            return None

    def _decompose(self, goal: str, strategy: str) -> List[Dict[str, Any]]:

        # minimal decomposition logic (replace later with LLM if needed)

        if strategy == "code":
            return [
                {"tool": "calculator", "args": {"input": goal}}
            ]

        if strategy == "analysis":
            return [
                {"tool": "weather", "args": {"query": goal}}
            ]

        return [
            {"tool": "calculator", "args": {"input": goal}}
        ]