class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(
        self,
        event: str,
        callback,
    ):
        callbacks = self.subscribers.setdefault(
            event,
            [],
        )

        callbacks.append(callback)

    async def publish(
        self,
        event: str,
        payload,
    ):
        callbacks = self.subscribers.get(
            event,
            [],
        )

        for callback in callbacks:
            await callback(payload)