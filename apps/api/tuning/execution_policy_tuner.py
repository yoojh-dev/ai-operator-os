class ExecutionPolicyTuner:

    def fallback_policy(self, error_stats):

        if error_stats.get("timeout") > 0.2:
            return "reduce_concurrency"

        if error_stats.get("tool_failures") > 0.3:
            return "simplify_tool_calls"

        return "default"