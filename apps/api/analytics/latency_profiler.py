class LatencyProfiler:

    def analyze(self, traces):

        latencies = [
            t.get("latency", 0)
            for t in traces
        ]

        return {
            "avg_latency": sum(latencies) / len(latencies) if latencies else 0,
            "max_latency": max(latencies) if latencies else 0,
            "min_latency": min(latencies) if latencies else 0,
        }