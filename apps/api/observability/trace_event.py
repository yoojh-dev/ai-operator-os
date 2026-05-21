from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass(frozen=True)
class TraceEvent:

    # unique event id
    event_id: str

    # trace grouping id
    trace_id: str

    # execution node id
    node_id: str

    # event type (standardized string)
    event_type: str

    # actual data payload
    payload: Dict[str, Any]

    # event time (unix timestamp)
    timestamp: float

    # parent event (for tree reconstruction)
    parent_id: Optional[str] = None

    # system metadata (latency, cost, model, etc)
    meta: Dict[str, Any] = None