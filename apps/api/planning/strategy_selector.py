class StrategySelector:

    def select(self, query, memories):

        if len(memories) > 5:
            return "memory-heavy"

        if "tool" in query:
            return "tool-first"

        return "default"