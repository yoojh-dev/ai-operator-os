class PolicyOptimizer:

    def optimize(self, analysis):

        policy_update = {}

        if len(analysis["high_latency_paths"]) > 10:
            policy_update["max_concurrency"] = 2

        if len(analysis["tool_failure_clusters"]) > 5:
            policy_update["tool_retry_limit"] = 1

        return policy_update