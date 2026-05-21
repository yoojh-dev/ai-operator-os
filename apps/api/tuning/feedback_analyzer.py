class FeedbackAnalyzer:

    def analyze(self, traces):

        metrics = {
            "success_rate": 0,
            "avg_latency": 0,
            "tool_error_rate": 0,
        }

        total = len(traces)

        if total == 0:
            return metrics

        metrics["success_rate"] = sum(
            1 for t in traces if t.get("success")
        ) / total

        metrics["avg_latency"] = sum(
            t.get("latency", 0) for t in traces
        ) / total

        metrics["tool_error_rate"] = sum(
            t.get("tool_failures", 0)
        ) / total

        return metrics