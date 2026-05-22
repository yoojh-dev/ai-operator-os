# apps/api/execution/runtime/execution_state.py

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Optional
import time


class NodeStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"


@dataclass
class ExecutionState:

    node_id: int
    status: NodeStatus = NodeStatus.PENDING

    input: Optional[Dict[str, Any]] = None
    output: Optional[Any] = None
    error: Optional[str] = None

    started_at: Optional[float] = None
    ended_at: Optional[float] = None

    def start(self, input_data: dict):
        self.status = NodeStatus.RUNNING
        self.input = input_data
        self.started_at = time.time()

    def success(self, output: Any):
        self.status = NodeStatus.SUCCESS
        self.output = output
        self.ended_at = time.time()

    def fail(self, error: str):
        self.status = NodeStatus.FAILED
        self.error = error
        self.ended_at = time.time()