class CostAnalyzer:

    def estimate(self, traces):

        total_tokens = sum(
            t.get("tokens", 0)
            for t in traces
        )

        return {
            "total_tokens": total_tokens,
            "estimated_cost": total_tokens * 0.00002,
        }