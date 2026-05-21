class MemoryTuner:

    def adjust_threshold(self, stats):

        noise_ratio = stats.get("low_score_ratio", 0)

        if noise_ratio > 0.4:
            return 0.7  # stricter filtering

        return 0.3

    def decay_old_memory(self, memory):

        if memory.get("age_days", 0) > 30:
            memory["weight"] *= 0.5

        return memory