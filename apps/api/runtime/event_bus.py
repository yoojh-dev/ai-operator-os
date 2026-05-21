class EventBus:

    def __init__(self):

        self.subscribers = {}

    def subscribe(self, event_type: str, handler):

        if event_type not in self.subscribers:
            self.subscribers[event_type] = []

        self.subscribers[event_type].append(handler)

    def emit(self, event_type: str, payload: dict):

        for handler in self.subscribers.get(event_type, []):
            handler(payload)