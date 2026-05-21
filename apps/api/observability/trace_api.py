class TraceAPI:

    def __init__(self, trace_store):

        self.trace_store = trace_store

    def get_trace(self, trace_id: str):

        return self.trace_store.get(trace_id)