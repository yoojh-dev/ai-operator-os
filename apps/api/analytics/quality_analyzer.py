class QualityAnalyzer:

    def evaluate(self, traces):

        success = sum(
            1 for t in traces
            if t.get("success") is True
        )

        total = len(traces)

        return {
            "success_rate": success / total if total else 0,
        }