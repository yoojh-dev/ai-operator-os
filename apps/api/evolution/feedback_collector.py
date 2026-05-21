class FeedbackCollector:

    def collect(self, trace):

        return {
            "success": trace.get("success"),
            "latency": trace.get("latency"),
            "tool_failures": trace.get("tool_failures"),
            "user_satisfaction": trace.get("rating", 0),
        }