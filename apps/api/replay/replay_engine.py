from typing import List, Dict, Any
from apps.api.observability.trace_event import TraceEvent


class ReplayEngine:

    def __init__(self, trace_store):
        self.trace_store = trace_store

    def replay(self, trace_id: str) -> Dict[str, Any]:

        # 1. trace 가져오기
        events: List[TraceEvent] = self.trace_store.get(trace_id)

        if not events:
            raise Exception(f"Trace not found: {trace_id}")

        # 2. 시간 순 정렬 (replay 핵심)
        events = sorted(events, key=lambda e: e.timestamp)

        timeline = []

        state = {
            "tools": {},
            "execution": {},
            "memory": {}
        }

        # 3. 이벤트 재생
        for event in events:

            # tool call
            if event.event_type == "tool.call":
                timeline.append({
                    "type": "tool.call",
                    "node_id": event.node_id,
                    "payload": event.payload,
                    "timestamp": event.timestamp,
                })

            # tool result
            elif event.event_type == "tool.result":
                state["tools"][event.node_id] = event.payload

                timeline.append({
                    "type": "tool.result",
                    "node_id": event.node_id,
                    "payload": event.payload,
                    "timestamp": event.timestamp,
                })

            # execution
            elif event.event_type.startswith("execution"):
                state["execution"][event.node_id] = event.payload

                timeline.append({
                    "type": event.event_type,
                    "node_id": event.node_id,
                    "payload": event.payload,
                    "timestamp": event.timestamp,
                })

            # memory
            elif event.event_type.startswith("memory"):
                state["memory"][event.node_id] = event.payload

                timeline.append({
                    "type": event.event_type,
                    "node_id": event.node_id,
                    "payload": event.payload,
                    "timestamp": event.timestamp,
                })

        # 4. 결과 반환
        return {
            "trace_id": trace_id,
            "state": state,
            "timeline": timeline,
        }