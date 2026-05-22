from collections import defaultdict
from typing import Callable, Dict, List, Any


class EventBus:
    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = defaultdict(list)

    def subscribe(self, event: str, handler: Callable):
        self._subscribers[event].append(handler)

    async def publish(self, event: str, payload: Any):
        handlers = self._subscribers.get(event, [])

        for handler in handlers:
            await handler(payload)