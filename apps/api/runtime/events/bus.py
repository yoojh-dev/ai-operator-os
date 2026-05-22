class EventBus:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event_type, handler):
        handlers = self._subscribers.setdefault(event_type, [])
        handlers.append(handler)

    async def publish(self, event):
        handlers = self._subscribers.get(event.type, [])

        for handler in handlers:
            await handler(event)