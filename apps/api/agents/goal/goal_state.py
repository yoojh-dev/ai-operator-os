from dataclasses import dataclass
from enum import Enum


class GoalStatus(Enum):

    PENDING = "pending"
    RUNNING = "running"
    FAILED = "failed"
    COMPLETED = "completed"


@dataclass
class Goal:

    id: str
    description: str
    status: GoalStatus
    context: dict
    result: dict | None = None