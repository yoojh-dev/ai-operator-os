class ReplayAPI:

    def __init__(self, trace_store, kernel):

        self.trace_store = trace_store
        self.kernel = kernel

    def replay(self, trace_id: str):

        trace = self.trace_store.get(trace_id)

        if not trace:
            raise Exception("Trace not found")

        results = []

        for event in trace:

            results.append({
                "node_id": event.node_id,
                "type": event.event_type,
                "payload": event.payload,
            })

        return {
            "trace_id": trace_id,
            "events": results,
        }