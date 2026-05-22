from types import SimpleNamespace


class PlannerPipeline:
    def __init__(
        self,
        strategy_selector,
        memory_retriever,
        decomposition_engine,
    ):
        self.strategy_selector = strategy_selector

        self.memory_retriever = memory_retriever

        self.decomposition_engine = decomposition_engine

    async def run(
        self,
        context,
    ):
        context.strategy = await self.strategy_selector.select(
            context.goal,
        )

        context.memories = await self.memory_retriever.retrieve(
            context.goal,
        )

        nodes = await self.decomposition_engine.decompose(
            goal=context.goal,
            strategy=context.strategy,
        )

        return SimpleNamespace(
            nodes=[
                SimpleNamespace(
                    type="tool",
                    tool=node["tool"],
                    arguments=node["arguments"],
                )
                for node in nodes
            ]
        )