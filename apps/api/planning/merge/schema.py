from dataclasses import dataclass
from typing import Any


@dataclass
class PlanStep:

    id: int
    action: str
    input: dict
    source: str  # research | execution | tool


@dataclass
class Plan:

    steps: list[PlanStep]