class BehaviorAnalyzer:

    def analyze(self, feedbacks):

        return {
            "high_latency_paths": [
                f for f in feedbacks
                if f["latency"] > 2.0
            ],
            "tool_failure_clusters": [
                f for f in feedbacks
                if f["tool_failures"] > 0
            ],
        }