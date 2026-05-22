from functools import lru_cache

from apps.api.execution.coordinator.execution_coordinator import (
    ExecutionCoordinator,
)

from apps.api.execution.executor import Executor
from apps.api.execution.node_executor import NodeExecutor

from apps.api.planning.planner import Planner
from apps.api.planning.planner_pipeline import PlannerPipeline

from apps.api.planning.strategies.selector import StrategySelector

from apps.api.tools.executor import ToolExecutor
from apps.api.tools.registry import ToolRegistry

from apps.api.planning.decomposition.engine import (
    DecompositionEngine,
)

from apps.api.memory.retriever import MemoryRetriever


class Container:
    def __init__(self):
        self.tool_registry = ToolRegistry()

        self.tool_executor = ToolExecutor(
            registry=self.tool_registry,
        )

        self.node_executor = NodeExecutor(
            tool_executor=self.tool_executor,
        )

        self.executor = Executor(
            node_executor=self.node_executor,
        )

        self.strategy_selector = StrategySelector()

        self.memory_retriever = MemoryRetriever()

        self.decomposition_engine = DecompositionEngine()

        self.planner_pipeline = PlannerPipeline(
            strategy_selector=self.strategy_selector,
            memory_retriever=self.memory_retriever,
            decomposition_engine=self.decomposition_engine,
        )

        self.planner = Planner(
            pipeline=self.planner_pipeline,
        )

        self.execution_coordinator = ExecutionCoordinator(
            planner=self.planner,
            executor=self.executor,
        )


@lru_cache
def get_container():
    return Container()