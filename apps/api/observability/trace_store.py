class TraceStore:

    def __init__(self):

        self.traces = {}

    def append(self, event: TraceEvent):

        if event.trace_id not in self.traces:
            self.traces[event.trace_id] = []

        self.traces[event.trace_id].append(event)

    def get(self, trace_id: str):

        return self.traces.get(trace_id, [])