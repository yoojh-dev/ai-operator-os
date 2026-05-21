class PlannerMutator:

    def __init__(self, strategy_optimizer, pattern_memory):

        self.strategy_optimizer = strategy_optimizer
        self.pattern_memory = pattern_memory

    def mutate(self, planner_config):

        strategy = self.strategy_optimizer.optimize(
            self.pattern_memory.patterns
        )

        planner_config["strategy"] = strategy

        return planner_config