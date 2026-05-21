class PlannerV2:

    def __init__(self, memory_planner, selector, optimizer):

        self.memory_planner = memory_planner
        self.selector = selector
        self.optimizer = optimizer

    def plan(self, query):

        memories = self.memory_planner.retriever.retrieve_context(query)

        strategy = self.selector.select(query, memories)

        raw_plan = self.memory_planner.plan(query)

        optimized = self.optimizer.optimize(raw_plan)

        return {
            "strategy": strategy,
            "plan": optimized,
        }