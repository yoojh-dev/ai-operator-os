class PlannerCalibrator:

    def adjust_temperature(self, history):

        failure_rate = history.get("failure_rate", 0)

        if failure_rate > 0.3:
            return 0.2  # more deterministic

        if failure_rate < 0.1:
            return 0.7  # more creative

        return 0.4

    def adjust_strategy_bias(self, success_patterns):

        if success_patterns.get("memory_grounded_success") > 0.7:
            return "memory-heavy"

        return "balanced"