# apps/api/execution/runtime/event_emitter.py

from apps.api.observability.trace_event import TraceEvent
import time
from uuid import uuid4


class EventEmitter:

    def __init__(self, trace_store):
        self.trace_store = trace_store

    def emit(self, trace_id, node_id, event_type, payload, parent_id=None):

        event = TraceEvent(
            event_id=str(uuid4()),
            trace_id=trace_id,
            node_id=node_id,
            event_type=event_type,
            payload=payload,
            timestamp=time.time(),
            parent_id=parent_id,
        )

        self.trace_store.append(event)

        return event