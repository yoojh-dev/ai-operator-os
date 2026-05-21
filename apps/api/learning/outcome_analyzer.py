class OutcomeAnalyzer:

    def analyze(self, execution_trace):

        success = execution_trace.get("success", False)

        latency = execution_trace.get("latency", 0)

        tool_failures = execution_trace.get("tool_failures", 0)

        score = 0

        if success:
            score += 1
        else:
            score -= 1

        score -= tool_failures * 0.2

        if latency > 3:
            score -= 0.3

        return {
            "score": score,
            "success": success,
        }