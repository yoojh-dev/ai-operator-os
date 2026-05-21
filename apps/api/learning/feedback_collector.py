class FeedbackCollector:

    def __init__(self, event_store):

        self.event_store = event_store

    def collect(self, trace_id: str):

        events = self.event_store.get_by_trace(trace_id)

        success = any(
            e.get("event_type") == "node_success"
            for e in events
        )

        failures = len([
            e for e in events
            if e.get("event_type") == "node_failed"
        ])

        latency = len(events)

        return {
            "trace_id": trace_id,
            "success": success,
            "failures": failures,
            "latency": latency,
        }