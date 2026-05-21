class EventStore:

    def __init__(self):

        self.events = []

    def append(self, event):

        self.events.append(event)

    def get_by_trace(self, trace_id: str):

        return [
            e for e in self.events
            if e.get("trace_id") == trace_id
        ]

    def all(self):

        return self.events