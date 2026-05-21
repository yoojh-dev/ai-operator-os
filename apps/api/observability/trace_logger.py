class TraceLogger:

    def __init__(self, store):
        self.store = store

    def log(self, event):
        # event is already TraceEvent
        self.store.append(event)
        return event