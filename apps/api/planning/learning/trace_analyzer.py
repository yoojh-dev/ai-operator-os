class TraceAnalyzer:

    def analyze(self, trace):

        steps = trace.steps

        success = all(
            s["status"] == "success"
            for s in steps
        )

        tool_sequence = [
            s["action"] for s in steps
        ]

        return {
            "success": success,
            "tool_sequence": tool_sequence,
            "step_count": len(steps),
        }