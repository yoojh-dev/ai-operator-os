class ReasoningStrategy:

    def select(self, query, top_memories):

        if len(top_memories) == 0:
            return "zero-shot"

        if top_memories[0]["weight"] > 0.8:
            return "memory-grounded"

        if len(top_memories) > 5:
            return "multi-context"

        return "balanced"